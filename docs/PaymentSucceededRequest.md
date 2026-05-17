# PaymentSucceededRequest

Request for payment succeeded callback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**payment_id** | **str** | Payment identifier (idempotency key) | 
**amount_micros** | **int** | Amount in micros | 
**fx_rate_version** | **str** | FX rate version | [optional] 
**credits_per_usd_micros** | **int** | Credits per USD micros | [optional] 
**effective_at** | **datetime** | Effective timestamp | [optional] 

## Example

```python
from moolabs.models.payment_succeeded_request import PaymentSucceededRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSucceededRequest from a JSON string
payment_succeeded_request_instance = PaymentSucceededRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentSucceededRequest.to_json())

# convert the object into a dict
payment_succeeded_request_dict = payment_succeeded_request_instance.to_dict()
# create an instance of PaymentSucceededRequest from a dict
payment_succeeded_request_from_dict = PaymentSucceededRequest.from_dict(payment_succeeded_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


