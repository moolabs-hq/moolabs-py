# AddonReplaceUpdate

Resource update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**instance_type** | [**AddonInstanceType**](AddonInstanceType.md) | The instanceType of the add-ons. Can be \&quot;single\&quot; or \&quot;multiple\&quot;. | 
**rate_cards** | [**List[RateCard]**](RateCard.md) | The rate cards of the add-on. | 

## Example

```python
from moolabs.models.addon_replace_update import AddonReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AddonReplaceUpdate from a JSON string
addon_replace_update_instance = AddonReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(AddonReplaceUpdate.to_json())

# convert the object into a dict
addon_replace_update_dict = addon_replace_update_instance.to_dict()
# create an instance of AddonReplaceUpdate from a dict
addon_replace_update_from_dict = AddonReplaceUpdate.from_dict(addon_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


