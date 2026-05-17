# ReconciliationBasisOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade** | **str** |  | 
**data_freshness** | **str** |  | 
**cost_completeness_pct** | **float** |  | 
**observation_status** | **str** |  | 
**bom_approved_at** | **str** |  | 

## Example

```python
from moolabs.models.reconciliation_basis_out import ReconciliationBasisOut

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationBasisOut from a JSON string
reconciliation_basis_out_instance = ReconciliationBasisOut.from_json(json)
# print the JSON string representation of the object
print(ReconciliationBasisOut.to_json())

# convert the object into a dict
reconciliation_basis_out_dict = reconciliation_basis_out_instance.to_dict()
# create an instance of ReconciliationBasisOut from a dict
reconciliation_basis_out_from_dict = ReconciliationBasisOut.from_dict(reconciliation_basis_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


