# DisclosurePolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirement** | **str** |  | 
**disclosure_text** | **str** |  | [optional] 
**policy_hash** | **str** |  | 
**updated_by_actor_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.disclosure_policy_response import DisclosurePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosurePolicyResponse from a JSON string
disclosure_policy_response_instance = DisclosurePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(DisclosurePolicyResponse.to_json())

# convert the object into a dict
disclosure_policy_response_dict = disclosure_policy_response_instance.to_dict()
# create an instance of DisclosurePolicyResponse from a dict
disclosure_policy_response_from_dict = DisclosurePolicyResponse.from_dict(disclosure_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


