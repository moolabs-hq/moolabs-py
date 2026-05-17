# TemplateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**enabled** | **bool** |  | 
**subject** | **str** |  | 
**body** | **str** |  | 
**variable_count** | **int** |  | 

## Example

```python
from moolabs.models.template_item import TemplateItem

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateItem from a JSON string
template_item_instance = TemplateItem.from_json(json)
# print the JSON string representation of the object
print(TemplateItem.to_json())

# convert the object into a dict
template_item_dict = template_item_instance.to_dict()
# create an instance of TemplateItem from a dict
template_item_from_dict = TemplateItem.from_dict(template_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


