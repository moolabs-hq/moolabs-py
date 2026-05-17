# BackfillCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispute_id** | **str** |  | 
**case_id** | **str** |  | 
**current_amount_micros** | **int** |  | 
**current_invoice_id** | **str** |  | 
**would_soft_mark** | **bool** |  | 
**comm_id** | **str** |  | 

## Example

```python
from moolabs.models.backfill_candidate import BackfillCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillCandidate from a JSON string
backfill_candidate_instance = BackfillCandidate.from_json(json)
# print the JSON string representation of the object
print(BackfillCandidate.to_json())

# convert the object into a dict
backfill_candidate_dict = backfill_candidate_instance.to_dict()
# create an instance of BackfillCandidate from a dict
backfill_candidate_from_dict = BackfillCandidate.from_dict(backfill_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


