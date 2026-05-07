# FeatureCreateInputs

Represents a feature that can be enabled or disabled for a plan. Used both for product catalog and entitlements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A key is a unique string that is used to identify a resource. | 
**name** | **str** |  | 
**metadata** | **Dict[str, str]** | Set of key-value pairs. Metadata can be used to store additional information about a resource. | [optional] 
**meter_slug** | **str** | A key is a unique string that is used to identify a resource. | [optional] 
**meter_group_by_filters** | **Dict[str, str]** | Optional meter group by filters. Useful if the meter scope is broader than what feature tracks. Example scenario would be a meter tracking all token use with groupBy fields for the model, then the feature could filter for model&#x3D;gpt-4. | [optional] 
**advanced_meter_group_by_filters** | [**Dict[str, FilterString]**](FilterString.md) | Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. | [optional] 

## Example

```python
from moolabs.models.feature_create_inputs import FeatureCreateInputs

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureCreateInputs from a JSON string
feature_create_inputs_instance = FeatureCreateInputs.from_json(json)
# print the JSON string representation of the object
print(FeatureCreateInputs.to_json())

# convert the object into a dict
feature_create_inputs_dict = feature_create_inputs_instance.to_dict()
# create an instance of FeatureCreateInputs from a dict
feature_create_inputs_from_dict = FeatureCreateInputs.from_dict(feature_create_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


