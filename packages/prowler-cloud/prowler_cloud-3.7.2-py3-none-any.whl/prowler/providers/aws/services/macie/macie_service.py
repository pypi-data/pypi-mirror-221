import threading

from pydantic import BaseModel

from prowler.lib.logger import logger
from prowler.providers.aws.aws_provider import generate_regional_clients


################## Macie
class Macie:
    def __init__(self, audit_info):
        self.service = "macie2"
        self.session = audit_info.audit_session
        self.audited_account = audit_info.audited_account
        self.audited_partition = audit_info.audited_partition
        self.audited_account_arn = audit_info.audited_account_arn
        self.regional_clients = generate_regional_clients(self.service, audit_info)
        self.sessions = []
        self.__threading_call__(self.__get_macie_session__)

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

    def __get_macie_session__(self, regional_client):
        logger.info("Macie - Get Macie Session...")
        try:
            self.sessions.append(
                Session(
                    status=regional_client.get_macie_session()["status"],
                    region=regional_client.region,
                )
            )

        except Exception as error:
            if "Macie is not enabled" in str(error):
                self.sessions.append(
                    Session(
                        status="DISABLED",
                        region=regional_client.region,
                    )
                )
            else:
                logger.error(
                    f"{regional_client.region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
                )


class Session(BaseModel):
    status: str
    region: str
