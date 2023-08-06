# import sys
# import unittest
#
# sys.path.append("../")
# from services.variables import (RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME,
#                                ACTION,
#                                PRESENCE)
# from services.services import process_client_message
#
#
# class TestServer(unittest.TestCase):
#     err_dict = {
#         RESPONSE: 400,
#         ERROR: "Bad Request"
#     }
#     ok_dict = {RESPONSE: 200}
#
#     def test_no_action_field(self):
#         self.assertEqual(process_client_message(
#             {TIME: 123456.32165, USER: {ACCOUNT_NAME: "Guest"}}),
#             self.err_dict)
#
#     def test_wrong_action_field(self):
#         self.assertEqual(process_client_message(
#             {ACTION: "Wrong", TIME: 123456.32165,
#              USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)
#
#     def test_no_time_field(self):
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)
#
#     def test_no_user_data(self):
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: 123456.32165}), self.err_dict)
#
#     def test_unknown_user_data(self):
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: 123456.32165,
#              USER: {ACCOUNT_NAME: "Guest1"}}), self.err_dict)
#
#     def test_ok_data(self):
#         self.assertEqual(process_client_message(
#             {ACTION: PRESENCE, TIME: 123456.32165,
#              USER: {ACCOUNT_NAME: "Guest"}}), self.ok_dict)
#
#
# if __name__ == "__main__":
#     unittest.main()
