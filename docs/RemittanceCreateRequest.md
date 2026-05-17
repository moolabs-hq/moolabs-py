# RemittanceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**external_reference** | **str** |  | [optional] 
**payer_name** | **str** |  | [optional] 
**payer_account_ref** | **str** |  | [optional] 
**raw_reference_text** | **str** |  | [optional] 
**received_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.remittance_create_request import RemittanceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemittanceCreateRequest from a JSON string
remittance_create_request_instance = RemittanceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RemittanceCreateRequest.to_json())

# convert the object into a dict
remittance_create_request_dict = remittance_create_request_instance.to_dict()
# create an instance of RemittanceCreateRequest from a dict
remittance_create_request_from_dict = RemittanceCreateRequest.from_dict(remittance_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


