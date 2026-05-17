# TaskResponse

Task response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | [optional] 
**task_type** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**status** | **str** |  | 
**priority** | **str** |  | 
**due_at** | **datetime** |  | [optional] 
**context** | **Dict[str, object]** |  | [optional] 
**payload** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**parent_task_id** | **str** |  | [optional] 
**draft_version** | **int** |  | [optional] [default to 1]
**lock_version** | **int** |  | [optional] [default to 1]
**completion_kind** | **str** |  | [optional] 
**prior_drafts** | **List[object]** |  | [optional] [default to []]
**associated_activity_id** | **str** |  | [optional] 
**associated_activity_type** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 

## Example

```python
from moolabs.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


