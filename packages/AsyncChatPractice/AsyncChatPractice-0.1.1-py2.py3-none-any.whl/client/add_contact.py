import logging
from PyQt6.QtWidgets import QDialog, QLabel, QComboBox, QPushButton
from PyQt6.QtCore import Qt

LOGGER = logging.getLogger("client")


class AddContactDialog(QDialog):
    def __init__(self, transport, database):
        super().__init__()
        self.transport = transport
        self.database = database

        self.setFixedSize(350, 120)
        self.setWindowTitle("Choose contact to add:")
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setModal(True)

        self.selector_label = QLabel("Choose contact to add:", self)
        self.selector_label.setFixedSize(200, 20)
        self.selector_label.move(10, 0)

        self.selector = QComboBox(self)
        self.selector.setFixedSize(200, 20)
        self.selector.move(10, 30)

        self.btn_refresh = QPushButton("Update list", self)
        self.btn_refresh.setFixedSize(100, 30)
        self.btn_refresh.move(60, 60)

        self.btn_ok = QPushButton("Add", self)
        self.btn_ok.setFixedSize(100, 30)
        self.btn_ok.move(230, 20)

        self.btn_cancel = QPushButton("Cancel", self)
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.move(230, 60)
        self.btn_cancel.clicked.connect(self.close)

        self.possible_contacts_update()
        self.btn_refresh.clicked.connect(self.update_possible_contacts)

    def possible_contacts_update(self) -> None:
        """
        Check contacts, which could be updated
        :return:
        """
        self.selector.clear()
        contacts_list = set(self.database.get_contacts())
        users_list = set(self.database.get_users())
        users_list.remove(self.transport.username)
        self.selector.addItems(users_list - contacts_list)

    def update_possible_contacts(self) -> None:
        """
        Update contact list
        :return:
        """
        try:
            self.transport.user_list_update()
        except OSError:
            pass
        else:
            LOGGER.debug("Contact list updated successfully")
            self.possible_contacts_update()
