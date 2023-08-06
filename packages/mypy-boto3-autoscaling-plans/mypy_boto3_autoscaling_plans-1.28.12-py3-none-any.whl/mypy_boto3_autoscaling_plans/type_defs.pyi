"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/type_defs/)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.type_defs import TagFilterOutputTypeDef

    data: TagFilterOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ForecastDataTypeType,
    LoadMetricTypeType,
    MetricStatisticType,
    PredictiveScalingMaxCapacityBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingMetricTypeType,
    ScalingPlanStatusCodeType,
    ScalingPolicyUpdateBehaviorType,
    ScalingStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "TagFilterOutputTypeDef",
    "TagFilterTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "MetricDimensionOutputTypeDef",
    "MetricDimensionTypeDef",
    "DatapointTypeDef",
    "DeleteScalingPlanRequestRequestTypeDef",
    "DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedLoadMetricSpecificationOutputTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationOutputTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "ApplicationSourceOutputTypeDef",
    "ApplicationSourceTypeDef",
    "CustomizedLoadMetricSpecificationOutputTypeDef",
    "CustomizedScalingMetricSpecificationOutputTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    "DescribeScalingPlansRequestRequestTypeDef",
    "TargetTrackingConfigurationOutputTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ScalingInstructionOutputTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPlanResourceTypeDef",
    "CreateScalingPlanRequestRequestTypeDef",
    "UpdateScalingPlanRequestRequestTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
)

TagFilterOutputTypeDef = TypedDict(
    "TagFilterOutputTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
    total=False,
)

CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef",
    {
        "ScalingPlanVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionOutputTypeDef = TypedDict(
    "MetricDimensionOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
    total=False,
)

DeleteScalingPlanRequestRequestTypeDef = TypedDict(
    "DeleteScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)

_RequiredDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef = TypedDict(
    "_RequiredDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)
_OptionalDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef = TypedDict(
    "_OptionalDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef(
    _RequiredDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef,
    _OptionalDescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef,
):
    pass

_RequiredDescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)
_OptionalDescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScalingPlanResourcesRequestRequestTypeDef(
    _RequiredDescribeScalingPlanResourcesRequestRequestTypeDef,
    _OptionalDescribeScalingPlanResourcesRequestRequestTypeDef,
):
    pass

GetScalingPlanResourceForecastDataRequestRequestTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ForecastDataType": ForecastDataTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPredefinedLoadMetricSpecificationOutputTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationOutputTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
    },
)
_OptionalPredefinedLoadMetricSpecificationOutputTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationOutputTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedLoadMetricSpecificationOutputTypeDef(
    _RequiredPredefinedLoadMetricSpecificationOutputTypeDef,
    _OptionalPredefinedLoadMetricSpecificationOutputTypeDef,
):
    pass

_RequiredPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
    },
)
_OptionalPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef,
    _OptionalPredefinedLoadMetricSpecificationTypeDef,
):
    pass

_RequiredPredefinedScalingMetricSpecificationOutputTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationOutputTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
    },
)
_OptionalPredefinedScalingMetricSpecificationOutputTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationOutputTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedScalingMetricSpecificationOutputTypeDef(
    _RequiredPredefinedScalingMetricSpecificationOutputTypeDef,
    _OptionalPredefinedScalingMetricSpecificationOutputTypeDef,
):
    pass

_RequiredPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
    },
)
_OptionalPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationTypeDef",
    {
        "ResourceLabel": str,
    },
    total=False,
)

class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef,
    _OptionalPredefinedScalingMetricSpecificationTypeDef,
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

ApplicationSourceOutputTypeDef = TypedDict(
    "ApplicationSourceOutputTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": List[TagFilterOutputTypeDef],
    },
    total=False,
)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": str,
        "TagFilters": Sequence[TagFilterTypeDef],
    },
    total=False,
)

_RequiredCustomizedLoadMetricSpecificationOutputTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationOutputTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedLoadMetricSpecificationOutputTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationOutputTypeDef",
    {
        "Dimensions": List[MetricDimensionOutputTypeDef],
        "Unit": str,
    },
    total=False,
)

class CustomizedLoadMetricSpecificationOutputTypeDef(
    _RequiredCustomizedLoadMetricSpecificationOutputTypeDef,
    _OptionalCustomizedLoadMetricSpecificationOutputTypeDef,
):
    pass

_RequiredCustomizedScalingMetricSpecificationOutputTypeDef = TypedDict(
    "_RequiredCustomizedScalingMetricSpecificationOutputTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedScalingMetricSpecificationOutputTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationOutputTypeDef",
    {
        "Dimensions": List[MetricDimensionOutputTypeDef],
        "Unit": str,
    },
    total=False,
)

class CustomizedScalingMetricSpecificationOutputTypeDef(
    _RequiredCustomizedScalingMetricSpecificationOutputTypeDef,
    _OptionalCustomizedScalingMetricSpecificationOutputTypeDef,
):
    pass

_RequiredCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationTypeDef",
    {
        "Dimensions": Sequence[MetricDimensionTypeDef],
        "Unit": str,
    },
    total=False,
)

class CustomizedLoadMetricSpecificationTypeDef(
    _RequiredCustomizedLoadMetricSpecificationTypeDef,
    _OptionalCustomizedLoadMetricSpecificationTypeDef,
):
    pass

_RequiredCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
    },
)
_OptionalCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationTypeDef",
    {
        "Dimensions": Sequence[MetricDimensionTypeDef],
        "Unit": str,
    },
    total=False,
)

class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef,
    _OptionalCustomizedScalingMetricSpecificationTypeDef,
):
    pass

GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List[DatapointTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef = TypedDict(
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    {
        "ScalingPlanNames": Sequence[str],
        "ScalingPlanVersion": int,
        "ApplicationSources": Sequence[ApplicationSourceTypeDef],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeScalingPlansRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlansRequestRequestTypeDef",
    {
        "ScalingPlanNames": Sequence[str],
        "ScalingPlanVersion": int,
        "ApplicationSources": Sequence[ApplicationSourceTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredTargetTrackingConfigurationOutputTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationOutputTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalTargetTrackingConfigurationOutputTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationOutputTypeDef",
    {
        "PredefinedScalingMetricSpecification": PredefinedScalingMetricSpecificationOutputTypeDef,
        "CustomizedScalingMetricSpecification": CustomizedScalingMetricSpecificationOutputTypeDef,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

class TargetTrackingConfigurationOutputTypeDef(
    _RequiredTargetTrackingConfigurationOutputTypeDef,
    _OptionalTargetTrackingConfigurationOutputTypeDef,
):
    pass

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": PredefinedScalingMetricSpecificationTypeDef,
        "CustomizedScalingMetricSpecification": CustomizedScalingMetricSpecificationTypeDef,
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)

class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass

_RequiredScalingInstructionOutputTypeDef = TypedDict(
    "_RequiredScalingInstructionOutputTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[TargetTrackingConfigurationOutputTypeDef],
    },
)
_OptionalScalingInstructionOutputTypeDef = TypedDict(
    "_OptionalScalingInstructionOutputTypeDef",
    {
        "PredefinedLoadMetricSpecification": PredefinedLoadMetricSpecificationOutputTypeDef,
        "CustomizedLoadMetricSpecification": CustomizedLoadMetricSpecificationOutputTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": PredictiveScalingMaxCapacityBehaviorType,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": PredictiveScalingModeType,
        "ScalingPolicyUpdateBehavior": ScalingPolicyUpdateBehaviorType,
        "DisableDynamicScaling": bool,
    },
    total=False,
)

class ScalingInstructionOutputTypeDef(
    _RequiredScalingInstructionOutputTypeDef, _OptionalScalingInstructionOutputTypeDef
):
    pass

_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
    },
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": TargetTrackingConfigurationOutputTypeDef,
    },
    total=False,
)

class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass

_RequiredScalingInstructionTypeDef = TypedDict(
    "_RequiredScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": Sequence[TargetTrackingConfigurationTypeDef],
    },
)
_OptionalScalingInstructionTypeDef = TypedDict(
    "_OptionalScalingInstructionTypeDef",
    {
        "PredefinedLoadMetricSpecification": PredefinedLoadMetricSpecificationTypeDef,
        "CustomizedLoadMetricSpecification": CustomizedLoadMetricSpecificationTypeDef,
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": PredictiveScalingMaxCapacityBehaviorType,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": PredictiveScalingModeType,
        "ScalingPolicyUpdateBehavior": ScalingPolicyUpdateBehaviorType,
        "DisableDynamicScaling": bool,
    },
    total=False,
)

class ScalingInstructionTypeDef(
    _RequiredScalingInstructionTypeDef, _OptionalScalingInstructionTypeDef
):
    pass

_RequiredScalingPlanTypeDef = TypedDict(
    "_RequiredScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ApplicationSourceOutputTypeDef,
        "ScalingInstructions": List[ScalingInstructionOutputTypeDef],
        "StatusCode": ScalingPlanStatusCodeType,
    },
)
_OptionalScalingPlanTypeDef = TypedDict(
    "_OptionalScalingPlanTypeDef",
    {
        "StatusMessage": str,
        "StatusStartTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, _OptionalScalingPlanTypeDef):
    pass

_RequiredScalingPlanResourceTypeDef = TypedDict(
    "_RequiredScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
    },
)
_OptionalScalingPlanResourceTypeDef = TypedDict(
    "_OptionalScalingPlanResourceTypeDef",
    {
        "ScalingPolicies": List[ScalingPolicyTypeDef],
        "ScalingStatusMessage": str,
    },
    total=False,
)

class ScalingPlanResourceTypeDef(
    _RequiredScalingPlanResourceTypeDef, _OptionalScalingPlanResourceTypeDef
):
    pass

CreateScalingPlanRequestRequestTypeDef = TypedDict(
    "CreateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": Sequence[ScalingInstructionTypeDef],
    },
)

_RequiredUpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)
_OptionalUpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScalingPlanRequestRequestTypeDef",
    {
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": Sequence[ScalingInstructionTypeDef],
    },
    total=False,
)

class UpdateScalingPlanRequestRequestTypeDef(
    _RequiredUpdateScalingPlanRequestRequestTypeDef, _OptionalUpdateScalingPlanRequestRequestTypeDef
):
    pass

DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List[ScalingPlanTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[ScalingPlanResourceTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
