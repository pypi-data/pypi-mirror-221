
from loguru import logger

from bastion_integration.dto.attendance_dto import Attendance
from bastion_integration.dto.card_dto import GetCardEvents
from bastion_integration.dto.config import BastionConfig
from bastion_integration.dto.core_dto import Command, Object
from bastion_integration.dto.department_dto import DepartmentDto
from bastion_integration.dto.device_dto import DeviceDto
from bastion_integration.dto.organization_dto import OrganizationDto
from bastion_integration.dto.pass_dto import PassDto, GetPassInDto
from bastion_integration.logic import BastionV2, BastionV3


class Core:
    def __init__(self, config: BastionConfig):
        self.bastion = BastionV2() if config.bastion_version == 2 else BastionV3() if config.bastion_version == 3 else None
        self.config = config

    def autarization(self):
        self.bastion.autarization()

    def init(self):
        self.bastion.config = self.config

    def get_servers(self):
        self.bastion.get_servers()
        if self.config.debug_log:
            logger.debug(self.bastion.bastion_servers)
        return self.bastion.bastion_servers

    # =============================================================================================
    def _create(self, dto: OrganizationDto.Create | DepartmentDto.Create | PassDto.Create, object: Object):
        match object:
            case Object.ORGANIZATION:
                return self.bastion.create_organization(dto.organization)
            case Object.DEPARTMENT:
                return self.bastion.create_department(dto.department)
            case Object.PASS:
                return self.bastion.create_pass(dto=dto.pass_info, use_access_levels=dto.use_access_levels)
            case _:
                raise NotImplementedError

    # =============================================================================================
    def _update(self, dto: OrganizationDto.Update | DepartmentDto.Update | PassDto.Update, object: Object):
        match object:
            case Object.ORGANIZATION:
                return self.bastion.update_organization(new_org_name=dto.new_name, dto=dto.organization)
            case Object.DEPARTMENT:
                return self.bastion.update_department(new_name=dto.new_name, dto=dto.department)
            case Object.PASS:
                return self.bastion.update_pass(dto=dto.pass_info, use_access_levels=dto.use_access_levels)
            case _:
                raise NotImplementedError

    # =============================================================================================
    def _delete(self, dto: OrganizationDto.Delete | DepartmentDto.Delete, object: Object):
        match object:
            case Object.ORGANIZATION:
                return self.bastion.delete_organization(dto=dto.organization)
            case Object.DEPARTMENT:
                return self.bastion.delete_department(dto=dto.department)
            case _:
                raise NotImplementedError

    # =============================================================================================
    def _get(self, dto: OrganizationDto.Get |
                        DepartmentDto.Get |
                        GetPassInDto |
                        GetCardEvents |
                        Attendance | DeviceDto, object: Object):
        match object:
            case object.ORGANIZATION:
                return self.bastion.get_organisations(organizations_names=dto.name)
            case object.DEPARTMENT:
                return self.bastion.get_department(organization_name=dto.organization_name)
            case object.PASS:
                return self.bastion.get_passes(dto=dto)
            case object.ENTRY_POINT:
                return self.bastion.get_entry_points()
            case object.ACCESS_LEVELS:
                return self.bastion.get_access_levels()
            case object.CONTROL_AREA:
                return self.bastion.get_control_areas()
            case object.ACCESS_POINT:
                return self.bastion.get_access_points()
            case object.CARD_EVENT:
                return self.bastion.get_card_events(dto=dto)
            case object.ATTENDANCE:
                return self.bastion.get_attendance(dto=dto)
            case object.DEVICE:
                return self.bastion.get_devices(dto=dto)
            case _:
                raise NotImplementedError

    # =============================================================================================
    def logic(self, command: Command, object: Object, dto):
        match command:
            case Command.CREATE:
                response = self._create(dto, object)
            case Command.UPDATE:
                response = self._update(dto, object)
            case Command.DELETE:
                response = self._delete(dto, object)
            case Command.GET:
                response = self._get(dto, object)
            case command.BLOCK_PASS:
                response = self.bastion.block_pass(card_code=dto.card_code, comment=dto.comment)
            case command.UNLOCK_PASS:
                response = self.bastion.unblock_pass(card_code=dto.card_code)
            case command.ARCHIVE_PASS:
                response = self.bastion.archive_pass(card_code=dto.card_code)
            case command.ISSUE_PASS:
                response = self.bastion.issue_pass(dto=dto)
            case _:
                raise NotImplementedError
        if self.config.debug_log:
            logger.debug(f"\nCommand: {command}, \nObject: {object}, \nDTO: {dto}\nResponse: {response}")
        return response
