# BillingProfile

BillingProfile represents a billing profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**supplier** | [**BillingParty**](BillingParty.md) | The name and contact information for the supplier this billing profile represents | 
**workflow** | [**BillingWorkflow**](BillingWorkflow.md) | The billing workflow settings for this profile | [readonly] 
**apps** | [**BillingProfileAppsOrReference**](BillingProfileAppsOrReference.md) | The applications used by this billing profile.  Expand settings govern if this includes the whole app object or just the ID references. | [readonly] 
**default** | **bool** | Is this the default profile? | 

## Example

```python
from moolabs.models.billing_profile import BillingProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfile from a JSON string
billing_profile_instance = BillingProfile.from_json(json)
# print the JSON string representation of the object
print(BillingProfile.to_json())

# convert the object into a dict
billing_profile_dict = billing_profile_instance.to_dict()
# create an instance of BillingProfile from a dict
billing_profile_from_dict = BillingProfile.from_dict(billing_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


