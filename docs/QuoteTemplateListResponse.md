# QuoteTemplateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[QuoteTemplateResponse]**](QuoteTemplateResponse.md) |  | 

## Example

```python
from moolabs.models.quote_template_list_response import QuoteTemplateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteTemplateListResponse from a JSON string
quote_template_list_response_instance = QuoteTemplateListResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteTemplateListResponse.to_json())

# convert the object into a dict
quote_template_list_response_dict = quote_template_list_response_instance.to_dict()
# create an instance of QuoteTemplateListResponse from a dict
quote_template_list_response_from_dict = QuoteTemplateListResponse.from_dict(quote_template_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


