# CommercialOverridesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** |  | 
**customer_id** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**effective_from** | **str** |  | 
**entitlement_overrides** | [**List[EntitlementOverrideInput]**](EntitlementOverrideInput.md) |  | [optional] 
**credit_override** | [**CreditOverrideInput**](CreditOverrideInput.md) |  | [optional] 
**rate_card_discount** | [**RateCardDiscountInput**](RateCardDiscountInput.md) |  | [optional] 

## Example

```python
from moolabs.models.commercial_overrides_input import CommercialOverridesInput

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOverridesInput from a JSON string
commercial_overrides_input_instance = CommercialOverridesInput.from_json(json)
# print the JSON string representation of the object
print(CommercialOverridesInput.to_json())

# convert the object into a dict
commercial_overrides_input_dict = commercial_overrides_input_instance.to_dict()
# create an instance of CommercialOverridesInput from a dict
commercial_overrides_input_from_dict = CommercialOverridesInput.from_dict(commercial_overrides_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


