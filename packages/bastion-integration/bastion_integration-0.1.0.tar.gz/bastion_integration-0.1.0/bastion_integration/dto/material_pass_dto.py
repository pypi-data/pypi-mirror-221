from typing import List

from pydantic import BaseModel

from bastion_integration.dto.pass_dto import PassBriefDto
from bastion_integration.dto.person_dto import PersonBriefDto



class MatValusueDto(BaseModel):
    Type: str
    ValFld1: str = ""
    ValFld2: str = ""
    ValFld3: str = ""
    ValFld4: str = ""
    ValFld5: str = ""
    ValFld6: str = ""
    ValFld7: str = ""
    ValFld8: str = ""
    ValFld9: str = ""
    ValFld10: str = ""
    ValFld11: str = ""
    ValFld12: str = ""
    ValFld13: str = ""
    ValFld14: str = ""
    ValFld15: str = ""
    ValFld16: str = ""
    ValFld17: str = ""
    ValFld18: str = ""
    ValFld19: str = ""
    ValFld20: str = ""
    OrderNum: int | None = None



class CreateMaterialPassInDto(BaseModel):
    Id: int | None = None # pass id
    PassNum: str = ""
    CreateDate: str = ""
    MatPerson: PersonBriefDto | None = None
    ToExport: bool
    ToImport: bool
    Status: int | None = None
    MatValues: List[MatValusueDto]
    Pass: PassBriefDto
    StartDate: str
    EndDate: str
    GoalOrganization: str = ""
    GoalDepartment: str = ""