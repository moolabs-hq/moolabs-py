# RateCardDiscountPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_bps** | **int** |  | 

## Example

```python
from moolabs.models.rate_card_discount_payload import RateCardDiscountPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardDiscountPayload from a JSON string
rate_card_discount_payload_instance = RateCardDiscountPayload.from_json(json)
# print the JSON string representation of the object
print(RateCardDiscountPayload.to_json())

# convert the object into a dict
rate_card_discount_payload_dict = rate_card_discount_payload_instance.to_dict()
# create an instance of RateCardDiscountPayload from a dict
rate_card_discount_payload_from_dict = RateCardDiscountPayload.from_dict(rate_card_discount_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


