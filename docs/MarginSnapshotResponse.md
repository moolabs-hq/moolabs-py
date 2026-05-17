# MarginSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**total_billing_events** | **int** |  | 
**fully_reconciled_count** | **int** |  | 
**partially_reconciled_count** | **int** |  | 
**unreconciled_count** | **int** |  | 
**total_valued_burn** | **str** |  | 
**total_cost** | **str** |  | 
**direct_margin** | **str** |  | 
**direct_margin_pct** | **str** |  | 
**margin_includes_grade** | **str** |  | 
**reconciliation_completeness** | **str** |  | 
**loaded_margin** | **str** |  | [optional] 
**loaded_margin_pct** | **str** |  | [optional] 
**loaded_margin_available** | **bool** |  | [optional] [default to False]
**standard_cost** | **str** |  | [optional] 
**standard_margin** | **str** |  | [optional] 
**standard_margin_pct** | **str** |  | [optional] 
**observation_status** | **str** |  | [optional] 
**reconciliation_basis** | [**ReconciliationBasis**](ReconciliationBasis.md) |  | 

## Example

```python
from moolabs.models.margin_snapshot_response import MarginSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarginSnapshotResponse from a JSON string
margin_snapshot_response_instance = MarginSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(MarginSnapshotResponse.to_json())

# convert the object into a dict
margin_snapshot_response_dict = margin_snapshot_response_instance.to_dict()
# create an instance of MarginSnapshotResponse from a dict
margin_snapshot_response_from_dict = MarginSnapshotResponse.from_dict(margin_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


