# Plan

Plans provide a template for subscriptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**key** | **str** | A semi-unique identifier for the resource. | 
**alignment** | [**Alignment**](Alignment.md) | Alignment configuration for the plan. | [optional] 
**version** | **int** | Version of the plan. Incremented when the plan is updated. | [readonly] [default to 1]
**currency** | **str** | The currency code of the plan. | 
**billing_cadence** | **str** | The default billing cadence for subscriptions using this plan. Defines how often customers are billed using ISO8601 duration format. Examples: \&quot;P1M\&quot; (monthly), \&quot;P3M\&quot; (quarterly), \&quot;P1Y\&quot; (annually). | 
**pro_rating_config** | [**ProRatingConfig**](ProRatingConfig.md) | Default pro-rating configuration for subscriptions using this plan. | [optional] 
**credit_config** | [**CreditConfig**](CreditConfig.md) | Default credit allowance configuration for subscriptions using this plan (first-class column). | [optional] 
**effective_from** | **datetime** | The date and time when the plan becomes effective. When not specified, the plan is a draft. | [optional] [readonly] 
**effective_to** | **datetime** | The date and time when the plan is no longer effective. When not specified, the plan is effective indefinitely. | [optional] [readonly] 
**status** | [**PlanStatus**](PlanStatus.md) | The status of the plan. Computed based on the effective start and end dates: - draft &#x3D; no effectiveFrom - active &#x3D; effectiveFrom &lt;&#x3D; now &lt; effectiveTo - archived / inactive &#x3D; effectiveTo &lt;&#x3D; now - scheduled &#x3D; now &lt; effectiveFrom &lt; effectiveTo | [readonly] 
**phases** | [**List[PlanPhase]**](PlanPhase.md) | The plan phase or pricing ramp allows changing a plan&#39;s rate cards over time as a subscription progresses. A phase switch occurs only at the end of a billing period, ensuring that a single subscription invoice will not include charges from different phase prices. | 
**validation_errors** | [**List[MeterValidationError]**](MeterValidationError.md) | List of validation errors. | 

## Example

```python
from moolabs.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print(Plan.to_json())

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_from_dict = Plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


