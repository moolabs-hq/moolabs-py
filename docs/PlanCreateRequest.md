# PlanCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount_micros** | **int** |  | 
**installment_count** | **int** |  | 
**frequency** | **str** |  | [optional] [default to 'monthly']
**first_due_date** | **date** |  | 
**proposed_by** | **str** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**grace_period_days** | **int** |  | [optional] [default to 3]
**max_missed_before_default** | **int** |  | [optional] [default to 2]

## Example

```python
from moolabs.models.plan_create_request import PlanCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanCreateRequest from a JSON string
plan_create_request_instance = PlanCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PlanCreateRequest.to_json())

# convert the object into a dict
plan_create_request_dict = plan_create_request_instance.to_dict()
# create an instance of PlanCreateRequest from a dict
plan_create_request_from_dict = PlanCreateRequest.from_dict(plan_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


