# CrmQuoteContextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_type** | **str** |  | 
**record_id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 

## Example

```python
from moolabs.models.crm_quote_context_request import CrmQuoteContextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrmQuoteContextRequest from a JSON string
crm_quote_context_request_instance = CrmQuoteContextRequest.from_json(json)
# print the JSON string representation of the object
print(CrmQuoteContextRequest.to_json())

# convert the object into a dict
crm_quote_context_request_dict = crm_quote_context_request_instance.to_dict()
# create an instance of CrmQuoteContextRequest from a dict
crm_quote_context_request_from_dict = CrmQuoteContextRequest.from_dict(crm_quote_context_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


