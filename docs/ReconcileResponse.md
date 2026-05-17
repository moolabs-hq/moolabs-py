# ReconcileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**tenant_id** | **str** |  | 
**status** | **str** |  | 
**cost_event_ids_count** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from moolabs.models.reconcile_response import ReconcileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReconcileResponse from a JSON string
reconcile_response_instance = ReconcileResponse.from_json(json)
# print the JSON string representation of the object
print(ReconcileResponse.to_json())

# convert the object into a dict
reconcile_response_dict = reconcile_response_instance.to_dict()
# create an instance of ReconcileResponse from a dict
reconcile_response_from_dict = ReconcileResponse.from_dict(reconcile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


