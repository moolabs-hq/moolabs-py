# SegmentOut

A document segment as returned by the quick-redline endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**page** | **int** |  | 
**ordinal** | **int** |  | 
**char_start** | **int** |  | 
**char_end** | **int** |  | 

## Example

```python
from moolabs.models.segment_out import SegmentOut

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentOut from a JSON string
segment_out_instance = SegmentOut.from_json(json)
# print the JSON string representation of the object
print(SegmentOut.to_json())

# convert the object into a dict
segment_out_dict = segment_out_instance.to_dict()
# create an instance of SegmentOut from a dict
segment_out_from_dict = SegmentOut.from_dict(segment_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


