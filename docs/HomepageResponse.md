# HomepageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insights** | [**List[InsightCard]**](InsightCard.md) |  | 
**quick_actions** | [**List[QuickAction]**](QuickAction.md) |  | 
**greeting** | **str** |  | 

## Example

```python
from moolabs.models.homepage_response import HomepageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HomepageResponse from a JSON string
homepage_response_instance = HomepageResponse.from_json(json)
# print the JSON string representation of the object
print(HomepageResponse.to_json())

# convert the object into a dict
homepage_response_dict = homepage_response_instance.to_dict()
# create an instance of HomepageResponse from a dict
homepage_response_from_dict = HomepageResponse.from_dict(homepage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


