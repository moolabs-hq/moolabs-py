# DryRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**span_attributes** | **Dict[str, object]** |  | 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from moolabs.models.dry_run_request import DryRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunRequest from a JSON string
dry_run_request_instance = DryRunRequest.from_json(json)
# print the JSON string representation of the object
print(DryRunRequest.to_json())

# convert the object into a dict
dry_run_request_dict = dry_run_request_instance.to_dict()
# create an instance of DryRunRequest from a dict
dry_run_request_from_dict = DryRunRequest.from_dict(dry_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


