# RemittanceResponse

Response for a single remittance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**external_reference** | **str** |  | [optional] 
**source** | **str** |  | 
**payer_name** | **str** |  | [optional] 
**payer_account_ref** | **str** |  | [optional] 
**raw_reference_text** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | 
**received_at** | **datetime** |  | 
**status** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.remittance_response import RemittanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemittanceResponse from a JSON string
remittance_response_instance = RemittanceResponse.from_json(json)
# print the JSON string representation of the object
print(RemittanceResponse.to_json())

# convert the object into a dict
remittance_response_dict = remittance_response_instance.to_dict()
# create an instance of RemittanceResponse from a dict
remittance_response_from_dict = RemittanceResponse.from_dict(remittance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


