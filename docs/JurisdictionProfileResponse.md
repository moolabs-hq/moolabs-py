# JurisdictionProfileResponse

Resolved jurisdiction profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**effective_country_code** | **str** |  | 
**effective_region_code** | **str** |  | [optional] 
**effective_timezone** | **str** |  | 
**rule_profile** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.jurisdiction_profile_response import JurisdictionProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JurisdictionProfileResponse from a JSON string
jurisdiction_profile_response_instance = JurisdictionProfileResponse.from_json(json)
# print the JSON string representation of the object
print(JurisdictionProfileResponse.to_json())

# convert the object into a dict
jurisdiction_profile_response_dict = jurisdiction_profile_response_instance.to_dict()
# create an instance of JurisdictionProfileResponse from a dict
jurisdiction_profile_response_from_dict = JurisdictionProfileResponse.from_dict(jurisdiction_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


