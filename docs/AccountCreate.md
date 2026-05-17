# AccountCreate

POST /accounts — create an ARC account linked to a MooMeter customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | MooMeter customer_id | 
**billing_account_id** | **str** |  | [optional] 
**bill_to_entity_id** | **str** |  | [optional] 
**legal_name** | **str** |  | 
**billing_country_code** | **str** |  | [optional] 
**billing_region_code** | **str** |  | [optional] 
**billing_timezone** | **str** |  | [optional] 
**default_language_code** | **str** |  | [optional] [default to 'en']
**default_currency_code** | **str** |  | [optional] [default to 'USD']
**portal_required** | **bool** |  | [optional] [default to False]
**is_strategic** | **bool** |  | [optional] [default to False]
**payment_terms** | **str** |  | [optional] 
**source_system** | **str** |  | [optional] [default to 'moometer']
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.account_create import AccountCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreate from a JSON string
account_create_instance = AccountCreate.from_json(json)
# print the JSON string representation of the object
print(AccountCreate.to_json())

# convert the object into a dict
account_create_dict = account_create_instance.to_dict()
# create an instance of AccountCreate from a dict
account_create_from_dict = AccountCreate.from_dict(account_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


