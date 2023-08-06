from pydantic import BaseModel


class PersonDto(BaseModel):
    name: str
    firstName: str
    secondName: str
    tableNo: str | None = ""
    personCat: str | None = ""
    org: str
    dep: str
    post: str
    comments: str | None = ""
    docIssueOrgan: str | None = ""
    docSer: str | None = ""
    docNo: str | None = ""
    docIssueDate: str | None = ""
    birthDate: str | None = ""
    birthPlace: str | None = ""
    address: str | None = ""
    phone: str | None = ""
    foto: str | None = ""
    addField1: str | None = ""
    addField2: str | None = ""
    addField3: str | None = ""
    addField4: str | None = ""
    addField5: str | None = ""
    addField6: str | None = ""
    addField7: str | None = ""
    addField8: str | None = ""
    addField9: str | None = ""
    addField10: str | None = ""
    addField11: str | None = ""
    addField12: str | None = ""
    addField13: str | None = ""
    addField14: str | None = ""
    addField15: str | None = ""
    addField16: str | None = ""
    addField17: str | None = ""
    addField18: str | None = ""
    addField19: str | None = ""
    addField20: str | None = ""
    createDate: str | None = ""


class PersonBriefDto(BaseModel):
    Name: str
    FirstName: str = ""
    SecondName: str = ""
    BirthDate: str = ""