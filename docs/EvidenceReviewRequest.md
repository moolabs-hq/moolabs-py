# EvidenceReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_status** | **str** | upheld, denied, or partial | 
**resolved_amount_micros** | **int** |  | 

## Example

```python
from moolabs.models.evidence_review_request import EvidenceReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceReviewRequest from a JSON string
evidence_review_request_instance = EvidenceReviewRequest.from_json(json)
# print the JSON string representation of the object
print(EvidenceReviewRequest.to_json())

# convert the object into a dict
evidence_review_request_dict = evidence_review_request_instance.to_dict()
# create an instance of EvidenceReviewRequest from a dict
evidence_review_request_from_dict = EvidenceReviewRequest.from_dict(evidence_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


