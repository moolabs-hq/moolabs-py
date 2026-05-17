# EntitlementPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_id** | **str** |  | 
**feature_key** | **str** |  | 
**entitlement_type** | **str** |  | 
**amount** | [**Amount1**](Amount1.md) |  | [optional] 
**rate_card** | [**RateCardPayload**](RateCardPayload.md) |  | [optional] 

## Example

```python
from moolabs.models.entitlement_payload import EntitlementPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementPayload from a JSON string
entitlement_payload_instance = EntitlementPayload.from_json(json)
# print the JSON string representation of the object
print(EntitlementPayload.to_json())

# convert the object into a dict
entitlement_payload_dict = entitlement_payload_instance.to_dict()
# create an instance of EntitlementPayload from a dict
entitlement_payload_from_dict = EntitlementPayload.from_dict(entitlement_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


