from pydantic import BaseModel


class OrganizationInDto(BaseModel):
    orgName: str


class OrganizationDto:
    class Get(BaseModel):
        name: str

    class Create(BaseModel):
        organization: OrganizationInDto

    class Update(BaseModel):
        new_name: str
        organization: OrganizationInDto

    class Delete(BaseModel):
        organization: OrganizationInDto
