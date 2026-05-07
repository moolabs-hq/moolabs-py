# ValidationResponse

Response from snapshot validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** |  | 
**is_valid** | **bool** |  | 
**balance_matches** | **bool** |  | 
**fingerprint_matches** | **bool** |  | 
**stored_balance_micros** | **int** |  | 
**recalculated_balance_micros** | **int** |  | 
**stored_fingerprint** | **str** |  | 
**recalculated_fingerprint** | **str** |  | 
**as_of_effective_at** | **str** |  | 
**as_of_recorded_at** | **str** |  | 

## Example

```python
from moolabs.models.validation_response import ValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResponse from a JSON string
validation_response_instance = ValidationResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationResponse.to_json())

# convert the object into a dict
validation_response_dict = validation_response_instance.to_dict()
# create an instance of ValidationResponse from a dict
validation_response_from_dict = ValidationResponse.from_dict(validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


