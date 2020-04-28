import unittest

from worldoftanks.action.tankopedia_badges import TankopediaBadgesData


class TestParsers(unittest.TestCase):

    def test_parser_tankopedia_badges(self):
        test_data = {
            "status": "ok",
            "meta": {
                "count": 1
            },
            "data": {
                "1": {
                    "images": {
                        "medium_icon": "a.png",
                        "small_icon": "b.png",
                        "big_icon": "c.png"
                    },
                    "badge_id": 1,
                    "name": "Gold, Beta Season",
                    "description": "Blank Description."
                }
            }
        }

        expected_result = [
            {'account_id': '1234',
             'badge_id': 1,
             'name': 'Gold, Beta Season',
             'description': 'Blank Description.',
             'medium_icon': 'a.png',
             'small_icon': 'b.png',
             'big_icon': 'c.png'
             }
        ]

        badge = TankopediaBadgesData._parse_data(test_data, account_id='1234')

        self.assertListEqual(badge, expected_result)
