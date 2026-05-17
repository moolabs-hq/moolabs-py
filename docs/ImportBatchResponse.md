# ImportBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_batch_id** | **str** |  | 
**tenant_id** | **str** |  | 
**cloud_provider** | **str** |  | 
**billing_period_start** | **str** |  | 
**billing_period_end** | **str** |  | 
**row_count** | **int** |  | 
**reporting_currency** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from moolabs.models.import_batch_response import ImportBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBatchResponse from a JSON string
import_batch_response_instance = ImportBatchResponse.from_json(json)
# print the JSON string representation of the object
print(ImportBatchResponse.to_json())

# convert the object into a dict
import_batch_response_dict = import_batch_response_instance.to_dict()
# create an instance of ImportBatchResponse from a dict
import_batch_response_from_dict = ImportBatchResponse.from_dict(import_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


