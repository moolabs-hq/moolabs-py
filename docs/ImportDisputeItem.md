# ImportDisputeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**invoice_id** | **str** |  | 
**disputed_amount_micros** | **int** |  | 
**dispute_type** | **str** |  | [optional] [default to 'admin']
**status** | **str** |  | [optional] [default to 'open']
**description** | **str** |  | [optional] [default to 'Imported from Growfin']
**external_dispute_id** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 

## Example

```python
from moolabs.models.import_dispute_item import ImportDisputeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDisputeItem from a JSON string
import_dispute_item_instance = ImportDisputeItem.from_json(json)
# print the JSON string representation of the object
print(ImportDisputeItem.to_json())

# convert the object into a dict
import_dispute_item_dict = import_dispute_item_instance.to_dict()
# create an instance of ImportDisputeItem from a dict
import_dispute_item_from_dict = ImportDisputeItem.from_dict(import_dispute_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


