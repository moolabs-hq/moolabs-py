# EvidenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**dispute_id** | **str** |  | 
**evidence_type** | **str** |  | [optional] 
**source_table** | **str** |  | 
**source_id** | **str** |  | 
**summary** | **str** |  | [optional] 
**amount_micros** | **int** |  | [optional] 
**resolved_amount_micros** | **int** |  | [optional] 
**resolution_status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.evidence_response import EvidenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceResponse from a JSON string
evidence_response_instance = EvidenceResponse.from_json(json)
# print the JSON string representation of the object
print(EvidenceResponse.to_json())

# convert the object into a dict
evidence_response_dict = evidence_response_instance.to_dict()
# create an instance of EvidenceResponse from a dict
evidence_response_from_dict = EvidenceResponse.from_dict(evidence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


