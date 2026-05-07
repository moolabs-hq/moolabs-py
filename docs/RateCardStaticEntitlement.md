# RateCardStaticEntitlement

Entitlement template of a static entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**type** | **str** |  | 
**config** | **str** | The JSON parsable config of the entitlement. This value is also returned when checking entitlement access and it is useful for configuring fine-grained access settings to the feature, implemented in your own system. Has to be an object. | 

## Example

```python
from moolabs.models.rate_card_static_entitlement import RateCardStaticEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardStaticEntitlement from a JSON string
rate_card_static_entitlement_instance = RateCardStaticEntitlement.from_json(json)
# print the JSON string representation of the object
print(RateCardStaticEntitlement.to_json())

# convert the object into a dict
rate_card_static_entitlement_dict = rate_card_static_entitlement_instance.to_dict()
# create an instance of RateCardStaticEntitlement from a dict
rate_card_static_entitlement_from_dict = RateCardStaticEntitlement.from_dict(rate_card_static_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


