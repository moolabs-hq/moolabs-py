# FeatureFlagUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 

## Example

```python
from moolabs.models.feature_flag_update import FeatureFlagUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagUpdate from a JSON string
feature_flag_update_instance = FeatureFlagUpdate.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagUpdate.to_json())

# convert the object into a dict
feature_flag_update_dict = feature_flag_update_instance.to_dict()
# create an instance of FeatureFlagUpdate from a dict
feature_flag_update_from_dict = FeatureFlagUpdate.from_dict(feature_flag_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


