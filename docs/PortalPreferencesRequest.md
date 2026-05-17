# PortalPreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **Dict[str, object]** | {\&quot;email\&quot;: {\&quot;opt_out\&quot;: false}, \&quot;sms\&quot;: {\&quot;opt_out\&quot;: true}} | 

## Example

```python
from moolabs.models.portal_preferences_request import PortalPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortalPreferencesRequest from a JSON string
portal_preferences_request_instance = PortalPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(PortalPreferencesRequest.to_json())

# convert the object into a dict
portal_preferences_request_dict = portal_preferences_request_instance.to_dict()
# create an instance of PortalPreferencesRequest from a dict
portal_preferences_request_from_dict = PortalPreferencesRequest.from_dict(portal_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


