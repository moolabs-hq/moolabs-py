# ConnectorHealthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**connector_type** | **str** |  | 
**status** | **str** |  | 
**last_synced_at** | **datetime** |  | 
**events_ingested_total** | **int** |  | 
**events_last_24h** | **int** |  | 
**errors_last_24h** | **int** |  | 
**is_aggregate_only** | **bool** |  | 

## Example

```python
from moolabs.models.connector_health_response import ConnectorHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorHealthResponse from a JSON string
connector_health_response_instance = ConnectorHealthResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorHealthResponse.to_json())

# convert the object into a dict
connector_health_response_dict = connector_health_response_instance.to_dict()
# create an instance of ConnectorHealthResponse from a dict
connector_health_response_from_dict = ConnectorHealthResponse.from_dict(connector_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


