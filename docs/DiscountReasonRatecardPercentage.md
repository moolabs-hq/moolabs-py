# DiscountReasonRatecardPercentage

The reason for the discount is a ratecard percentage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**percentage** | **float** | The percentage of the discount. | 
**correlation_id** | **str** | Correlation ID for the discount.  This is used to link discounts across different invoices (progressive billing use case).  If not provided, the invoicing engine will auto-generate one. When editing an invoice line, please make sure to keep the same correlation ID of the discount or in progressive billing setups the discount amounts might be incorrect. | [optional] 

## Example

```python
from moolabs.models.discount_reason_ratecard_percentage import DiscountReasonRatecardPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountReasonRatecardPercentage from a JSON string
discount_reason_ratecard_percentage_instance = DiscountReasonRatecardPercentage.from_json(json)
# print the JSON string representation of the object
print(DiscountReasonRatecardPercentage.to_json())

# convert the object into a dict
discount_reason_ratecard_percentage_dict = discount_reason_ratecard_percentage_instance.to_dict()
# create an instance of DiscountReasonRatecardPercentage from a dict
discount_reason_ratecard_percentage_from_dict = DiscountReasonRatecardPercentage.from_dict(discount_reason_ratecard_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


