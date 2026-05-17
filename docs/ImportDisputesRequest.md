# ImportDisputesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disputes** | [**List[ImportDisputeItem]**](ImportDisputeItem.md) |  | 

## Example

```python
from moolabs.models.import_disputes_request import ImportDisputesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDisputesRequest from a JSON string
import_disputes_request_instance = ImportDisputesRequest.from_json(json)
# print the JSON string representation of the object
print(ImportDisputesRequest.to_json())

# convert the object into a dict
import_disputes_request_dict = import_disputes_request_instance.to_dict()
# create an instance of ImportDisputesRequest from a dict
import_disputes_request_from_dict = ImportDisputesRequest.from_dict(import_disputes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


