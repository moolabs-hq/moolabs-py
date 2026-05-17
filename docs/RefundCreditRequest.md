# RefundCreditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_micros** | **int** |  | 
**refund_reference** | **str** |  | [optional] 

## Example

```python
from moolabs.models.refund_credit_request import RefundCreditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundCreditRequest from a JSON string
refund_credit_request_instance = RefundCreditRequest.from_json(json)
# print the JSON string representation of the object
print(RefundCreditRequest.to_json())

# convert the object into a dict
refund_credit_request_dict = refund_credit_request_instance.to_dict()
# create an instance of RefundCreditRequest from a dict
refund_credit_request_from_dict = RefundCreditRequest.from_dict(refund_credit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


