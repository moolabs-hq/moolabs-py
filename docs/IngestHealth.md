# IngestHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_last_hour** | **int** |  | 
**events_last_24h** | **int** |  | 
**consumer_lag_estimate** | **int** |  | 
**cache_hit_ratio** | **float** |  | 
**dlq_count_24h** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.ingest_health import IngestHealth

# TODO update the JSON string below
json = "{}"
# create an instance of IngestHealth from a JSON string
ingest_health_instance = IngestHealth.from_json(json)
# print the JSON string representation of the object
print(IngestHealth.to_json())

# convert the object into a dict
ingest_health_dict = ingest_health_instance.to_dict()
# create an instance of IngestHealth from a dict
ingest_health_from_dict = IngestHealth.from_dict(ingest_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


