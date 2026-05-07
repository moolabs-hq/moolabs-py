# AddonCreate

Resource create operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**key** | **str** | A semi-unique identifier for the resource. | 
**instance_type** | [**AddonInstanceType**](AddonInstanceType.md) | The instanceType of the add-ons. Can be \&quot;single\&quot; or \&quot;multiple\&quot;. | 
**currency** | **str** | The currency code of the add-on. | 
**rate_cards** | [**List[RateCard]**](RateCard.md) | The rate cards of the add-on. | 

## Example

```python
from moolabs.models.addon_create import AddonCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AddonCreate from a JSON string
addon_create_instance = AddonCreate.from_json(json)
# print the JSON string representation of the object
print(AddonCreate.to_json())

# convert the object into a dict
addon_create_dict = addon_create_instance.to_dict()
# create an instance of AddonCreate from a dict
addon_create_from_dict = AddonCreate.from_dict(addon_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


