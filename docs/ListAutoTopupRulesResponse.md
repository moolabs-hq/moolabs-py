# ListAutoTopupRulesResponse

Response from listing auto top-up rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AutoTopupRuleResponse]**](AutoTopupRuleResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from moolabs.models.list_auto_topup_rules_response import ListAutoTopupRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAutoTopupRulesResponse from a JSON string
list_auto_topup_rules_response_instance = ListAutoTopupRulesResponse.from_json(json)
# print the JSON string representation of the object
print(ListAutoTopupRulesResponse.to_json())

# convert the object into a dict
list_auto_topup_rules_response_dict = list_auto_topup_rules_response_instance.to_dict()
# create an instance of ListAutoTopupRulesResponse from a dict
list_auto_topup_rules_response_from_dict = ListAutoTopupRulesResponse.from_dict(list_auto_topup_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


