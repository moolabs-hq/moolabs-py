# AccountUpdate

PATCH /accounts/{id} — partial update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | [optional] 
**billing_country_code** | **str** |  | [optional] 
**billing_region_code** | **str** |  | [optional] 
**billing_timezone** | **str** |  | [optional] 
**default_language_code** | **str** |  | [optional] 
**default_currency_code** | **str** |  | [optional] 
**portal_required** | **bool** |  | [optional] 
**payment_terms** | **str** |  | [optional] 
**is_strategic** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.account_update import AccountUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdate from a JSON string
account_update_instance = AccountUpdate.from_json(json)
# print the JSON string representation of the object
print(AccountUpdate.to_json())

# convert the object into a dict
account_update_dict = account_update_instance.to_dict()
# create an instance of AccountUpdate from a dict
account_update_from_dict = AccountUpdate.from_dict(account_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


