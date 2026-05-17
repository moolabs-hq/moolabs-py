# TenantProvisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from moolabs.models.tenant_provision_request import TenantProvisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantProvisionRequest from a JSON string
tenant_provision_request_instance = TenantProvisionRequest.from_json(json)
# print the JSON string representation of the object
print(TenantProvisionRequest.to_json())

# convert the object into a dict
tenant_provision_request_dict = tenant_provision_request_instance.to_dict()
# create an instance of TenantProvisionRequest from a dict
tenant_provision_request_from_dict = TenantProvisionRequest.from_dict(tenant_provision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


