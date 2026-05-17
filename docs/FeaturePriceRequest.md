# FeaturePriceRequest

Feature-level pricing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | Feature key | 
**currency** | **str** | Currency code | [optional] [default to 'USD']
**list_price_micros** | **int** | List price in micros | 
**net_price_micros** | **int** | Net price in micros (after discounts) | 

## Example

```python
from moolabs.models.feature_price_request import FeaturePriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePriceRequest from a JSON string
feature_price_request_instance = FeaturePriceRequest.from_json(json)
# print the JSON string representation of the object
print(FeaturePriceRequest.to_json())

# convert the object into a dict
feature_price_request_dict = feature_price_request_instance.to_dict()
# create an instance of FeaturePriceRequest from a dict
feature_price_request_from_dict = FeaturePriceRequest.from_dict(feature_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


