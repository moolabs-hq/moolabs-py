# CreditConfigPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**global_pool_enabled** | **bool** |  | 
**feature_pools_enabled** | **bool** |  | 
**initial_amount** | [**Initialamount**](Initialamount.md) |  | 
**recurring_amount** | [**Recurringamount**](Recurringamount.md) |  | 
**cadence** | **str** |  | 
**expires_in_days** | **int** |  | 
**rollover_enabled** | **bool** |  | 
**rollover_percent** | [**Rolloverpercent**](Rolloverpercent.md) |  | [optional] 
**rollover_cap_amount** | [**Rollovercapamount**](Rollovercapamount.md) |  | [optional] 
**rollover_expires_after_days** | **int** |  | [optional] 
**rollover_priority_delta** | **int** |  | [optional] 
**feature_pools** | [**List[FeaturePoolPayload]**](FeaturePoolPayload.md) |  | [optional] 

## Example

```python
from moolabs.models.credit_config_payload import CreditConfigPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreditConfigPayload from a JSON string
credit_config_payload_instance = CreditConfigPayload.from_json(json)
# print the JSON string representation of the object
print(CreditConfigPayload.to_json())

# convert the object into a dict
credit_config_payload_dict = credit_config_payload_instance.to_dict()
# create an instance of CreditConfigPayload from a dict
credit_config_payload_from_dict = CreditConfigPayload.from_dict(credit_config_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


