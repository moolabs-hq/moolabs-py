# BillingProfileReplaceUpdateWithWorkflow

BillingProfileReplaceUpdate represents the input for updating a billing profile  The apps field cannot be updated directly, if an app change is desired a new profile should be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**supplier** | [**BillingParty**](BillingParty.md) | The name and contact information for the supplier this billing profile represents | 
**default** | **bool** | Is this the default profile? | 
**workflow** | [**BillingWorkflow**](BillingWorkflow.md) | The billing workflow settings for this profile. | 

## Example

```python
from moolabs.models.billing_profile_replace_update_with_workflow import BillingProfileReplaceUpdateWithWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileReplaceUpdateWithWorkflow from a JSON string
billing_profile_replace_update_with_workflow_instance = BillingProfileReplaceUpdateWithWorkflow.from_json(json)
# print the JSON string representation of the object
print(BillingProfileReplaceUpdateWithWorkflow.to_json())

# convert the object into a dict
billing_profile_replace_update_with_workflow_dict = billing_profile_replace_update_with_workflow_instance.to_dict()
# create an instance of BillingProfileReplaceUpdateWithWorkflow from a dict
billing_profile_replace_update_with_workflow_from_dict = BillingProfileReplaceUpdateWithWorkflow.from_dict(billing_profile_replace_update_with_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


