# CustomerAppData

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
from moolabs.models.customer_app_data import CustomerAppData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAppData from a JSON string
customer_app_data_instance = CustomerAppData.from_json(json)
# print the JSON string representation of the object
print(CustomerAppData.to_json())

# convert the object into a dict
customer_app_data_dict = customer_app_data_instance.to_dict()
# create an instance of CustomerAppData from a dict
customer_app_data_from_dict = CustomerAppData.from_dict(customer_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


