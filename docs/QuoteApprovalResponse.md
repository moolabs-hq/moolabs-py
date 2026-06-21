# QuoteApprovalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** |  | 
**tenant_id** | **str** |  | 
**version** | **int** |  | 
**status** | **str** |  | 
**approval_required** | **bool** |  | 
**required_role** | **str** |  | [optional] 
**approval_policy_version** | **str** |  | 
**approval_basis_digest** | **str** |  | [optional] 
**reasons** | **List[Dict[str, object]]** |  | [optional] 
**approval_id** | **str** |  | [optional] 
**chain** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.quote_approval_response import QuoteApprovalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteApprovalResponse from a JSON string
quote_approval_response_instance = QuoteApprovalResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteApprovalResponse.to_json())

# convert the object into a dict
quote_approval_response_dict = quote_approval_response_instance.to_dict()
# create an instance of QuoteApprovalResponse from a dict
quote_approval_response_from_dict = QuoteApprovalResponse.from_dict(quote_approval_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


