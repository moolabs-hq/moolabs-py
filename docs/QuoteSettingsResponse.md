# QuoteSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**booking_trigger** | **str** |  | 

## Example

```python
from moolabs.models.quote_settings_response import QuoteSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSettingsResponse from a JSON string
quote_settings_response_instance = QuoteSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteSettingsResponse.to_json())

# convert the object into a dict
quote_settings_response_dict = quote_settings_response_instance.to_dict()
# create an instance of QuoteSettingsResponse from a dict
quote_settings_response_from_dict = QuoteSettingsResponse.from_dict(quote_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


