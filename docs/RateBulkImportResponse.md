# RateBulkImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted** | **int** |  | 
**skipped** | **int** |  | 
**details** | **List[Dict[str, object]]** |  | 

## Example

```python
from moolabs.models.rate_bulk_import_response import RateBulkImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateBulkImportResponse from a JSON string
rate_bulk_import_response_instance = RateBulkImportResponse.from_json(json)
# print the JSON string representation of the object
print(RateBulkImportResponse.to_json())

# convert the object into a dict
rate_bulk_import_response_dict = rate_bulk_import_response_instance.to_dict()
# create an instance of RateBulkImportResponse from a dict
rate_bulk_import_response_from_dict = RateBulkImportResponse.from_dict(rate_bulk_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


