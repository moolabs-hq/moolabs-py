# RatifyRefinementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_id** | **str** |  | 
**industry_vertical** | **str** |  | 
**owner** | **str** |  | 
**position_tier** | **str** |  | [optional] [default to 'preferred']

## Example

```python
from moolabs.models.ratify_refinement_request import RatifyRefinementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatifyRefinementRequest from a JSON string
ratify_refinement_request_instance = RatifyRefinementRequest.from_json(json)
# print the JSON string representation of the object
print(RatifyRefinementRequest.to_json())

# convert the object into a dict
ratify_refinement_request_dict = ratify_refinement_request_instance.to_dict()
# create an instance of RatifyRefinementRequest from a dict
ratify_refinement_request_from_dict = RatifyRefinementRequest.from_dict(ratify_refinement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


