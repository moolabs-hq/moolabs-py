# WebhookUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] [default to 'none']
**secret** | **str** |  | [optional] 
**subscribed_events** | **List[str]** |  | [optional] 
**owner_email** | **str** |  | [optional] 

## Example

```python
from moolabs.models.webhook_update import WebhookUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdate from a JSON string
webhook_update_instance = WebhookUpdate.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdate.to_json())

# convert the object into a dict
webhook_update_dict = webhook_update_instance.to_dict()
# create an instance of WebhookUpdate from a dict
webhook_update_from_dict = WebhookUpdate.from_dict(webhook_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


