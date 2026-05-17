# ContactUpdate

PATCH /contacts/{id} — partial update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**is_primary_ap** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from moolabs.models.contact_update import ContactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ContactUpdate from a JSON string
contact_update_instance = ContactUpdate.from_json(json)
# print the JSON string representation of the object
print(ContactUpdate.to_json())

# convert the object into a dict
contact_update_dict = contact_update_instance.to_dict()
# create an instance of ContactUpdate from a dict
contact_update_from_dict = ContactUpdate.from_dict(contact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


