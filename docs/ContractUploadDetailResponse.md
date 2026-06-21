# ContractUploadDetailResponse

Response for GET /quotes/{quote_id}/contract-uploads/latest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**filename** | **str** |  | 
**page_count** | **int** |  | 
**extracted_text** | **str** |  | 
**segments** | [**List[ContractSegmentResponse]**](ContractSegmentResponse.md) |  | 

## Example

```python
from moolabs.models.contract_upload_detail_response import ContractUploadDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractUploadDetailResponse from a JSON string
contract_upload_detail_response_instance = ContractUploadDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ContractUploadDetailResponse.to_json())

# convert the object into a dict
contract_upload_detail_response_dict = contract_upload_detail_response_instance.to_dict()
# create an instance of ContractUploadDetailResponse from a dict
contract_upload_detail_response_from_dict = ContractUploadDetailResponse.from_dict(contract_upload_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


