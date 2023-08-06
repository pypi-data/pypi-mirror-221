from pydantic import BaseModel

from prowler.lib.logger import logger
from prowler.providers.gcp.gcp_provider import generate_client


################## CloudResourceManager
class CloudResourceManager:
    def __init__(self, audit_info):
        self.service = "cloudresourcemanager"
        self.api_version = "v1"
        self.region = "global"
        self.project_ids = audit_info.project_ids
        self.client = generate_client(self.service, self.api_version, audit_info)
        self.bindings = []
        self.projects = []
        self.organizations = []
        self.__get_iam_policy__()
        self.__get_organizations__()

    def __get_client__(self):
        return self.client

    def __get_iam_policy__(self):
        for project_id in self.project_ids:
            try:
                policy = (
                    self.client.projects().getIamPolicy(resource=project_id).execute()
                )
                audit_logging = False
                if policy.get("auditConfigs"):
                    audit_logging = True
                self.projects.append(
                    Project(id=project_id, audit_logging=audit_logging)
                )
                for binding in policy["bindings"]:
                    self.bindings.append(
                        Binding(
                            role=binding["role"],
                            members=binding["members"],
                            project_id=project_id,
                        )
                    )
            except Exception as error:
                logger.error(
                    f"{self.region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
                )

    def __get_organizations__(self):
        try:
            response = self.client.organizations().search().execute()
            for org in response["organizations"]:
                self.organizations.append(
                    Organization(id=org["name"].split("/")[-1], name=org["displayName"])
                )
        except Exception as error:
            logger.error(
                f"{self.region} -- {error.__class__.__name__}[{error.__traceback__.tb_lineno}]: {error}"
            )


class Binding(BaseModel):
    role: str
    members: list
    project_id: str


class Project(BaseModel):
    id: str
    audit_logging: bool


class Organization(BaseModel):
    id: str
    name: str
