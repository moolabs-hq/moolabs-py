# PaymentMatchRequest

POST /payments/{id}/match — exact match to invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 

## Example

```python
from moolabs.models.payment_match_request import PaymentMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMatchRequest from a JSON string
payment_match_request_instance = PaymentMatchRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMatchRequest.to_json())

# convert the object into a dict
payment_match_request_dict = payment_match_request_instance.to_dict()
# create an instance of PaymentMatchRequest from a dict
payment_match_request_from_dict = PaymentMatchRequest.from_dict(payment_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


