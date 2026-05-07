# ListEntitlementsResult

List entitlements result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Entitlement]**](Entitlement.md) | The items in the current page. | 

## Example

```python
from moolabs.models.list_entitlements_result import ListEntitlementsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ListEntitlementsResult from a JSON string
list_entitlements_result_instance = ListEntitlementsResult.from_json(json)
# print the JSON string representation of the object
print(ListEntitlementsResult.to_json())

# convert the object into a dict
list_entitlements_result_dict = list_entitlements_result_instance.to_dict()
# create an instance of ListEntitlementsResult from a dict
list_entitlements_result_from_dict = ListEntitlementsResult.from_dict(list_entitlements_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


