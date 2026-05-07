# AutoTopupActivityResponse

Response from listing auto-topup activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AutoTopupActivityItem]**](AutoTopupActivityItem.md) |  | 
**total** | **int** |  | 

## Example

```python
from moolabs.models.auto_topup_activity_response import AutoTopupActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopupActivityResponse from a JSON string
auto_topup_activity_response_instance = AutoTopupActivityResponse.from_json(json)
# print the JSON string representation of the object
print(AutoTopupActivityResponse.to_json())

# convert the object into a dict
auto_topup_activity_response_dict = auto_topup_activity_response_instance.to_dict()
# create an instance of AutoTopupActivityResponse from a dict
auto_topup_activity_response_from_dict = AutoTopupActivityResponse.from_dict(auto_topup_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


