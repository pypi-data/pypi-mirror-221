from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QAction
from PyQt6.QtCore import QTimer
from .statistic_window import StatisticWindow
from .config_window import ConfigWindow
from .add_user import RegisterUser
from .remove_user import DelUserDialog


class MainWindow(QMainWindow):
    def __init__(self, database, server, config):
        super().__init__()

        # База данных сервера
        self.database = database

        self.server_thread = server
        self.config = config

        self.exitAction = QAction("Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(QApplication.quit)

        self.refresh_button = QAction("Update list", self)

        self.config_btn = QAction("Server Settings", self)

        self.register_btn = QAction("User registration", self)

        self.remove_btn = QAction("User removing", self)

        self.show_history_button = QAction("Clients history", self)

        self.statusBar()
        self.statusBar().showMessage("Server Working")

        self.toolbar = self.addToolBar("MainBar")
        self.toolbar.addAction(self.exitAction)
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)
        self.toolbar.addAction(self.register_btn)
        self.toolbar.addAction(self.remove_btn)

        self.setFixedSize(800, 600)
        self.setWindowTitle("Messaging Server alpha release")

        self.label = QLabel("List connected clients:", self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        self.active_clients_table = QTableView(self)
        self.active_clients_table.move(10, 45)
        self.active_clients_table.setFixedSize(780, 400)

        self.timer = QTimer()
        self.timer.timeout.connect(self.create_users_model)
        self.timer.start(1000)

        self.refresh_button.triggered.connect(self.create_users_model)
        self.show_history_button.triggered.connect(self.show_statistics)
        self.config_btn.triggered.connect(self.server_config)
        self.register_btn.triggered.connect(self.register_user)
        self.remove_btn.triggered.connect(self.remove_user)

        self.show()

    def create_users_model(self) -> None:
        """
        Trigger to create or update active users list
        :return:
        """
        list_users = self.database.active_users_list()
        list_ = QStandardItemModel()
        list_.setHorizontalHeaderLabels(
            ["Client username", "IP address", "Port", "Connection time"]
        )
        for row in list_users:
            user, ip, port, time = row
            user = QStandardItem(user)
            user.setEditable(False)
            ip = QStandardItem(ip)
            ip.setEditable(False)
            port = QStandardItem(str(port))
            port.setEditable(False)
            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)
            list_.appendRow([user, ip, port, time])
        self.active_clients_table.setModel(list_)
        self.active_clients_table.resizeColumnsToContents()
        self.active_clients_table.resizeRowsToContents()

    def show_statistics(self) -> None:
        """
        Init and show statistic window
        :return:
        """
        global start_window
        start_window = StatisticWindow(self.database)
        start_window.show()

    def server_config(self) -> None:
        """
        Init server config window
        :return:
        """
        global config_window
        config_window = ConfigWindow(self.config)

    def register_user(self) -> None:
        """
        Init and show user registration window
        :return:
        """
        global reg_window
        reg_window = RegisterUser(self.database, self.server_thread)
        reg_window.show()

    def remove_user(self) -> None:
        """
        Init and show delete user window
        :return:
        """
        global rem_window
        rem_window = DelUserDialog(self.database, self.server_thread)
        rem_window.show()
