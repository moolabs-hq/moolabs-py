# ListAppsRequest

Query params for listing installed apps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page index.  Default is 1. | [optional] [default to 1]
**page_size** | **int** | The maximum number of items per page.  Default is 100. | [optional] [default to 100]

## Example

```python
from moolabs.models.list_apps_request import ListAppsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListAppsRequest from a JSON string
list_apps_request_instance = ListAppsRequest.from_json(json)
# print the JSON string representation of the object
print(ListAppsRequest.to_json())

# convert the object into a dict
list_apps_request_dict = list_apps_request_instance.to_dict()
# create an instance of ListAppsRequest from a dict
list_apps_request_from_dict = ListAppsRequest.from_dict(list_apps_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


