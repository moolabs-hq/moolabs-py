# AccountFilterOptionsResponse

GET /accounts/filter-options — distinct filter values for list UI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_systems** | **List[str]** |  | 
**subsidiaries** | [**List[AccountSubsidiaryOption]**](AccountSubsidiaryOption.md) |  | [optional] 

## Example

```python
from moolabs.models.account_filter_options_response import AccountFilterOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountFilterOptionsResponse from a JSON string
account_filter_options_response_instance = AccountFilterOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountFilterOptionsResponse.to_json())

# convert the object into a dict
account_filter_options_response_dict = account_filter_options_response_instance.to_dict()
# create an instance of AccountFilterOptionsResponse from a dict
account_filter_options_response_from_dict = AccountFilterOptionsResponse.from_dict(account_filter_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


