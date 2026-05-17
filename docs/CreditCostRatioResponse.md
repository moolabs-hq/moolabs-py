# CreditCostRatioResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreditCostRatioItem]**](CreditCostRatioItem.md) |  | 
**reconciliation_basis** | [**ReconciliationBasis**](ReconciliationBasis.md) |  | 

## Example

```python
from moolabs.models.credit_cost_ratio_response import CreditCostRatioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCostRatioResponse from a JSON string
credit_cost_ratio_response_instance = CreditCostRatioResponse.from_json(json)
# print the JSON string representation of the object
print(CreditCostRatioResponse.to_json())

# convert the object into a dict
credit_cost_ratio_response_dict = credit_cost_ratio_response_instance.to_dict()
# create an instance of CreditCostRatioResponse from a dict
credit_cost_ratio_response_from_dict = CreditCostRatioResponse.from_dict(credit_cost_ratio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


