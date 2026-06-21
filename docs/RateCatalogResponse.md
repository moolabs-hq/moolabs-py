# RateCatalogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | 
**metric_type** | **str** |  | 
**tier** | **str** |  | 
**rate_per_unit** | **str** |  | 
**rate_unit_scale** | **int** |  | 
**currency** | **str** |  | 
**source** | **str** |  | 
**source_ref** | **str** |  | 
**effective_from** | **datetime** |  | 
**effective_to** | **datetime** |  | 
**pricing_rules** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.rate_catalog_response import RateCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateCatalogResponse from a JSON string
rate_catalog_response_instance = RateCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(RateCatalogResponse.to_json())

# convert the object into a dict
rate_catalog_response_dict = rate_catalog_response_instance.to_dict()
# create an instance of RateCatalogResponse from a dict
rate_catalog_response_from_dict = RateCatalogResponse.from_dict(rate_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


