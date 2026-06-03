# DisclosurePolicyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirement** | **str** |  | [optional] [default to 'not_required']
**disclosure_text** | **str** |  | [optional] 
**change_reason** | **str** |  | 

## Example

```python
from moolabs.models.disclosure_policy_update_request import DisclosurePolicyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosurePolicyUpdateRequest from a JSON string
disclosure_policy_update_request_instance = DisclosurePolicyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DisclosurePolicyUpdateRequest.to_json())

# convert the object into a dict
disclosure_policy_update_request_dict = disclosure_policy_update_request_instance.to_dict()
# create an instance of DisclosurePolicyUpdateRequest from a dict
disclosure_policy_update_request_from_dict = DisclosurePolicyUpdateRequest.from_dict(disclosure_policy_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


