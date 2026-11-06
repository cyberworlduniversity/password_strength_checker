import unittest
from unittest.mock import patch

import password_checker


class PasswordPrivacyTests(unittest.TestCase):
    def test_mask_password_reveals_no_characters(self):
        self.assertEqual(password_checker.mask_password("Secret123!"), "**********")
        self.assertEqual(password_checker.mask_password("abc"), "***")
        self.assertEqual(password_checker.mask_password(""), "")

    @patch("password_checker.print_report")
    @patch("password_checker.getpass.getpass", side_effect=[" password with spaces ", "exit"])
    def test_interactive_input_preserves_spaces_without_echo(self, getpass_mock, report_mock):
        password_checker.run_interactive()
        getpass_mock.assert_any_call("\\n  Enter password (input hidden): ")
        report_mock.assert_called_once()
        self.assertEqual(report_mock.call_args.args[0].password, " password with spaces ")


if __name__ == "__main__":
    unittest.main()
