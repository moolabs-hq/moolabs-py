# EntitlementOverridePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from moolabs.models.entitlement_override_payload import EntitlementOverridePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverridePayload from a JSON string
entitlement_override_payload_instance = EntitlementOverridePayload.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverridePayload.to_json())

# convert the object into a dict
entitlement_override_payload_dict = entitlement_override_payload_instance.to_dict()
# create an instance of EntitlementOverridePayload from a dict
entitlement_override_payload_from_dict = EntitlementOverridePayload.from_dict(entitlement_override_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


