# SDKBatchIngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[SDKEvent]**](SDKEvent.md) |  | 

## Example

```python
from moolabs.models.sdk_batch_ingest_request import SDKBatchIngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SDKBatchIngestRequest from a JSON string
sdk_batch_ingest_request_instance = SDKBatchIngestRequest.from_json(json)
# print the JSON string representation of the object
print(SDKBatchIngestRequest.to_json())

# convert the object into a dict
sdk_batch_ingest_request_dict = sdk_batch_ingest_request_instance.to_dict()
# create an instance of SDKBatchIngestRequest from a dict
sdk_batch_ingest_request_from_dict = SDKBatchIngestRequest.from_dict(sdk_batch_ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


