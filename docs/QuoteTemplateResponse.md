# QuoteTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** |  | 
**is_default** | **bool** |  | 
**company_legal_name** | **str** |  | [optional] 
**company_address** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**terms_and_conditions** | **str** |  | [optional] 
**footer_text** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_template_response import QuoteTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteTemplateResponse from a JSON string
quote_template_response_instance = QuoteTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteTemplateResponse.to_json())

# convert the object into a dict
quote_template_response_dict = quote_template_response_instance.to_dict()
# create an instance of QuoteTemplateResponse from a dict
quote_template_response_from_dict = QuoteTemplateResponse.from_dict(quote_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


