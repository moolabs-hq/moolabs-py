# RetryUnpricedRequest

Request to retry an UNPRICED usage event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**usage_event_id** | **str** | Usage event ID to retry | 

## Example

```python
from moolabs.models.retry_unpriced_request import RetryUnpricedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetryUnpricedRequest from a JSON string
retry_unpriced_request_instance = RetryUnpricedRequest.from_json(json)
# print the JSON string representation of the object
print(RetryUnpricedRequest.to_json())

# convert the object into a dict
retry_unpriced_request_dict = retry_unpriced_request_instance.to_dict()
# create an instance of RetryUnpricedRequest from a dict
retry_unpriced_request_from_dict = RetryUnpricedRequest.from_dict(retry_unpriced_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


