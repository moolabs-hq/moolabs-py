# EntitlementV2

Entitlement templates are used to define the entitlements of a plan. Features are omitted from the entitlement template, as they are defined in the rate card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**is_soft_limit** | **bool** | If softLimit&#x3D;true the subject can use the feature even if the entitlement is exhausted, hasAccess will always be true. | [optional] [default to False]
**preserve_overage_at_reset** | **bool** | If true, the overage is preserved at reset. If false, the usage is reset to 0. | [optional] [default to False]
**issue_after_reset** | **float** | You can grant usage automatically alongside the entitlement, the example scenario would be creating a starting balance. If an amount is specified here, a grant will be created alongside the entitlement with the specified amount. That grant will have it&#39;s rollover settings configured in a way that after each reset operation, the balance will return the original amount specified here. Manually creating such a grant would mean having the \&quot;amount\&quot;, \&quot;minRolloverAmount\&quot;, and \&quot;maxRolloverAmount\&quot; fields all be the same. | [optional] 
**issue_after_reset_priority** | **int** | Defines the grant priority for the default grant. | [optional] [default to 1]
**issue** | [**IssueAfterReset**](IssueAfterReset.md) | Issue after reset | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**annotations** | **Dict[str, object]** | The annotations of the entitlement. | [optional] [readonly] 
**id** | **str** | Readonly unique ULID identifier. | [readonly] 
**feature_key** | **str** | The feature the subject is entitled to use. | 
**feature_id** | **str** | The feature the subject is entitled to use. | 
**last_reset** | **datetime** | The time the last reset happened. | [readonly] 
**current_usage_period** | [**Period**](Period.md) | The current usage period. | 
**measure_usage_from** | **datetime** | The time from which usage is measured. If not specified on creation, defaults to entitlement creation time. | [readonly] 
**usage_period** | [**RecurringPeriod**](RecurringPeriod.md) | The defined usage period of the entitlement | 
**customer_key** | **str** | The identifier key unique to the customer | [optional] 
**customer_id** | **str** | The identifier unique to the customer | 
**config** | **str** | The JSON parsable config of the entitlement. This value is also returned when checking entitlement access and it is useful for configuring fine-grained access settings to the feature, implemented in your own system. Has to be an object. | 

## Example

```python
from moolabs.models.entitlement_v2 import EntitlementV2

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementV2 from a JSON string
entitlement_v2_instance = EntitlementV2.from_json(json)
# print the JSON string representation of the object
print(EntitlementV2.to_json())

# convert the object into a dict
entitlement_v2_dict = entitlement_v2_instance.to_dict()
# create an instance of EntitlementV2 from a dict
entitlement_v2_from_dict = EntitlementV2.from_dict(entitlement_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


