from pydantic import BaseModel


class OperatorInfo(BaseModel):
    login: str
    password: str


class ServerConfig(BaseModel):
    host: str
    port: int
    certificate: str = ""
    https: bool = False


class BastionConfig(BaseModel):
    server_config: ServerConfig
    operator_info: OperatorInfo
    bastion_version: int
    debug_log: bool = False