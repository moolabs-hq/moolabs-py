# PaymentFailedResponse

Response from payment failed callback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 
**wallet_id** | **str** |  | 
**failure_reason** | **str** |  | 
**outbox_event_id** | **str** |  | 

## Example

```python
from moolabs.models.payment_failed_response import PaymentFailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFailedResponse from a JSON string
payment_failed_response_instance = PaymentFailedResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentFailedResponse.to_json())

# convert the object into a dict
payment_failed_response_dict = payment_failed_response_instance.to_dict()
# create an instance of PaymentFailedResponse from a dict
payment_failed_response_from_dict = PaymentFailedResponse.from_dict(payment_failed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


