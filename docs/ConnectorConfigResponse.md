# ConnectorConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**connector_type** | **str** |  | 
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from moolabs.models.connector_config_response import ConnectorConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorConfigResponse from a JSON string
connector_config_response_instance = ConnectorConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorConfigResponse.to_json())

# convert the object into a dict
connector_config_response_dict = connector_config_response_instance.to_dict()
# create an instance of ConnectorConfigResponse from a dict
connector_config_response_from_dict = ConnectorConfigResponse.from_dict(connector_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


