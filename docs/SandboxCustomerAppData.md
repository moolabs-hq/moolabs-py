# SandboxCustomerAppData

Sandbox Customer App Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**SandboxApp**](SandboxApp.md) | The installed sandbox app this data belongs to. | [optional] [readonly] 
**id** | **str** | The app ID. If not provided, it will use the global default for the app type. | [optional] 
**type** | **str** | The app name. | 

## Example

```python
from moolabs.models.sandbox_customer_app_data import SandboxCustomerAppData

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxCustomerAppData from a JSON string
sandbox_customer_app_data_instance = SandboxCustomerAppData.from_json(json)
# print the JSON string representation of the object
print(SandboxCustomerAppData.to_json())

# convert the object into a dict
sandbox_customer_app_data_dict = sandbox_customer_app_data_instance.to_dict()
# create an instance of SandboxCustomerAppData from a dict
sandbox_customer_app_data_from_dict = SandboxCustomerAppData.from_dict(sandbox_customer_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


