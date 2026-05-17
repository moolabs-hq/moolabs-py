# FxRateResponse

Response from creating an FX rate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**pool_id** | **str** |  | 
**credits_per_usd_micros** | **int** |  | 
**usd_micros** | **int** |  | 
**effective_at** | **datetime** |  | 
**rate_version** | **str** |  | 
**recorded_at** | **datetime** |  | 
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.fx_rate_response import FxRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FxRateResponse from a JSON string
fx_rate_response_instance = FxRateResponse.from_json(json)
# print the JSON string representation of the object
print(FxRateResponse.to_json())

# convert the object into a dict
fx_rate_response_dict = fx_rate_response_instance.to_dict()
# create an instance of FxRateResponse from a dict
fx_rate_response_from_dict = FxRateResponse.from_dict(fx_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


