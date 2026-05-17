# JurisdictionResolutionRequest

POST /accounts/{id}/resolve-jurisdiction — resolve effective jurisdiction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**region_code** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from moolabs.models.jurisdiction_resolution_request import JurisdictionResolutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionResolutionRequest from a JSON string
jurisdiction_resolution_request_instance = JurisdictionResolutionRequest.from_json(json)
# print the JSON string representation of the object
print(JurisdictionResolutionRequest.to_json())

# convert the object into a dict
jurisdiction_resolution_request_dict = jurisdiction_resolution_request_instance.to_dict()
# create an instance of JurisdictionResolutionRequest from a dict
jurisdiction_resolution_request_from_dict = JurisdictionResolutionRequest.from_dict(jurisdiction_resolution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


