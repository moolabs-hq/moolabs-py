# RateCardEntitlement

Entitlement templates are used to define the entitlements of a plan. Features are omitted from the entitlement template, as they are defined in the rate card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**type** | **str** |  | 
**is_soft_limit** | **bool** | If softLimit&#x3D;true the subject can use the feature even if the entitlement is exhausted, hasAccess will always be true. | [optional] [default to False]
**issue_after_reset** | **float** | You can grant usage automatically alongside the entitlement, the example scenario would be creating a starting balance. If an amount is specified here, a grant will be created alongside the entitlement with the specified amount. That grant will have it&#39;s rollover settings configured in a way that after each reset operation, the balance will return the original amount specified here. Manually creating such a grant would mean having the \&quot;amount\&quot;, \&quot;minRolloverAmount\&quot;, and \&quot;maxRolloverAmount\&quot; fields all be the same. | [optional] 
**issue_after_reset_priority** | **int** | Defines the grant priority for the default grant. | [optional] [default to 1]
**preserve_overage_at_reset** | **bool** | If true, the overage is preserved at reset. If false, the usage is reset to 0. | [optional] [default to False]
**usage_period** | **str** | The interval of the metered entitlement. Defaults to the billing cadence of the rate card. | [optional] 
**config** | **str** | The JSON parsable config of the entitlement. This value is also returned when checking entitlement access and it is useful for configuring fine-grained access settings to the feature, implemented in your own system. Has to be an object. | 

## Example

```python
from moolabs.models.rate_card_entitlement import RateCardEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardEntitlement from a JSON string
rate_card_entitlement_instance = RateCardEntitlement.from_json(json)
# print the JSON string representation of the object
print(RateCardEntitlement.to_json())

# convert the object into a dict
rate_card_entitlement_dict = rate_card_entitlement_instance.to_dict()
# create an instance of RateCardEntitlement from a dict
rate_card_entitlement_from_dict = RateCardEntitlement.from_dict(rate_card_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


