# CustomerCreate

Resource create operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**key** | **str** | An optional unique key of the customer. Useful to reference the customer in external systems. For example, your database ID. | [optional] 
**usage_attribution** | [**CustomerUsageAttribution**](CustomerUsageAttribution.md) | Mapping to attribute metered usage to the customer | 
**primary_email** | **str** | The primary email address of the customer. | [optional] 
**currency** | **str** | Currency of the customer. Used for billing, tax and invoicing. | [optional] 
**billing_address** | [**Address**](Address.md) | The billing address of the customer. Used for tax and invoicing. | [optional] 

## Example

```python
from moolabs.models.customer_create import CustomerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreate from a JSON string
customer_create_instance = CustomerCreate.from_json(json)
# print the JSON string representation of the object
print(CustomerCreate.to_json())

# convert the object into a dict
customer_create_dict = customer_create_instance.to_dict()
# create an instance of CustomerCreate from a dict
customer_create_from_dict = CustomerCreate.from_dict(customer_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


