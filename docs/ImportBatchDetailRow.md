# ImportBatchDetailRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**service_name** | **str** |  | 
**resource_id** | **str** |  | 
**region** | **str** |  | 
**usage_type** | **str** |  | 
**cost** | **str** |  | 
**currency** | **str** |  | 
**reporting_currency_cost** | **str** |  | 
**reporting_currency** | **str** |  | 
**fx_rate_at_import** | **str** |  | 
**batch_status** | **str** |  | 
**imported_at** | **str** |  | 

## Example

```python
from moolabs.models.import_batch_detail_row import ImportBatchDetailRow

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBatchDetailRow from a JSON string
import_batch_detail_row_instance = ImportBatchDetailRow.from_json(json)
# print the JSON string representation of the object
print(ImportBatchDetailRow.to_json())

# convert the object into a dict
import_batch_detail_row_dict = import_batch_detail_row_instance.to_dict()
# create an instance of ImportBatchDetailRow from a dict
import_batch_detail_row_from_dict = ImportBatchDetailRow.from_dict(import_batch_detail_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


