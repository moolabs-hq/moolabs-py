# SpendCommitments

Spending commitments. The customer is committed to spend at least the minimum amount and at most the maximum amount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 

## Example

```python
from moolabs.models.spend_commitments import SpendCommitments

# TODO update the JSON string below
json = "{}"
# create an instance of SpendCommitments from a JSON string
spend_commitments_instance = SpendCommitments.from_json(json)
# print the JSON string representation of the object
print(SpendCommitments.to_json())

# convert the object into a dict
spend_commitments_dict = spend_commitments_instance.to_dict()
# create an instance of SpendCommitments from a dict
spend_commitments_from_dict = SpendCommitments.from_dict(spend_commitments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


