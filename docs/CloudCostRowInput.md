# CloudCostRowInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 
**resource_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**usage_type** | **str** |  | [optional] 
**cost** | [**Cost**](Cost.md) |  | 
**currency** | **str** |  | [optional] [default to 'USD']
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.cloud_cost_row_input import CloudCostRowInput

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCostRowInput from a JSON string
cloud_cost_row_input_instance = CloudCostRowInput.from_json(json)
# print the JSON string representation of the object
print(CloudCostRowInput.to_json())

# convert the object into a dict
cloud_cost_row_input_dict = cloud_cost_row_input_instance.to_dict()
# create an instance of CloudCostRowInput from a dict
cloud_cost_row_input_from_dict = CloudCostRowInput.from_dict(cloud_cost_row_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


