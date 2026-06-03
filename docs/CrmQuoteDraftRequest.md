# CrmQuoteDraftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_type** | **str** |  | 
**record_id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**candidate_lines** | **List[Dict[str, object]]** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from moolabs.models.crm_quote_draft_request import CrmQuoteDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrmQuoteDraftRequest from a JSON string
crm_quote_draft_request_instance = CrmQuoteDraftRequest.from_json(json)
# print the JSON string representation of the object
print(CrmQuoteDraftRequest.to_json())

# convert the object into a dict
crm_quote_draft_request_dict = crm_quote_draft_request_instance.to_dict()
# create an instance of CrmQuoteDraftRequest from a dict
crm_quote_draft_request_from_dict = CrmQuoteDraftRequest.from_dict(crm_quote_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


