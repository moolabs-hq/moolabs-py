# CreateFxRateRequest

Request to create an FX rate version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**credits_per_usd_micros** | **int** | Credits per USD in micros | 
**effective_at** | **datetime** | Effective timestamp for this rate | 
**rate_version** | **str** | Rate version identifier (auto-generated if not provided) | [optional] 
**usd_micros** | **int** | USD amount in micros (default 1 USD) | [optional] [default to 1000000]
**created_by** | **str** | Email or identifier of the user creating this rate | [optional] 

## Example

```python
from moolabs.models.create_fx_rate_request import CreateFxRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFxRateRequest from a JSON string
create_fx_rate_request_instance = CreateFxRateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFxRateRequest.to_json())

# convert the object into a dict
create_fx_rate_request_dict = create_fx_rate_request_instance.to_dict()
# create an instance of CreateFxRateRequest from a dict
create_fx_rate_request_from_dict = CreateFxRateRequest.from_dict(create_fx_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


