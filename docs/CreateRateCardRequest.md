# CreateRateCardRequest

Request to create a rate card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**plan_id** | **str** | Plan ID for plan-scoped rate cards (optional) | [optional] 
**feature_key** | **str** | Feature key | 
**currency** | **str** | Currency code (ISO 4217) | [optional] [default to 'USD']
**version** | **str** | Rate card version | 
**effective_from** | **datetime** | Effective from timestamp | 
**effective_to** | **datetime** | Effective to timestamp (None &#x3D; indefinite) | [optional] 
**pricing_model** | **Dict[str, object]** | Pricing model (JSON object) | 

## Example

```python
from moolabs.models.create_rate_card_request import CreateRateCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRateCardRequest from a JSON string
create_rate_card_request_instance = CreateRateCardRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRateCardRequest.to_json())

# convert the object into a dict
create_rate_card_request_dict = create_rate_card_request_instance.to_dict()
# create an instance of CreateRateCardRequest from a dict
create_rate_card_request_from_dict = CreateRateCardRequest.from_dict(create_rate_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


