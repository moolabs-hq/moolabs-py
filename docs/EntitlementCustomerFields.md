# EntitlementCustomerFields

Customer fields for entitlements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_key** | **str** | The identifier key unique to the customer | [optional] 
**customer_id** | **str** | The identifier unique to the customer | 

## Example

```python
from moolabs.models.entitlement_customer_fields import EntitlementCustomerFields

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementCustomerFields from a JSON string
entitlement_customer_fields_instance = EntitlementCustomerFields.from_json(json)
# print the JSON string representation of the object
print(EntitlementCustomerFields.to_json())

# convert the object into a dict
entitlement_customer_fields_dict = entitlement_customer_fields_instance.to_dict()
# create an instance of EntitlementCustomerFields from a dict
entitlement_customer_fields_from_dict = EntitlementCustomerFields.from_dict(entitlement_customer_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


