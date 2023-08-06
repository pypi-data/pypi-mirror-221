from typing import Optional

from anyscale.sdk.anyscale_client.api.default_api import DefaultApi as BaseApi
from anyscale.sdk.anyscale_client.models.cloud import Cloud
from anyscale.sdk.anyscale_client.models.cluster_management_stack_versions import (
    ClusterManagementStackVersions,
)


def _is_v2_cloud(base_api: BaseApi, cloud_id: str) -> bool:
    cloud: Cloud = base_api.get_cloud(cloud_id).result
    cloud_version: Optional[
        ClusterManagementStackVersions
    ] = cloud.cluster_management_stack_version
    return not cloud_version or cloud_version == ClusterManagementStackVersions.V2
