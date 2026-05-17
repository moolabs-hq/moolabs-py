# TaskCompleteRequest

POST /tasks/{id}/complete  ``resolution`` and ``payload`` are the legacy free-form fields used for operator notes / arbitrary annotations.  ``dispatch_payload`` is the structured side-effect input read by ``app.services.task_dispatch`` (e.g. ``promised_amount_micros`` for a ``confirm_ptp`` completion). Keeping the two split avoids dispatch handlers accidentally reading operator-supplied free-text where they expected a structured field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** |  | [optional] 
**payload** | **Dict[str, object]** |  | [optional] 
**dispatch_payload** | **Dict[str, object]** | Structured input consumed by app.services.task_dispatch — shape depends on task_type (see task_dispatch handlers). | [optional] 

## Example

```python
from moolabs.models.task_complete_request import TaskCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCompleteRequest from a JSON string
task_complete_request_instance = TaskCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(TaskCompleteRequest.to_json())

# convert the object into a dict
task_complete_request_dict = task_complete_request_instance.to_dict()
# create an instance of TaskCompleteRequest from a dict
task_complete_request_from_dict = TaskCompleteRequest.from_dict(task_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


