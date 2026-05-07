# EntitlementGrantV2

The grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**amount** | **float** | The amount to grant. Should be a positive number. | 
**priority** | **int** | The priority of the grant. Grants with higher priority are applied first. Priority is a positive decimal numbers. With lower numbers indicating higher importance. For example, a priority of 1 is more urgent than a priority of 2. When there are several grants available for the same subject, the system selects the grant with the highest priority. In cases where grants share the same priority level, the grant closest to its expiration will be used first. In the case of two grants have identical priorities and expiration dates, the system will use the grant that was created first. | [optional] 
**effective_at** | **datetime** | Effective date for grants and anchor for recurring grants. Provided value will be ceiled to metering windowSize (minute). | 
**min_rollover_amount** | **float** | Grants are rolled over at reset, after which they can have a different balance compared to what they had before the reset. Balance after the reset is calculated as: Balance_After_Reset &#x3D; MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount)) | [optional] [default to 0]
**metadata** | **Dict[str, str]** | The grant metadata. | [optional] 
**max_rollover_amount** | **float** | Grants are rolled over at reset, after which they can have a different balance compared to what they had before the reset. The default value equals grant amount. Balance after the reset is calculated as: Balance_After_Reset &#x3D; MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount)) | [optional] 
**expiration** | [**ExpirationPeriod**](ExpirationPeriod.md) | The grant expiration definition. If no expiration is provided, the grant can be active indefinitely. | [optional] 
**annotations** | **Dict[str, object]** | Grant annotations | [optional] 
**id** | **str** | Readonly unique ULID identifier. | [readonly] 
**entitlement_id** | **str** | The unique entitlement ULID that the grant is associated with. | [readonly] 
**next_recurrence** | **datetime** | The next time the grant will recurr. | [optional] 
**expires_at** | **datetime** | The time the grant expires. | [optional] [readonly] 
**voided_at** | **datetime** | The time the grant was voided. | [optional] 
**recurrence** | [**RecurringPeriod**](RecurringPeriod.md) | The recurrence period of the grant. | [optional] 

## Example

```python
from moolabs.models.entitlement_grant_v2 import EntitlementGrantV2

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementGrantV2 from a JSON string
entitlement_grant_v2_instance = EntitlementGrantV2.from_json(json)
# print the JSON string representation of the object
print(EntitlementGrantV2.to_json())

# convert the object into a dict
entitlement_grant_v2_dict = entitlement_grant_v2_instance.to_dict()
# create an instance of EntitlementGrantV2 from a dict
entitlement_grant_v2_from_dict = EntitlementGrantV2.from_dict(entitlement_grant_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


