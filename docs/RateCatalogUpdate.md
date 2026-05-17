# RateCatalogUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_per_unit** | [**RatePerUnit1**](RatePerUnit1.md) |  | [optional] 
**rate_unit_scale** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_ref** | **str** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**pricing_rules** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.rate_catalog_update import RateCatalogUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RateCatalogUpdate from a JSON string
rate_catalog_update_instance = RateCatalogUpdate.from_json(json)
# print the JSON string representation of the object
print(RateCatalogUpdate.to_json())

# convert the object into a dict
rate_catalog_update_dict = rate_catalog_update_instance.to_dict()
# create an instance of RateCatalogUpdate from a dict
rate_catalog_update_from_dict = RateCatalogUpdate.from_dict(rate_catalog_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


