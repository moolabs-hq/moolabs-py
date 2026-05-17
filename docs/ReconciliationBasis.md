# ReconciliationBasis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade** | **str** |  | 
**include_partial** | **bool** |  | 
**fully_reconciled_count_by_usage_time** | **int** |  | 
**partially_reconciled_count_by_usage_time** | **int** |  | 
**unreconciled_count_by_usage_time** | **int** |  | 
**completeness_pct** | **str** |  | 
**data_freshness** | **str** |  | 

## Example

```python
from moolabs.models.reconciliation_basis import ReconciliationBasis

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationBasis from a JSON string
reconciliation_basis_instance = ReconciliationBasis.from_json(json)
# print the JSON string representation of the object
print(ReconciliationBasis.to_json())

# convert the object into a dict
reconciliation_basis_dict = reconciliation_basis_instance.to_dict()
# create an instance of ReconciliationBasis from a dict
reconciliation_basis_from_dict = ReconciliationBasis.from_dict(reconciliation_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


