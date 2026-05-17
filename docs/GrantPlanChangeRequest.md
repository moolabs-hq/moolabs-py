# GrantPlanChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**subscription_id** | **str** |  | 
**customer_id** | **str** |  | 
**old_plan_id** | **str** |  | 
**old_plan_version** | **int** |  | 
**new_plan_id** | **str** |  | 
**new_plan_version** | **int** |  | 
**effective_at** | **datetime** |  | 
**new_credit_config** | [**CreditConfigPayload**](CreditConfigPayload.md) |  | 
**commercial_overrides** | [**CommercialOverridesPayload**](CommercialOverridesPayload.md) |  | [optional] 
**entitlements** | [**List[EntitlementPayload]**](EntitlementPayload.md) |  | 
**subject_keys** | **List[str]** |  | 

## Example

```python
from moolabs.models.grant_plan_change_request import GrantPlanChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantPlanChangeRequest from a JSON string
grant_plan_change_request_instance = GrantPlanChangeRequest.from_json(json)
# print the JSON string representation of the object
print(GrantPlanChangeRequest.to_json())

# convert the object into a dict
grant_plan_change_request_dict = grant_plan_change_request_instance.to_dict()
# create an instance of GrantPlanChangeRequest from a dict
grant_plan_change_request_from_dict = GrantPlanChangeRequest.from_dict(grant_plan_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


