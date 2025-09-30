from typing import Dict

from openstackquery.enums.enum_with_aliases import EnumWithAliases

# pylint:disable=too-few-public-methods


class MockQueryPresets(EnumWithAliases):
    """
    An Enum class to mock query presets for various unit tests
    """

    @staticmethod
    def _get_aliases() -> Dict:
        return {
            "item_1": MockQueryPresets.ITEM_1,
            "item_2": MockQueryPresets.ITEM_2,
            "item_3": MockQueryPresets.ITEM_3,
            "item_4": MockQueryPresets.ITEM_4,
        }

    ITEM_1 = 1
    ITEM_2 = 2
    ITEM_3 = 3
    ITEM_4 = 4
