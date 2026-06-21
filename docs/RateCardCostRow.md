# RateCardCostRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**feature_key** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**currency** | **str** |  | 
**unit_price_micros** | **int** |  | [optional] 
**cost_unit_micros** | **int** |  | [optional] 
**cost_source** | **str** |  | 
**margin_pct** | **float** |  | [optional] 
**pricing_shape** | **str** |  | [optional] 

## Example

```python
from moolabs.models.rate_card_cost_row import RateCardCostRow

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardCostRow from a JSON string
rate_card_cost_row_instance = RateCardCostRow.from_json(json)
# print the JSON string representation of the object
print(RateCardCostRow.to_json())

# convert the object into a dict
rate_card_cost_row_dict = rate_card_cost_row_instance.to_dict()
# create an instance of RateCardCostRow from a dict
rate_card_cost_row_from_dict = RateCardCostRow.from_dict(rate_card_cost_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


