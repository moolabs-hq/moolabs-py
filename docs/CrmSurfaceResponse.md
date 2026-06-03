# CrmSurfaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surface** | **str** |  | 
**provider** | **str** |  | 
**plain_text_summary** | **str** |  | 
**deep_links** | **List[Dict[str, str]]** |  | 
**confirmation_status** | **str** |  | 
**redacted_evidence_summary** | **List[Dict[str, str]]** |  | 

## Example

```python
from moolabs.models.crm_surface_response import CrmSurfaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrmSurfaceResponse from a JSON string
crm_surface_response_instance = CrmSurfaceResponse.from_json(json)
# print the JSON string representation of the object
print(CrmSurfaceResponse.to_json())

# convert the object into a dict
crm_surface_response_dict = crm_surface_response_instance.to_dict()
# create an instance of CrmSurfaceResponse from a dict
crm_surface_response_from_dict = CrmSurfaceResponse.from_dict(crm_surface_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


