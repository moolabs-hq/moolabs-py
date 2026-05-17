# PromoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promoted_rows** | **int** |  | 
**shadow_run_id** | **str** |  | 

## Example

```python
from moolabs.models.promote_response import PromoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteResponse from a JSON string
promote_response_instance = PromoteResponse.from_json(json)
# print the JSON string representation of the object
print(PromoteResponse.to_json())

# convert the object into a dict
promote_response_dict = promote_response_instance.to_dict()
# create an instance of PromoteResponse from a dict
promote_response_from_dict = PromoteResponse.from_dict(promote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


