# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetFunctionResult',
    'AwaitableGetFunctionResult',
    'get_function',
    'get_function_output',
]

@pulumi.output_type
class GetFunctionResult:
    """
    A collection of values returned by getFunction.
    """
    def __init__(__self__, cpu_limit=None, deploy=None, description=None, domain_name=None, environment_variables=None, function_id=None, handler=None, http_option=None, id=None, max_scale=None, memory_limit=None, min_scale=None, name=None, namespace_id=None, organization_id=None, privacy=None, project_id=None, region=None, runtime=None, secret_environment_variables=None, timeout=None, zip_file=None, zip_hash=None):
        if cpu_limit and not isinstance(cpu_limit, int):
            raise TypeError("Expected argument 'cpu_limit' to be a int")
        pulumi.set(__self__, "cpu_limit", cpu_limit)
        if deploy and not isinstance(deploy, bool):
            raise TypeError("Expected argument 'deploy' to be a bool")
        pulumi.set(__self__, "deploy", deploy)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if environment_variables and not isinstance(environment_variables, dict):
            raise TypeError("Expected argument 'environment_variables' to be a dict")
        pulumi.set(__self__, "environment_variables", environment_variables)
        if function_id and not isinstance(function_id, str):
            raise TypeError("Expected argument 'function_id' to be a str")
        pulumi.set(__self__, "function_id", function_id)
        if handler and not isinstance(handler, str):
            raise TypeError("Expected argument 'handler' to be a str")
        pulumi.set(__self__, "handler", handler)
        if http_option and not isinstance(http_option, str):
            raise TypeError("Expected argument 'http_option' to be a str")
        pulumi.set(__self__, "http_option", http_option)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_scale and not isinstance(max_scale, int):
            raise TypeError("Expected argument 'max_scale' to be a int")
        pulumi.set(__self__, "max_scale", max_scale)
        if memory_limit and not isinstance(memory_limit, int):
            raise TypeError("Expected argument 'memory_limit' to be a int")
        pulumi.set(__self__, "memory_limit", memory_limit)
        if min_scale and not isinstance(min_scale, int):
            raise TypeError("Expected argument 'min_scale' to be a int")
        pulumi.set(__self__, "min_scale", min_scale)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace_id and not isinstance(namespace_id, str):
            raise TypeError("Expected argument 'namespace_id' to be a str")
        pulumi.set(__self__, "namespace_id", namespace_id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if privacy and not isinstance(privacy, str):
            raise TypeError("Expected argument 'privacy' to be a str")
        pulumi.set(__self__, "privacy", privacy)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if runtime and not isinstance(runtime, str):
            raise TypeError("Expected argument 'runtime' to be a str")
        pulumi.set(__self__, "runtime", runtime)
        if secret_environment_variables and not isinstance(secret_environment_variables, dict):
            raise TypeError("Expected argument 'secret_environment_variables' to be a dict")
        pulumi.set(__self__, "secret_environment_variables", secret_environment_variables)
        if timeout and not isinstance(timeout, int):
            raise TypeError("Expected argument 'timeout' to be a int")
        pulumi.set(__self__, "timeout", timeout)
        if zip_file and not isinstance(zip_file, str):
            raise TypeError("Expected argument 'zip_file' to be a str")
        pulumi.set(__self__, "zip_file", zip_file)
        if zip_hash and not isinstance(zip_hash, str):
            raise TypeError("Expected argument 'zip_hash' to be a str")
        pulumi.set(__self__, "zip_hash", zip_hash)

    @property
    @pulumi.getter(name="cpuLimit")
    def cpu_limit(self) -> int:
        return pulumi.get(self, "cpu_limit")

    @property
    @pulumi.getter
    def deploy(self) -> bool:
        return pulumi.get(self, "deploy")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Mapping[str, str]:
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="functionId")
    def function_id(self) -> Optional[str]:
        return pulumi.get(self, "function_id")

    @property
    @pulumi.getter
    def handler(self) -> str:
        return pulumi.get(self, "handler")

    @property
    @pulumi.getter(name="httpOption")
    def http_option(self) -> str:
        return pulumi.get(self, "http_option")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxScale")
    def max_scale(self) -> int:
        return pulumi.get(self, "max_scale")

    @property
    @pulumi.getter(name="memoryLimit")
    def memory_limit(self) -> int:
        return pulumi.get(self, "memory_limit")

    @property
    @pulumi.getter(name="minScale")
    def min_scale(self) -> int:
        return pulumi.get(self, "min_scale")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> str:
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def privacy(self) -> str:
        return pulumi.get(self, "privacy")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def runtime(self) -> str:
        return pulumi.get(self, "runtime")

    @property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(self) -> Mapping[str, str]:
        return pulumi.get(self, "secret_environment_variables")

    @property
    @pulumi.getter
    def timeout(self) -> int:
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> str:
        return pulumi.get(self, "zip_file")

    @property
    @pulumi.getter(name="zipHash")
    def zip_hash(self) -> str:
        return pulumi.get(self, "zip_hash")


class AwaitableGetFunctionResult(GetFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFunctionResult(
            cpu_limit=self.cpu_limit,
            deploy=self.deploy,
            description=self.description,
            domain_name=self.domain_name,
            environment_variables=self.environment_variables,
            function_id=self.function_id,
            handler=self.handler,
            http_option=self.http_option,
            id=self.id,
            max_scale=self.max_scale,
            memory_limit=self.memory_limit,
            min_scale=self.min_scale,
            name=self.name,
            namespace_id=self.namespace_id,
            organization_id=self.organization_id,
            privacy=self.privacy,
            project_id=self.project_id,
            region=self.region,
            runtime=self.runtime,
            secret_environment_variables=self.secret_environment_variables,
            timeout=self.timeout,
            zip_file=self.zip_file,
            zip_hash=self.zip_hash)


def get_function(function_id: Optional[str] = None,
                 name: Optional[str] = None,
                 namespace_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFunctionResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['functionId'] = function_id
    __args__['name'] = name
    __args__['namespaceId'] = namespace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('scaleway:index/getFunction:getFunction', __args__, opts=opts, typ=GetFunctionResult).value

    return AwaitableGetFunctionResult(
        cpu_limit=pulumi.get(__ret__, 'cpu_limit'),
        deploy=pulumi.get(__ret__, 'deploy'),
        description=pulumi.get(__ret__, 'description'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        environment_variables=pulumi.get(__ret__, 'environment_variables'),
        function_id=pulumi.get(__ret__, 'function_id'),
        handler=pulumi.get(__ret__, 'handler'),
        http_option=pulumi.get(__ret__, 'http_option'),
        id=pulumi.get(__ret__, 'id'),
        max_scale=pulumi.get(__ret__, 'max_scale'),
        memory_limit=pulumi.get(__ret__, 'memory_limit'),
        min_scale=pulumi.get(__ret__, 'min_scale'),
        name=pulumi.get(__ret__, 'name'),
        namespace_id=pulumi.get(__ret__, 'namespace_id'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        privacy=pulumi.get(__ret__, 'privacy'),
        project_id=pulumi.get(__ret__, 'project_id'),
        region=pulumi.get(__ret__, 'region'),
        runtime=pulumi.get(__ret__, 'runtime'),
        secret_environment_variables=pulumi.get(__ret__, 'secret_environment_variables'),
        timeout=pulumi.get(__ret__, 'timeout'),
        zip_file=pulumi.get(__ret__, 'zip_file'),
        zip_hash=pulumi.get(__ret__, 'zip_hash'))


@_utilities.lift_output_func(get_function)
def get_function_output(function_id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        namespace_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFunctionResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
