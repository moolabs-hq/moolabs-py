# HostedCheckoutSettlementRequest

POST /payments/hosted-checkout-settlements — settle a successful hosted checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**ptp_id** | **str** |  | 
**invoice_id** | **str** |  | 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] 
**base_currency_code** | **str** |  | [optional] 
**amount_base_micros** | **int** |  | [optional] 
**external_payment_id** | **str** |  | 
**received_at** | **datetime** |  | 
**payment_method** | **str** | stripe, ach, wire, check, credit_adjustment, other | [optional] [default to 'stripe']
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.hosted_checkout_settlement_request import HostedCheckoutSettlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostedCheckoutSettlementRequest from a JSON string
hosted_checkout_settlement_request_instance = HostedCheckoutSettlementRequest.from_json(json)
# print the JSON string representation of the object
print(HostedCheckoutSettlementRequest.to_json())

# convert the object into a dict
hosted_checkout_settlement_request_dict = hosted_checkout_settlement_request_instance.to_dict()
# create an instance of HostedCheckoutSettlementRequest from a dict
hosted_checkout_settlement_request_from_dict = HostedCheckoutSettlementRequest.from_dict(hosted_checkout_settlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


