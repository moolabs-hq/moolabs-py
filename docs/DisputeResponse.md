# DisputeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**invoice_id** | **str** |  | 
**dispute_type** | **str** |  | [optional] 
**classification_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**accounting_class** | **str** |  | [optional] 
**accounting_reason_code** | **str** |  | [optional] 
**disputed_amount_micros** | **int** |  | 
**resolved_amount_micros** | **int** |  | [optional] 
**description** | **str** |  | 
**resolution_notes** | **str** |  | [optional] 
**external_dispute_id** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**resolution_deadline** | **datetime** |  | [optional] 
**resolved_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**aging_bucket** | **str** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**invoice_due_date** | **str** |  | [optional] 

## Example

```python
from moolabs.models.dispute_response import DisputeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeResponse from a JSON string
dispute_response_instance = DisputeResponse.from_json(json)
# print the JSON string representation of the object
print(DisputeResponse.to_json())

# convert the object into a dict
dispute_response_dict = dispute_response_instance.to_dict()
# create an instance of DisputeResponse from a dict
dispute_response_from_dict = DisputeResponse.from_dict(dispute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


