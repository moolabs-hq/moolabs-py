# MarketplaceInstallResponse

Marketplace install response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**App**](App.md) |  | 
**default_for_capability_types** | [**List[AppCapabilityType]**](AppCapabilityType.md) | Default for capabilities | 

## Example

```python
from moolabs.models.marketplace_install_response import MarketplaceInstallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceInstallResponse from a JSON string
marketplace_install_response_instance = MarketplaceInstallResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceInstallResponse.to_json())

# convert the object into a dict
marketplace_install_response_dict = marketplace_install_response_instance.to_dict()
# create an instance of MarketplaceInstallResponse from a dict
marketplace_install_response_from_dict = MarketplaceInstallResponse.from_dict(marketplace_install_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


