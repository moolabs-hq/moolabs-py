# AccountSummary

Lightweight account info embedded in case responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**customer_id** | **str** |  | 
**legal_name** | **str** |  | 
**billing_country_code** | **str** |  | [optional] 
**default_currency_code** | **str** |  | [optional] [default to 'USD']
**is_strategic** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.account_summary import AccountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummary from a JSON string
account_summary_instance = AccountSummary.from_json(json)
# print the JSON string representation of the object
print(AccountSummary.to_json())

# convert the object into a dict
account_summary_dict = account_summary_instance.to_dict()
# create an instance of AccountSummary from a dict
account_summary_from_dict = AccountSummary.from_dict(account_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


