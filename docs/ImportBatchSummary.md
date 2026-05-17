# ImportBatchSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_batch_id** | **str** |  | 
**cloud_provider** | **str** |  | 
**billing_period_start** | **str** |  | 
**billing_period_end** | **str** |  | 
**batch_status** | **str** |  | 
**row_count** | **int** |  | 
**total_reporting_cost** | **str** |  | 
**reporting_currency** | **str** |  | 
**imported_at** | **str** |  | 
**clickhouse_sync_status** | **str** |  | [optional] [default to 'pending']
**clickhouse_synced_at** | **str** |  | [optional] 
**clickhouse_sync_error** | **str** |  | [optional] 
**clickhouse_sync_attempts** | **int** |  | [optional] [default to 0]

## Example

```python
from moolabs.models.import_batch_summary import ImportBatchSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBatchSummary from a JSON string
import_batch_summary_instance = ImportBatchSummary.from_json(json)
# print the JSON string representation of the object
print(ImportBatchSummary.to_json())

# convert the object into a dict
import_batch_summary_dict = import_batch_summary_instance.to_dict()
# create an instance of ImportBatchSummary from a dict
import_batch_summary_from_dict = ImportBatchSummary.from_dict(import_batch_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


