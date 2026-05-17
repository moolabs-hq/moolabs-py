# CommercialOverridesPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_card_discount** | [**RateCardDiscountPayload**](RateCardDiscountPayload.md) |  | [optional] 
**credit_override** | [**CreditOverridePayload**](CreditOverridePayload.md) |  | [optional] 
**entitlement_overrides** | [**List[EntitlementOverridePayload]**](EntitlementOverridePayload.md) |  | [optional] 
**overdraft_settings** | [**OverdraftSettingsPayload**](OverdraftSettingsPayload.md) |  | [optional] 

## Example

```python
from moolabs.models.commercial_overrides_payload import CommercialOverridesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOverridesPayload from a JSON string
commercial_overrides_payload_instance = CommercialOverridesPayload.from_json(json)
# print the JSON string representation of the object
print(CommercialOverridesPayload.to_json())

# convert the object into a dict
commercial_overrides_payload_dict = commercial_overrides_payload_instance.to_dict()
# create an instance of CommercialOverridesPayload from a dict
commercial_overrides_payload_from_dict = CommercialOverridesPayload.from_dict(commercial_overrides_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


