# QuoteLineItemInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_no** | **int** |  | [optional] 
**sku_ref** | **str** |  | 
**feature_key** | **str** |  | [optional] 
**sku_version** | **str** |  | [optional] 
**rate_card_ref** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**plan_version** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] [default to '1']
**quantity_unit** | **str** |  | [optional] [default to 'unit']
**pricing_basis** | **str** |  | [optional] [default to 'recurring']
**requested_discount** | **Dict[str, object]** |  | [optional] 
**feature_overrides** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from moolabs.models.quote_line_item_input import QuoteLineItemInput

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLineItemInput from a JSON string
quote_line_item_input_instance = QuoteLineItemInput.from_json(json)
# print the JSON string representation of the object
print(QuoteLineItemInput.to_json())

# convert the object into a dict
quote_line_item_input_dict = quote_line_item_input_instance.to_dict()
# create an instance of QuoteLineItemInput from a dict
quote_line_item_input_from_dict = QuoteLineItemInput.from_dict(quote_line_item_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


