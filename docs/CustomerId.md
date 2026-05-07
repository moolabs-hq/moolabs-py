# CustomerId

Create Stripe checkout session with customer ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ULID (Universally Unique Lexicographically Sortable Identifier). | 

## Example

```python
from moolabs.models.customer_id import CustomerId

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerId from a JSON string
customer_id_instance = CustomerId.from_json(json)
# print the JSON string representation of the object
print(CustomerId.to_json())

# convert the object into a dict
customer_id_dict = customer_id_instance.to_dict()
# create an instance of CustomerId from a dict
customer_id_from_dict = CustomerId.from_dict(customer_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


