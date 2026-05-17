# CustomerItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**netsuite_id** | **str** |  | 
**entity_id_display** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_person** | **bool** |  | 
**currency_code** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**managed_through_portal** | **Dict[str, object]** |  | [optional] 
**managed_through_portal_source_field_id** | **str** |  | [optional] 
**ns_last_modified** | **datetime** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.customer_item import CustomerItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerItem from a JSON string
customer_item_instance = CustomerItem.from_json(json)
# print the JSON string representation of the object
print(CustomerItem.to_json())

# convert the object into a dict
customer_item_dict = customer_item_instance.to_dict()
# create an instance of CustomerItem from a dict
customer_item_from_dict = CustomerItem.from_dict(customer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


