# FeaturePool

Per-feature credit pool settings within a plan credit configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | Feature key this pool applies to. | 
**enabled** | **bool** |  | 
**initial_amount** | **float** |  | 
**recurring_amount** | **float** |  | 
**cadence** | **str** | Optional cadence override for this pool (e.g. same as plan billing when empty). | [optional] 
**expires_in_days** | **int** |  | 
**rollover_enabled** | **bool** |  | 

## Example

```python
from moolabs.models.feature_pool import FeaturePool

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePool from a JSON string
feature_pool_instance = FeaturePool.from_json(json)
# print the JSON string representation of the object
print(FeaturePool.to_json())

# convert the object into a dict
feature_pool_dict = feature_pool_instance.to_dict()
# create an instance of FeaturePool from a dict
feature_pool_from_dict = FeaturePool.from_dict(feature_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


