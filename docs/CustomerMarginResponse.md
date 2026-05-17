# CustomerMarginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CustomerMarginItem]**](CustomerMarginItem.md) |  | 
**reconciliation_basis** | [**ReconciliationBasis**](ReconciliationBasis.md) |  | 

## Example

```python
from moolabs.models.customer_margin_response import CustomerMarginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMarginResponse from a JSON string
customer_margin_response_instance = CustomerMarginResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerMarginResponse.to_json())

# convert the object into a dict
customer_margin_response_dict = customer_margin_response_instance.to_dict()
# create an instance of CustomerMarginResponse from a dict
customer_margin_response_from_dict = CustomerMarginResponse.from_dict(customer_margin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


