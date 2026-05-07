# CustomerKey

Create Stripe checkout session with customer key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from moolabs.models.customer_key import CustomerKey

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerKey from a JSON string
customer_key_instance = CustomerKey.from_json(json)
# print the JSON string representation of the object
print(CustomerKey.to_json())

# convert the object into a dict
customer_key_dict = customer_key_instance.to_dict()
# create an instance of CustomerKey from a dict
customer_key_from_dict = CustomerKey.from_dict(customer_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


