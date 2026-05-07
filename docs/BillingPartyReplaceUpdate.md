# BillingPartyReplaceUpdate

Resource update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | An optional unique key of the party (if available) | [optional] 
**name** | **str** | Legal name or representation of the organization. | [optional] 
**tax_id** | [**BillingPartyTaxIdentity**](BillingPartyTaxIdentity.md) | The entity&#39;s legal ID code used for tax purposes. They may have other numbers, but we&#39;re only interested in those valid for tax purposes. | [optional] 
**addresses** | [**List[Address]**](Address.md) | Regular post addresses for where information should be sent if needed. | [optional] 

## Example

```python
from moolabs.models.billing_party_replace_update import BillingPartyReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BillingPartyReplaceUpdate from a JSON string
billing_party_replace_update_instance = BillingPartyReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(BillingPartyReplaceUpdate.to_json())

# convert the object into a dict
billing_party_replace_update_dict = billing_party_replace_update_instance.to_dict()
# create an instance of BillingPartyReplaceUpdate from a dict
billing_party_replace_update_from_dict = BillingPartyReplaceUpdate.from_dict(billing_party_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


