# EntitlementOverride

Override amount for a static entitlement feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**amount** | **float** |  | 

## Example

```python
from moolabs.models.entitlement_override import EntitlementOverride

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverride from a JSON string
entitlement_override_instance = EntitlementOverride.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverride.to_json())

# convert the object into a dict
entitlement_override_dict = entitlement_override_instance.to_dict()
# create an instance of EntitlementOverride from a dict
entitlement_override_from_dict = EntitlementOverride.from_dict(entitlement_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


