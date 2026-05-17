# RateBulkImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**rates** | [**List[RateCatalogCreate]**](RateCatalogCreate.md) |  | 

## Example

```python
from moolabs.models.rate_bulk_import_request import RateBulkImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateBulkImportRequest from a JSON string
rate_bulk_import_request_instance = RateBulkImportRequest.from_json(json)
# print the JSON string representation of the object
print(RateBulkImportRequest.to_json())

# convert the object into a dict
rate_bulk_import_request_dict = rate_bulk_import_request_instance.to_dict()
# create an instance of RateBulkImportRequest from a dict
rate_bulk_import_request_from_dict = RateBulkImportRequest.from_dict(rate_bulk_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


