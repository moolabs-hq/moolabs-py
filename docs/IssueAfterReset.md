# IssueAfterReset

Issue after reset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The initial grant amount | 
**priority** | **int** | The priority of the issue after reset | [optional] [default to 1]

## Example

```python
from moolabs.models.issue_after_reset import IssueAfterReset

# TODO update the JSON string below
json = "{}"
# create an instance of IssueAfterReset from a JSON string
issue_after_reset_instance = IssueAfterReset.from_json(json)
# print the JSON string representation of the object
print(IssueAfterReset.to_json())

# convert the object into a dict
issue_after_reset_dict = issue_after_reset_instance.to_dict()
# create an instance of IssueAfterReset from a dict
issue_after_reset_from_dict = IssueAfterReset.from_dict(issue_after_reset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


