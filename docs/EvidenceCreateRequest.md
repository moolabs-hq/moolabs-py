# EvidenceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidence_type** | **str** |  | 
**source_table** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**amount_micros** | **int** |  | [optional] 

## Example

```python
from moolabs.models.evidence_create_request import EvidenceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceCreateRequest from a JSON string
evidence_create_request_instance = EvidenceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(EvidenceCreateRequest.to_json())

# convert the object into a dict
evidence_create_request_dict = evidence_create_request_instance.to_dict()
# create an instance of EvidenceCreateRequest from a dict
evidence_create_request_from_dict = EvidenceCreateRequest.from_dict(evidence_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


