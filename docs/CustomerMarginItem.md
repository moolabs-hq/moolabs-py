# CustomerMarginItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | 
**total_valued_burn** | **str** |  | 
**total_cost** | **str** |  | 
**margin** | **str** |  | 
**margin_pct** | **str** |  | 
**margin_reason** | **str** |  | 
**billing_event_count** | **int** |  | 

## Example

```python
from moolabs.models.customer_margin_item import CustomerMarginItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMarginItem from a JSON string
customer_margin_item_instance = CustomerMarginItem.from_json(json)
# print the JSON string representation of the object
print(CustomerMarginItem.to_json())

# convert the object into a dict
customer_margin_item_dict = customer_margin_item_instance.to_dict()
# create an instance of CustomerMarginItem from a dict
customer_margin_item_from_dict = CustomerMarginItem.from_dict(customer_margin_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


