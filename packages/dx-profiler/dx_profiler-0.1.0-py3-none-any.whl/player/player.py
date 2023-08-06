import sys
from collections import defaultdict

import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, \
QProgressBar, QHBoxLayout, QVBoxLayout, QWidget, QPushButton


VIDEO_EXTENSIONS = [".avi", ".mp4", ".mov"]


class VideoPlayer(QMainWindow):
    """Dx Video Player

    동영상 파일에 record.txt을 통해, 후처리를 한 Video를 관리하는 클래스.
    Space-bar로 동영상 재생 및 정지, Q/E 를 통해 Frame 이동 등의 기능을 제공한다.

    Attributes:
        cap (VideoCapture): cv2로 생성한 VideoCapture 객체.
        fps (int): cap에서 획득한 FPS(FramePerSeconds).
        total_frames (int): cap에서 획득한 total_frames
        current_frame (int): 현재 video_label에 그려지는 frame_number.
        
        video_label (QLabel): 후처리 된 영상을 출력하는 라벨.
        progress_bar (QProgressBar): 현재 프레임 / 전체 프레임을 보여주는 진행바.
        start_stop_button (QPushButton): 재생/정지 기능을 하는 toggle 버튼.

        timer (QTimer): fps에 맞게 video_label을 업데이트 하는 인터럽트 타이머.
        playing (bool): 동영상이 재생이면 True, 정지면 False.
        scaled_width (int): resize 된  video label의 width.
        scaled_height (int): resize 된 video_label의 height.
        data (List[Dict]): dict 형태의 record 정보가 들어있는 data list.
                        bbox, id, label, classifier 등이 존재.
    """

    def __init__(self, video_path: str, record: str, st_time_stamp: int) -> None:
        """
        Args:
            video_path: 동영상 파일의 경로
            record: object message의 내용
            st_time_stamp: 동영상 시작 시간의 time-stamp ex) 1690210800

        Raises:
            OpenError: 파일을 열 수 없음
            TimeError: st_time_stamp가 유효하지 않음 
        """
        super().__init__()

        file_ext = video_path[video_path.rfind("."):]
        # 파일 확장자가 영상 확장자인지 확인.
        if file_ext not in VIDEO_EXTENSIONS:
            raise Exception # OpenError : 동영상 확장자를 가지지 않는 파일

        #! cv2.VideoCapture에서 발생한 error는 except로 잡히지 않는다..
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            raise Exception # OpenError : 동영상이 열리지 않음
        
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setMaximum(self.total_frames)
        self.progress_bar.setValue(0)

        self.start_stop_button = QPushButton("II", self)
        self.start_stop_button.clicked.connect(self.toggle_video)
        self.start_stop_button.setGeometry(10, 10, 100, 30)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_stop_button)
        button_layout.addWidget(self.progress_bar)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_label)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.playing = True 

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // self.fps)

        desktop = QDesktopWidget().screenGeometry()
        self.setMinimumSize(800, 600)
        self.setMaximumSize(desktop.width(), desktop.height())

        self.current_frame = 0 
        self.data = defaultdict(list)

        # 나노 시간 처리 후에, 시작 time_stamp 값을 빼서 초(second)를 구합니다.
        # 초(second)에다가 fps 값을 곱해 frame_number를 구합니다.
        for line in record:
            line_data = eval(line)
            time_in_seconds = (line_data["metadata"]["timestamp"] / 1e9) - st_time_stamp
            frame_num = int(time_in_seconds * self.fps)
            self.data[frame_num].append(line_data["objects"])

    def toggle_video(self):
        # video의 상태를 전환. 정지 -> 재생, 재생 -> 정지
        # 재생 -> 정지 시에는 timer는 정지.
        # 정지 -> 재생 시에는 timer를 다시 시작.
        if self.playing:
            self.timer.stop()
            self.start_stop_button.setText("▶")
        
        else:
            self.timer.start(1000 // self.fps)
            self.start_stop_button.setText("II")
        
        self.playing = not self.playing

    def update_frame(self):
        # frame을 하나 읽어들임
        # 현재 gui window의 size를 받아들여 frame을 resize.
                            # current_frame 값에 있는 data를 가져와서 id, label등을 draw.
        # frame 업데이트.

        ret, frame = self.cap.read()
        self.current_frame += 1

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape

            # GUI 창의 크기를 가져와서 비율에 맞게 영상 크기를 조절
            window_width = self.video_label.width()
            window_height = self.video_label.height()
            aspect_ratio = w / h

            if window_width / window_height > aspect_ratio:
                self.scaled_width = int(window_height * aspect_ratio)
                self.scaled_height = window_height
            
            else:
                self.scaled_width = window_width
                self.scaled_height = int(window_width / aspect_ratio)

            frame = cv2.resize(frame, (self.scaled_width, self.scaled_height))

            bytes_per_line = ch * self.scaled_width
            q_image = QImage(frame.data, self.scaled_width, self.scaled_height, bytes_per_line, QImage.Format_RGB888)
            
            painter = QPainter(q_image)
            red_pen = QPen(Qt.red, 3)
            green_pen = QPen(Qt.green, 2)
            
            if self.current_frame in self.data: # 현재 frame에 해당하는 값의 정보들을 draw
                data = self.data[self.current_frame]

                for datum in data:
                    datum = datum[0]
                    painter.setPen(red_pen)
                    
                    bbox = datum["bbox"]
                    x, y, w, h = bbox["x"], bbox["y"], bbox["w"], bbox["h"]
                    x, y, w, h = x * self.scaled_width, y * self.scaled_height, \
                                    w * self.scaled_width, h * self.scaled_height

                    if datum["id"] >= 10000:
                        datum["id"] = -1

                    x, y, w, h = map(int, [x, y, w, h])
                    painter.drawRect(x, y, w, h)
                    
                    if datum["id"] != -1:
                        painter.drawText(x, y-10, f"[{datum['id']}] {datum['label']}")
                    else:
                        painter.drawText(x, y-10, f"[None] {datum['label']}")

                    painter.setPen(green_pen)

                    drawing_texts = []

                    if "classifiers" in datum:
                        for idx, val in enumerate(datum["classifiers"]):
                            drawing_texts.append(f"[{val['label']}] {val['type']}")
                    
                    if "score_d" in datum:
                            drawing_texts.append(f"Score: {datum['score_d']:.2f}")
                    
                    for idx, val in enumerate(drawing_texts):
                        painter.drawText(x, y + (idx+1)*15, val)

            painter.end()
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)
            self.progress_bar.setValue(self.current_frame)

        else:
            # exit
            self.timer.stop()
            self.cap.release()
            self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.toggle_video()
        
        elif event.key() == Qt.Key_Q:  # 이전 프레임으로 이동
            self.current_frame -= 2
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
            self.update_frame()

        elif event.key() == Qt.Key_E:  # 다음 프레임으로 이동
            self.update_frame()

    def closeEvent(self, event):
        self.cap.release()
        self.timer.stop()


def text_input_player(text: str):
    """text 파일로 Videoplayer에 입력.
    
    첫 번째 줄, 영상 파일 경로
    두 번째 줄, timestamp (second)
    세번 째 줄 ~, 오브젝트 메시지

    Args:
        text: 위에 내용으로 구성된 text
    """
    with open(text, "r") as f:
        video_path = f.readline().strip()
        st_time_stamp = int(f.readline().strip())
        record = f.readlines()
    
    return VideoPlayer(video_path, record, st_time_stamp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = text_input_player("sample.txt")
    player.show()
    sys.exit(app.exec_())
