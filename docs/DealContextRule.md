# DealContextRule

A conditional rule that fires based on deal-context variable values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **str** |  | 
**escalate_to** | **str** |  | [optional] 
**require_approver** | **str** |  | [optional] 
**verdict_override** | **str** |  | [optional] 
**flag** | **str** |  | [optional] 

## Example

```python
from moolabs.models.deal_context_rule import DealContextRule

# TODO update the JSON string below
json = "{}"
# create an instance of DealContextRule from a JSON string
deal_context_rule_instance = DealContextRule.from_json(json)
# print the JSON string representation of the object
print(DealContextRule.to_json())

# convert the object into a dict
deal_context_rule_dict = deal_context_rule_instance.to_dict()
# create an instance of DealContextRule from a dict
deal_context_rule_from_dict = DealContextRule.from_dict(deal_context_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


