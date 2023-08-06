from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel


class DeviceType(Enum):
    DEVICES = 0
    DOORS = 3
    CONTROLLER = 5
    RELAY = 10
    ALARM_INPUT = 12
    READER = 19
    TURNSTILE = 22
    NETWORK_GROUP = 40


class DeviceDto(BaseModel):
    srvCode: str
    driverId: int | str = ""
    deviceType: int | DeviceType


class DeviceOutDto(BaseModel):
    """Тип Device представляет собой набор данных устройства. Объект типа Device используется в методе
получения набора устройств GetDevices"""
    sdn: int  # Идентификатор устройства
    parentSdn: int | None  # Идентификатор родительского устройства
    driverId: int  # Идентификатор типа драйвера, которому принадлежит устройство
    name: str  # Наименование устройства
    deviceType: int  # Код типа устройства
    deviceTypeName: str  # Текстовое имя типа устройства
    childs: List[DeviceOutDto] | None  # Коллекция дочерних устройств
