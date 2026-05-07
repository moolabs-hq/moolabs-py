# Addon

Add-on allows extending subscriptions with compatible plans with additional ratecards.

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
**key** | **str** | A semi-unique identifier for the resource. | 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**version** | **int** | Version of the add-on. Incremented when the add-on is updated. | [readonly] [default to 1]
**instance_type** | [**AddonInstanceType**](AddonInstanceType.md) | The instanceType of the add-ons. Can be \&quot;single\&quot; or \&quot;multiple\&quot;. | 
**currency** | **str** | The currency code of the add-on. | 
**effective_from** | **datetime** | The date and time when the add-on becomes effective. When not specified, the add-on is a draft. | [optional] [readonly] 
**effective_to** | **datetime** | The date and time when the add-on is no longer effective. When not specified, the add-on is effective indefinitely. | [optional] [readonly] 
**status** | [**AddonStatus**](AddonStatus.md) | The status of the add-on. Computed based on the effective start and end dates: - draft &#x3D; no effectiveFrom - active &#x3D; effectiveFrom &lt;&#x3D; now &lt; effectiveTo - archived  &#x3D; effectiveTo &lt;&#x3D; now | [readonly] 
**rate_cards** | [**List[RateCard]**](RateCard.md) | The rate cards of the add-on. | 
**validation_errors** | [**List[MeterValidationError]**](MeterValidationError.md) | List of validation errors. | 

## Example

```python
from moolabs.models.addon import Addon

# TODO update the JSON string below
json = "{}"
# create an instance of Addon from a JSON string
addon_instance = Addon.from_json(json)
# print the JSON string representation of the object
print(Addon.to_json())

# convert the object into a dict
addon_dict = addon_instance.to_dict()
# create an instance of Addon from a dict
addon_from_dict = Addon.from_dict(addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


