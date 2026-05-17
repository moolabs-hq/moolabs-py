# ReportCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [optional] [default to True]
**report_id** | **str** |  | 
**status** | **str** |  | 
**report_type** | **str** |  | 
**requested_format** | **str** |  | 
**actual_format** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**download_url** | **str** |  | [optional] 
**generated_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**summary** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.report_create_response import ReportCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreateResponse from a JSON string
report_create_response_instance = ReportCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ReportCreateResponse.to_json())

# convert the object into a dict
report_create_response_dict = report_create_response_instance.to_dict()
# create an instance of ReportCreateResponse from a dict
report_create_response_from_dict = ReportCreateResponse.from_dict(report_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


