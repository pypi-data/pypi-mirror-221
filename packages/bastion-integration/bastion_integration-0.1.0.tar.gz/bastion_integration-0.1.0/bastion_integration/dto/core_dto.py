from enum import Enum


class Command(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    GET = "get"

    BLOCK_PASS = "block_pass"
    UNLOCK_PASS = "unlock_pass"
    ARCHIVE_PASS = "archive_pass"
    ISSUE_PASS = "issue_pass"



class Object(Enum):
    ORGANIZATION = "organization"
    DEPARTMENT = "department"
    PASS = "pass"
    MATERIAL_PASS = "material_pass"
    CAR_PASS = "car_pass"
    ENTRY_POINT = "entry_point"
    ACCESS_LEVELS = "access_levels"
    CONTROL_AREA = "control_area"
    ACCESS_POINT = "access_point"
    CARD_EVENT = "card_event"
    ATTENDANCE = "attendance"
    DEVICE = "device"



