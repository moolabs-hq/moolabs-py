# ProviderConfirmationRepairRequest

POST resolve-provider-confirmation — operator repair payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **str** |  | 
**note** | **str** |  | [optional] 
**external_message_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.provider_confirmation_repair_request import ProviderConfirmationRepairRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderConfirmationRepairRequest from a JSON string
provider_confirmation_repair_request_instance = ProviderConfirmationRepairRequest.from_json(json)
# print the JSON string representation of the object
print(ProviderConfirmationRepairRequest.to_json())

# convert the object into a dict
provider_confirmation_repair_request_dict = provider_confirmation_repair_request_instance.to_dict()
# create an instance of ProviderConfirmationRepairRequest from a dict
provider_confirmation_repair_request_from_dict = ProviderConfirmationRepairRequest.from_dict(provider_confirmation_repair_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


