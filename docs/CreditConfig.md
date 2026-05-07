# CreditConfig

Plan-level defaults for subscription credit allowances (persisted as first-class column).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**global_pool_enabled** | **bool** |  | 
**feature_pools_enabled** | **bool** |  | 
**initial_amount** | **float** |  | 
**recurring_amount** | **float** |  | 
**cadence** | **str** | Billing cadence key for credit allowance (e.g. MONTHLY), aligned with plan usage. | 
**expires_in_days** | **int** |  | 
**rollover_enabled** | **bool** |  | 
**rollover_percent** | **float** |  | [optional] 
**rollover_cap_amount** | **float** |  | [optional] 
**rollover_expires_after_days** | **int** |  | [optional] 
**rollover_priority_delta** | **int** |  | [optional] 
**feature_pools** | [**List[FeaturePool]**](FeaturePool.md) |  | [optional] 

## Example

```python
from moolabs.models.credit_config import CreditConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreditConfig from a JSON string
credit_config_instance = CreditConfig.from_json(json)
# print the JSON string representation of the object
print(CreditConfig.to_json())

# convert the object into a dict
credit_config_dict = credit_config_instance.to_dict()
# create an instance of CreditConfig from a dict
credit_config_from_dict = CreditConfig.from_dict(credit_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


