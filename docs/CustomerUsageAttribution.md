# CustomerUsageAttribution

Mapping to attribute metered usage to the customer. One customer can have zero or more subjects, but one subject can only belong to one customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_keys** | **List[str]** | The subjects that are attributed to the customer. Can be empty when no subjects are associated with the customer. | 

## Example

```python
from moolabs.models.customer_usage_attribution import CustomerUsageAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerUsageAttribution from a JSON string
customer_usage_attribution_instance = CustomerUsageAttribution.from_json(json)
# print the JSON string representation of the object
print(CustomerUsageAttribution.to_json())

# convert the object into a dict
customer_usage_attribution_dict = customer_usage_attribution_instance.to_dict()
# create an instance of CustomerUsageAttribution from a dict
customer_usage_attribution_from_dict = CustomerUsageAttribution.from_dict(customer_usage_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


