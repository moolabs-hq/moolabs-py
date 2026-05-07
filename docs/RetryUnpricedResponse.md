# RetryUnpricedResponse

Response from retrying UNPRICED event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_event_id** | **str** |  | 
**rating_status** | **str** |  | 
**retried_at** | **str** |  | 

## Example

```python
from moolabs.models.retry_unpriced_response import RetryUnpricedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetryUnpricedResponse from a JSON string
retry_unpriced_response_instance = RetryUnpricedResponse.from_json(json)
# print the JSON string representation of the object
print(RetryUnpricedResponse.to_json())

# convert the object into a dict
retry_unpriced_response_dict = retry_unpriced_response_instance.to_dict()
# create an instance of RetryUnpricedResponse from a dict
retry_unpriced_response_from_dict = RetryUnpricedResponse.from_dict(retry_unpriced_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


