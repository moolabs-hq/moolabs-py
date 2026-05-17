# CompletenessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completeness_pct** | **str** |  | 
**completeness_mode** | **str** |  | 
**total_ai_events** | **int** |  | 
**fully_reconciled_count** | **int** |  | 
**partially_reconciled_count** | **int** |  | 
**unreconciled_count** | **int** |  | 
**computed_at** | **str** |  | 
**reconciliation_basis** | [**ReconciliationBasis**](ReconciliationBasis.md) |  | 

## Example

```python
from moolabs.models.completeness_response import CompletenessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompletenessResponse from a JSON string
completeness_response_instance = CompletenessResponse.from_json(json)
# print the JSON string representation of the object
print(CompletenessResponse.to_json())

# convert the object into a dict
completeness_response_dict = completeness_response_instance.to_dict()
# create an instance of CompletenessResponse from a dict
completeness_response_from_dict = CompletenessResponse.from_dict(completeness_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


