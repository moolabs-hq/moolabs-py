# CaseResponse

GET /cases/{id} response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**account_id** | **str** |  | 
**customer_id** | **str** |  | 
**scope_hash** | **str** |  | 
**currency_code** | **str** |  | 
**base_currency_code** | **str** |  | 
**status** | **str** |  | 
**risk_tier** | **str** |  | 
**autonomy_level** | **int** |  | 
**total_outstanding_micros** | **int** |  | 
**total_outstanding_base_micros** | **int** |  | 
**total_disputed_micros** | **int** |  | [optional] [default to 0]
**oldest_due_date** | **date** |  | [optional] 
**last_contact_at** | **datetime** |  | [optional] 
**last_payment_at** | **datetime** |  | [optional] 
**next_action_at** | **datetime** |  | [optional] 
**next_action_type** | [**NextActionType**](NextActionType.md) |  | [optional] 
**next_promise_due_at** | **datetime** |  | [optional] 
**dunning_stage** | **str** |  | 
**current_strategy_step** | **str** |  | [optional] 
**strategy_id** | **str** |  | [optional] 
**assigned_agent** | **str** |  | [optional] 
**assigned_human** | **str** |  | [optional] 
**case_owner_team** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**invoices** | [**List[CaseInvoiceResponse]**](CaseInvoiceResponse.md) |  | [optional] 
**promises** | [**List[PromiseResponse]**](PromiseResponse.md) |  | [optional] 
**account** | [**AccountSummary**](AccountSummary.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.case_response import CaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseResponse from a JSON string
case_response_instance = CaseResponse.from_json(json)
# print the JSON string representation of the object
print(CaseResponse.to_json())

# convert the object into a dict
case_response_dict = case_response_instance.to_dict()
# create an instance of CaseResponse from a dict
case_response_from_dict = CaseResponse.from_dict(case_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


