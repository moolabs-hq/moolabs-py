# CustomerAccess

CustomerAccess describes what features the customer has access to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | [**Dict[str, EntitlementValue]**](EntitlementValue.md) | Map of entitlements the customer has access to. The key is the feature key, the value is the entitlement value + the entitlement ID. | [readonly] 

## Example

```python
from moolabs.models.customer_access import CustomerAccess

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAccess from a JSON string
customer_access_instance = CustomerAccess.from_json(json)
# print the JSON string representation of the object
print(CustomerAccess.to_json())

# convert the object into a dict
customer_access_dict = customer_access_instance.to_dict()
# create an instance of CustomerAccess from a dict
customer_access_from_dict = CustomerAccess.from_dict(customer_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


