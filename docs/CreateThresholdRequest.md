# CreateThresholdRequest

Request to create a threshold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_type** | **str** | PERCENT or ABSOLUTE | 
**threshold_value** | **int** | Threshold value (0-100 for PERCENT, micros for ABSOLUTE) | 
**notify_channels** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.create_threshold_request import CreateThresholdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThresholdRequest from a JSON string
create_threshold_request_instance = CreateThresholdRequest.from_json(json)
# print the JSON string representation of the object
print(CreateThresholdRequest.to_json())

# convert the object into a dict
create_threshold_request_dict = create_threshold_request_instance.to_dict()
# create an instance of CreateThresholdRequest from a dict
create_threshold_request_from_dict = CreateThresholdRequest.from_dict(create_threshold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


