# GrantRenewalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**subscription_id** | **str** |  | 
**customer_id** | **str** |  | 
**plan_id** | **str** |  | 
**plan_version** | **int** |  | 
**billing_period_end** | **datetime** |  | 
**credit_config** | [**CreditConfigPayload**](CreditConfigPayload.md) |  | 
**commercial_overrides** | [**CommercialOverridesPayload**](CommercialOverridesPayload.md) |  | [optional] 
**entitlements** | [**List[EntitlementPayload]**](EntitlementPayload.md) |  | 
**subject_keys** | **List[str]** |  | 

## Example

```python
from moolabs.models.grant_renewal_request import GrantRenewalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantRenewalRequest from a JSON string
grant_renewal_request_instance = GrantRenewalRequest.from_json(json)
# print the JSON string representation of the object
print(GrantRenewalRequest.to_json())

# convert the object into a dict
grant_renewal_request_dict = grant_renewal_request_instance.to_dict()
# create an instance of GrantRenewalRequest from a dict
grant_renewal_request_from_dict = GrantRenewalRequest.from_dict(grant_renewal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


