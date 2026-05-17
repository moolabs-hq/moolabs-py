# HostedCheckoutSettlementPTPResponse

Promise-to-pay summary returned from hosted checkout settlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**case_id** | **str** |  | 
**invoice_id** | **str** |  | [optional] 
**promised_amount_micros** | **int** |  | 
**fulfilled_amount_micros** | **int** |  | 
**status** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.hosted_checkout_settlement_ptp_response import HostedCheckoutSettlementPTPResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HostedCheckoutSettlementPTPResponse from a JSON string
hosted_checkout_settlement_ptp_response_instance = HostedCheckoutSettlementPTPResponse.from_json(json)
# print the JSON string representation of the object
print(HostedCheckoutSettlementPTPResponse.to_json())

# convert the object into a dict
hosted_checkout_settlement_ptp_response_dict = hosted_checkout_settlement_ptp_response_instance.to_dict()
# create an instance of HostedCheckoutSettlementPTPResponse from a dict
hosted_checkout_settlement_ptp_response_from_dict = HostedCheckoutSettlementPTPResponse.from_dict(hosted_checkout_settlement_ptp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


