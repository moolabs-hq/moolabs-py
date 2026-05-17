# FeatureOverrideRequest

Feature-level price override.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | Feature key | 
**currency** | **str** | Currency code | [optional] [default to 'USD']
**override_price_micros** | **int** | Override price in micros | [optional] 
**override_discount_bps** | **int** | Override discount in basis points | [optional] 

## Example

```python
from moolabs.models.feature_override_request import FeatureOverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureOverrideRequest from a JSON string
feature_override_request_instance = FeatureOverrideRequest.from_json(json)
# print the JSON string representation of the object
print(FeatureOverrideRequest.to_json())

# convert the object into a dict
feature_override_request_dict = feature_override_request_instance.to_dict()
# create an instance of FeatureOverrideRequest from a dict
feature_override_request_from_dict = FeatureOverrideRequest.from_dict(feature_override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


