# PromiseResponse

Embedded PTP within a case-detail response.  Slim projection of ArcPromiseToPay — enough for the case-detail UI to render the promise list without a separate API call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**case_id** | **str** |  | 
**invoice_id** | **str** |  | [optional] 
**promised_amount_micros** | **int** |  | 
**fulfilled_amount_micros** | **int** |  | [optional] [default to 0]
**currency_code** | **str** |  | 
**promised_date** | **date** |  | 
**status** | **str** |  | 
**broken_at** | **datetime** |  | [optional] 
**captured_from_channel** | **str** |  | 
**captured_by** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.promise_response import PromiseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromiseResponse from a JSON string
promise_response_instance = PromiseResponse.from_json(json)
# print the JSON string representation of the object
print(PromiseResponse.to_json())

# convert the object into a dict
promise_response_dict = promise_response_instance.to_dict()
# create an instance of PromiseResponse from a dict
promise_response_from_dict = PromiseResponse.from_dict(promise_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


