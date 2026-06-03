# EffectivePermissionGrantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**permission** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.effective_permission_grant_dto import EffectivePermissionGrantDto

# TODO update the JSON string below
json = "{}"
# create an instance of EffectivePermissionGrantDto from a JSON string
effective_permission_grant_dto_instance = EffectivePermissionGrantDto.from_json(json)
# print the JSON string representation of the object
print(EffectivePermissionGrantDto.to_json())

# convert the object into a dict
effective_permission_grant_dto_dict = effective_permission_grant_dto_instance.to_dict()
# create an instance of EffectivePermissionGrantDto from a dict
effective_permission_grant_dto_from_dict = EffectivePermissionGrantDto.from_dict(effective_permission_grant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


