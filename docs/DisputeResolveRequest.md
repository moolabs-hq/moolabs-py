# DisputeResolveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** | resolved_valid or resolved_invalid | 
**resolved_amount_micros** | **int** |  | [optional] 
**resolution_notes** | **str** |  | [optional] 

## Example

```python
from moolabs.models.dispute_resolve_request import DisputeResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeResolveRequest from a JSON string
dispute_resolve_request_instance = DisputeResolveRequest.from_json(json)
# print the JSON string representation of the object
print(DisputeResolveRequest.to_json())

# convert the object into a dict
dispute_resolve_request_dict = dispute_resolve_request_instance.to_dict()
# create an instance of DisputeResolveRequest from a dict
dispute_resolve_request_from_dict = DisputeResolveRequest.from_dict(dispute_resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


