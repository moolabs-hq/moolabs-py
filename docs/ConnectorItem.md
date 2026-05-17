# ConnectorItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**category** | **str** |  | 
**status** | **str** |  | 
**auth_status** | **str** |  | 
**last_sync** | **str** |  | 
**mapping_info** | **str** |  | [optional] 
**sync_direction** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**config** | **Dict[str, object]** |  | 

## Example

```python
from moolabs.models.connector_item import ConnectorItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorItem from a JSON string
connector_item_instance = ConnectorItem.from_json(json)
# print the JSON string representation of the object
print(ConnectorItem.to_json())

# convert the object into a dict
connector_item_dict = connector_item_instance.to_dict()
# create an instance of ConnectorItem from a dict
connector_item_from_dict = ConnectorItem.from_dict(connector_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


