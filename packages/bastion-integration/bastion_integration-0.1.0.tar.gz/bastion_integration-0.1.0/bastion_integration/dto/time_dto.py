from pydantic import BaseModel


class TimeIntervalDto(BaseModel):
    timeStart: str  # указывается в форматах «HH:MM:SS» либо «HH:MM»
    timeEnd: str  # указывается в форматах «HH:MM:SS» либо «HH:MM»
    inSaturday: int = 0  # 1/0 – Разрешение/запрет прохода
    inSunday: int = 0  # 1/0 – Разрешение/запрет прохода
    inHolidays: int = 0  # 1/0 – Разрешение/запрет прохода