# SDKBatchIngestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted** | **int** |  | 
**skipped** | **int** |  | 
**errors** | **int** |  | 

## Example

```python
from moolabs.models.sdk_batch_ingest_response import SDKBatchIngestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SDKBatchIngestResponse from a JSON string
sdk_batch_ingest_response_instance = SDKBatchIngestResponse.from_json(json)
# print the JSON string representation of the object
print(SDKBatchIngestResponse.to_json())

# convert the object into a dict
sdk_batch_ingest_response_dict = sdk_batch_ingest_response_instance.to_dict()
# create an instance of SDKBatchIngestResponse from a dict
sdk_batch_ingest_response_from_dict = SDKBatchIngestResponse.from_dict(sdk_batch_ingest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


