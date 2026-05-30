# QuoteApprovalDecisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_approval_decision_request import QuoteApprovalDecisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteApprovalDecisionRequest from a JSON string
quote_approval_decision_request_instance = QuoteApprovalDecisionRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteApprovalDecisionRequest.to_json())

# convert the object into a dict
quote_approval_decision_request_dict = quote_approval_decision_request_instance.to_dict()
# create an instance of QuoteApprovalDecisionRequest from a dict
quote_approval_decision_request_from_dict = QuoteApprovalDecisionRequest.from_dict(quote_approval_decision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


