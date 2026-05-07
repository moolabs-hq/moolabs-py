# GetFxRateRequest

Request to get FX rate at a timestamp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**as_of** | **datetime** | Timestamp to get rate for | 

## Example

```python
from moolabs.models.get_fx_rate_request import GetFxRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetFxRateRequest from a JSON string
get_fx_rate_request_instance = GetFxRateRequest.from_json(json)
# print the JSON string representation of the object
print(GetFxRateRequest.to_json())

# convert the object into a dict
get_fx_rate_request_dict = get_fx_rate_request_instance.to_dict()
# create an instance of GetFxRateRequest from a dict
get_fx_rate_request_from_dict = GetFxRateRequest.from_dict(get_fx_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


