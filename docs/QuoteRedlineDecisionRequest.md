# QuoteRedlineDecisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_redline_decision_request import QuoteRedlineDecisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRedlineDecisionRequest from a JSON string
quote_redline_decision_request_instance = QuoteRedlineDecisionRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteRedlineDecisionRequest.to_json())

# convert the object into a dict
quote_redline_decision_request_dict = quote_redline_decision_request_instance.to_dict()
# create an instance of QuoteRedlineDecisionRequest from a dict
quote_redline_decision_request_from_dict = QuoteRedlineDecisionRequest.from_dict(quote_redline_decision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


