import threading
from typing import Optional

from pydantic import BaseModel

from prowler.lib.logger import logger
from prowler.lib.scan_filters.scan_filters import is_resource_filtered
from prowler.providers.aws.aws_provider import generate_regional_clients


################## SecretsManager
class SecretsManager:
    def __init__(self, audit_info):
        self.service = "secretsmanager"
        self.session = audit_info.audit_session
        self.audited_account = audit_info.audited_account
        self.audit_resources = audit_info.audit_resources
        self.regional_clients = generate_regional_clients(self.service, audit_info)
        self.secrets = {}
        self.__threading_call__(self.__list_secrets__)

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

    def __list_secrets__(self, regional_client):
        logger.info("SecretsManager - Listing Secrets...")
        try:
            list_secrets_paginator = regional_client.get_paginator("list_secrets")
            for page in list_secrets_paginator.paginate():
                for secret in page["SecretList"]:
                    if not self.audit_resources or (
                        is_resource_filtered(secret["ARN"], self.audit_resources)
                    ):
                        # We must use the Secret ARN as the dict key to have unique keys
                        self.secrets[secret["ARN"]] = Secret(
                            arn=secret["ARN"],
                            name=secret["Name"],
                            region=regional_client.region,
                            tags=secret.get("Tags"),
                        )
                        if "RotationEnabled" in secret:
                            self.secrets[secret["ARN"]].rotation_enabled = secret[
                                "RotationEnabled"
                            ]

        except Exception as error:
            logger.error(
                f"{regional_client.region} --"
                f" {error.__class__.__name__}[{error.__traceback__.tb_lineno}]:"
                f" {error}"
            )


class Secret(BaseModel):
    arn: str
    name: str
    region: str
    rotation_enabled: bool = False
    tags: Optional[list] = []
