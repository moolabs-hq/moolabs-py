# ULIDOrExternalKey

ULID (Universally Unique Lexicographically Sortable Identifier) or external unique key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from moolabs.models.ulidor_external_key import ULIDOrExternalKey

# TODO update the JSON string below
json = "{}"
# create an instance of ULIDOrExternalKey from a JSON string
ulidor_external_key_instance = ULIDOrExternalKey.from_json(json)
# print the JSON string representation of the object
print(ULIDOrExternalKey.to_json())

# convert the object into a dict
ulidor_external_key_dict = ulidor_external_key_instance.to_dict()
# create an instance of ULIDOrExternalKey from a dict
ulidor_external_key_from_dict = ULIDOrExternalKey.from_dict(ulidor_external_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


