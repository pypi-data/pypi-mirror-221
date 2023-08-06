import threading
from typing import Optional

from pydantic import BaseModel

from prowler.lib.logger import logger
from prowler.lib.scan_filters.scan_filters import is_resource_filtered
from prowler.providers.aws.aws_provider import generate_regional_clients


################## AppStream
class AppStream:
    def __init__(self, audit_info):
        self.service = "appstream"
        self.session = audit_info.audit_session
        self.audited_account = audit_info.audited_account
        self.audit_resources = audit_info.audit_resources
        self.regional_clients = generate_regional_clients(self.service, audit_info)
        self.fleets = []
        self.__threading_call__(self.__describe_fleets__)
        self.__list_tags_for_resource__()

    def __get_session__(self):
        return self.session

    def __threading_call__(self, call):
        threads = []
        for regional_client in self.regional_clients.values():
            threads.append(threading.Thread(target=call, args=(regional_client,)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def __describe_fleets__(self, regional_client):
        logger.info("AppStream - Describing Fleets...")
        try:
            describe_fleets_paginator = regional_client.get_paginator("describe_fleets")
            for page in describe_fleets_paginator.paginate():
                for fleet in page["Fleets"]:
                    if not self.audit_resources or (
                        is_resource_filtered(fleet["Arn"], self.audit_resources)
                    ):
                        self.fleets.append(
                            Fleet(
                                arn=fleet["Arn"],
                                name=fleet["Name"],
                                max_user_duration_in_seconds=fleet[
                                    "MaxUserDurationInSeconds"
                                ],
                                disconnect_timeout_in_seconds=fleet[
                                    "DisconnectTimeoutInSeconds"
                                ],
                                idle_disconnect_timeout_in_seconds=fleet.get(
                                    "IdleDisconnectTimeoutInSeconds"
                                ),
                                enable_default_internet_access=fleet[
                                    "EnableDefaultInternetAccess"
                                ],
                                region=regional_client.region,
                            )
                        )

        except Exception as error:
            logger.error(
                f"{regional_client.region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
            )

    def __list_tags_for_resource__(self):
        logger.info("AppStream - List Tags...")
        try:
            for fleet in self.fleets:
                regional_client = self.regional_clients[fleet.region]
                response = regional_client.list_tags_for_resource(
                    ResourceArn=fleet.arn
                )["Tags"]
                fleet.tags = [response]
        except Exception as error:
            logger.error(
                f"{regional_client.region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
            )


class Fleet(BaseModel):
    arn: str
    name: str
    max_user_duration_in_seconds: int
    disconnect_timeout_in_seconds: int
    idle_disconnect_timeout_in_seconds: Optional[int]
    enable_default_internet_access: bool
    region: str
    tags: Optional[list] = []
