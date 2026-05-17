# AccountSubsidiaryOption

Normalized account subsidiary filter/display option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from moolabs.models.account_subsidiary_option import AccountSubsidiaryOption

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSubsidiaryOption from a JSON string
account_subsidiary_option_instance = AccountSubsidiaryOption.from_json(json)
# print the JSON string representation of the object
print(AccountSubsidiaryOption.to_json())

# convert the object into a dict
account_subsidiary_option_dict = account_subsidiary_option_instance.to_dict()
# create an instance of AccountSubsidiaryOption from a dict
account_subsidiary_option_from_dict = AccountSubsidiaryOption.from_dict(account_subsidiary_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


