# CreditCostRatioItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**total_valued_burn** | **str** |  | 
**total_cost** | **str** |  | 
**credit_cost_ratio** | **str** |  | 

## Example

```python
from moolabs.models.credit_cost_ratio_item import CreditCostRatioItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCostRatioItem from a JSON string
credit_cost_ratio_item_instance = CreditCostRatioItem.from_json(json)
# print the JSON string representation of the object
print(CreditCostRatioItem.to_json())

# convert the object into a dict
credit_cost_ratio_item_dict = credit_cost_ratio_item_instance.to_dict()
# create an instance of CreditCostRatioItem from a dict
credit_cost_ratio_item_from_dict = CreditCostRatioItem.from_dict(credit_cost_ratio_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


