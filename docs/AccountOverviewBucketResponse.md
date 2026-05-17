# AccountOverviewBucketResponse

Single aging bucket in the account overview response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**invoice_count** | **int** |  | 
**total_amount_micros** | **int** |  | 

## Example

```python
from moolabs.models.account_overview_bucket_response import AccountOverviewBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOverviewBucketResponse from a JSON string
account_overview_bucket_response_instance = AccountOverviewBucketResponse.from_json(json)
# print the JSON string representation of the object
print(AccountOverviewBucketResponse.to_json())

# convert the object into a dict
account_overview_bucket_response_dict = account_overview_bucket_response_instance.to_dict()
# create an instance of AccountOverviewBucketResponse from a dict
account_overview_bucket_response_from_dict = AccountOverviewBucketResponse.from_dict(account_overview_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


