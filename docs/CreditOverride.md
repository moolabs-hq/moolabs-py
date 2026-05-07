# CreditOverride

Adjusts credit pool amounts; keys are feature keys or \"__global__\" for the global pool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_overrides** | **Dict[str, float]** |  | 

## Example

```python
from moolabs.models.credit_override import CreditOverride

# TODO update the JSON string below
json = "{}"
# create an instance of CreditOverride from a JSON string
credit_override_instance = CreditOverride.from_json(json)
# print the JSON string representation of the object
print(CreditOverride.to_json())

# convert the object into a dict
credit_override_dict = credit_override_instance.to_dict()
# create an instance of CreditOverride from a dict
credit_override_from_dict = CreditOverride.from_dict(credit_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


