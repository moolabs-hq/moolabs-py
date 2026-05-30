# BuyerQuoteLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_no** | **int** |  | 
**sku_ref** | **str** |  | 
**feature_key** | **str** |  | [optional] 
**quantity** | **str** |  | 
**quantity_unit** | **str** |  | [optional] 
**unit_price_micros** | **int** |  | [optional] 
**subtotal_micros** | **int** |  | 
**discount_micros** | **int** |  | 
**total_micros** | **int** |  | 

## Example

```python
from moolabs.models.buyer_quote_line_item import BuyerQuoteLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerQuoteLineItem from a JSON string
buyer_quote_line_item_instance = BuyerQuoteLineItem.from_json(json)
# print the JSON string representation of the object
print(BuyerQuoteLineItem.to_json())

# convert the object into a dict
buyer_quote_line_item_dict = buyer_quote_line_item_instance.to_dict()
# create an instance of BuyerQuoteLineItem from a dict
buyer_quote_line_item_from_dict = BuyerQuoteLineItem.from_dict(buyer_quote_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


