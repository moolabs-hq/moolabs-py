# BillingParty

Party represents a person or business entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the party (if available) | [optional] [readonly] 
**key** | **str** | An optional unique key of the party (if available) | [optional] 
**name** | **str** | Legal name or representation of the organization. | [optional] 
**tax_id** | [**BillingPartyTaxIdentity**](BillingPartyTaxIdentity.md) | The entity&#39;s legal ID code used for tax purposes. They may have other numbers, but we&#39;re only interested in those valid for tax purposes. | [optional] 
**addresses** | [**List[Address]**](Address.md) | Regular post addresses for where information should be sent if needed. | [optional] 

## Example

```python
from moolabs.models.billing_party import BillingParty

# TODO update the JSON string below
json = "{}"
# create an instance of BillingParty from a JSON string
billing_party_instance = BillingParty.from_json(json)
# print the JSON string representation of the object
print(BillingParty.to_json())

# convert the object into a dict
billing_party_dict = billing_party_instance.to_dict()
# create an instance of BillingParty from a dict
billing_party_from_dict = BillingParty.from_dict(billing_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


