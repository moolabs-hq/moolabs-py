# LineItemCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_type** | **str** |  | 
**quantity** | [**Quantity**](Quantity.md) |  | 
**unit** | **str** |  | 
**rate_snapshot_id** | **str** |  | [optional] 
**unit_cost** | [**UnitCost**](UnitCost.md) |  | 
**line_total** | [**LineTotal**](LineTotal.md) |  | 
**reporting_line_total** | [**ReportingLineTotal**](ReportingLineTotal.md) |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.line_item_create import LineItemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemCreate from a JSON string
line_item_create_instance = LineItemCreate.from_json(json)
# print the JSON string representation of the object
print(LineItemCreate.to_json())

# convert the object into a dict
line_item_create_dict = line_item_create_instance.to_dict()
# create an instance of LineItemCreate from a dict
line_item_create_from_dict = LineItemCreate.from_dict(line_item_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


