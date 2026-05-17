# MergeRemittancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** |  | 
**target_id** | **str** |  | 

## Example

```python
from moolabs.models.merge_remittances_request import MergeRemittancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeRemittancesRequest from a JSON string
merge_remittances_request_instance = MergeRemittancesRequest.from_json(json)
# print the JSON string representation of the object
print(MergeRemittancesRequest.to_json())

# convert the object into a dict
merge_remittances_request_dict = merge_remittances_request_instance.to_dict()
# create an instance of MergeRemittancesRequest from a dict
merge_remittances_request_from_dict = MergeRemittancesRequest.from_dict(merge_remittances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


