# CustomerCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | 
**total_cost** | **float** |  | 
**request_count** | **int** |  | 
**avg_cost_per_request** | **float** |  | 
**top_model** | **str** |  | 

## Example

```python
from moolabs.models.customer_cost_item import CustomerCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCostItem from a JSON string
customer_cost_item_instance = CustomerCostItem.from_json(json)
# print the JSON string representation of the object
print(CustomerCostItem.to_json())

# convert the object into a dict
customer_cost_item_dict = customer_cost_item_instance.to_dict()
# create an instance of CustomerCostItem from a dict
customer_cost_item_from_dict = CustomerCostItem.from_dict(customer_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


