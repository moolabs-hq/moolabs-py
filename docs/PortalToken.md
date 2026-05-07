# PortalToken

A consumer portal token.  Validator doesn't obey required for readOnly properties See: https://github.com/stoplightio/spectral/issues/1274

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ULID (Universally Unique Lexicographically Sortable Identifier). | [optional] [readonly] 
**subject** | **str** |  | 
**expires_at** | **datetime** | [RFC3339](https://tools.ietf.org/html/rfc3339) formatted date-time string in UTC. | [optional] [readonly] 
**expired** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** | [RFC3339](https://tools.ietf.org/html/rfc3339) formatted date-time string in UTC. | [optional] [readonly] 
**token** | **str** | The token is only returned at creation. | [optional] [readonly] 
**allowed_meter_slugs** | **List[str]** | Optional, if defined only the specified meters will be allowed. | [optional] 

## Example

```python
from moolabs.models.portal_token import PortalToken

# TODO update the JSON string below
json = "{}"
# create an instance of PortalToken from a JSON string
portal_token_instance = PortalToken.from_json(json)
# print the JSON string representation of the object
print(PortalToken.to_json())

# convert the object into a dict
portal_token_dict = portal_token_instance.to_dict()
# create an instance of PortalToken from a dict
portal_token_from_dict = PortalToken.from_dict(portal_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


