# HostedCheckoutSettlementResponse

Hosted checkout settlement response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**PaymentResponse**](PaymentResponse.md) |  | 
**ptp** | [**HostedCheckoutSettlementPTPResponse**](HostedCheckoutSettlementPTPResponse.md) |  | 

## Example

```python
from moolabs.models.hosted_checkout_settlement_response import HostedCheckoutSettlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedCheckoutSettlementResponse from a JSON string
hosted_checkout_settlement_response_instance = HostedCheckoutSettlementResponse.from_json(json)
# print the JSON string representation of the object
print(HostedCheckoutSettlementResponse.to_json())

# convert the object into a dict
hosted_checkout_settlement_response_dict = hosted_checkout_settlement_response_instance.to_dict()
# create an instance of HostedCheckoutSettlementResponse from a dict
hosted_checkout_settlement_response_from_dict = HostedCheckoutSettlementResponse.from_dict(hosted_checkout_settlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


