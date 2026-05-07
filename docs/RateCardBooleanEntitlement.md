# RateCardBooleanEntitlement

Entitlement template of a boolean entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**type** | **str** |  | 

## Example

```python
from moolabs.models.rate_card_boolean_entitlement import RateCardBooleanEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardBooleanEntitlement from a JSON string
rate_card_boolean_entitlement_instance = RateCardBooleanEntitlement.from_json(json)
# print the JSON string representation of the object
print(RateCardBooleanEntitlement.to_json())

# convert the object into a dict
rate_card_boolean_entitlement_dict = rate_card_boolean_entitlement_instance.to_dict()
# create an instance of RateCardBooleanEntitlement from a dict
rate_card_boolean_entitlement_from_dict = RateCardBooleanEntitlement.from_dict(rate_card_boolean_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


