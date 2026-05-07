# PackagePrice

Package price.  The item is sold in packages. Each package contains quantityPerPackage items, the price of the package is set in amount.  The total price of the usage will be enough packages that can accomodate all the usage.  Examples (given a package size of 20, and an amount of $10): - if the quantity is 98, the price will be 5*$10=$50. - if the quantity is zero, the price will be 0*$10=$0, as even the first package is not purchased. - if the quantity is 20, the price will be 1*$10=$10, as the usage fits into the first package. - if the quantity is 20.1, the price will be 2*$10=$20, as the additional 0.1 usage (compared to the previous example) requires a new package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The price of one package. | 
**quantity_per_package** | **str** | The quantity per package. | 

## Example

```python
from moolabs.models.package_price import PackagePrice

# TODO update the JSON string below
json = "{}"
# create an instance of PackagePrice from a JSON string
package_price_instance = PackagePrice.from_json(json)
# print the JSON string representation of the object
print(PackagePrice.to_json())

# convert the object into a dict
package_price_dict = package_price_instance.to_dict()
# create an instance of PackagePrice from a dict
package_price_from_dict = PackagePrice.from_dict(package_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


