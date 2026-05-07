# MarketplaceListing

A marketplace listing. Represent an available app in the app marketplace that can be installed to the organization.  Marketplace apps only exist in config so they don't extend the Resource model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppType**](AppType.md) | The app&#39;s type | 
**name** | **str** | The app&#39;s name. | 
**description** | **str** | The app&#39;s description. | 
**capabilities** | [**List[AppCapability]**](AppCapability.md) | The app&#39;s capabilities. | 
**install_methods** | [**List[InstallMethod]**](InstallMethod.md) | Install methods.  List of methods to install the app. | 

## Example

```python
from moolabs.models.marketplace_listing import MarketplaceListing

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceListing from a JSON string
marketplace_listing_instance = MarketplaceListing.from_json(json)
# print the JSON string representation of the object
print(MarketplaceListing.to_json())

# convert the object into a dict
marketplace_listing_dict = marketplace_listing_instance.to_dict()
# create an instance of MarketplaceListing from a dict
marketplace_listing_from_dict = MarketplaceListing.from_dict(marketplace_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


