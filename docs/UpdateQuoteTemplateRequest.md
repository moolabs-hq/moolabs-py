# UpdateQuoteTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**company_legal_name** | **str** |  | [optional] 
**company_address** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**footer_text** | **str** |  | [optional] 

## Example

```python
from moolabs.models.update_quote_template_request import UpdateQuoteTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuoteTemplateRequest from a JSON string
update_quote_template_request_instance = UpdateQuoteTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuoteTemplateRequest.to_json())

# convert the object into a dict
update_quote_template_request_dict = update_quote_template_request_instance.to_dict()
# create an instance of UpdateQuoteTemplateRequest from a dict
update_quote_template_request_from_dict = UpdateQuoteTemplateRequest.from_dict(update_quote_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


