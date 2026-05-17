# PaymentFailedRequest

Request for payment failed callback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**payment_id** | **str** | Payment identifier (idempotency key) | 
**failure_reason** | **str** | Failure reason | 
**amount_micros** | **int** | Amount in micros | [optional] 
**failed_at** | **datetime** | Failure timestamp | [optional] 

## Example

```python
from moolabs.models.payment_failed_request import PaymentFailedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFailedRequest from a JSON string
payment_failed_request_instance = PaymentFailedRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFailedRequest.to_json())

# convert the object into a dict
payment_failed_request_dict = payment_failed_request_instance.to_dict()
# create an instance of PaymentFailedRequest from a dict
payment_failed_request_from_dict = PaymentFailedRequest.from_dict(payment_failed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


