# CommercialOverrides

Subscription-level commercial terms (persisted column; metadata fallback for legacy rows).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_card_discount** | [**RateCardDiscount**](RateCardDiscount.md) |  | [optional] 
**credit_override** | [**CreditOverride**](CreditOverride.md) |  | [optional] 
**entitlement_overrides** | [**List[EntitlementOverride]**](EntitlementOverride.md) |  | [optional] 
**overdraft_settings** | [**OverdraftSettings**](OverdraftSettings.md) |  | [optional] 

## Example

```python
from moolabs.models.commercial_overrides import CommercialOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOverrides from a JSON string
commercial_overrides_instance = CommercialOverrides.from_json(json)
# print the JSON string representation of the object
print(CommercialOverrides.to_json())

# convert the object into a dict
commercial_overrides_dict = commercial_overrides_instance.to_dict()
# create an instance of CommercialOverrides from a dict
commercial_overrides_from_dict = CommercialOverrides.from_dict(commercial_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


