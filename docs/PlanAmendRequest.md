# PlanAmendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount_micros** | **int** |  | 
**installment_count** | **int** |  | 
**frequency** | **str** |  | [optional] [default to 'monthly']
**first_due_date** | **date** |  | 
**proposed_by** | **str** |  | [optional] [default to 'human']
**currency_code** | **str** |  | [optional] [default to 'USD']
**grace_period_days** | **int** |  | [optional] [default to 3]
**max_missed_before_default** | **int** |  | [optional] [default to 2]

## Example

```python
from moolabs.models.plan_amend_request import PlanAmendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAmendRequest from a JSON string
plan_amend_request_instance = PlanAmendRequest.from_json(json)
# print the JSON string representation of the object
print(PlanAmendRequest.to_json())

# convert the object into a dict
plan_amend_request_dict = plan_amend_request_instance.to_dict()
# create an instance of PlanAmendRequest from a dict
plan_amend_request_from_dict = PlanAmendRequest.from_dict(plan_amend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


