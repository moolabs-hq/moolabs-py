# Customer

A customer object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**key** | **str** | An optional unique key of the customer. Useful to reference the customer in external systems. For example, your database ID. | [optional] 
**usage_attribution** | [**CustomerUsageAttribution**](CustomerUsageAttribution.md) | Mapping to attribute metered usage to the customer | 
**primary_email** | **str** | The primary email address of the customer. | [optional] 
**currency** | **str** | Currency of the customer. Used for billing, tax and invoicing. | [optional] 
**billing_address** | [**Address**](Address.md) | The billing address of the customer. Used for tax and invoicing. | [optional] 
**current_subscription_id** | **str** | The ID of the Subscription if the customer has one. | [optional] [readonly] 
**subscriptions** | [**List[Subscription]**](Subscription.md) | The subscriptions of the customer. Only with the &#x60;subscriptions&#x60; expand option. | [optional] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 

## Example

```python
from moolabs.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


