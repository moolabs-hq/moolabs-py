# ImportPromisesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promises** | [**List[ImportPromiseItem]**](ImportPromiseItem.md) |  | 

## Example

```python
from moolabs.models.import_promises_request import ImportPromisesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPromisesRequest from a JSON string
import_promises_request_instance = ImportPromisesRequest.from_json(json)
# print the JSON string representation of the object
print(ImportPromisesRequest.to_json())

# convert the object into a dict
import_promises_request_dict = import_promises_request_instance.to_dict()
# create an instance of ImportPromisesRequest from a dict
import_promises_request_from_dict = ImportPromisesRequest.from_dict(import_promises_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


