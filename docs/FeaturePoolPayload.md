# FeaturePoolPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**enabled** | **bool** |  | 
**initial_amount** | [**Initialamount**](Initialamount.md) |  | 
**recurring_amount** | [**Recurringamount**](Recurringamount.md) |  | 
**cadence** | **str** |  | [optional] 
**expires_in_days** | **int** |  | 
**rollover_enabled** | **bool** |  | 

## Example

```python
from moolabs.models.feature_pool_payload import FeaturePoolPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePoolPayload from a JSON string
feature_pool_payload_instance = FeaturePoolPayload.from_json(json)
# print the JSON string representation of the object
print(FeaturePoolPayload.to_json())

# convert the object into a dict
feature_pool_payload_dict = feature_pool_payload_instance.to_dict()
# create an instance of FeaturePoolPayload from a dict
feature_pool_payload_from_dict = FeaturePoolPayload.from_dict(feature_pool_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


