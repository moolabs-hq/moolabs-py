# OptOutRequest

POST /contacts/{id}/opt-out — opt out of a channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel to opt out of: email, sms, phone, portal | 
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.opt_out_request import OptOutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OptOutRequest from a JSON string
opt_out_request_instance = OptOutRequest.from_json(json)
# print the JSON string representation of the object
print(OptOutRequest.to_json())

# convert the object into a dict
opt_out_request_dict = opt_out_request_instance.to_dict()
# create an instance of OptOutRequest from a dict
opt_out_request_from_dict = OptOutRequest.from_dict(opt_out_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


