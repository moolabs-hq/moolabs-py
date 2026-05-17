# CreditOverrideInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**amount** | **float** |  | [optional] [default to 0.0]
**unit** | **str** |  | [optional] [default to 'credits']
**expiry** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**pool_overrides** | **Dict[str, float]** |  | [optional] 

## Example

```python
from moolabs.models.credit_override_input import CreditOverrideInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreditOverrideInput from a JSON string
credit_override_input_instance = CreditOverrideInput.from_json(json)
# print the JSON string representation of the object
print(CreditOverrideInput.to_json())

# convert the object into a dict
credit_override_input_dict = credit_override_input_instance.to_dict()
# create an instance of CreditOverrideInput from a dict
credit_override_input_from_dict = CreditOverrideInput.from_dict(credit_override_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


