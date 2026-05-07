# BillingWorkflowCollectionAlignment

The alignment for collecting the pending line items into an invoice.  Defaults to subscription, which means that we are to create a new invoice every time the a subscription period starts (for in advance items) or ends (for in arrears items).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of alignment. | 
**recurring_period** | [**RecurringPeriodV2**](RecurringPeriodV2.md) | The recurring period for the alignment. | 

## Example

```python
from moolabs.models.billing_workflow_collection_alignment import BillingWorkflowCollectionAlignment

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowCollectionAlignment from a JSON string
billing_workflow_collection_alignment_instance = BillingWorkflowCollectionAlignment.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowCollectionAlignment.to_json())

# convert the object into a dict
billing_workflow_collection_alignment_dict = billing_workflow_collection_alignment_instance.to_dict()
# create an instance of BillingWorkflowCollectionAlignment from a dict
billing_workflow_collection_alignment_from_dict = BillingWorkflowCollectionAlignment.from_dict(billing_workflow_collection_alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


