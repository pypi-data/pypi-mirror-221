from enum import Enum, unique


@unique
class FilterTypeEnum(Enum):
    EQUAL = "equal"
    IN = "in"
    NOT = "not"
    NOT_IN = "not_in"
