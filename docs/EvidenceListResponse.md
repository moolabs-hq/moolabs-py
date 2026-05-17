# EvidenceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EvidenceResponse]**](EvidenceResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from moolabs.models.evidence_list_response import EvidenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceListResponse from a JSON string
evidence_list_response_instance = EvidenceListResponse.from_json(json)
# print the JSON string representation of the object
print(EvidenceListResponse.to_json())

# convert the object into a dict
evidence_list_response_dict = evidence_list_response_instance.to_dict()
# create an instance of EvidenceListResponse from a dict
evidence_list_response_from_dict = EvidenceListResponse.from_dict(evidence_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


