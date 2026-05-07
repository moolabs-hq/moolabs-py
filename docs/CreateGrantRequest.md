# CreateGrantRequest

Request to create a credit grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Credit pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**amount_micros** | **int** | Grant amount in micros | 
**priority** | **int** | Grant priority (lower numbers &#x3D; higher priority, priority 0 is used before priority 100) | [optional] [default to 100]
**valid_from** | **datetime** | Grant valid from timestamp | 
**expires_at** | **datetime** |  | [optional] 
**source_type** | [**GrantSourceType**](GrantSourceType.md) | Grant source type | 
**source_id** | **str** | Source identifier (idempotency key) | 
**subscription_id** | **str** |  | [optional] 
**scope_type** | [**ScopeType**](ScopeType.md) | Grant scope type | [optional] 
**scope_values** | **List[str]** |  | [optional] 
**rollover_mode** | [**RolloverMode**](RolloverMode.md) | Rollover mode | [optional] 
**rollover_percent** | **int** |  | [optional] 
**rollover_cap_micros** | **int** |  | [optional] 
**rollover_expires_after_days** | **int** |  | [optional] 
**rollover_priority_delta** | **int** |  | [optional] 
**paid_amount_usd_micros** | **int** |  | [optional] 
**locked_fx_rate_version** | **str** |  | [optional] 
**locked_credits_per_usd_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.create_grant_request import CreateGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGrantRequest from a JSON string
create_grant_request_instance = CreateGrantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGrantRequest.to_json())

# convert the object into a dict
create_grant_request_dict = create_grant_request_instance.to_dict()
# create an instance of CreateGrantRequest from a dict
create_grant_request_from_dict = CreateGrantRequest.from_dict(create_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


