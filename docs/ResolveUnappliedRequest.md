# ResolveUnappliedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition** | **str** | One of: applied_as_credit, refunded, abandoned_property, operational_void, de_minimis_writeoff, reversal_return | 

## Example

```python
from moolabs.models.resolve_unapplied_request import ResolveUnappliedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveUnappliedRequest from a JSON string
resolve_unapplied_request_instance = ResolveUnappliedRequest.from_json(json)
# print the JSON string representation of the object
print(ResolveUnappliedRequest.to_json())

# convert the object into a dict
resolve_unapplied_request_dict = resolve_unapplied_request_instance.to_dict()
# create an instance of ResolveUnappliedRequest from a dict
resolve_unapplied_request_from_dict = ResolveUnappliedRequest.from_dict(resolve_unapplied_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


