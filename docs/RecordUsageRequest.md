# RecordUsageRequest

Request to record usage event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**subject_id** | **str** | Subject identifier | 
**pool_id** | **str** | Credit pool identifier | 
**wallet_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**feature_key** | **str** | Feature key | 
**meter_slug** | **str** |  | [optional] 
**usage_event_id** | **str** | Usage event ID (idempotency key) | 
**request_id** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 
**effective_at** | **datetime** | Effective timestamp | 
**usage_vector** | **Dict[str, object]** | Usage vector (JSON object) | 

## Example

```python
from moolabs.models.record_usage_request import RecordUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordUsageRequest from a JSON string
record_usage_request_instance = RecordUsageRequest.from_json(json)
# print the JSON string representation of the object
print(RecordUsageRequest.to_json())

# convert the object into a dict
record_usage_request_dict = record_usage_request_instance.to_dict()
# create an instance of RecordUsageRequest from a dict
record_usage_request_from_dict = RecordUsageRequest.from_dict(record_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


