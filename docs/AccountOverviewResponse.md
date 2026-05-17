# AccountOverviewResponse

GET /accounts/{account_id}/overview — account aging summary for Customer 360.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**total_invoices** | **int** |  | 
**total_amount_micros** | **int** |  | 
**last_payment_at** | **datetime** |  | [optional] 
**buckets** | [**List[AccountOverviewBucketResponse]**](AccountOverviewBucketResponse.md) |  | 

## Example

```python
from moolabs.models.account_overview_response import AccountOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOverviewResponse from a JSON string
account_overview_response_instance = AccountOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(AccountOverviewResponse.to_json())

# convert the object into a dict
account_overview_response_dict = account_overview_response_instance.to_dict()
# create an instance of AccountOverviewResponse from a dict
account_overview_response_from_dict = AccountOverviewResponse.from_dict(account_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


