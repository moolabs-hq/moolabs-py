# XeroConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_direction** | **str** |  | 
**sync_frequency** | **str** |  | 
**owner** | **str** |  | [optional] 

## Example

```python
from moolabs.models.xero_connect_request import XeroConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of XeroConnectRequest from a JSON string
xero_connect_request_instance = XeroConnectRequest.from_json(json)
# print the JSON string representation of the object
print(XeroConnectRequest.to_json())

# convert the object into a dict
xero_connect_request_dict = xero_connect_request_instance.to_dict()
# create an instance of XeroConnectRequest from a dict
xero_connect_request_from_dict = XeroConnectRequest.from_dict(xero_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


