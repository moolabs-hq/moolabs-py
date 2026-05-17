# CreditOverridePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_overrides** | [**Dict[str, PooloverridesValue]**](PooloverridesValue.md) |  | 

## Example

```python
from moolabs.models.credit_override_payload import CreditOverridePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditOverridePayload from a JSON string
credit_override_payload_instance = CreditOverridePayload.from_json(json)
# print the JSON string representation of the object
print(CreditOverridePayload.to_json())

# convert the object into a dict
credit_override_payload_dict = credit_override_payload_instance.to_dict()
# create an instance of CreditOverridePayload from a dict
credit_override_payload_from_dict = CreditOverridePayload.from_dict(credit_override_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


