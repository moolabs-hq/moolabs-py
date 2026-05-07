# BillingProfileCreate

BillingProfileCreate represents the input for creating a billing profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**supplier** | [**BillingParty**](BillingParty.md) | The name and contact information for the supplier this billing profile represents | 
**default** | **bool** | Is this the default profile? | 
**workflow** | [**BillingWorkflowCreate**](BillingWorkflowCreate.md) | The billing workflow settings for this profile. | 
**apps** | [**BillingProfileAppsCreate**](BillingProfileAppsCreate.md) | The apps used by this billing profile. | 

## Example

```python
from moolabs.models.billing_profile_create import BillingProfileCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCreate from a JSON string
billing_profile_create_instance = BillingProfileCreate.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCreate.to_json())

# convert the object into a dict
billing_profile_create_dict = billing_profile_create_instance.to_dict()
# create an instance of BillingProfileCreate from a dict
billing_profile_create_from_dict = BillingProfileCreate.from_dict(billing_profile_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


