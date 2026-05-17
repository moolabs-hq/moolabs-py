# CreatePortalTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expires_at** | **str** |  | 
**subject** | **str** |  | 

## Example

```python
from moolabs.models.create_portal_token_response import CreatePortalTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortalTokenResponse from a JSON string
create_portal_token_response_instance = CreatePortalTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePortalTokenResponse.to_json())

# convert the object into a dict
create_portal_token_response_dict = create_portal_token_response_instance.to_dict()
# create an instance of CreatePortalTokenResponse from a dict
create_portal_token_response_from_dict = CreatePortalTokenResponse.from_dict(create_portal_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


