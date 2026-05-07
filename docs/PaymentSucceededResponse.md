# PaymentSucceededResponse

Response from payment succeeded callback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 
**grant_id** | **str** |  | 
**journal_entry_id** | **str** |  | 
**amount_micros** | **int** |  | 
**fx_rate_version** | **str** |  | 
**paid_amount_usd_micros** | **int** |  | 

## Example

```python
from moolabs.models.payment_succeeded_response import PaymentSucceededResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSucceededResponse from a JSON string
payment_succeeded_response_instance = PaymentSucceededResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentSucceededResponse.to_json())

# convert the object into a dict
payment_succeeded_response_dict = payment_succeeded_response_instance.to_dict()
# create an instance of PaymentSucceededResponse from a dict
payment_succeeded_response_from_dict = PaymentSucceededResponse.from_dict(payment_succeeded_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


