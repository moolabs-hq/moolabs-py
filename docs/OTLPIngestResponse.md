# OTLPIngestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted** | **int** |  | 
**skipped** | **int** |  | 
**errors** | **int** |  | 

## Example

```python
from moolabs.models.otlp_ingest_response import OTLPIngestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OTLPIngestResponse from a JSON string
otlp_ingest_response_instance = OTLPIngestResponse.from_json(json)
# print the JSON string representation of the object
print(OTLPIngestResponse.to_json())

# convert the object into a dict
otlp_ingest_response_dict = otlp_ingest_response_instance.to_dict()
# create an instance of OTLPIngestResponse from a dict
otlp_ingest_response_from_dict = OTLPIngestResponse.from_dict(otlp_ingest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


