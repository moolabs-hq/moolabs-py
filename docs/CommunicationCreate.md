# CommunicationCreate

POST /cases/{case_id}/communications — create a communication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** |  | [optional] 
**direction** | **str** | outbound or inbound | [optional] [default to 'outbound']
**channel** | **str** | email, sms, phone, portal, letter, internal_note | [optional] [default to 'email']
**audience** | **str** | customer, internal, or inbound_system (optional; server infers default when omitted) | [optional] 
**subject** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**dunning_stage** | **str** |  | [optional] [default to 'pre_due']
**generated_by** | **str** | agent, human, system, portal_customer | [optional] [default to 'human']
**thread_id** | **str** |  | [optional] 
**parent_communication_id** | **str** |  | [optional] 
**external_message_id** | **str** | Optional pre-set external message ID (test/migration use). Production sends populate this from the email provider response. | [optional] 

## Example

```python
from moolabs.models.communication_create import CommunicationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationCreate from a JSON string
communication_create_instance = CommunicationCreate.from_json(json)
# print the JSON string representation of the object
print(CommunicationCreate.to_json())

# convert the object into a dict
communication_create_dict = communication_create_instance.to_dict()
# create an instance of CommunicationCreate from a dict
communication_create_from_dict = CommunicationCreate.from_dict(communication_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


