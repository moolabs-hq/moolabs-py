# BatchIngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[CostEventIngest]**](CostEventIngest.md) |  | 

## Example

```python
from moolabs.models.batch_ingest_request import BatchIngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchIngestRequest from a JSON string
batch_ingest_request_instance = BatchIngestRequest.from_json(json)
# print the JSON string representation of the object
print(BatchIngestRequest.to_json())

# convert the object into a dict
batch_ingest_request_dict = batch_ingest_request_instance.to_dict()
# create an instance of BatchIngestRequest from a dict
batch_ingest_request_from_dict = BatchIngestRequest.from_dict(batch_ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


