# CreateCheckoutSessionTaxIdCollection

Create Stripe checkout session tax ID collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable tax ID collection during checkout. Defaults to false. | 
**required** | [**CreateCheckoutSessionTaxIdCollectionRequired**](CreateCheckoutSessionTaxIdCollectionRequired.md) | Describes whether a tax ID is required during checkout. Defaults to never. | [optional] 

## Example

```python
from moolabs.models.create_checkout_session_tax_id_collection import CreateCheckoutSessionTaxIdCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutSessionTaxIdCollection from a JSON string
create_checkout_session_tax_id_collection_instance = CreateCheckoutSessionTaxIdCollection.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutSessionTaxIdCollection.to_json())

# convert the object into a dict
create_checkout_session_tax_id_collection_dict = create_checkout_session_tax_id_collection_instance.to_dict()
# create an instance of CreateCheckoutSessionTaxIdCollection from a dict
create_checkout_session_tax_id_collection_from_dict = CreateCheckoutSessionTaxIdCollection.from_dict(create_checkout_session_tax_id_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


