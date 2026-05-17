# EnableTier3Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**connector_type** | **str** |  | 
**status** | **str** |  | 
**warning** | **str** |  | 

## Example

```python
from moolabs.models.enable_tier3_response import EnableTier3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EnableTier3Response from a JSON string
enable_tier3_response_instance = EnableTier3Response.from_json(json)
# print the JSON string representation of the object
print(EnableTier3Response.to_json())

# convert the object into a dict
enable_tier3_response_dict = enable_tier3_response_instance.to_dict()
# create an instance of EnableTier3Response from a dict
enable_tier3_response_from_dict = EnableTier3Response.from_dict(enable_tier3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


