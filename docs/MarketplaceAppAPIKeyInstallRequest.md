# MarketplaceAppAPIKeyInstallRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the application to install.  If name is not provided defaults to the marketplace listing&#39;s name. | [optional] 
**create_billing_profile** | **bool** | If true, a billing profile will be created for the app. The Stripe app will be also set as the default billing profile if the current default is a Sandbox app. | [optional] [default to True]
**api_key** | **str** | The API key for the provider. For example, the Stripe API key. | 

## Example

```python
from moolabs.models.marketplace_app_api_key_install_request import MarketplaceAppAPIKeyInstallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceAppAPIKeyInstallRequest from a JSON string
marketplace_app_api_key_install_request_instance = MarketplaceAppAPIKeyInstallRequest.from_json(json)
# print the JSON string representation of the object
print(MarketplaceAppAPIKeyInstallRequest.to_json())

# convert the object into a dict
marketplace_app_api_key_install_request_dict = marketplace_app_api_key_install_request_instance.to_dict()
# create an instance of MarketplaceAppAPIKeyInstallRequest from a dict
marketplace_app_api_key_install_request_from_dict = MarketplaceAppAPIKeyInstallRequest.from_dict(marketplace_app_api_key_install_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


