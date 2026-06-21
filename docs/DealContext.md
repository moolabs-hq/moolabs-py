# DealContext

Dynamic deal-context bindings and evaluation rules for a clause family.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind** | **Dict[str, str]** |  | 
**rules** | [**List[DealContextRule]**](DealContextRule.md) |  | 

## Example

```python
from moolabs.models.deal_context import DealContext

# TODO update the JSON string below
json = "{}"
# create an instance of DealContext from a JSON string
deal_context_instance = DealContext.from_json(json)
# print the JSON string representation of the object
print(DealContext.to_json())

# convert the object into a dict
deal_context_dict = deal_context_instance.to_dict()
# create an instance of DealContext from a dict
deal_context_from_dict = DealContext.from_dict(deal_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


