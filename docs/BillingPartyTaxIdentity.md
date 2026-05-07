# BillingPartyTaxIdentity

Identity stores the details required to identify an entity for tax purposes in a specific country.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Normalized tax code shown on the original identity document. | [optional] 

## Example

```python
from moolabs.models.billing_party_tax_identity import BillingPartyTaxIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPartyTaxIdentity from a JSON string
billing_party_tax_identity_instance = BillingPartyTaxIdentity.from_json(json)
# print the JSON string representation of the object
print(BillingPartyTaxIdentity.to_json())

# convert the object into a dict
billing_party_tax_identity_dict = billing_party_tax_identity_instance.to_dict()
# create an instance of BillingPartyTaxIdentity from a dict
billing_party_tax_identity_from_dict = BillingPartyTaxIdentity.from_dict(billing_party_tax_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


