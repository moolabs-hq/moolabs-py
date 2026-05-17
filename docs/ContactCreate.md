# ContactCreate

POST /accounts/{account_id}/contacts — create a contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**role** | **str** | One of: ap, finance_admin, procurement, buyer, legal, exec, other | 
**is_primary_ap** | **bool** |  | [optional] [default to False]
**locale** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from moolabs.models.contact_create import ContactCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCreate from a JSON string
contact_create_instance = ContactCreate.from_json(json)
# print the JSON string representation of the object
print(ContactCreate.to_json())

# convert the object into a dict
contact_create_dict = contact_create_instance.to_dict()
# create an instance of ContactCreate from a dict
contact_create_from_dict = ContactCreate.from_dict(contact_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


