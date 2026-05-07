# RateCardResponse

Rate card response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**plan_id** | **str** |  | [optional] 
**feature_key** | **str** |  | 
**currency** | **str** |  | 
**version** | **str** |  | 
**effective_from** | **datetime** |  | 
**effective_to** | **datetime** |  | 
**pricing_fingerprint** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.rate_card_response import RateCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardResponse from a JSON string
rate_card_response_instance = RateCardResponse.from_json(json)
# print the JSON string representation of the object
print(RateCardResponse.to_json())

# convert the object into a dict
rate_card_response_dict = rate_card_response_instance.to_dict()
# create an instance of RateCardResponse from a dict
rate_card_response_from_dict = RateCardResponse.from_dict(rate_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


