# OptOutResponse

Response confirming opt-out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** |  | 
**channel** | **str** |  | 
**opt_out** | **bool** |  | [optional] [default to True]
**message** | **str** |  | 

## Example

```python
from moolabs.models.opt_out_response import OptOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptOutResponse from a JSON string
opt_out_response_instance = OptOutResponse.from_json(json)
# print the JSON string representation of the object
print(OptOutResponse.to_json())

# convert the object into a dict
opt_out_response_dict = opt_out_response_instance.to_dict()
# create an instance of OptOutResponse from a dict
opt_out_response_from_dict = OptOutResponse.from_dict(opt_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


