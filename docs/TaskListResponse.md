# TaskListResponse

Paginated task list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TaskResponse]**](TaskResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from moolabs.models.task_list_response import TaskListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskListResponse from a JSON string
task_list_response_instance = TaskListResponse.from_json(json)
# print the JSON string representation of the object
print(TaskListResponse.to_json())

# convert the object into a dict
task_list_response_dict = task_list_response_instance.to_dict()
# create an instance of TaskListResponse from a dict
task_list_response_from_dict = TaskListResponse.from_dict(task_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


