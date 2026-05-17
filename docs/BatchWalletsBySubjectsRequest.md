# BatchWalletsBySubjectsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_ids** | **List[str]** |  | 

## Example

```python
from moolabs.models.batch_wallets_by_subjects_request import BatchWalletsBySubjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWalletsBySubjectsRequest from a JSON string
batch_wallets_by_subjects_request_instance = BatchWalletsBySubjectsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchWalletsBySubjectsRequest.to_json())

# convert the object into a dict
batch_wallets_by_subjects_request_dict = batch_wallets_by_subjects_request_instance.to_dict()
# create an instance of BatchWalletsBySubjectsRequest from a dict
batch_wallets_by_subjects_request_from_dict = BatchWalletsBySubjectsRequest.from_dict(batch_wallets_by_subjects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


