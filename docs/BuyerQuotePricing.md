# BuyerQuotePricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**subtotal_micros** | **int** |  | 
**discount_micros** | **int** |  | 
**total_micros** | **int** |  | 

## Example

```python
from moolabs.models.buyer_quote_pricing import BuyerQuotePricing

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerQuotePricing from a JSON string
buyer_quote_pricing_instance = BuyerQuotePricing.from_json(json)
# print the JSON string representation of the object
print(BuyerQuotePricing.to_json())

# convert the object into a dict
buyer_quote_pricing_dict = buyer_quote_pricing_instance.to_dict()
# create an instance of BuyerQuotePricing from a dict
buyer_quote_pricing_from_dict = BuyerQuotePricing.from_dict(buyer_quote_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


