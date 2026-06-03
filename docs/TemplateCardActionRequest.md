# TemplateCardActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**idempotency_key** | **str** |  | 
**chat_session_id** | **str** |  | [optional] 
**confirmation** | **Dict[str, object]** |  | [optional] 
**change_reason** | **str** |  | [optional] 
**preview_case_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.template_card_action_request import TemplateCardActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateCardActionRequest from a JSON string
template_card_action_request_instance = TemplateCardActionRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateCardActionRequest.to_json())

# convert the object into a dict
template_card_action_request_dict = template_card_action_request_instance.to_dict()
# create an instance of TemplateCardActionRequest from a dict
template_card_action_request_from_dict = TemplateCardActionRequest.from_dict(template_card_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


