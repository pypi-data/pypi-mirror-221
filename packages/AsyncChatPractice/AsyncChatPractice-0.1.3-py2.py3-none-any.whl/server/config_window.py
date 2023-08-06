import os
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class ConfigWindow(QDialog):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(365, 260)
        self.setWindowTitle("Server settings")
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setModal(True)

        self.db_path_label = QLabel("Database file path: ", self)
        self.db_path_label.move(10, 10)
        self.db_path_label.setFixedSize(240, 15)

        self.db_path = QLineEdit(self)
        self.db_path.setFixedSize(250, 20)
        self.db_path.move(10, 30)
        self.db_path.setReadOnly(True)

        self.db_path_select = QPushButton("Open...", self)
        self.db_path_select.move(275, 28)

        self.db_file_label = QLabel("Database file name: ", self)
        self.db_file_label.move(10, 68)
        self.db_file_label.setFixedSize(180, 15)

        self.db_file = QLineEdit(self)
        self.db_file.move(200, 66)
        self.db_file.setFixedSize(150, 20)

        self.port_label = QLabel("Listening port: ", self)
        self.port_label.move(10, 108)
        self.port_label.setFixedSize(180, 15)

        self.port = QLineEdit(self)
        self.port.move(200, 108)
        self.port.setFixedSize(150, 20)

        self.ip_label = QLabel("Listening IP address: ", self)
        self.ip_label.move(10, 148)
        self.ip_label.setFixedSize(180, 15)

        self.ip_label_note = QLabel(
            "keep it empty to received connections by any IP address", self
        )
        self.ip_label_note.move(10, 168)
        self.ip_label_note.setFixedSize(500, 30)

        self.ip = QLineEdit(self)
        self.ip.move(200, 148)
        self.ip.setFixedSize(150, 20)

        self.save_btn = QPushButton("Save", self)
        self.save_btn.move(190, 220)

        self.close_button = QPushButton("Close", self)
        self.close_button.move(275, 220)
        self.close_button.clicked.connect(self.close)

        self.db_path_select.clicked.connect(self.open_file_dialog)

        self.show()

        self.db_path.insert(self.config["SETTINGS"]["Database_path"])
        self.db_file.insert(self.config["SETTINGS"]["Database_file"])
        self.port.insert(self.config["SETTINGS"]["Default_port"])
        self.ip.insert(self.config["SETTINGS"]["Listen_Address"])
        self.save_btn.clicked.connect(self.save_server_config)

    def open_file_dialog(self) -> None:
        """
        Init choose file dialog
        :return:
        """
        global dialog
        dialog = QFileDialog(self)
        path = dialog.getExistingDirectory()
        path = path.replace("/", "\\")
        self.db_path.clear()
        self.db_path.insert(path)

    def save_server_config(self) -> None:
        """
        Trigger on button to save server configurations
        :return:
        """
        global config_window
        message = QMessageBox()
        self.config["SETTINGS"]["Database_path"] = self.db_path.text()
        self.config["SETTINGS"]["Database_file"] = self.db_file.text()
        try:
            port = int(self.port.text())
        except ValueError:
            message.warning(self, "Error", "Port is a int value")
        else:
            self.config["SETTINGS"]["Listen_Address"] = self.ip.text()
            if 1023 < port < 65536:
                self.config["SETTINGS"]["Default_port"] = str(port)
                dir_path = os.path.dirname(os.path.realpath(__file__))
                dir_path = os.path.dirname(dir_path)
                with open(f"{dir_path}/server.ini", "w") as conf:
                    self.config.write(conf)
                    message.information(
                        self, "OK", "Successfully settings has been saved"
                    )
            else:
                message.warning(
                    self,
                    "Error",
                    "Invalid port value, valid values are from 1024 to 65536",
                )
