# DryRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**derived_fields** | **Dict[str, str]** |  | 
**match_grade** | **str** |  | 
**rules_applied** | **List[str]** |  | 
**rules_skipped** | **List[object]** |  | 
**tier3_enabled** | **bool** |  | 
**note** | **str** |  | 

## Example

```python
from moolabs.models.dry_run_response import DryRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunResponse from a JSON string
dry_run_response_instance = DryRunResponse.from_json(json)
# print the JSON string representation of the object
print(DryRunResponse.to_json())

# convert the object into a dict
dry_run_response_dict = dry_run_response_instance.to_dict()
# create an instance of DryRunResponse from a dict
dry_run_response_from_dict = DryRunResponse.from_dict(dry_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


