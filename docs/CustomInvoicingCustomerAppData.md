# CustomInvoicingCustomerAppData

Custom Invoicing Customer App Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**CustomInvoicingApp**](CustomInvoicingApp.md) | The installed custom invoicing app this data belongs to. | [optional] [readonly] 
**id** | **str** | The app ID. If not provided, it will use the global default for the app type. | [optional] 
**type** | **str** | The app name. | 
**metadata** | **Dict[str, str]** | Metadata to be used by the custom invoicing provider. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_customer_app_data import CustomInvoicingCustomerAppData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingCustomerAppData from a JSON string
custom_invoicing_customer_app_data_instance = CustomInvoicingCustomerAppData.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingCustomerAppData.to_json())

# convert the object into a dict
custom_invoicing_customer_app_data_dict = custom_invoicing_customer_app_data_instance.to_dict()
# create an instance of CustomInvoicingCustomerAppData from a dict
custom_invoicing_customer_app_data_from_dict = CustomInvoicingCustomerAppData.from_dict(custom_invoicing_customer_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


