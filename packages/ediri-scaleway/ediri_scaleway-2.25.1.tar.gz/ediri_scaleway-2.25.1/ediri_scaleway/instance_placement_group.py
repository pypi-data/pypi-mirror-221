# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InstancePlacementGroupArgs', 'InstancePlacementGroup']

@pulumi.input_type
class InstancePlacementGroupArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_mode: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstancePlacementGroup resource.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[str] policy_mode: The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        :param pulumi.Input[str] policy_type: The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        :param pulumi.Input[str] project_id: `project_id`) The ID of the project the placement group is associated with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the placement group.
        :param pulumi.Input[str] zone: `zone`) The zone in which the placement group should be created.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_mode is not None:
            pulumi.set(__self__, "policy_mode", policy_mode)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the placement group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyMode")
    def policy_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        """
        return pulumi.get(self, "policy_mode")

    @policy_mode.setter
    def policy_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_mode", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        `project_id`) The ID of the project the placement group is associated with.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of tags to apply to the placement group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        `zone`) The zone in which the placement group should be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _InstancePlacementGroupState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 policy_mode: Optional[pulumi.Input[str]] = None,
                 policy_respected: Optional[pulumi.Input[bool]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstancePlacementGroup resources.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[str] organization_id: The organization ID the placement group is associated with.
        :param pulumi.Input[str] policy_mode: The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        :param pulumi.Input[bool] policy_respected: Is true when the policy is respected.
        :param pulumi.Input[str] policy_type: The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        :param pulumi.Input[str] project_id: `project_id`) The ID of the project the placement group is associated with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the placement group.
        :param pulumi.Input[str] zone: `zone`) The zone in which the placement group should be created.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if policy_mode is not None:
            pulumi.set(__self__, "policy_mode", policy_mode)
        if policy_respected is not None:
            pulumi.set(__self__, "policy_respected", policy_respected)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the placement group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The organization ID the placement group is associated with.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="policyMode")
    def policy_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        """
        return pulumi.get(self, "policy_mode")

    @policy_mode.setter
    def policy_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_mode", value)

    @property
    @pulumi.getter(name="policyRespected")
    def policy_respected(self) -> Optional[pulumi.Input[bool]]:
        """
        Is true when the policy is respected.
        """
        return pulumi.get(self, "policy_respected")

    @policy_respected.setter
    def policy_respected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "policy_respected", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[str]]:
        """
        The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        `project_id`) The ID of the project the placement group is associated with.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of tags to apply to the placement group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        `zone`) The zone in which the placement group should be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class InstancePlacementGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_mode: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages Compute Instance Placement Groups. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653).

        ## Example Usage

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        availability_group = scaleway.InstancePlacementGroup("availabilityGroup")
        ```

        ## Import

        Placement groups can be imported using the `{zone}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/instancePlacementGroup:InstancePlacementGroup availability_group fr-par-1/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[str] policy_mode: The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        :param pulumi.Input[str] policy_type: The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        :param pulumi.Input[str] project_id: `project_id`) The ID of the project the placement group is associated with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the placement group.
        :param pulumi.Input[str] zone: `zone`) The zone in which the placement group should be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstancePlacementGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages Compute Instance Placement Groups. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653).

        ## Example Usage

        ```python
        import pulumi
        import ediri_scaleway as scaleway

        availability_group = scaleway.InstancePlacementGroup("availabilityGroup")
        ```

        ## Import

        Placement groups can be imported using the `{zone}/{id}`, e.g. bash

        ```sh
         $ pulumi import scaleway:index/instancePlacementGroup:InstancePlacementGroup availability_group fr-par-1/11111111-1111-1111-1111-111111111111
        ```

        :param str resource_name: The name of the resource.
        :param InstancePlacementGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstancePlacementGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_mode: Optional[pulumi.Input[str]] = None,
                 policy_type: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstancePlacementGroupArgs.__new__(InstancePlacementGroupArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["policy_mode"] = policy_mode
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["policy_respected"] = None
        super(InstancePlacementGroup, __self__).__init__(
            'scaleway:index/instancePlacementGroup:InstancePlacementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            policy_mode: Optional[pulumi.Input[str]] = None,
            policy_respected: Optional[pulumi.Input[bool]] = None,
            policy_type: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstancePlacementGroup':
        """
        Get an existing InstancePlacementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the placement group.
        :param pulumi.Input[str] organization_id: The organization ID the placement group is associated with.
        :param pulumi.Input[str] policy_mode: The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        :param pulumi.Input[bool] policy_respected: Is true when the policy is respected.
        :param pulumi.Input[str] policy_type: The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        :param pulumi.Input[str] project_id: `project_id`) The ID of the project the placement group is associated with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of tags to apply to the placement group.
        :param pulumi.Input[str] zone: `zone`) The zone in which the placement group should be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstancePlacementGroupState.__new__(_InstancePlacementGroupState)

        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["policy_mode"] = policy_mode
        __props__.__dict__["policy_respected"] = policy_respected
        __props__.__dict__["policy_type"] = policy_type
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return InstancePlacementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the placement group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The organization ID the placement group is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="policyMode")
    def policy_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The [policy mode](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `optional` or `enforced`.
        """
        return pulumi.get(self, "policy_mode")

    @property
    @pulumi.getter(name="policyRespected")
    def policy_respected(self) -> pulumi.Output[bool]:
        """
        Is true when the policy is respected.
        """
        return pulumi.get(self, "policy_respected")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        The [policy type](https://developers.scaleway.com/en/products/instance/api/#placement-groups-d8f653) of the placement group. Possible values are: `low_latency` or `max_availability`.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        `project_id`) The ID of the project the placement group is associated with.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of tags to apply to the placement group.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        `zone`) The zone in which the placement group should be created.
        """
        return pulumi.get(self, "zone")

