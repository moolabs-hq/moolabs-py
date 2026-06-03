# CrmQuoteContextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**record_type** | **str** |  | 
**record_id** | **str** |  | 
**record_title** | **str** |  | 
**record_summary** | **str** |  | 
**crm_refs** | **Dict[str, str]** |  | 
**source_uri** | **str** |  | 
**source_evidence_id** | **str** |  | 

## Example

```python
from moolabs.models.crm_quote_context_response import CrmQuoteContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrmQuoteContextResponse from a JSON string
crm_quote_context_response_instance = CrmQuoteContextResponse.from_json(json)
# print the JSON string representation of the object
print(CrmQuoteContextResponse.to_json())

# convert the object into a dict
crm_quote_context_response_dict = crm_quote_context_response_instance.to_dict()
# create an instance of CrmQuoteContextResponse from a dict
crm_quote_context_response_from_dict = CrmQuoteContextResponse.from_dict(crm_quote_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


