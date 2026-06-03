# QuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**account_ref** | **Dict[str, object]** |  | 
**deal_ref** | **Dict[str, object]** |  | 
**buyer_contact_ref** | **Dict[str, object]** |  | 
**quote_type** | **str** |  | [optional] [default to 'new_subscription']
**owner_user_id** | **str** |  | 
**current_version** | **int** |  | 
**state** | **str** |  | 
**expires_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quote_response import QuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponse from a JSON string
quote_response_instance = QuoteResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteResponse.to_json())

# convert the object into a dict
quote_response_dict = quote_response_instance.to_dict()
# create an instance of QuoteResponse from a dict
quote_response_from_dict = QuoteResponse.from_dict(quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


