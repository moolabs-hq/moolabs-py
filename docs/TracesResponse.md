# TracesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger** | **int** |  | 
**outbox** | **int** |  | 
**dlq** | **int** |  | 
**unpriced** | **int** |  | 
**warnings** | **int** |  | 

## Example

```python
from moolabs.models.traces_response import TracesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TracesResponse from a JSON string
traces_response_instance = TracesResponse.from_json(json)
# print the JSON string representation of the object
print(TracesResponse.to_json())

# convert the object into a dict
traces_response_dict = traces_response_instance.to_dict()
# create an instance of TracesResponse from a dict
traces_response_from_dict = TracesResponse.from_dict(traces_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


