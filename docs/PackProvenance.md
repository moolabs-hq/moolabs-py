# PackProvenance

Provenance metadata for a clause pack.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authored_by** | **str** |  | [optional] [default to 'moolabs']
**forked_from** | **str** |  | [optional] 
**signoffs** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from moolabs.models.pack_provenance import PackProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of PackProvenance from a JSON string
pack_provenance_instance = PackProvenance.from_json(json)
# print the JSON string representation of the object
print(PackProvenance.to_json())

# convert the object into a dict
pack_provenance_dict = pack_provenance_instance.to_dict()
# create an instance of PackProvenance from a dict
pack_provenance_from_dict = PackProvenance.from_dict(pack_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


