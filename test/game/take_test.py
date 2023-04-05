import io
import unittest
from unittest.mock import patch

from src.constants import dialog
from src.game.take import take
from src.model.map import zone_map, ITEMS, CAN_BE_TAKEN, EXAMINATION
from src.model.player import player


class TestTake(unittest.TestCase):
    TEST_EXAMINATION = "You are in a room."

    def setUp(self):
        player.location = (0, 0)
        zone_map[player.location[0]][player.location[1]] = {
            EXAMINATION: self.TEST_EXAMINATION,
            ITEMS: {
                "Book": {
                    CAN_BE_TAKEN: True
                },
                "Chair": {
                    CAN_BE_TAKEN: False
                }
            }
        }

    def test_take_success(self):
        # Arrange
        item_to_take = "book"
        expected_output = f'{self.TEST_EXAMINATION}\nWhat would you like to pick up?\n' \
                          f'(You can take {item_to_take.capitalize()})\n' \
                          f'You have taken {item_to_take.capitalize()}.\n\n{dialog.CONTINUE}\n'

        # Act
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch('builtins.input', return_value='Book'):
                take()

        # Assert
        self.assertEqual(expected_output, mock_stdout.getvalue())
        self.assertIn(item_to_take.capitalize(), player.inventory)
        self.assertEqual(1, len(player.inventory))

    def test_take_no_items(self):
        # Arrange
        zone_map[player.location[0]][player.location[1]][ITEMS] = {}
        expected_output = f'{self.TEST_EXAMINATION}\nThere are no items that can be taken at the moment.' \
                          f'\n\n{dialog.CONTINUE}\n'

        # Act
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch('builtins.input', return_value=''):
                take()

        # Assert
        self.assertEqual(expected_output, mock_stdout.getvalue())
