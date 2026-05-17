# PaymentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**netsuite_id** | **str** |  | 
**customer_internal_id** | **str** |  | 
**payment_amount** | **str** |  | [optional] 
**applied_invoice_id** | **str** |  | 
**applied_amount** | **str** |  | [optional] 
**tran_date** | **str** |  | [optional] 
**ns_last_modified** | **datetime** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.payment_item import PaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentItem from a JSON string
payment_item_instance = PaymentItem.from_json(json)
# print the JSON string representation of the object
print(PaymentItem.to_json())

# convert the object into a dict
payment_item_dict = payment_item_instance.to_dict()
# create an instance of PaymentItem from a dict
payment_item_from_dict = PaymentItem.from_dict(payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


