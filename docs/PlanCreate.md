# PlanCreate

Resource create operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**key** | **str** | A semi-unique identifier for the resource. | 
**alignment** | [**Alignment**](Alignment.md) | Alignment configuration for the plan. | [optional] 
**currency** | **str** | The currency code of the plan. | 
**billing_cadence** | **str** | The default billing cadence for subscriptions using this plan. Defines how often customers are billed using ISO8601 duration format. Examples: \&quot;P1M\&quot; (monthly), \&quot;P3M\&quot; (quarterly), \&quot;P1Y\&quot; (annually). | 
**pro_rating_config** | [**ProRatingConfig**](ProRatingConfig.md) | Default pro-rating configuration for subscriptions using this plan. | [optional] 
**credit_config** | [**CreditConfig**](CreditConfig.md) | Default credit allowance configuration for subscriptions using this plan (first-class column). | [optional] 
**phases** | [**List[PlanPhase]**](PlanPhase.md) | The plan phase or pricing ramp allows changing a plan&#39;s rate cards over time as a subscription progresses. A phase switch occurs only at the end of a billing period, ensuring that a single subscription invoice will not include charges from different phase prices. | 

## Example

```python
from moolabs.models.plan_create import PlanCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlanCreate from a JSON string
plan_create_instance = PlanCreate.from_json(json)
# print the JSON string representation of the object
print(PlanCreate.to_json())

# convert the object into a dict
plan_create_dict = plan_create_instance.to_dict()
# create an instance of PlanCreate from a dict
plan_create_from_dict = PlanCreate.from_dict(plan_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


