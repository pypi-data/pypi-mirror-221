# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetLbRoutesResult',
    'AwaitableGetLbRoutesResult',
    'get_lb_routes',
    'get_lb_routes_output',
]

@pulumi.output_type
class GetLbRoutesResult:
    """
    A collection of values returned by getLbRoutes.
    """
    def __init__(__self__, frontend_id=None, id=None, organization_id=None, project_id=None, routes=None, zone=None):
        if frontend_id and not isinstance(frontend_id, str):
            raise TypeError("Expected argument 'frontend_id' to be a str")
        pulumi.set(__self__, "frontend_id", frontend_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if routes and not isinstance(routes, list):
            raise TypeError("Expected argument 'routes' to be a list")
        pulumi.set(__self__, "routes", routes)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[str]:
        return pulumi.get(self, "frontend_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def routes(self) -> Sequence['outputs.GetLbRoutesRouteResult']:
        """
        List of found routes
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


class AwaitableGetLbRoutesResult(GetLbRoutesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLbRoutesResult(
            frontend_id=self.frontend_id,
            id=self.id,
            organization_id=self.organization_id,
            project_id=self.project_id,
            routes=self.routes,
            zone=self.zone)


def get_lb_routes(frontend_id: Optional[str] = None,
                  project_id: Optional[str] = None,
                  zone: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLbRoutesResult:
    """
    Gets information about multiple Load Balancer Routes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    by_frontend_id = scaleway.get_lb_routes(frontend_id=scaleway_lb_frontend["frt01"]["id"])
    my_key = scaleway.get_lb_routes(frontend_id="11111111-1111-1111-1111-111111111111",
        zone="fr-par-2")
    ```


    :param str frontend_id: The frontend ID origin of redirection used as a filter. routes with a frontend ID like it are listed.
    :param str zone: `zone`) The zone in which routes exist.
    """
    __args__ = dict()
    __args__['frontendId'] = frontend_id
    __args__['projectId'] = project_id
    __args__['zone'] = zone
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scaleway:index/getLbRoutes:getLbRoutes', __args__, opts=opts, typ=GetLbRoutesResult).value

    return AwaitableGetLbRoutesResult(
        frontend_id=pulumi.get(__ret__, 'frontend_id'),
        id=pulumi.get(__ret__, 'id'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        routes=pulumi.get(__ret__, 'routes'),
        zone=pulumi.get(__ret__, 'zone'))


@_utilities.lift_output_func(get_lb_routes)
def get_lb_routes_output(frontend_id: Optional[pulumi.Input[Optional[str]]] = None,
                         project_id: Optional[pulumi.Input[Optional[str]]] = None,
                         zone: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLbRoutesResult]:
    """
    Gets information about multiple Load Balancer Routes.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_scaleway as scaleway

    by_frontend_id = scaleway.get_lb_routes(frontend_id=scaleway_lb_frontend["frt01"]["id"])
    my_key = scaleway.get_lb_routes(frontend_id="11111111-1111-1111-1111-111111111111",
        zone="fr-par-2")
    ```


    :param str frontend_id: The frontend ID origin of redirection used as a filter. routes with a frontend ID like it are listed.
    :param str zone: `zone`) The zone in which routes exist.
    """
    ...
