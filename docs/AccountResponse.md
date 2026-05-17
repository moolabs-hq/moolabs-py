# AccountResponse

GET /accounts/{id} response.

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

## Example

```python
from moolabs.models.account_response import AccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponse from a JSON string
account_response_instance = AccountResponse.from_json(json)
# print the JSON string representation of the object
print(AccountResponse.to_json())

# convert the object into a dict
account_response_dict = account_response_instance.to_dict()
# create an instance of AccountResponse from a dict
account_response_from_dict = AccountResponse.from_dict(account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


