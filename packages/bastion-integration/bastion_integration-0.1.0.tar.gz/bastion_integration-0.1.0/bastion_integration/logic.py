from typing import List

import requests
from loguru import logger
from pydantic import BaseModel
from requests.cookies import RequestsCookieJar

from bastion_integration.dto.attendance_dto import Attendance, OutAttendance
from bastion_integration.dto.card_dto import GetCardEvents, OutCardEvents
from bastion_integration.dto.config import BastionConfig
from bastion_integration.dto.department_dto import DepartmentInDto, DepartmentOutDto
from bastion_integration.dto.device_dto import DeviceDto, DeviceOutDto
from bastion_integration.dto.dict_dto import DictValues
from bastion_integration.dto.organization_dto import OrganizationInDto
from bastion_integration.dto.pass_dto import GetPassInDto, PassDto, PassOutDto, PassInDto
from bastion_integration.dto.points_dto import EntryPoint, AccessLevel, ControlArea, AccessPoint
from bastion_integration.handlers import BastionIntegrationError, _handle_response


class Bastion:
    config: BastionConfig
    code_for_url: str
    cookies = RequestsCookieJar
    _code_for_url = ""
    token: str = ""


class BastionV3(Bastion): pass


class BastionV2(Bastion):

    def __init__(self):
        self.bastion_servers = ""

    def init(self, bastion_config: BastionConfig):
        self.config = bastion_config

    def _url_build(self, route: str, params: dict = None) -> str:
        params_string = ""
        if params:
            for key, value in params.items():
                params_string = params_string + f"&{key}={value}"
        url = ""
        if not route.startswith("/"):
            route = "/" + route
        if self.config.server_config.https:
            url = f"https://{self.config.server_config.host}/api{route}?{self.bastion_servers}{params_string if params_string else ''}"
        if not self.config.server_config.https:
            url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api{route}?{self.bastion_servers}{params_string if params_string else ''}"
        # logger.error(url)
        return url

    # =============================================================================================
    def logic(self, method: str, route: str, dto: dict | BaseModel = None, params: dict = None) -> requests.Response:
        if not self.token:
            raise BastionIntegrationError("Not authenticated in Bastion IKS")
        session = requests.Session()
        session.cookies = self.cookies
        url = self._url_build(route, params)
        response: requests.Response
        headers = {
            'Content-type': 'application/body+json',
            'Accept': 'application/body+json',
        }
        # logger.debug(url)
        try:
            match method:
                case "GET":
                    response = session.get(url=url)
                case "POST":
                    response = session.post(url=url, json=dto if dto else {}, headers=headers)
                case "PATCH":
                    response = session.patch(url=url, json=dto if dto else {}, headers=headers)
                case "PUT":
                    response = session.put(url=url, json=dto if dto else {}, headers=headers)
                case "DELETE":
                    response = session.delete(url=url)
            if response.status_code != 200:
                raise BastionIntegrationError(
                    f"\nStatus code {response.status_code}\nReason: {response.reason}\n Headers: {response.headers}")
            return response
        except requests.exceptions.ConnectionError as ex:
            logger.warning(f"Bastion connection error: validation error: {ex}\n")
            session.close()
        # except CookieJar.extract_cookies as e:
        #     logger.warning(f"Bastion connection error: validation error: {e}\n")
        #     session.close()

    # =============================================================================================
    def autarization(self) -> None:
        session = requests.Session()
        try:
            url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/Login"
            response = session.post(url, json={"Opername": self.config.operator_info.login,
                                               "Password": self.config.operator_info.password})
            if response.status_code != 200:
                raise BastionIntegrationError(
                    f"\nStatus code {response.status_code}\nReason: {response.reason}\n Headers: {response.headers}")
            elif response.json() == "success":
                logger.info("Authorization success")
                self.token = response.cookies.values()
                self.cookies = session.cookies
                return
            else:
                logger.error(
                    f"\nAuthorization failed with operator info:\n    Login: {self.config.operator_info.login},\n    Password: {self.config.operator_info.password}")
                session.close()
                return
        except requests.exceptions.ConnectionError as ex:
            logger.error(f"Bastion connection error: validation error:\n {ex}")
            session.close()
            return

    def logout(self):
        self.logic("POST", "LogOff")

    # =============================================================================================
    def get_servers(self, servers: list = None):
        if not self.token:
            raise BastionIntegrationError("Not authenticated in Bastion IKS")
        session = requests.Session()
        session.cookies = self.cookies
        url = f"http://{self.config.server_config.host}:{self.config.server_config.port}/api/GetServers"
        self.bastion_servers = session.get(url).text
        new_serves = []
        if servers:
            for server in servers:
                if server in self.bastion_servers:
                    new_serves.append(server)
                else:
                    raise BastionIntegrationError(message=f"Server not found: {server}")
        else:
            new_serves = self.bastion_servers
        for server_code in [new_serves]:
            self._code_for_url = self._code_for_url + f"srvCode={server_code}&"

    # =============================================================================================
    def get_version(self):
        logger.info(f'version: {(self.logic("GET", "GetVersion")).text}')

    def check_connection(self):
        logger.info(f'connection: {self.logic("GET", "CheckConnection").text}')

    def get_bastion_dict_values(self, category: int = "") -> DictValues:
        return _handle_response((self.logic("GET", "GetDictVals", params={"category": category})).json(), DictValues)

    def get_devices(self, dto: DeviceDto) -> DeviceOutDto:
        return _handle_response(self.logic("GET", "GetDevices", params=dto.dict()).json(), DeviceOutDto)

    # =============================================================================================
    def get_organisations(self, organizations_names: str):
        return _handle_response(
            (self.logic("GET", "GetOrgs", params={"filter": organizations_names})).json(), OrganizationInDto)

    def create_organization(self, dto: OrganizationInDto) -> str:
        return _handle_response(
            (self.logic("PUT", "PutOrg", dto=dto.dict())))

    def update_organization(self, new_org_name: str, dto: OrganizationInDto) -> str:
        return _handle_response(
            (self.logic("POST", "UpdateOrg", dto=dto.dict(), params={"orgNewName": new_org_name})))

    def delete_organization(self, dto: OrganizationInDto) -> str:
        return _handle_response(
            (self.logic("POST", "DeleteOrg", dto=dto.dict())))

    # =============================================================================================
    def get_department(self, organization_name: str) -> List[DepartmentOutDto]:
        return _handle_response(
            (self.logic("GET", "GetDeparts", params={"parentOrgName": organization_name})).json(), DepartmentOutDto)

    def create_department(self, dto: DepartmentInDto) -> str:
        if self.get_organisations(dto.OrgName):
            return _handle_response(
                (self.logic("PUT", "PutDepart", dto=dto.dict())))
        else:
            raise BastionIntegrationError(message=f"Organization {dto.OrgName} not found")

    def update_department(self, new_name: str, dto: DepartmentInDto) -> str:
        return _handle_response(
            (self.logic("POST", "UpdateDepart", params={"departNewName": new_name}, dto=dto.dict())))

    def delete_department(self, dto: DepartmentInDto) -> str:
        return _handle_response(
            (self.logic("POST", "DeleteDepart", dto=dto.dict())))

    # =============================================================================================
    def get_passes(self, dto: GetPassInDto) -> List[PassOutDto]:
        """Метод предоставляет возможность одним запросом получить пропуска
             только с одного конкретного сервера и требует обязательного указания параметра srvCode."""

        if len([self.bastion_servers]) != 1:
            raise BastionIntegrationError(message="Method get_bastion_pass can be used only with one server")
        if not dto.srvCode:
            raise BastionIntegrationError(message="Method get_bastion_pass can be used with srvCode")
        if dto.card_code:
            return _handle_response(self.logic("GET", "GetPassesByCardCode",
                                               params={"srvCode": dto.srvCode,
                                                       "cardCode": dto.card_code,
                                                       "withoutPhoto": dto.withoutPhoto}).json(), PassOutDto)
        else:
            return _handle_response(self.logic("GET", "GetPasses", params=dto.dict()).json(), PassOutDto)

    def create_pass(self, dto: PassInDto, use_access_levels: bool = False):
        """Флаг, при выставлении которого в значение true при создании пропуска учитываются данные поля AccessLevels.
         По умолчанию значение флага – false, в этом случае используются данные поля EntryPoints."""
        if self.get_organisations(dto.PersonData.org):
            deps = self.get_department(dto.PersonData.org)
            list_deps = []
            for one_dep in deps:
                list_deps.append(one_dep.depName)
            if dto.PersonData.dep not in list_deps:
                raise BastionIntegrationError(message=f"Department {dto.PersonData.dep} not found")
        else:
            raise BastionIntegrationError(message=f"Organization {dto.PersonData.org} not found")

        if use_access_levels and not dto.AccessLevels:
            raise BastionIntegrationError(message="Method create_bastion_pass can be used without accessLevels")
        if not dto.DateFrom:
            raise BastionIntegrationError(message="Method create_bastion_pass can be used with dateFrom")
        if dto.CardCode == "" and (dto.EntryPoints != '' or dto.AccessLevels != ''):
            return _handle_response(self.logic("PUT", "PutPass",
                                               params={"useAccessLevelsInsteadOfEntryPoints": use_access_levels},
                                               dto=dto.dict()))
        else:
            raise BastionIntegrationError(
                message="Method create_bastion_pass can be used without card code. You need set entryPoints or "
                        "accessLevels")

    def update_pass(self, dto: PassInDto, use_access_levels: bool = False):
        if dto.EntryPoints or dto.AccessLevels:
            return _handle_response(self.logic(method="PUT", route="PutPass", params={
                "useAccessLevelsInsteadOfEntryPoints": use_access_levels}, dto=dto.dict()))
        else:
            raise BastionIntegrationError(message="Method update_bastion_pass can be used with card code")

    def block_pass(self, card_code: str, comment: str) -> str:
        return _handle_response(
            (self.logic("GET", "BlockPass", params={"cardCode": card_code, "blockReason": comment})))

    def unblock_pass(self, card_code: str) -> str:
        return _handle_response(
            (self.logic("GET", "UnBlockPass", params={"cardCode": card_code})))

    def archive_pass(self, card_code: str):
        """Возможно убрать в архив только выданную карту"""
        return _handle_response(
            (self.logic("GET", "ReturnPass", params={"cardCode": card_code})))

    def issue_pass(self, dto: PassDto.Issue):
        if dto.cardCode == "" or not dto.cardCode:
            raise BastionIntegrationError(message="Method issue_bastion_pass can be used with card code")
        return _handle_response(
            (self.logic("GET", "IssuePass", params=dto.dict())))

    # =============================================================================================
    def get_entry_points(self) -> EntryPoint:
        return _handle_response((self.logic("GET", "GetEntryPoints")).json(), EntryPoint)

    def get_access_levels(self) -> AccessLevel:
        return _handle_response((self.logic("GET", "GetAccessLevels")).json(), AccessLevel)

    def get_control_areas(self):
        return _handle_response(self.logic("GET", "GetControlAreas").json(), ControlArea)

    def get_access_points(self):
        return _handle_response(self.logic("GET", "GetAccessPoints").json(), AccessPoint)

    # =============================================================================================
    def get_card_events(self, dto: GetCardEvents) -> GetCardEvents:
        return _handle_response((self.logic("GET", "GetCardEvents", params=dto.dict())).json(), OutCardEvents)

    def get_attendance(self, dto: Attendance) -> Attendance:
        return _handle_response(self.logic("GET", "GetAttendance", params=dto.dict() if dto else {}).json(),
                                OutAttendance)

#
# class BastionPass(BastionV2):
#
#     def get_bastion_pass_count(self):
#         response = self.logic("GET", "GetPassCount")
#
#     def get_bastion_passes_by_person(self):
#         response = self.logic("GET", "GetPassesByPerson")
#
#     def return_bastion_pass_for_card(self):
#         response = self.logic("PUT", "PutPass")
#
#
# class BastionMaterialPass(BastionV2):
#     def create_or_update_bastion_material_pass(self, claim: bool = False, dto: CreateMaterialPassInDto = None) -> str:
#         return _handle_response(self.logic("PUT", "PutMVPass", params={"issuePass ": claim}, dto=dto.dict()))
#
#     def get_bastion_material_pass_by_pass_id(self):
#         response = self.logic("GET", "IssueMVPass")
#
#     def ban_bastion_material_pass(self):
#         response = self.logic("GET", "WithdrawMVPass")
#
#     def get_bastion_material_pass(self):
#         response = self.logic("GET", "GetMVPasses")
#
#     def get_bastion_material_pass_by_person(self):
#         response = self.logic("POST", "GetMVPassesByPersonPass")
#
#     def create_or_update_bastion_car_pass(self):
#         response = self.logic("PUT", "PutCarPass")
#
#


#
#
# class BastionCardPass(BastionV2):
#
#
#     def get_bastion_car_passes(self):
#         response = self.logic("GET", "GetCarPasses")
#
#     def get_bastion_car_passes_by_person_pass(self):
#         response = self.logic("POST", "GetCarPassesByPersonPass")
#
#     def issue_bastion_car_pass_by_claim(self):
#         response = self.logic("GET", "IssueCarPass")
#
#     def banned_bastion_car_pass(self):
#         response = self.logic("GET", "WithdrawCarPass")
