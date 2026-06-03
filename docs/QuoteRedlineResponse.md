# QuoteRedlineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**proposed_terms** | **Dict[str, object]** |  | 
**redline_text** | **str** |  | 
**evidence_metadata** | **Dict[str, object]** |  | 
**created_by_actor_type** | **str** |  | 
**created_by_actor_id** | **str** |  | 
**accepted_by_actor_id** | **str** |  | [optional] 
**accepted_at** | **str** |  | [optional] 
**resulting_quote_version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_redline_response import QuoteRedlineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRedlineResponse from a JSON string
quote_redline_response_instance = QuoteRedlineResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteRedlineResponse.to_json())

# convert the object into a dict
quote_redline_response_dict = quote_redline_response_instance.to_dict()
# create an instance of QuoteRedlineResponse from a dict
quote_redline_response_from_dict = QuoteRedlineResponse.from_dict(quote_redline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


