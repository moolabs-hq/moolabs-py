# PackagePriceWithCommitments

Package price with spend commitments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The price of one package. | 
**quantity_per_package** | **str** | The quantity per package. | 
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 

## Example

```python
from moolabs.models.package_price_with_commitments import PackagePriceWithCommitments

# TODO update the JSON string below
json = "{}"
# create an instance of PackagePriceWithCommitments from a JSON string
package_price_with_commitments_instance = PackagePriceWithCommitments.from_json(json)
# print the JSON string representation of the object
print(PackagePriceWithCommitments.to_json())

# convert the object into a dict
package_price_with_commitments_dict = package_price_with_commitments_instance.to_dict()
# create an instance of PackagePriceWithCommitments from a dict
package_price_with_commitments_from_dict = PackagePriceWithCommitments.from_dict(package_price_with_commitments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


