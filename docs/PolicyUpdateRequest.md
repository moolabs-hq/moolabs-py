# PolicyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_autonomy** | **int** |  | [optional] 
**allowed_actions** | **Dict[str, object]** |  | [optional] 
**requires_human_for** | **Dict[str, object]** |  | [optional] 
**policy_version** | **str** |  | [optional] 

## Example

```python
from moolabs.models.policy_update_request import PolicyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyUpdateRequest from a JSON string
policy_update_request_instance = PolicyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyUpdateRequest.to_json())

# convert the object into a dict
policy_update_request_dict = policy_update_request_instance.to_dict()
# create an instance of PolicyUpdateRequest from a dict
policy_update_request_from_dict = PolicyUpdateRequest.from_dict(policy_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


