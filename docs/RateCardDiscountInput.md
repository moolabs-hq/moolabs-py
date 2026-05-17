# RateCardDiscountInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'percentage']
**value** | **float** |  | 
**scope** | **str** |  | [optional] [default to 'all']
**duration** | **str** |  | [optional] [default to 'entire']
**cycles** | **int** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**selected_items** | **List[str]** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.rate_card_discount_input import RateCardDiscountInput

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardDiscountInput from a JSON string
rate_card_discount_input_instance = RateCardDiscountInput.from_json(json)
# print the JSON string representation of the object
print(RateCardDiscountInput.to_json())

# convert the object into a dict
rate_card_discount_input_dict = rate_card_discount_input_instance.to_dict()
# create an instance of RateCardDiscountInput from a dict
rate_card_discount_input_from_dict = RateCardDiscountInput.from_dict(rate_card_discount_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


