# SenderUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** |  | [optional] 
**from_address** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**support_contact** | **str** |  | [optional] 

## Example

```python
from moolabs.models.sender_update import SenderUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SenderUpdate from a JSON string
sender_update_instance = SenderUpdate.from_json(json)
# print the JSON string representation of the object
print(SenderUpdate.to_json())

# convert the object into a dict
sender_update_dict = sender_update_instance.to_dict()
# create an instance of SenderUpdate from a dict
sender_update_from_dict = SenderUpdate.from_dict(sender_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


