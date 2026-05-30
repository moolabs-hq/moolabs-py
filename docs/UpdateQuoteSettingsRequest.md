# UpdateQuoteSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_trigger** | **str** |  | 

## Example

```python
from moolabs.models.update_quote_settings_request import UpdateQuoteSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuoteSettingsRequest from a JSON string
update_quote_settings_request_instance = UpdateQuoteSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuoteSettingsRequest.to_json())

# convert the object into a dict
update_quote_settings_request_dict = update_quote_settings_request_instance.to_dict()
# create an instance of UpdateQuoteSettingsRequest from a dict
update_quote_settings_request_from_dict = UpdateQuoteSettingsRequest.from_dict(update_quote_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


