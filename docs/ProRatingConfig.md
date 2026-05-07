# ProRatingConfig

Configuration for pro-rating behavior.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether pro-rating is enabled for this plan. | [default to True]
**mode** | [**ProRatingMode**](ProRatingMode.md) | How to handle pro-rating for billing period changes. | 

## Example

```python
from moolabs.models.pro_rating_config import ProRatingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProRatingConfig from a JSON string
pro_rating_config_instance = ProRatingConfig.from_json(json)
# print the JSON string representation of the object
print(ProRatingConfig.to_json())

# convert the object into a dict
pro_rating_config_dict = pro_rating_config_instance.to_dict()
# create an instance of ProRatingConfig from a dict
pro_rating_config_from_dict = ProRatingConfig.from_dict(pro_rating_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


