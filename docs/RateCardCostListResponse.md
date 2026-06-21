# RateCardCostListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_cards** | [**List[RateCardCostRow]**](RateCardCostRow.md) |  | 

## Example

```python
from moolabs.models.rate_card_cost_list_response import RateCardCostListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardCostListResponse from a JSON string
rate_card_cost_list_response_instance = RateCardCostListResponse.from_json(json)
# print the JSON string representation of the object
print(RateCardCostListResponse.to_json())

# convert the object into a dict
rate_card_cost_list_response_dict = rate_card_cost_list_response_instance.to_dict()
# create an instance of RateCardCostListResponse from a dict
rate_card_cost_list_response_from_dict = RateCardCostListResponse.from_dict(rate_card_cost_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


