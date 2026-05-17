# CashAppConfigUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuzzy_match_tolerance_pct** | **float** | Fuzzy match tolerance as decimal (e.g. 0.01 &#x3D; ±1%) | [optional] 
**exact_match_auto_apply** | **bool** |  | [optional] 
**fuzzy_match_threshold** | **float** | Confidence threshold for fuzzy name matching | [optional] 
**multi_invoice_match_enabled** | **bool** |  | [optional] 
**max_auto_allocation_amount_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.cash_app_config_update_request import CashAppConfigUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashAppConfigUpdateRequest from a JSON string
cash_app_config_update_request_instance = CashAppConfigUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CashAppConfigUpdateRequest.to_json())

# convert the object into a dict
cash_app_config_update_request_dict = cash_app_config_update_request_instance.to_dict()
# create an instance of CashAppConfigUpdateRequest from a dict
cash_app_config_update_request_from_dict = CashAppConfigUpdateRequest.from_dict(cash_app_config_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


