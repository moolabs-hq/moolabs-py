# ReviewQuarantinedResponse

Response from reviewing QUARANTINED event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_event_id** | **str** |  | 
**rating_status** | **str** |  | 
**action** | **str** |  | 
**reviewed_at** | **str** |  | 
**notes** | **str** |  | 

## Example

```python
from moolabs.models.review_quarantined_response import ReviewQuarantinedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewQuarantinedResponse from a JSON string
review_quarantined_response_instance = ReviewQuarantinedResponse.from_json(json)
# print the JSON string representation of the object
print(ReviewQuarantinedResponse.to_json())

# convert the object into a dict
review_quarantined_response_dict = review_quarantined_response_instance.to_dict()
# create an instance of ReviewQuarantinedResponse from a dict
review_quarantined_response_from_dict = ReviewQuarantinedResponse.from_dict(review_quarantined_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


