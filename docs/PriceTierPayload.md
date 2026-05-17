# PriceTierPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**up_to** | [**Upto**](Upto.md) |  | [optional] 
**unit_amount** | [**Unitamount**](Unitamount.md) |  | 
**flat_amount** | [**Flatamount**](Flatamount.md) |  | [optional] 

## Example

```python
from moolabs.models.price_tier_payload import PriceTierPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PriceTierPayload from a JSON string
price_tier_payload_instance = PriceTierPayload.from_json(json)
# print the JSON string representation of the object
print(PriceTierPayload.to_json())

# convert the object into a dict
price_tier_payload_dict = price_tier_payload_instance.to_dict()
# create an instance of PriceTierPayload from a dict
price_tier_payload_from_dict = PriceTierPayload.from_dict(price_tier_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


