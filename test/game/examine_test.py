import io
import unittest
from unittest.mock import patch

from src.constants import dialog
from src.game.examine import examine
from src.model.map import zone_map, ITEMS, EXAMINATION, DESC
from src.model.player import player


class TestExamine(unittest.TestCase):

    def setUp(self):
        self.ITEMS = ITEMS
        self.EXAMINATION = EXAMINATION
        self.DESC = DESC
        self.player = player
        self.zone_map = zone_map

    def test_examine_with_available_items(self):
        # Arrange
        self.player.location = (0, 0)
        self.zone_map[0][0] = {
            self.EXAMINATION: "You see a table with a key on it.",
            self.ITEMS: {
                "key": {
                    self.DESC: "A shiny golden key."
                },
                "table": {
                    self.DESC: "An old table."
                }
            }
        }
        expected_output = "You see a table with a key on it.\n\n" \
                          "What would you like to examine?\n" \
                          "(You can choose key, table)\n" \
                          "A shiny golden key.\n\n" + dialog.CONTINUE + "\n"

        # Act
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch('builtins.input', return_value='key'):
                examine()

        # Assert
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_examine_with_no_items(self):
        # Arrange
        self.player.location = (0, 0)
        self.zone_map[0][0] = {self.EXAMINATION: "You see an empty room.", self.ITEMS: {}}
        expected_output = "You see an empty room.\nThere's no available items for examination.\n\n" \
                          + dialog.CONTINUE + "\n"

        # Act
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch('builtins.input', return_value='key'):
                examine()

        # Assert
        self.assertEqual(expected_output, mock_stdout.getvalue())
