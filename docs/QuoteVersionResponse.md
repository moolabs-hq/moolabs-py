# QuoteVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** |  | 
**tenant_id** | **str** |  | 
**version** | **int** |  | 
**state** | **str** |  | 
**line_items** | **List[Dict[str, object]]** |  | 
**commercial_terms** | **Dict[str, object]** |  | 
**credit_terms** | **Dict[str, object]** |  | 
**source_versions** | **Dict[str, object]** |  | [optional] 
**pricing_snapshot_id** | **str** |  | 
**quote_version_digest** | **str** |  | [optional] 
**booking_trigger** | **str** |  | [optional] 
**locked_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_version_response import QuoteVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteVersionResponse from a JSON string
quote_version_response_instance = QuoteVersionResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteVersionResponse.to_json())

# convert the object into a dict
quote_version_response_dict = quote_version_response_instance.to_dict()
# create an instance of QuoteVersionResponse from a dict
quote_version_response_from_dict = QuoteVersionResponse.from_dict(quote_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


