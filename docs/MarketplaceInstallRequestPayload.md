# MarketplaceInstallRequestPayload

Marketplace install request payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the application to install.  If name is not provided defaults to the marketplace listing&#39;s name. | [optional] 
**create_billing_profile** | **bool** | If true, a billing profile will be created for the app. The Stripe app will be also set as the default billing profile if the current default is a Sandbox app. | [optional] [default to True]

## Example

```python
from moolabs.models.marketplace_install_request_payload import MarketplaceInstallRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceInstallRequestPayload from a JSON string
marketplace_install_request_payload_instance = MarketplaceInstallRequestPayload.from_json(json)
# print the JSON string representation of the object
print(MarketplaceInstallRequestPayload.to_json())

# convert the object into a dict
marketplace_install_request_payload_dict = marketplace_install_request_payload_instance.to_dict()
# create an instance of MarketplaceInstallRequestPayload from a dict
marketplace_install_request_payload_from_dict = MarketplaceInstallRequestPayload.from_dict(marketplace_install_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


