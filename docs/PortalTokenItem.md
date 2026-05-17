# PortalTokenItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**subject** | **str** |  | 
**expires_at** | **str** |  | 
**scopes** | **List[object]** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from moolabs.models.portal_token_item import PortalTokenItem

# TODO update the JSON string below
json = "{}"
# create an instance of PortalTokenItem from a JSON string
portal_token_item_instance = PortalTokenItem.from_json(json)
# print the JSON string representation of the object
print(PortalTokenItem.to_json())

# convert the object into a dict
portal_token_item_dict = portal_token_item_instance.to_dict()
# create an instance of PortalTokenItem from a dict
portal_token_item_from_dict = PortalTokenItem.from_dict(portal_token_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


