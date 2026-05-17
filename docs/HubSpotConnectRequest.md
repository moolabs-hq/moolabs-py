# HubSpotConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_direction** | **str** |  | 
**sync_frequency** | **str** |  | 
**owner** | **str** |  | [optional] 

## Example

```python
from moolabs.models.hub_spot_connect_request import HubSpotConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HubSpotConnectRequest from a JSON string
hub_spot_connect_request_instance = HubSpotConnectRequest.from_json(json)
# print the JSON string representation of the object
print(HubSpotConnectRequest.to_json())

# convert the object into a dict
hub_spot_connect_request_dict = hub_spot_connect_request_instance.to_dict()
# create an instance of HubSpotConnectRequest from a dict
hub_spot_connect_request_from_dict = HubSpotConnectRequest.from_dict(hub_spot_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


