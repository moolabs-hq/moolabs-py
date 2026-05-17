# GrantActivationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**subscription_id** | **str** |  | 
**customer_id** | **str** |  | 
**plan_id** | **str** |  | 
**plan_version** | **int** |  | 
**effective_at** | **datetime** |  | 
**credit_config** | [**CreditConfigPayload**](CreditConfigPayload.md) |  | 
**commercial_overrides** | [**CommercialOverridesPayload**](CommercialOverridesPayload.md) |  | [optional] 
**entitlements** | [**List[EntitlementPayload]**](EntitlementPayload.md) |  | 
**subject_keys** | **List[str]** |  | 

## Example

```python
from moolabs.models.grant_activation_request import GrantActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantActivationRequest from a JSON string
grant_activation_request_instance = GrantActivationRequest.from_json(json)
# print the JSON string representation of the object
print(GrantActivationRequest.to_json())

# convert the object into a dict
grant_activation_request_dict = grant_activation_request_instance.to_dict()
# create an instance of GrantActivationRequest from a dict
grant_activation_request_from_dict = GrantActivationRequest.from_dict(grant_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


