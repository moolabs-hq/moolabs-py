# EntitlementGrantCreateInput

The grant creation input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to grant. Should be a positive number. | 
**priority** | **int** | The priority of the grant. Grants with higher priority are applied first. Priority is a positive decimal numbers. With lower numbers indicating higher importance. For example, a priority of 1 is more urgent than a priority of 2. When there are several grants available for the same subject, the system selects the grant with the highest priority. In cases where grants share the same priority level, the grant closest to its expiration will be used first. In the case of two grants have identical priorities and expiration dates, the system will use the grant that was created first. | [optional] 
**effective_at** | **datetime** | Effective date for grants and anchor for recurring grants. Provided value will be ceiled to metering windowSize (minute). | 
**expiration** | [**ExpirationPeriod**](ExpirationPeriod.md) | The grant expiration definition | 
**max_rollover_amount** | **float** | Grants are rolled over at reset, after which they can have a different balance compared to what they had before the reset. Balance after the reset is calculated as: Balance_After_Reset &#x3D; MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount)) | [optional] [default to 0]
**min_rollover_amount** | **float** | Grants are rolled over at reset, after which they can have a different balance compared to what they had before the reset. Balance after the reset is calculated as: Balance_After_Reset &#x3D; MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount)) | [optional] [default to 0]
**metadata** | **Dict[str, str]** | The grant metadata. | [optional] 
**recurrence** | [**RecurringPeriodCreateInput**](RecurringPeriodCreateInput.md) | The subject of the grant. | [optional] 

## Example

```python
from moolabs.models.entitlement_grant_create_input import EntitlementGrantCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementGrantCreateInput from a JSON string
entitlement_grant_create_input_instance = EntitlementGrantCreateInput.from_json(json)
# print the JSON string representation of the object
print(EntitlementGrantCreateInput.to_json())

# convert the object into a dict
entitlement_grant_create_input_dict = entitlement_grant_create_input_instance.to_dict()
# create an instance of EntitlementGrantCreateInput from a dict
entitlement_grant_create_input_from_dict = EntitlementGrantCreateInput.from_dict(entitlement_grant_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


