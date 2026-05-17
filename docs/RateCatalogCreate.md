# RateCatalogCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | 
**metric_type** | **str** |  | 
**tier** | **str** |  | [optional] [default to 'default']
**rate_per_unit** | [**RatePerUnit**](RatePerUnit.md) |  | 
**rate_unit_scale** | **int** |  | [optional] [default to 1000000]
**currency** | **str** |  | [optional] [default to 'USD']
**source** | **str** |  | [optional] [default to 'manual_override']
**source_ref** | **str** |  | [optional] 
**effective_from** | **datetime** |  | 
**effective_to** | **datetime** |  | [optional] 
**pricing_rules** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.rate_catalog_create import RateCatalogCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RateCatalogCreate from a JSON string
rate_catalog_create_instance = RateCatalogCreate.from_json(json)
# print the JSON string representation of the object
print(RateCatalogCreate.to_json())

# convert the object into a dict
rate_catalog_create_dict = rate_catalog_create_instance.to_dict()
# create an instance of RateCatalogCreate from a dict
rate_catalog_create_from_dict = RateCatalogCreate.from_dict(rate_catalog_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


