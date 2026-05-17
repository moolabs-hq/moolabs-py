# NetSuiteConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**sync_direction** | **str** |  | 
**sync_frequency** | **str** |  | 
**owner** | **str** |  | [optional] 
**invoice_pdf_render_script_id** | **str** |  | [optional] 
**invoice_pdf_render_deploy_id** | **str** |  | [optional] 
**invoice_pdf_form_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.net_suite_connect_request import NetSuiteConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetSuiteConnectRequest from a JSON string
net_suite_connect_request_instance = NetSuiteConnectRequest.from_json(json)
# print the JSON string representation of the object
print(NetSuiteConnectRequest.to_json())

# convert the object into a dict
net_suite_connect_request_dict = net_suite_connect_request_instance.to_dict()
# create an instance of NetSuiteConnectRequest from a dict
net_suite_connect_request_from_dict = NetSuiteConnectRequest.from_dict(net_suite_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


