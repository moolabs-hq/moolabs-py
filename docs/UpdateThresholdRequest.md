# UpdateThresholdRequest

Request to update a threshold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_value** | **int** |  | [optional] 
**notify_channels** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.update_threshold_request import UpdateThresholdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThresholdRequest from a JSON string
update_threshold_request_instance = UpdateThresholdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateThresholdRequest.to_json())

# convert the object into a dict
update_threshold_request_dict = update_threshold_request_instance.to_dict()
# create an instance of UpdateThresholdRequest from a dict
update_threshold_request_from_dict = UpdateThresholdRequest.from_dict(update_threshold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


