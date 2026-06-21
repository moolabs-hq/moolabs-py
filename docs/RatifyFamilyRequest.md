# RatifyFamilyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**industry_vertical** | **str** |  | 
**family_id** | **str** |  | 
**owner** | **str** |  | 

## Example

```python
from moolabs.models.ratify_family_request import RatifyFamilyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatifyFamilyRequest from a JSON string
ratify_family_request_instance = RatifyFamilyRequest.from_json(json)
# print the JSON string representation of the object
print(RatifyFamilyRequest.to_json())

# convert the object into a dict
ratify_family_request_dict = ratify_family_request_instance.to_dict()
# create an instance of RatifyFamilyRequest from a dict
ratify_family_request_from_dict = RatifyFamilyRequest.from_dict(ratify_family_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


