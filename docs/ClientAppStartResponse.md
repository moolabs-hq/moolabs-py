# ClientAppStartResponse

Response from the client app (OpenMeter backend) to start the OAuth2 flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to start the OAuth2 authorization code grant flow. | 

## Example

```python
from moolabs.models.client_app_start_response import ClientAppStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAppStartResponse from a JSON string
client_app_start_response_instance = ClientAppStartResponse.from_json(json)
# print the JSON string representation of the object
print(ClientAppStartResponse.to_json())

# convert the object into a dict
client_app_start_response_dict = client_app_start_response_instance.to_dict()
# create an instance of ClientAppStartResponse from a dict
client_app_start_response_from_dict = ClientAppStartResponse.from_dict(client_app_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


