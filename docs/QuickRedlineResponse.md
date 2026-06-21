# QuickRedlineResponse

Response from POST /clause-packs/quick-redline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** |  | 
**audit_id** | **str** |  | 
**filename** | **str** |  | 
**page_count** | **int** |  | 
**extracted_text** | **str** |  | 
**segments** | [**List[SegmentOut]**](SegmentOut.md) |  | 
**findings** | [**List[ClauseFinding]**](ClauseFinding.md) |  | 
**divergences** | **List[object]** |  | 
**summary** | [**RedlineSummary**](RedlineSummary.md) |  | 

## Example

```python
from moolabs.models.quick_redline_response import QuickRedlineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuickRedlineResponse from a JSON string
quick_redline_response_instance = QuickRedlineResponse.from_json(json)
# print the JSON string representation of the object
print(QuickRedlineResponse.to_json())

# convert the object into a dict
quick_redline_response_dict = quick_redline_response_instance.to_dict()
# create an instance of QuickRedlineResponse from a dict
quick_redline_response_from_dict = QuickRedlineResponse.from_dict(quick_redline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


