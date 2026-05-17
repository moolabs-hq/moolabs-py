# PaginatedPayments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PaymentItem]**](PaymentItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from moolabs.models.paginated_payments import PaginatedPayments

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPayments from a JSON string
paginated_payments_instance = PaginatedPayments.from_json(json)
# print the JSON string representation of the object
print(PaginatedPayments.to_json())

# convert the object into a dict
paginated_payments_dict = paginated_payments_instance.to_dict()
# create an instance of PaginatedPayments from a dict
paginated_payments_from_dict = PaginatedPayments.from_dict(paginated_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


