# ArcTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arc_txn_id** | **str** |  | 
**txn_type** | **str** |  | 
**moometer_customer_id** | **str** |  | 
**moometer_invoice_id** | **str** |  | [optional] 
**amount_micros** | **int** |  | 
**currency_code** | **str** |  | 
**effective_at** | **datetime** |  | 
**payload** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.arc_transaction_request import ArcTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArcTransactionRequest from a JSON string
arc_transaction_request_instance = ArcTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(ArcTransactionRequest.to_json())

# convert the object into a dict
arc_transaction_request_dict = arc_transaction_request_instance.to_dict()
# create an instance of ArcTransactionRequest from a dict
arc_transaction_request_from_dict = ArcTransactionRequest.from_dict(arc_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


