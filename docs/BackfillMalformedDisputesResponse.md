# BackfillMalformedDisputesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scanned** | **int** |  | 
**candidates** | [**List[BackfillCandidate]**](BackfillCandidate.md) |  | 
**soft_marked** | **int** |  | 
**rerouted** | **int** |  | 

## Example

```python
from moolabs.models.backfill_malformed_disputes_response import BackfillMalformedDisputesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillMalformedDisputesResponse from a JSON string
backfill_malformed_disputes_response_instance = BackfillMalformedDisputesResponse.from_json(json)
# print the JSON string representation of the object
print(BackfillMalformedDisputesResponse.to_json())

# convert the object into a dict
backfill_malformed_disputes_response_dict = backfill_malformed_disputes_response_instance.to_dict()
# create an instance of BackfillMalformedDisputesResponse from a dict
backfill_malformed_disputes_response_from_dict = BackfillMalformedDisputesResponse.from_dict(backfill_malformed_disputes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


