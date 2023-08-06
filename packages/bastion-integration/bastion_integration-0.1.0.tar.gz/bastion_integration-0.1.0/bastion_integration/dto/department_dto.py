from pydantic import BaseModel


class DepartmentInDto(BaseModel):
    srvCode: str = ""
    DepName: str
    OrgName: str


class DepartmentDto:
    class Create(BaseModel):
        department: DepartmentInDto

    class Update(BaseModel):
        new_name: str
        department: DepartmentInDto

    class Delete(BaseModel):
        department: DepartmentInDto

    class Get(BaseModel):
        organization_name: str


class DepartmentOutDto(BaseModel):
    depName: str
    orgName: str
