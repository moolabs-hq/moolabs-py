# ApplyCreditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**amount_micros** | **int** |  | 
**case_id** | **str** | Case ID to disambiguate when invoice_id exists in multiple cases | [optional] 

## Example

```python
from moolabs.models.apply_credit_request import ApplyCreditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditRequest from a JSON string
apply_credit_request_instance = ApplyCreditRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditRequest.to_json())

# convert the object into a dict
apply_credit_request_dict = apply_credit_request_instance.to_dict()
# create an instance of ApplyCreditRequest from a dict
apply_credit_request_from_dict = ApplyCreditRequest.from_dict(apply_credit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


