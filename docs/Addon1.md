# Addon1

Partially populated add-on properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the add-on. | 
**key** | **str** | A semi-unique identifier for the resource. | [readonly] 
**version** | **int** | The version of the Add-on which templates this instance. | [readonly] [default to 1]
**instance_type** | [**AddonInstanceType**](AddonInstanceType.md) | The instance type of the add-on. | [readonly] 

## Example

```python
from moolabs.models.addon1 import Addon1

# TODO update the JSON string below
json = "{}"
# create an instance of Addon1 from a JSON string
addon1_instance = Addon1.from_json(json)
# print the JSON string representation of the object
print(Addon1.to_json())

# convert the object into a dict
addon1_dict = addon1_instance.to_dict()
# create an instance of Addon1 from a dict
addon1_from_dict = Addon1.from_dict(addon1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


