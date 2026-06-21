# CreateQuoteTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_default** | **bool** |  | [optional] [default to False]
**company_legal_name** | **str** |  | [optional] 
**company_address** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**footer_text** | **str** |  | [optional] 

## Example

```python
from moolabs.models.create_quote_template_request import CreateQuoteTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuoteTemplateRequest from a JSON string
create_quote_template_request_instance = CreateQuoteTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQuoteTemplateRequest.to_json())

# convert the object into a dict
create_quote_template_request_dict = create_quote_template_request_instance.to_dict()
# create an instance of CreateQuoteTemplateRequest from a dict
create_quote_template_request_from_dict = CreateQuoteTemplateRequest.from_dict(create_quote_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


