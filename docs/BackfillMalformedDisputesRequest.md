# BackfillMalformedDisputesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] [default to True]

## Example

```python
from moolabs.models.backfill_malformed_disputes_request import BackfillMalformedDisputesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BackfillMalformedDisputesRequest from a JSON string
backfill_malformed_disputes_request_instance = BackfillMalformedDisputesRequest.from_json(json)
# print the JSON string representation of the object
print(BackfillMalformedDisputesRequest.to_json())

# convert the object into a dict
backfill_malformed_disputes_request_dict = backfill_malformed_disputes_request_instance.to_dict()
# create an instance of BackfillMalformedDisputesRequest from a dict
backfill_malformed_disputes_request_from_dict = BackfillMalformedDisputesRequest.from_dict(backfill_malformed_disputes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


