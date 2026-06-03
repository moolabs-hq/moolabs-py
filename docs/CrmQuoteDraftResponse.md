# CrmQuoteDraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**draft_status** | **str** |  | 
**confirmation_required** | **bool** |  | 
**surface_response** | [**CrmSurfaceResponse**](CrmSurfaceResponse.md) |  | 
**open_quote_url** | **str** |  | 
**source_evidence_id** | **str** |  | 
**surface_session_id** | **str** |  | 
**command** | **Dict[str, object]** |  | [optional] 
**card** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.crm_quote_draft_response import CrmQuoteDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrmQuoteDraftResponse from a JSON string
crm_quote_draft_response_instance = CrmQuoteDraftResponse.from_json(json)
# print the JSON string representation of the object
print(CrmQuoteDraftResponse.to_json())

# convert the object into a dict
crm_quote_draft_response_dict = crm_quote_draft_response_instance.to_dict()
# create an instance of CrmQuoteDraftResponse from a dict
crm_quote_draft_response_from_dict = CrmQuoteDraftResponse.from_dict(crm_quote_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


