# CrmQuoteRecordCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**quote_state** | **str** |  | 
**last_agent_summary** | **str** |  | [optional] 
**open_quote_url** | **str** |  | 

## Example

```python
from moolabs.models.crm_quote_record_card_response import CrmQuoteRecordCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrmQuoteRecordCardResponse from a JSON string
crm_quote_record_card_response_instance = CrmQuoteRecordCardResponse.from_json(json)
# print the JSON string representation of the object
print(CrmQuoteRecordCardResponse.to_json())

# convert the object into a dict
crm_quote_record_card_response_dict = crm_quote_record_card_response_instance.to_dict()
# create an instance of CrmQuoteRecordCardResponse from a dict
crm_quote_record_card_response_from_dict = CrmQuoteRecordCardResponse.from_dict(crm_quote_record_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


