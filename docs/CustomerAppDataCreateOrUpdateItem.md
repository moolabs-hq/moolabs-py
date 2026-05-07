# CustomerAppDataCreateOrUpdateItem

CustomerAppData Stores the app specific data for the customer. One of: stripe, sandbox, custom_invoicing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The app ID. If not provided, it will use the global default for the app type. | [optional] 
**type** | **str** | The app name. | 
**stripe_customer_id** | **str** | The Stripe customer ID. | 
**stripe_default_payment_method_id** | **str** | The Stripe default payment method ID. | [optional] 
**app** | [**CustomInvoicingApp**](CustomInvoicingApp.md) | The installed custom invoicing app this data belongs to. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Metadata to be used by the custom invoicing provider. | [optional] 

## Example

```python
from moolabs.models.customer_app_data_create_or_update_item import CustomerAppDataCreateOrUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAppDataCreateOrUpdateItem from a JSON string
customer_app_data_create_or_update_item_instance = CustomerAppDataCreateOrUpdateItem.from_json(json)
# print the JSON string representation of the object
print(CustomerAppDataCreateOrUpdateItem.to_json())

# convert the object into a dict
customer_app_data_create_or_update_item_dict = customer_app_data_create_or_update_item_instance.to_dict()
# create an instance of CustomerAppDataCreateOrUpdateItem from a dict
customer_app_data_create_or_update_item_from_dict = CustomerAppDataCreateOrUpdateItem.from_dict(customer_app_data_create_or_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


