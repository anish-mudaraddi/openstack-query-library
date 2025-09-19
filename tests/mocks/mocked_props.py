from openstackquery.enums.props.prop_enum import PropEnum

# pylint:disable=too-few-public-methods

# We're just using this for testing so we're not worried about implementing abstract methods
# pylint:disable=abstract-method


class MockProperties(PropEnum):
    """
    A Enum class to mock query properties for various unit tests
    """

    PROP_1 = 1
    PROP_2 = 2
    PROP_3 = 3
    PROP_4 = 4

    @staticmethod
    def _get_aliases():
        return {
            MockProperties.PROP_1: ["PROP_1", "prop_1"],
            MockProperties.PROP_2: ["PROP_2"],
            MockProperties.PROP_3: ["PROP_3"],
            MockProperties.PROP_4: ["PROP_4"],
        }
