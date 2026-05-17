# OverrideFirstIngressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**usage_event_id** | **str** | External usage event id | 
**new_first_ingress_at** | **datetime** | Replacement ingress timestamp | 
**override_ticket_id** | **str** | Break-glass ticket id (INC/CHG/JIRA) | 

## Example

```python
from moolabs.models.override_first_ingress_request import OverrideFirstIngressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideFirstIngressRequest from a JSON string
override_first_ingress_request_instance = OverrideFirstIngressRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideFirstIngressRequest.to_json())

# convert the object into a dict
override_first_ingress_request_dict = override_first_ingress_request_instance.to_dict()
# create an instance of OverrideFirstIngressRequest from a dict
override_first_ingress_request_from_dict = OverrideFirstIngressRequest.from_dict(override_first_ingress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


