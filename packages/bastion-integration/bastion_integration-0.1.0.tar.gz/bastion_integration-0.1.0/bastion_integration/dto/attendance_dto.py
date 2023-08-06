from pydantic import BaseModel

from bastion_integration.dto.person_dto import PersonBriefDto


class Attendance(BaseModel):
    cardCode: str = ""
    dateFrom: str = ""
    dateTo: str = ""


class OutAttendance(BaseModel):
    cardCode: str
    isEntrance: bool
    dateTime: str
    comments: str
    ctrlArea: str
    tableno: str
    personData: PersonBriefDto