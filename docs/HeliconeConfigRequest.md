# HeliconeConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | 
**webhook_secret** | **str** |  | [optional] 
**poll_interval_minutes** | **int** |  | [optional] [default to 5]

## Example

```python
from moolabs.models.helicone_config_request import HeliconeConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeliconeConfigRequest from a JSON string
helicone_config_request_instance = HeliconeConfigRequest.from_json(json)
# print the JSON string representation of the object
print(HeliconeConfigRequest.to_json())

# convert the object into a dict
helicone_config_request_dict = helicone_config_request_instance.to_dict()
# create an instance of HeliconeConfigRequest from a dict
helicone_config_request_from_dict = HeliconeConfigRequest.from_dict(helicone_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


