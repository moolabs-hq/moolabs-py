# DiscountReasonRatecardUsage

The reason for the discount is a ratecard usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**quantity** | **str** | The quantity of the usage discount.  Must be positive. | 
**correlation_id** | **str** | Correlation ID for the discount.  This is used to link discounts across different invoices (progressive billing use case).  If not provided, the invoicing engine will auto-generate one. When editing an invoice line, please make sure to keep the same correlation ID of the discount or in progressive billing setups the discount amounts might be incorrect. | [optional] 

## Example

```python
from moolabs.models.discount_reason_ratecard_usage import DiscountReasonRatecardUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountReasonRatecardUsage from a JSON string
discount_reason_ratecard_usage_instance = DiscountReasonRatecardUsage.from_json(json)
# print the JSON string representation of the object
print(DiscountReasonRatecardUsage.to_json())

# convert the object into a dict
discount_reason_ratecard_usage_dict = discount_reason_ratecard_usage_instance.to_dict()
# create an instance of DiscountReasonRatecardUsage from a dict
discount_reason_ratecard_usage_from_dict = DiscountReasonRatecardUsage.from_dict(discount_reason_ratecard_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


