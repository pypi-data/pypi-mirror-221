"""
Type annotations for cloudwatch service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ActionsSuppressedByType,
    AlarmTypeType,
    AnomalyDetectorStateValueType,
    AnomalyDetectorTypeType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
    StatusCodeType,
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
    "AlarmHistoryItemTypeDef",
    "RangeOutputTypeDef",
    "RangeTypeDef",
    "DimensionOutputTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteAlarmsInputRequestTypeDef",
    "DimensionTypeDef",
    "DeleteDashboardsInputRequestTypeDef",
    "DeleteInsightRulesInputRequestTypeDef",
    "PartialFailureTypeDef",
    "DeleteMetricStreamInputRequestTypeDef",
    "DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef",
    "DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef",
    "DescribeAlarmHistoryInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeAlarmsInputDescribeAlarmsPaginateTypeDef",
    "DescribeAlarmsInputRequestTypeDef",
    "DescribeInsightRulesInputRequestTypeDef",
    "InsightRuleTypeDef",
    "DimensionFilterTypeDef",
    "DisableAlarmActionsInputRequestTypeDef",
    "DisableInsightRulesInputRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableAlarmActionsInputRequestTypeDef",
    "EnableInsightRulesInputRequestTypeDef",
    "GetDashboardInputRequestTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportInputRequestTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "LabelOptionsTypeDef",
    "MessageDataTypeDef",
    "GetMetricStreamInputRequestTypeDef",
    "MetricStreamFilterOutputTypeDef",
    "GetMetricWidgetImageInputRequestTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "ListDashboardsInputListDashboardsPaginateTypeDef",
    "ListDashboardsInputRequestTypeDef",
    "ListManagedInsightRulesInputRequestTypeDef",
    "ListMetricStreamsInputRequestTypeDef",
    "MetricStreamEntryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "TagOutputTypeDef",
    "ManagedRuleStateTypeDef",
    "TagTypeDef",
    "StatisticSetTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricStreamStatisticsMetricOutputTypeDef",
    "MetricStreamStatisticsMetricTypeDef",
    "PaginatorConfigTypeDef",
    "PutDashboardInputRequestTypeDef",
    "PutMetricStreamOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SetAlarmStateInputAlarmSetStateTypeDef",
    "SetAlarmStateInputRequestTypeDef",
    "StartMetricStreamsInputRequestTypeDef",
    "StopMetricStreamsInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "AnomalyDetectorConfigurationOutputTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "MetricOutputTypeDef",
    "SingleMetricAnomalyDetectorOutputTypeDef",
    "ListDashboardsOutputTypeDef",
    "PutDashboardOutputTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "DescribeAlarmsForMetricInputRequestTypeDef",
    "DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef",
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    "GetMetricStatisticsInputMetricGetStatisticsTypeDef",
    "GetMetricStatisticsInputRequestTypeDef",
    "MetricTypeDef",
    "SingleMetricAnomalyDetectorTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "PutManagedInsightRulesOutputTypeDef",
    "DescribeAlarmsInputAlarmExistsWaitTypeDef",
    "DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "ListMetricsInputListMetricsPaginateTypeDef",
    "ListMetricsInputRequestTypeDef",
    "MetricDataResultTypeDef",
    "InsightRuleContributorTypeDef",
    "ListMetricStreamsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ManagedRuleDescriptionTypeDef",
    "ManagedRuleTypeDef",
    "PutCompositeAlarmInputRequestTypeDef",
    "PutInsightRuleInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "MetricDatumTypeDef",
    "MetricStreamStatisticsConfigurationOutputTypeDef",
    "MetricStreamStatisticsConfigurationTypeDef",
    "ListMetricsOutputTypeDef",
    "MetricStatOutputTypeDef",
    "MetricStatTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "ListManagedInsightRulesOutputTypeDef",
    "PutManagedInsightRulesInputRequestTypeDef",
    "PutMetricDataInputRequestTypeDef",
    "GetMetricStreamOutputTypeDef",
    "PutMetricStreamInputRequestTypeDef",
    "MetricDataQueryOutputTypeDef",
    "MetricDataQueryTypeDef",
    "MetricAlarmTypeDef",
    "MetricMathAnomalyDetectorOutputTypeDef",
    "GetMetricDataInputGetMetricDataPaginateTypeDef",
    "GetMetricDataInputRequestTypeDef",
    "MetricMathAnomalyDetectorTypeDef",
    "PutMetricAlarmInputMetricPutAlarmTypeDef",
    "PutMetricAlarmInputRequestTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "AnomalyDetectorTypeDef",
    "DeleteAnomalyDetectorInputRequestTypeDef",
    "PutAnomalyDetectorInputRequestTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
)

AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": str,
        "AlarmType": AlarmTypeType,
        "Timestamp": datetime,
        "HistoryItemType": HistoryItemTypeType,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

RangeOutputTypeDef = TypedDict(
    "RangeOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

DimensionOutputTypeDef = TypedDict(
    "DimensionOutputTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CompositeAlarmTypeDef = TypedDict(
    "CompositeAlarmTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmArn": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "AlarmDescription": str,
        "AlarmName": str,
        "AlarmRule": str,
        "InsufficientDataActions": List[str],
        "OKActions": List[str],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "StateValue": StateValueType,
        "StateTransitionedTimestamp": datetime,
        "ActionsSuppressedBy": ActionsSuppressedByType,
        "ActionsSuppressedReason": str,
        "ActionsSuppressor": str,
        "ActionsSuppressorWaitPeriod": int,
        "ActionsSuppressorExtensionPeriod": int,
    },
    total=False,
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {
        "DashboardName": str,
        "DashboardArn": str,
        "LastModified": datetime,
        "Size": int,
    },
    total=False,
)

DashboardValidationMessageTypeDef = TypedDict(
    "DashboardValidationMessageTypeDef",
    {
        "DataPath": str,
        "Message": str,
    },
    total=False,
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": StandardUnitType,
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

DeleteAlarmsInputRequestTypeDef = TypedDict(
    "DeleteAlarmsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DeleteDashboardsInputRequestTypeDef = TypedDict(
    "DeleteDashboardsInputRequestTypeDef",
    {
        "DashboardNames": Sequence[str],
    },
)

DeleteInsightRulesInputRequestTypeDef = TypedDict(
    "DeleteInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

PartialFailureTypeDef = TypedDict(
    "PartialFailureTypeDef",
    {
        "FailureResource": str,
        "ExceptionType": str,
        "FailureCode": str,
        "FailureDescription": str,
    },
    total=False,
)

DeleteMetricStreamInputRequestTypeDef = TypedDict(
    "DeleteMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef = TypedDict(
    "DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef",
    {
        "AlarmTypes": Sequence[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef = TypedDict(
    "DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef",
    {
        "AlarmName": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "ScanBy": ScanByType,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeAlarmHistoryInputRequestTypeDef = TypedDict(
    "DescribeAlarmHistoryInputRequestTypeDef",
    {
        "AlarmName": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeAlarmsInputDescribeAlarmsPaginateTypeDef = TypedDict(
    "DescribeAlarmsInputDescribeAlarmsPaginateTypeDef",
    {
        "AlarmNames": Sequence[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeAlarmsInputRequestTypeDef = TypedDict(
    "DescribeAlarmsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInsightRulesInputRequestTypeDef = TypedDict(
    "DescribeInsightRulesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredInsightRuleTypeDef = TypedDict(
    "_RequiredInsightRuleTypeDef",
    {
        "Name": str,
        "State": str,
        "Schema": str,
        "Definition": str,
    },
)
_OptionalInsightRuleTypeDef = TypedDict(
    "_OptionalInsightRuleTypeDef",
    {
        "ManagedRule": bool,
    },
    total=False,
)


class InsightRuleTypeDef(_RequiredInsightRuleTypeDef, _OptionalInsightRuleTypeDef):
    pass


_RequiredDimensionFilterTypeDef = TypedDict(
    "_RequiredDimensionFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalDimensionFilterTypeDef = TypedDict(
    "_OptionalDimensionFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, _OptionalDimensionFilterTypeDef):
    pass


DisableAlarmActionsInputRequestTypeDef = TypedDict(
    "DisableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

DisableInsightRulesInputRequestTypeDef = TypedDict(
    "DisableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAlarmActionsInputRequestTypeDef = TypedDict(
    "EnableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

EnableInsightRulesInputRequestTypeDef = TypedDict(
    "EnableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

GetDashboardInputRequestTypeDef = TypedDict(
    "GetDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
    },
)

GetDashboardOutputTypeDef = TypedDict(
    "GetDashboardOutputTypeDef",
    {
        "DashboardArn": str,
        "DashboardBody": str,
        "DashboardName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightRuleReportInputRequestTypeDef = TypedDict(
    "_RequiredGetInsightRuleReportInputRequestTypeDef",
    {
        "RuleName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetInsightRuleReportInputRequestTypeDef = TypedDict(
    "_OptionalGetInsightRuleReportInputRequestTypeDef",
    {
        "MaxContributorCount": int,
        "Metrics": Sequence[str],
        "OrderBy": str,
    },
    total=False,
)


class GetInsightRuleReportInputRequestTypeDef(
    _RequiredGetInsightRuleReportInputRequestTypeDef,
    _OptionalGetInsightRuleReportInputRequestTypeDef,
):
    pass


_RequiredInsightRuleMetricDatapointTypeDef = TypedDict(
    "_RequiredInsightRuleMetricDatapointTypeDef",
    {
        "Timestamp": datetime,
    },
)
_OptionalInsightRuleMetricDatapointTypeDef = TypedDict(
    "_OptionalInsightRuleMetricDatapointTypeDef",
    {
        "UniqueContributors": float,
        "MaxContributorValue": float,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)


class InsightRuleMetricDatapointTypeDef(
    _RequiredInsightRuleMetricDatapointTypeDef, _OptionalInsightRuleMetricDatapointTypeDef
):
    pass


LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Timezone": str,
    },
    total=False,
)

MessageDataTypeDef = TypedDict(
    "MessageDataTypeDef",
    {
        "Code": str,
        "Value": str,
    },
    total=False,
)

GetMetricStreamInputRequestTypeDef = TypedDict(
    "GetMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

MetricStreamFilterOutputTypeDef = TypedDict(
    "MetricStreamFilterOutputTypeDef",
    {
        "Namespace": str,
        "MetricNames": List[str],
    },
    total=False,
)

_RequiredGetMetricWidgetImageInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricWidgetImageInputRequestTypeDef",
    {
        "MetricWidget": str,
    },
)
_OptionalGetMetricWidgetImageInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricWidgetImageInputRequestTypeDef",
    {
        "OutputFormat": str,
    },
    total=False,
)


class GetMetricWidgetImageInputRequestTypeDef(
    _RequiredGetMetricWidgetImageInputRequestTypeDef,
    _OptionalGetMetricWidgetImageInputRequestTypeDef,
):
    pass


GetMetricWidgetImageOutputTypeDef = TypedDict(
    "GetMetricWidgetImageOutputTypeDef",
    {
        "MetricWidgetImage": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightRuleContributorDatapointTypeDef = TypedDict(
    "InsightRuleContributorDatapointTypeDef",
    {
        "Timestamp": datetime,
        "ApproximateValue": float,
    },
)

ListDashboardsInputListDashboardsPaginateTypeDef = TypedDict(
    "ListDashboardsInputListDashboardsPaginateTypeDef",
    {
        "DashboardNamePrefix": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListDashboardsInputRequestTypeDef = TypedDict(
    "ListDashboardsInputRequestTypeDef",
    {
        "DashboardNamePrefix": str,
        "NextToken": str,
    },
    total=False,
)

_RequiredListManagedInsightRulesInputRequestTypeDef = TypedDict(
    "_RequiredListManagedInsightRulesInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListManagedInsightRulesInputRequestTypeDef = TypedDict(
    "_OptionalListManagedInsightRulesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListManagedInsightRulesInputRequestTypeDef(
    _RequiredListManagedInsightRulesInputRequestTypeDef,
    _OptionalListManagedInsightRulesInputRequestTypeDef,
):
    pass


ListMetricStreamsInputRequestTypeDef = TypedDict(
    "ListMetricStreamsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

MetricStreamEntryTypeDef = TypedDict(
    "MetricStreamEntryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "Name": str,
        "FirehoseArn": str,
        "State": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
    total=False,
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ManagedRuleStateTypeDef = TypedDict(
    "ManagedRuleStateTypeDef",
    {
        "RuleName": str,
        "State": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "SampleCount": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
)

MetricStreamFilterTypeDef = TypedDict(
    "MetricStreamFilterTypeDef",
    {
        "Namespace": str,
        "MetricNames": Sequence[str],
    },
    total=False,
)

MetricStreamStatisticsMetricOutputTypeDef = TypedDict(
    "MetricStreamStatisticsMetricOutputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
    },
)

MetricStreamStatisticsMetricTypeDef = TypedDict(
    "MetricStreamStatisticsMetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
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

PutDashboardInputRequestTypeDef = TypedDict(
    "PutDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
        "DashboardBody": str,
    },
)

PutMetricStreamOutputTypeDef = TypedDict(
    "PutMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredSetAlarmStateInputAlarmSetStateTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputAlarmSetStateTypeDef",
    {
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputAlarmSetStateTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputAlarmSetStateTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)


class SetAlarmStateInputAlarmSetStateTypeDef(
    _RequiredSetAlarmStateInputAlarmSetStateTypeDef, _OptionalSetAlarmStateInputAlarmSetStateTypeDef
):
    pass


_RequiredSetAlarmStateInputRequestTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputRequestTypeDef",
    {
        "AlarmName": str,
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputRequestTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputRequestTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)


class SetAlarmStateInputRequestTypeDef(
    _RequiredSetAlarmStateInputRequestTypeDef, _OptionalSetAlarmStateInputRequestTypeDef
):
    pass


StartMetricStreamsInputRequestTypeDef = TypedDict(
    "StartMetricStreamsInputRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)

StopMetricStreamsInputRequestTypeDef = TypedDict(
    "StopMetricStreamsInputRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

DescribeAlarmHistoryOutputTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputTypeDef",
    {
        "AlarmHistoryItems": List[AlarmHistoryItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnomalyDetectorConfigurationOutputTypeDef = TypedDict(
    "AnomalyDetectorConfigurationOutputTypeDef",
    {
        "ExcludedTimeRanges": List[RangeOutputTypeDef],
        "MetricTimezone": str,
    },
    total=False,
)

AnomalyDetectorConfigurationTypeDef = TypedDict(
    "AnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": Sequence[RangeTypeDef],
        "MetricTimezone": str,
    },
    total=False,
)

MetricOutputTypeDef = TypedDict(
    "MetricOutputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[DimensionOutputTypeDef],
    },
    total=False,
)

SingleMetricAnomalyDetectorOutputTypeDef = TypedDict(
    "SingleMetricAnomalyDetectorOutputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[DimensionOutputTypeDef],
        "Stat": str,
    },
    total=False,
)

ListDashboardsOutputTypeDef = TypedDict(
    "ListDashboardsOutputTypeDef",
    {
        "DashboardEntries": List[DashboardEntryTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDashboardOutputTypeDef = TypedDict(
    "PutDashboardOutputTypeDef",
    {
        "DashboardValidationMessages": List[DashboardValidationMessageTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricStatisticsOutputTypeDef = TypedDict(
    "GetMetricStatisticsOutputTypeDef",
    {
        "Label": str,
        "Datapoints": List[DatapointTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAlarmsForMetricInputRequestTypeDef = TypedDict(
    "_RequiredDescribeAlarmsForMetricInputRequestTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
    },
)
_OptionalDescribeAlarmsForMetricInputRequestTypeDef = TypedDict(
    "_OptionalDescribeAlarmsForMetricInputRequestTypeDef",
    {
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Period": int,
        "Unit": StandardUnitType,
    },
    total=False,
)


class DescribeAlarmsForMetricInputRequestTypeDef(
    _RequiredDescribeAlarmsForMetricInputRequestTypeDef,
    _OptionalDescribeAlarmsForMetricInputRequestTypeDef,
):
    pass


DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef = TypedDict(
    "DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "AnomalyDetectorTypes": Sequence[AnomalyDetectorTypeType],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

DescribeAnomalyDetectorsInputRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "AnomalyDetectorTypes": Sequence[AnomalyDetectorTypeType],
    },
    total=False,
)

_RequiredGetMetricStatisticsInputMetricGetStatisticsTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputMetricGetStatisticsTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputMetricGetStatisticsTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputMetricGetStatisticsTypeDef",
    {
        "Dimensions": Sequence[DimensionTypeDef],
        "Statistics": Sequence[StatisticType],
        "ExtendedStatistics": Sequence[str],
        "Unit": StandardUnitType,
    },
    total=False,
)


class GetMetricStatisticsInputMetricGetStatisticsTypeDef(
    _RequiredGetMetricStatisticsInputMetricGetStatisticsTypeDef,
    _OptionalGetMetricStatisticsInputMetricGetStatisticsTypeDef,
):
    pass


_RequiredGetMetricStatisticsInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputRequestTypeDef",
    {
        "Dimensions": Sequence[DimensionTypeDef],
        "Statistics": Sequence[StatisticType],
        "ExtendedStatistics": Sequence[str],
        "Unit": StandardUnitType,
    },
    total=False,
)


class GetMetricStatisticsInputRequestTypeDef(
    _RequiredGetMetricStatisticsInputRequestTypeDef, _OptionalGetMetricStatisticsInputRequestTypeDef
):
    pass


MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
    },
    total=False,
)

SingleMetricAnomalyDetectorTypeDef = TypedDict(
    "SingleMetricAnomalyDetectorTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Stat": str,
    },
    total=False,
)

DeleteInsightRulesOutputTypeDef = TypedDict(
    "DeleteInsightRulesOutputTypeDef",
    {
        "Failures": List[PartialFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableInsightRulesOutputTypeDef = TypedDict(
    "DisableInsightRulesOutputTypeDef",
    {
        "Failures": List[PartialFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableInsightRulesOutputTypeDef = TypedDict(
    "EnableInsightRulesOutputTypeDef",
    {
        "Failures": List[PartialFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutManagedInsightRulesOutputTypeDef = TypedDict(
    "PutManagedInsightRulesOutputTypeDef",
    {
        "Failures": List[PartialFailureTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsInputAlarmExistsWaitTypeDef = TypedDict(
    "DescribeAlarmsInputAlarmExistsWaitTypeDef",
    {
        "AlarmNames": Sequence[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "MaxRecords": int,
        "NextToken": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef = TypedDict(
    "DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef",
    {
        "AlarmNames": Sequence[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": Sequence[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "MaxRecords": int,
        "NextToken": str,
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)

DescribeInsightRulesOutputTypeDef = TypedDict(
    "DescribeInsightRulesOutputTypeDef",
    {
        "NextToken": str,
        "InsightRules": List[InsightRuleTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricsInputListMetricsPaginateTypeDef = TypedDict(
    "ListMetricsInputListMetricsPaginateTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionFilterTypeDef],
        "RecentlyActive": Literal["PT3H"],
        "IncludeLinkedAccounts": bool,
        "OwningAccount": str,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

ListMetricsInputRequestTypeDef = TypedDict(
    "ListMetricsInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionFilterTypeDef],
        "NextToken": str,
        "RecentlyActive": Literal["PT3H"],
        "IncludeLinkedAccounts": bool,
        "OwningAccount": str,
    },
    total=False,
)

MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": StatusCodeType,
        "Messages": List[MessageDataTypeDef],
    },
    total=False,
)

InsightRuleContributorTypeDef = TypedDict(
    "InsightRuleContributorTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List[InsightRuleContributorDatapointTypeDef],
    },
)

ListMetricStreamsOutputTypeDef = TypedDict(
    "ListMetricStreamsOutputTypeDef",
    {
        "NextToken": str,
        "Entries": List[MetricStreamEntryTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagOutputTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedRuleDescriptionTypeDef = TypedDict(
    "ManagedRuleDescriptionTypeDef",
    {
        "TemplateName": str,
        "ResourceARN": str,
        "RuleState": ManagedRuleStateTypeDef,
    },
    total=False,
)

_RequiredManagedRuleTypeDef = TypedDict(
    "_RequiredManagedRuleTypeDef",
    {
        "TemplateName": str,
        "ResourceARN": str,
    },
)
_OptionalManagedRuleTypeDef = TypedDict(
    "_OptionalManagedRuleTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class ManagedRuleTypeDef(_RequiredManagedRuleTypeDef, _OptionalManagedRuleTypeDef):
    pass


_RequiredPutCompositeAlarmInputRequestTypeDef = TypedDict(
    "_RequiredPutCompositeAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "AlarmRule": str,
    },
)
_OptionalPutCompositeAlarmInputRequestTypeDef = TypedDict(
    "_OptionalPutCompositeAlarmInputRequestTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": Sequence[str],
        "AlarmDescription": str,
        "InsufficientDataActions": Sequence[str],
        "OKActions": Sequence[str],
        "Tags": Sequence[TagTypeDef],
        "ActionsSuppressor": str,
        "ActionsSuppressorWaitPeriod": int,
        "ActionsSuppressorExtensionPeriod": int,
    },
    total=False,
)


class PutCompositeAlarmInputRequestTypeDef(
    _RequiredPutCompositeAlarmInputRequestTypeDef, _OptionalPutCompositeAlarmInputRequestTypeDef
):
    pass


_RequiredPutInsightRuleInputRequestTypeDef = TypedDict(
    "_RequiredPutInsightRuleInputRequestTypeDef",
    {
        "RuleName": str,
        "RuleDefinition": str,
    },
)
_OptionalPutInsightRuleInputRequestTypeDef = TypedDict(
    "_OptionalPutInsightRuleInputRequestTypeDef",
    {
        "RuleState": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class PutInsightRuleInputRequestTypeDef(
    _RequiredPutInsightRuleInputRequestTypeDef, _OptionalPutInsightRuleInputRequestTypeDef
):
    pass


TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef",
    {
        "MetricName": str,
    },
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": Sequence[DimensionTypeDef],
        "Timestamp": Union[datetime, str],
        "Value": float,
        "StatisticValues": StatisticSetTypeDef,
        "Values": Sequence[float],
        "Counts": Sequence[float],
        "Unit": StandardUnitType,
        "StorageResolution": int,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


MetricStreamStatisticsConfigurationOutputTypeDef = TypedDict(
    "MetricStreamStatisticsConfigurationOutputTypeDef",
    {
        "IncludeMetrics": List[MetricStreamStatisticsMetricOutputTypeDef],
        "AdditionalStatistics": List[str],
    },
)

MetricStreamStatisticsConfigurationTypeDef = TypedDict(
    "MetricStreamStatisticsConfigurationTypeDef",
    {
        "IncludeMetrics": Sequence[MetricStreamStatisticsMetricTypeDef],
        "AdditionalStatistics": Sequence[str],
    },
)

ListMetricsOutputTypeDef = TypedDict(
    "ListMetricsOutputTypeDef",
    {
        "Metrics": List[MetricOutputTypeDef],
        "NextToken": str,
        "OwningAccounts": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMetricStatOutputTypeDef = TypedDict(
    "_RequiredMetricStatOutputTypeDef",
    {
        "Metric": MetricOutputTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricStatOutputTypeDef = TypedDict(
    "_OptionalMetricStatOutputTypeDef",
    {
        "Unit": StandardUnitType,
    },
    total=False,
)


class MetricStatOutputTypeDef(_RequiredMetricStatOutputTypeDef, _OptionalMetricStatOutputTypeDef):
    pass


_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef",
    {
        "Metric": MetricTypeDef,
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": StandardUnitType,
    },
    total=False,
)


class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass


GetMetricDataOutputTypeDef = TypedDict(
    "GetMetricDataOutputTypeDef",
    {
        "MetricDataResults": List[MetricDataResultTypeDef],
        "NextToken": str,
        "Messages": List[MessageDataTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightRuleReportOutputTypeDef = TypedDict(
    "GetInsightRuleReportOutputTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List[InsightRuleContributorTypeDef],
        "MetricDatapoints": List[InsightRuleMetricDatapointTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedInsightRulesOutputTypeDef = TypedDict(
    "ListManagedInsightRulesOutputTypeDef",
    {
        "ManagedRules": List[ManagedRuleDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutManagedInsightRulesInputRequestTypeDef = TypedDict(
    "PutManagedInsightRulesInputRequestTypeDef",
    {
        "ManagedRules": Sequence[ManagedRuleTypeDef],
    },
)

PutMetricDataInputRequestTypeDef = TypedDict(
    "PutMetricDataInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricData": Sequence[MetricDatumTypeDef],
    },
)

GetMetricStreamOutputTypeDef = TypedDict(
    "GetMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "IncludeFilters": List[MetricStreamFilterOutputTypeDef],
        "ExcludeFilters": List[MetricStreamFilterOutputTypeDef],
        "FirehoseArn": str,
        "RoleArn": str,
        "State": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "OutputFormat": MetricStreamOutputFormatType,
        "StatisticsConfigurations": List[MetricStreamStatisticsConfigurationOutputTypeDef],
        "IncludeLinkedAccountsMetrics": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutMetricStreamInputRequestTypeDef = TypedDict(
    "_RequiredPutMetricStreamInputRequestTypeDef",
    {
        "Name": str,
        "FirehoseArn": str,
        "RoleArn": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
)
_OptionalPutMetricStreamInputRequestTypeDef = TypedDict(
    "_OptionalPutMetricStreamInputRequestTypeDef",
    {
        "IncludeFilters": Sequence[MetricStreamFilterTypeDef],
        "ExcludeFilters": Sequence[MetricStreamFilterTypeDef],
        "Tags": Sequence[TagTypeDef],
        "StatisticsConfigurations": Sequence[MetricStreamStatisticsConfigurationTypeDef],
        "IncludeLinkedAccountsMetrics": bool,
    },
    total=False,
)


class PutMetricStreamInputRequestTypeDef(
    _RequiredPutMetricStreamInputRequestTypeDef, _OptionalPutMetricStreamInputRequestTypeDef
):
    pass


_RequiredMetricDataQueryOutputTypeDef = TypedDict(
    "_RequiredMetricDataQueryOutputTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricDataQueryOutputTypeDef = TypedDict(
    "_OptionalMetricDataQueryOutputTypeDef",
    {
        "MetricStat": MetricStatOutputTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
        "AccountId": str,
    },
    total=False,
)


class MetricDataQueryOutputTypeDef(
    _RequiredMetricDataQueryOutputTypeDef, _OptionalMetricDataQueryOutputTypeDef
):
    pass


_RequiredMetricDataQueryTypeDef = TypedDict(
    "_RequiredMetricDataQueryTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": MetricStatTypeDef,
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
        "AccountId": str,
    },
    total=False,
)


class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, _OptionalMetricDataQueryTypeDef):
    pass


MetricAlarmTypeDef = TypedDict(
    "MetricAlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": StateValueType,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List[DimensionOutputTypeDef],
        "Period": int,
        "Unit": StandardUnitType,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List[MetricDataQueryOutputTypeDef],
        "ThresholdMetricId": str,
        "EvaluationState": Literal["PARTIAL_DATA"],
        "StateTransitionedTimestamp": datetime,
    },
    total=False,
)

MetricMathAnomalyDetectorOutputTypeDef = TypedDict(
    "MetricMathAnomalyDetectorOutputTypeDef",
    {
        "MetricDataQueries": List[MetricDataQueryOutputTypeDef],
    },
    total=False,
)

_RequiredGetMetricDataInputGetMetricDataPaginateTypeDef = TypedDict(
    "_RequiredGetMetricDataInputGetMetricDataPaginateTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryTypeDef],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetMetricDataInputGetMetricDataPaginateTypeDef = TypedDict(
    "_OptionalGetMetricDataInputGetMetricDataPaginateTypeDef",
    {
        "ScanBy": ScanByType,
        "LabelOptions": LabelOptionsTypeDef,
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class GetMetricDataInputGetMetricDataPaginateTypeDef(
    _RequiredGetMetricDataInputGetMetricDataPaginateTypeDef,
    _OptionalGetMetricDataInputGetMetricDataPaginateTypeDef,
):
    pass


_RequiredGetMetricDataInputRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataInputRequestTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryTypeDef],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetMetricDataInputRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataInputRequestTypeDef",
    {
        "NextToken": str,
        "ScanBy": ScanByType,
        "MaxDatapoints": int,
        "LabelOptions": LabelOptionsTypeDef,
    },
    total=False,
)


class GetMetricDataInputRequestTypeDef(
    _RequiredGetMetricDataInputRequestTypeDef, _OptionalGetMetricDataInputRequestTypeDef
):
    pass


MetricMathAnomalyDetectorTypeDef = TypedDict(
    "MetricMathAnomalyDetectorTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryTypeDef],
    },
    total=False,
)

_RequiredPutMetricAlarmInputMetricPutAlarmTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputMetricPutAlarmTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputMetricPutAlarmTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputMetricPutAlarmTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": Sequence[str],
        "AlarmActions": Sequence[str],
        "InsufficientDataActions": Sequence[str],
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": Sequence[MetricDataQueryTypeDef],
        "Tags": Sequence[TagTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)


class PutMetricAlarmInputMetricPutAlarmTypeDef(
    _RequiredPutMetricAlarmInputMetricPutAlarmTypeDef,
    _OptionalPutMetricAlarmInputMetricPutAlarmTypeDef,
):
    pass


_RequiredPutMetricAlarmInputRequestTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputRequestTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputRequestTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": Sequence[str],
        "AlarmActions": Sequence[str],
        "InsufficientDataActions": Sequence[str],
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": Sequence[MetricDataQueryTypeDef],
        "Tags": Sequence[TagTypeDef],
        "ThresholdMetricId": str,
    },
    total=False,
)


class PutMetricAlarmInputRequestTypeDef(
    _RequiredPutMetricAlarmInputRequestTypeDef, _OptionalPutMetricAlarmInputRequestTypeDef
):
    pass


DescribeAlarmsForMetricOutputTypeDef = TypedDict(
    "DescribeAlarmsForMetricOutputTypeDef",
    {
        "MetricAlarms": List[MetricAlarmTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsOutputTypeDef = TypedDict(
    "DescribeAlarmsOutputTypeDef",
    {
        "CompositeAlarms": List[CompositeAlarmTypeDef],
        "MetricAlarms": List[MetricAlarmTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnomalyDetectorTypeDef = TypedDict(
    "AnomalyDetectorTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List[DimensionOutputTypeDef],
        "Stat": str,
        "Configuration": AnomalyDetectorConfigurationOutputTypeDef,
        "StateValue": AnomalyDetectorStateValueType,
        "SingleMetricAnomalyDetector": SingleMetricAnomalyDetectorOutputTypeDef,
        "MetricMathAnomalyDetector": MetricMathAnomalyDetectorOutputTypeDef,
    },
    total=False,
)

DeleteAnomalyDetectorInputRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Stat": str,
        "SingleMetricAnomalyDetector": SingleMetricAnomalyDetectorTypeDef,
        "MetricMathAnomalyDetector": MetricMathAnomalyDetectorTypeDef,
    },
    total=False,
)

PutAnomalyDetectorInputRequestTypeDef = TypedDict(
    "PutAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": Sequence[DimensionTypeDef],
        "Stat": str,
        "Configuration": AnomalyDetectorConfigurationTypeDef,
        "SingleMetricAnomalyDetector": SingleMetricAnomalyDetectorTypeDef,
        "MetricMathAnomalyDetector": MetricMathAnomalyDetectorTypeDef,
    },
    total=False,
)

DescribeAnomalyDetectorsOutputTypeDef = TypedDict(
    "DescribeAnomalyDetectorsOutputTypeDef",
    {
        "AnomalyDetectors": List[AnomalyDetectorTypeDef],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
