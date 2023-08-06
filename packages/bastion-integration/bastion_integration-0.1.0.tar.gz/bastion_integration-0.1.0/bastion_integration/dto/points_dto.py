from pydantic import BaseModel


class EntryPoint(BaseModel):
    servID: str
    subDeviceNo: int
    subDeviceName: str


class AccessLevel(BaseModel):
    servID: str
    id: int
    name: str


class ControlArea(BaseModel):
    servId: str
    id: int
    name: str


class AccessPoint(BaseModel):
    servID: str
    subDeviceNo: int
    subDeviceName: str
