# UnappliedCashResponse

Response for a single unapplied cash entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**remittance_id** | **str** |  | 
**original_amount_micros** | **int** |  | 
**remaining_amount_micros** | **int** |  | 
**reason_code** | **str** |  | 
**status** | **str** |  | 
**disposition_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.unapplied_cash_response import UnappliedCashResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnappliedCashResponse from a JSON string
unapplied_cash_response_instance = UnappliedCashResponse.from_json(json)
# print the JSON string representation of the object
print(UnappliedCashResponse.to_json())

# convert the object into a dict
unapplied_cash_response_dict = unapplied_cash_response_instance.to_dict()
# create an instance of UnappliedCashResponse from a dict
unapplied_cash_response_from_dict = UnappliedCashResponse.from_dict(unapplied_cash_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


