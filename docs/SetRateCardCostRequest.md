# SetRateCardCostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_unit_micros** | **int** | Per-unit cost in micros (&gt;&#x3D; 0). Null clears the cost. | [optional] 
**cost_source** | **str** | Provenance: none|manual|acute (acute treated as manual for now). | [optional] [default to 'manual']

## Example

```python
from moolabs.models.set_rate_card_cost_request import SetRateCardCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetRateCardCostRequest from a JSON string
set_rate_card_cost_request_instance = SetRateCardCostRequest.from_json(json)
# print the JSON string representation of the object
print(SetRateCardCostRequest.to_json())

# convert the object into a dict
set_rate_card_cost_request_dict = set_rate_card_cost_request_instance.to_dict()
# create an instance of SetRateCardCostRequest from a dict
set_rate_card_cost_request_from_dict = SetRateCardCostRequest.from_dict(set_rate_card_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


