# FeatureMeta

Limited representation of a feature resource which includes only its unique identifiers (id, key).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of a feature. | 
**key** | **str** | The key is an immutable unique identifier of the feature used throughout the API, for example when interacting with a subject&#39;s entitlements. | 

## Example

```python
from moolabs.models.feature_meta import FeatureMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMeta from a JSON string
feature_meta_instance = FeatureMeta.from_json(json)
# print the JSON string representation of the object
print(FeatureMeta.to_json())

# convert the object into a dict
feature_meta_dict = feature_meta_instance.to_dict()
# create an instance of FeatureMeta from a dict
feature_meta_from_dict = FeatureMeta.from_dict(feature_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


