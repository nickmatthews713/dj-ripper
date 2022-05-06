import sys

from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt5.uic import loadUiType

from dj_ripper_ui import Ui_MainWindow

baseUIClass, baseUIWidget = loadUiType("ui/dj_ripper.ui")


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.downloadBus = []
        self.setupUi(self)
        self.reset_ui()

    def reset_ui(self):
        self.ripButton.setEnabled(False)
        self.destButton.setEnabled(False)
        self.filePathDisplay.clear()
        self.destPathDisplay.clear()

    def browseButtonHandler(self):
        self.__print_to_console("Browse button pushed")
        filename = QFileDialog.getOpenFileName(filter="*.txt")
        if filename[0] == "":
            return
        self.filePathDisplay.clear()
        self.filePathDisplay.append(filename[0])
        self.destButton.setEnabled(True)

    def destButtonHandler(self):
        self.__print_to_console("Dest button pushed")
        directory = QFileDialog.getExistingDirectory()
        if directory == "":
            return
        self.destPathDisplay.clear()
        self.destPathDisplay.append(directory)
        self.ripButton.setEnabled(True)

    def ripButtonHandler(self):
        self.__print_to_console("Rip button pushed")
        file_path = self.filePathDisplay.toPlainText()
        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                if self.validate_youtube_link(line):
                    try:
                        yt = YouTube(line)
                        audio = yt.streams.filter(only_audio=True, abr="128kbps").first()
                        print(audio)
                        audio.download(output_path=self.destPathDisplay.toPlainText(), filename=f'{yt.title}.mp3')
                        self.downloadBus.append(
                            {
                                "title": f'{yt.title}.mp3',
                                "path": f'{self.destPathDisplay.toPlainText()}/{yt.title}.mp3'
                            }
                        )
                        self.__print_to_console(f'Successfully downloaded {self.get_song_name_and_artist(yt.title)}')
                    except:
                        self.__print_to_console(f'ERROR: failed download for: {self.get_song_name_and_artist(yt.title)}')
            print(self.downloadBus)
            self.generate_meta_data_config_ui()

    def generate_meta_data_config_ui(self):
        scrollable_area_layout = QVBoxLayout()
        self.metaDataConfigArea.setLayout(scrollable_area_layout)

        for audio in self.downloadBus:
            horizontal_layout = QHBoxLayout()
            title_label = QLabel("title:")
            artist_label = QLabel("artist:")
            song_artist = self.get_song_name_and_artist(audio["title"])
            title_input = QLineEdit(song_artist[0])
            artist_input = QLineEdit(song_artist[1])

            horizontal_layout.addWidget(title_label)
            horizontal_layout.addWidget(title_input)
            horizontal_layout.addWidget(artist_label)
            horizontal_layout.addWidget(artist_input)

            scrollable_area_layout.addLayout(horizontal_layout)

    def get_song_name_and_artist(self, title=""):
        name_artist_and_more = title.split(sep="-")
        name = name_artist_and_more[0].strip()
        artist = name_artist_and_more[1].strip()
        end_chars = ["[", "("]
        for char in end_chars:
            if char in name_artist_and_more[1]:
                iend = name_artist_and_more[1].index(char)
                artist = name_artist_and_more[1][0:iend]

        return [name, artist]

    def validate_youtube_link(self, link):
        return "https://www.youtube.com" in link

    def __print_to_console(self, message):
        self.console.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window(None)
    win.show()
    sys.exit(app.exec())
