# GrantBurnDownHistorySegment

A segment of the grant burn down history.  A given segment represents the usage of a grant between events that changed either the grant burn down priority order or the usag period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**Period**](Period.md) | The period of the segment. | 
**usage** | **float** | The total usage of the grant in the period. | [readonly] 
**overage** | **float** | Overuse that wasn&#39;t covered by grants. | [readonly] 
**balance_at_start** | **float** | entitlement balance at the start of the period. | [readonly] 
**grant_balances_at_start** | **Dict[str, float]** | The balance breakdown of each active grant at the start of the period: GrantID: Balance | [readonly] 
**balance_at_end** | **float** | The entitlement balance at the end of the period. | [readonly] 
**grant_balances_at_end** | **Dict[str, float]** | The balance breakdown of each active grant at the end of the period: GrantID: Balance | [readonly] 
**grant_usages** | [**List[GrantUsageRecord]**](GrantUsageRecord.md) | Which grants were actually burnt down in the period and by what amount. | 

## Example

```python
from moolabs.models.grant_burn_down_history_segment import GrantBurnDownHistorySegment

# TODO update the JSON string below
json = "{}"
# create an instance of GrantBurnDownHistorySegment from a JSON string
grant_burn_down_history_segment_instance = GrantBurnDownHistorySegment.from_json(json)
# print the JSON string representation of the object
print(GrantBurnDownHistorySegment.to_json())

# convert the object into a dict
grant_burn_down_history_segment_dict = grant_burn_down_history_segment_instance.to_dict()
# create an instance of GrantBurnDownHistorySegment from a dict
grant_burn_down_history_segment_from_dict = GrantBurnDownHistorySegment.from_dict(grant_burn_down_history_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


