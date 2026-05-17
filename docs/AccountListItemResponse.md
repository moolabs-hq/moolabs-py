# AccountListItemResponse

GET /accounts list row with computed account summary fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**customer_id** | **str** |  | 
**billing_account_id** | **str** |  | [optional] 
**bill_to_entity_id** | **str** |  | [optional] 
**legal_name** | **str** |  | 
**billing_country_code** | **str** |  | [optional] 
**billing_region_code** | **str** |  | [optional] 
**billing_timezone** | **str** |  | [optional] 
**default_language_code** | **str** |  | 
**default_currency_code** | **str** |  | 
**portal_required** | **bool** |  | 
**payment_terms** | **str** |  | [optional] 
**is_strategic** | **bool** |  | 
**source_system** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**subsidiaries** | [**List[AccountListItemResponseSubsidiariesInner]**](AccountListItemResponseSubsidiariesInner.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**open_balance_micros** | **int** | Display open balance. Uses the invoice currency when a single open currency exists; uses base currency when open invoices are mixed-currency. | [optional] [default to 0]
**open_balance_base_micros** | **int** | Base-currency open balance used for filtering and sorting. | [optional] [default to 0]
**open_balance_currency_code** | **str** | Currency code for open_balance_micros. | [optional] [default to 'USD']
**open_balance_base_currency_code** | **str** | Base currency code for open_balance_base_micros. | [optional] [default to 'USD']
**open_balance_has_mixed_currencies** | **bool** |  | [optional] [default to False]
**subsidiary_options** | [**List[AccountSubsidiaryOption]**](AccountSubsidiaryOption.md) |  | [optional] 

## Example

```python
from moolabs.models.account_list_item_response import AccountListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountListItemResponse from a JSON string
account_list_item_response_instance = AccountListItemResponse.from_json(json)
# print the JSON string representation of the object
print(AccountListItemResponse.to_json())

# convert the object into a dict
account_list_item_response_dict = account_list_item_response_instance.to_dict()
# create an instance of AccountListItemResponse from a dict
account_list_item_response_from_dict = AccountListItemResponse.from_dict(account_list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


