# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FlexibleIpArgs', 'FlexibleIp']

@pulumi.input_type
class FlexibleIpArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FlexibleIp resource.
        :param pulumi.Input[str] description: A description of the flexible IP.
        :param pulumi.Input[str] project_id: The project of the Flexible IP
        :param pulumi.Input[str] reverse: The reverse domain associated with this flexible IP.
        :param pulumi.Input[str] server_id: The ID of the associated server
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the flexible IP.
        :param pulumi.Input[str] zone: The zone of the Flexible IP
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if reverse is not None:
            pulumi.set(__self__, "reverse", reverse)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the flexible IP.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the Flexible IP
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def reverse(self) -> Optional[pulumi.Input[str]]:
        """
        The reverse domain associated with this flexible IP.
        """
        return pulumi.get(self, "reverse")

    @reverse.setter
    def reverse(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reverse", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the associated server
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of tags to apply to the flexible IP.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone of the Flexible IP
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _FlexibleIpState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FlexibleIp resources.
        :param pulumi.Input[str] created_at: The date and time of the creation of the Flexible IP (Format ISO 8601)
        :param pulumi.Input[str] description: A description of the flexible IP.
        :param pulumi.Input[str] ip_address: The IPv4 address of the Flexible IP
        :param pulumi.Input[str] mac_address: The MAC address of the server associated with this flexible IP
        :param pulumi.Input[str] organization_id: The organization of the Flexible IP
        :param pulumi.Input[str] project_id: The project of the Flexible IP
        :param pulumi.Input[str] reverse: The reverse domain associated with this flexible IP.
        :param pulumi.Input[str] server_id: The ID of the associated server
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the flexible IP.
        :param pulumi.Input[str] updated_at: The date and time of the last update of the Flexible IP (Format ISO 8601)
        :param pulumi.Input[str] zone: The zone of the Flexible IP
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if reverse is not None:
            pulumi.set(__self__, "reverse", reverse)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time of the creation of the Flexible IP (Format ISO 8601)
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the flexible IP.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address of the Flexible IP
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        """
        The MAC address of the server associated with this flexible IP
        """
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The organization of the Flexible IP
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the Flexible IP
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def reverse(self) -> Optional[pulumi.Input[str]]:
        """
        The reverse domain associated with this flexible IP.
        """
        return pulumi.get(self, "reverse")

    @reverse.setter
    def reverse(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reverse", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the associated server
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of tags to apply to the flexible IP.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time of the last update of the Flexible IP (Format ISO 8601)
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone of the Flexible IP
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class FlexibleIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages Scaleway flexible IPs.
        For more information, see [the documentation](https://developers.scaleway.com/en/products/flexible-ip/api).

        ## Examples

        ### Basic

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        main = scaleway.FlexibleIp("main", reverse="my-reverse.com")
        ```

        ### With zone

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        main = scaleway.FlexibleIp("main", zone="fr-par-2")
        ```

        ### With baremetal server

        ```python
        import pulumi
        import ediri_scaleway as scaleway
        import pulumi_scaleway as scaleway

        main_account_ssh_key = scaleway.AccountSshKey("mainAccountSshKey", public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILHy/M5FVm5ydLGcal3e5LNcfTalbeN7QL/ZGCvDEdqJ foobar@example.com")
        by_id = scaleway.get_baremetal_os(zone="fr-par-2",
            name="Ubuntu",
            version="20.04 LTS (Focal Fossa)")
        my_offer = scaleway.get_baremetal_offer(zone="fr-par-2",
            name="EM-A210R-HDD")
        base = scaleway.BaremetalServer("base",
            zone="fr-par-2",
            offer=my_offer.offer_id,
            os=by_id.os_id,
            ssh_key_ids=main_account_ssh_key.id)
        main_flexible_ip = scaleway.FlexibleIp("mainFlexibleIp",
            server_id=base.id,
            zone="fr-par-2")
        ```

        ## Import

        Flexible IPs can be imported using the `{zone}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/flexibleIp:FlexibleIp main fr-par-1/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the flexible IP.
        :param pulumi.Input[str] project_id: The project of the Flexible IP
        :param pulumi.Input[str] reverse: The reverse domain associated with this flexible IP.
        :param pulumi.Input[str] server_id: The ID of the associated server
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the flexible IP.
        :param pulumi.Input[str] zone: The zone of the Flexible IP
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FlexibleIpArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages Scaleway flexible IPs.
        For more information, see [the documentation](https://developers.scaleway.com/en/products/flexible-ip/api).

        ## Examples

        ### Basic

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        main = scaleway.FlexibleIp("main", reverse="my-reverse.com")
        ```

        ### With zone

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        main = scaleway.FlexibleIp("main", zone="fr-par-2")
        ```

        ### With baremetal server

        ```python
        import pulumi
        import ediri_scaleway as scaleway
        import pulumi_scaleway as scaleway

        main_account_ssh_key = scaleway.AccountSshKey("mainAccountSshKey", public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILHy/M5FVm5ydLGcal3e5LNcfTalbeN7QL/ZGCvDEdqJ foobar@example.com")
        by_id = scaleway.get_baremetal_os(zone="fr-par-2",
            name="Ubuntu",
            version="20.04 LTS (Focal Fossa)")
        my_offer = scaleway.get_baremetal_offer(zone="fr-par-2",
            name="EM-A210R-HDD")
        base = scaleway.BaremetalServer("base",
            zone="fr-par-2",
            offer=my_offer.offer_id,
            os=by_id.os_id,
            ssh_key_ids=main_account_ssh_key.id)
        main_flexible_ip = scaleway.FlexibleIp("mainFlexibleIp",
            server_id=base.id,
            zone="fr-par-2")
        ```

        ## Import

        Flexible IPs can be imported using the `{zone}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/flexibleIp:FlexibleIp main fr-par-1/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param FlexibleIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FlexibleIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FlexibleIpArgs.__new__(FlexibleIpArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["reverse"] = reverse
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["created_at"] = None
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["mac_address"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["updated_at"] = None
        super(FlexibleIp, __self__).__init__(
            'scaleway:index/flexibleIp:FlexibleIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            mac_address: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            reverse: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'FlexibleIp':
        """
        Get an existing FlexibleIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The date and time of the creation of the Flexible IP (Format ISO 8601)
        :param pulumi.Input[str] description: A description of the flexible IP.
        :param pulumi.Input[str] ip_address: The IPv4 address of the Flexible IP
        :param pulumi.Input[str] mac_address: The MAC address of the server associated with this flexible IP
        :param pulumi.Input[str] organization_id: The organization of the Flexible IP
        :param pulumi.Input[str] project_id: The project of the Flexible IP
        :param pulumi.Input[str] reverse: The reverse domain associated with this flexible IP.
        :param pulumi.Input[str] server_id: The ID of the associated server
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the flexible IP.
        :param pulumi.Input[str] updated_at: The date and time of the last update of the Flexible IP (Format ISO 8601)
        :param pulumi.Input[str] zone: The zone of the Flexible IP
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FlexibleIpState.__new__(_FlexibleIpState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["mac_address"] = mac_address
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["reverse"] = reverse
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["zone"] = zone
        return FlexibleIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time of the creation of the Flexible IP (Format ISO 8601)
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the flexible IP.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IPv4 address of the Flexible IP
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[str]:
        """
        The MAC address of the server associated with this flexible IP
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The organization of the Flexible IP
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project of the Flexible IP
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def reverse(self) -> pulumi.Output[str]:
        """
        The reverse domain associated with this flexible IP.
        """
        return pulumi.get(self, "reverse")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the associated server
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of tags to apply to the flexible IP.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The date and time of the last update of the Flexible IP (Format ISO 8601)
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone of the Flexible IP
        """
        return pulumi.get(self, "zone")

