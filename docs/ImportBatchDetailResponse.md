# ImportBatchDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_batch_id** | **str** |  | 
**cloud_provider** | **str** |  | 
**billing_period_start** | **str** |  | 
**billing_period_end** | **str** |  | 
**batch_status** | **str** |  | 
**rows** | [**List[ImportBatchDetailRow]**](ImportBatchDetailRow.md) |  | 

## Example

```python
from moolabs.models.import_batch_detail_response import ImportBatchDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBatchDetailResponse from a JSON string
import_batch_detail_response_instance = ImportBatchDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ImportBatchDetailResponse.to_json())

# convert the object into a dict
import_batch_detail_response_dict = import_batch_detail_response_instance.to_dict()
# create an instance of ImportBatchDetailResponse from a dict
import_batch_detail_response_from_dict = ImportBatchDetailResponse.from_dict(import_batch_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


