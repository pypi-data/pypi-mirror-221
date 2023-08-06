from pydantic import BaseModel

from bastion_integration.dto.points_dto import AccessPoint


class GetCardEvents(BaseModel):
    cardCode: str = ""
    dateFrom: str = ""
    dateTo: str = ""
    withPhotos: bool = False


class OutCardEvents(BaseModel):
    cardCode: str
    entryPoint: AccessPoint
    dateTime: str
    msgText: str
    msgCode: int
    msgType: int
    comments: str | None
    photo: str | None
