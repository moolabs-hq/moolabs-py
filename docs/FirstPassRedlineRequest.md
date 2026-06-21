# FirstPassRedlineRequest

Optional body for POST /quotes/{id}/redlines/first-pass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_vertical** | **str** |  | [optional] [default to 'ai-saas']

## Example

```python
from moolabs.models.first_pass_redline_request import FirstPassRedlineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FirstPassRedlineRequest from a JSON string
first_pass_redline_request_instance = FirstPassRedlineRequest.from_json(json)
# print the JSON string representation of the object
print(FirstPassRedlineRequest.to_json())

# convert the object into a dict
first_pass_redline_request_dict = first_pass_redline_request_instance.to_dict()
# create an instance of FirstPassRedlineRequest from a dict
first_pass_redline_request_from_dict = FirstPassRedlineRequest.from_dict(first_pass_redline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


