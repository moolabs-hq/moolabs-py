# ReviewQuarantinedRequest

Request to review a QUARANTINED usage event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**usage_event_id** | **str** | Usage event ID to review | 
**action** | **str** | Action: &#39;retry&#39;, &#39;manual_rate&#39;, or &#39;ignore&#39; | 
**notes** | **str** |  | [optional] 

## Example

```python
from moolabs.models.review_quarantined_request import ReviewQuarantinedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewQuarantinedRequest from a JSON string
review_quarantined_request_instance = ReviewQuarantinedRequest.from_json(json)
# print the JSON string representation of the object
print(ReviewQuarantinedRequest.to_json())

# convert the object into a dict
review_quarantined_request_dict = review_quarantined_request_instance.to_dict()
# create an instance of ReviewQuarantinedRequest from a dict
review_quarantined_request_from_dict = ReviewQuarantinedRequest.from_dict(review_quarantined_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


