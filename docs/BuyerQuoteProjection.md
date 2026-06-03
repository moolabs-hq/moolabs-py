# BuyerQuoteProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** |  | 
**version** | **int** |  | 
**status** | **str** |  | 
**quote_type** | **str** |  | [optional] [default to 'new_subscription']
**buyer_contact** | **Dict[str, object]** |  | 
**line_items** | [**List[BuyerQuoteLineItem]**](BuyerQuoteLineItem.md) |  | 
**commercial_terms** | **Dict[str, object]** |  | 
**credit_terms** | **Dict[str, object]** |  | 
**lifecycle_terms** | **Dict[str, object]** |  | [optional] 
**pricing** | [**BuyerQuotePricing**](BuyerQuotePricing.md) |  | 

## Example

```python
from moolabs.models.buyer_quote_projection import BuyerQuoteProjection

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerQuoteProjection from a JSON string
buyer_quote_projection_instance = BuyerQuoteProjection.from_json(json)
# print the JSON string representation of the object
print(BuyerQuoteProjection.to_json())

# convert the object into a dict
buyer_quote_projection_dict = buyer_quote_projection_instance.to_dict()
# create an instance of BuyerQuoteProjection from a dict
buyer_quote_projection_from_dict = BuyerQuoteProjection.from_dict(buyer_quote_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


