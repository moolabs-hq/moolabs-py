# ValidationIssue

ValidationIssue captures any validation issues related to the invoice.  Issues with severity \"critical\" will prevent the invoice from being issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | ID of the charge or discount. | [readonly] 
**severity** | [**ValidationIssueSeverity**](ValidationIssueSeverity.md) | The severity of the issue. | [readonly] 
**var_field** | **str** | The field that the issue is related to, if available in JSON path format. | [optional] [readonly] 
**code** | **str** | Machine indentifiable code for the issue, if available. | [optional] [readonly] 
**component** | **str** | Component reporting the issue. | [readonly] 
**message** | **str** | A human-readable description of the issue. | [readonly] 
**metadata** | **Dict[str, str]** | Additional context for the issue. | [optional] [readonly] 

## Example

```python
from moolabs.models.validation_issue import ValidationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationIssue from a JSON string
validation_issue_instance = ValidationIssue.from_json(json)
# print the JSON string representation of the object
print(ValidationIssue.to_json())

# convert the object into a dict
validation_issue_dict = validation_issue_instance.to_dict()
# create an instance of ValidationIssue from a dict
validation_issue_from_dict = ValidationIssue.from_dict(validation_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


