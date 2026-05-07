# ListFeaturesResult

List features result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Feature]**](Feature.md) | The items in the current page. | 

## Example

```python
from moolabs.models.list_features_result import ListFeaturesResult

# TODO update the JSON string below
json = "{}"
# create an instance of ListFeaturesResult from a JSON string
list_features_result_instance = ListFeaturesResult.from_json(json)
# print the JSON string representation of the object
print(ListFeaturesResult.to_json())

# convert the object into a dict
list_features_result_dict = list_features_result_instance.to_dict()
# create an instance of ListFeaturesResult from a dict
list_features_result_from_dict = ListFeaturesResult.from_dict(list_features_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


