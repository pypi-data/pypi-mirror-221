from typing import List

from pydantic import BaseModel

from bastion_integration.dto.person_dto import PersonBriefDto, PersonDto
from bastion_integration.dto.points_dto import EntryPoint, AccessLevel
from bastion_integration.dto.time_dto import TimeIntervalDto


class PassBriefDto(BaseModel):
    CardCode: str
    PersonData: PersonBriefDto
    PassType: int
    CardStatus: int


class PassInDto(BaseModel):
    CardCode: str = ""
    PersonData: PersonDto
    PassType: str = ""
    DateFrom: str = ""
    DateTo: str = ""
    CardStatus: int
    TimeInterval: TimeIntervalDto | str = ""
    EntryPoints: List[EntryPoint] | str = []
    AccessLevels: List[AccessLevel] | str = []
    PassCat: str
    CreateDate: str
    IssueDate: str = ""
    Pincode: int | str = ""


class GetPassInDto(BaseModel):
    card_code: str = ""
    srvCode: str = ""
    cardStatus: str | int = ""
    passType: str = ""
    withoutPhoto: bool = True  # true если фотографии возвращать не нужно
    startFrom: int | str = ""
    maxCount: int | str = ""
    startDateFrom: str = ""
    startDateTo: str = ""


class PassOutDto(BaseModel):
    cardCode: str = ""
    personData: PersonDto
    passType: str | int
    dateFrom: str = ""
    dateTo: str = ""
    cardStatus: int
    timeInterval: TimeIntervalDto | str | None = ""
    entryPoints: List[EntryPoint] | str = ""
    accessLevels: List[AccessLevel] | str = ""
    passCat: str
    createDate: str
    issueDate: str | None = ""
    pincode: int | str = ""


class PassDto:

    class Create(BaseModel):
        pass_info: PassInDto
        use_access_levels: bool

    class Update(BaseModel):
        pass_info: PassInDto
        use_access_levels: bool

    class Block(BaseModel):
        card_code: str
        comment: str

    class Unlock(BaseModel):
        card_code: str

    class Archive(BaseModel):
        card_code: str

    class Issue(BaseModel):
        srvCode: str = ""
        name: str  # Фамилия
        firstname: str  # Имя
        secondname: str  # Отчество
        birthDate: str
        passType: str  # (Постоянный - 1, Временный - 2,Разовый - 4)
        cardCode: str
