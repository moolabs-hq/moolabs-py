# FeatureMarginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FeatureMarginItem]**](FeatureMarginItem.md) |  | 
**reconciliation_basis** | [**ReconciliationBasis**](ReconciliationBasis.md) |  | 

## Example

```python
from moolabs.models.feature_margin_response import FeatureMarginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMarginResponse from a JSON string
feature_margin_response_instance = FeatureMarginResponse.from_json(json)
# print the JSON string representation of the object
print(FeatureMarginResponse.to_json())

# convert the object into a dict
feature_margin_response_dict = feature_margin_response_instance.to_dict()
# create an instance of FeatureMarginResponse from a dict
feature_margin_response_from_dict = FeatureMarginResponse.from_dict(feature_margin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


