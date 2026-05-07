# BillingWorkflowCollectionAlignmentAnchored

BillingWorkflowCollectionAlignmentAnchored specifies the alignment for collecting the pending line items into an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of alignment. | 
**recurring_period** | [**RecurringPeriodV2**](RecurringPeriodV2.md) | The recurring period for the alignment. | 

## Example

```python
from moolabs.models.billing_workflow_collection_alignment_anchored import BillingWorkflowCollectionAlignmentAnchored

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowCollectionAlignmentAnchored from a JSON string
billing_workflow_collection_alignment_anchored_instance = BillingWorkflowCollectionAlignmentAnchored.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowCollectionAlignmentAnchored.to_json())

# convert the object into a dict
billing_workflow_collection_alignment_anchored_dict = billing_workflow_collection_alignment_anchored_instance.to_dict()
# create an instance of BillingWorkflowCollectionAlignmentAnchored from a dict
billing_workflow_collection_alignment_anchored_from_dict = BillingWorkflowCollectionAlignmentAnchored.from_dict(billing_workflow_collection_alignment_anchored_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


