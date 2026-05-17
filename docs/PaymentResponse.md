# PaymentResponse

Payment response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**remittance_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | 
**base_currency_code** | **str** |  | 
**amount_base_micros** | **int** |  | 
**payment_method** | **str** |  | 
**external_payment_id** | **str** |  | [optional] 
**status** | **str** |  | 
**match_confidence** | **float** |  | [optional] 
**match_method** | **str** |  | [optional] 
**verification_status** | **str** |  | 
**verified_at** | **datetime** |  | [optional] 
**verified_source** | **str** |  | [optional] 
**verified_external_payment_id** | **str** |  | [optional] 
**received_at** | **datetime** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.payment_response import PaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponse from a JSON string
payment_response_instance = PaymentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentResponse.to_json())

# convert the object into a dict
payment_response_dict = payment_response_instance.to_dict()
# create an instance of PaymentResponse from a dict
payment_response_from_dict = PaymentResponse.from_dict(payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


