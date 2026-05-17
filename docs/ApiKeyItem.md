# ApiKeyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**environment** | **str** |  | 
**created_at** | **str** |  | 
**last_used_at** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.api_key_item import ApiKeyItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyItem from a JSON string
api_key_item_instance = ApiKeyItem.from_json(json)
# print the JSON string representation of the object
print(ApiKeyItem.to_json())

# convert the object into a dict
api_key_item_dict = api_key_item_instance.to_dict()
# create an instance of ApiKeyItem from a dict
api_key_item_from_dict = ApiKeyItem.from_dict(api_key_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


