# GrantResponse

Grant response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**pool_id** | **str** |  | 
**wallet_id** | **str** |  | 
**amount_micros** | **int** |  | 
**remaining_micros** | **int** |  | 
**priority** | **int** |  | 
**valid_from** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**source_type** | **str** |  | 
**source_id** | **str** |  | 
**subscription_id** | **str** |  | 
**scope_type** | [**ScopeType**](ScopeType.md) |  | 
**rollover_mode** | [**RolloverMode**](RolloverMode.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.grant_response import GrantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantResponse from a JSON string
grant_response_instance = GrantResponse.from_json(json)
# print the JSON string representation of the object
print(GrantResponse.to_json())

# convert the object into a dict
grant_response_dict = grant_response_instance.to_dict()
# create an instance of GrantResponse from a dict
grant_response_from_dict = GrantResponse.from_dict(grant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


