# BillingWorkflowCollectionAlignmentSubscription

BillingWorkflowCollectionAlignmentSubscription specifies the alignment for collecting the pending line items into an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of alignment. | 

## Example

```python
from moolabs.models.billing_workflow_collection_alignment_subscription import BillingWorkflowCollectionAlignmentSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowCollectionAlignmentSubscription from a JSON string
billing_workflow_collection_alignment_subscription_instance = BillingWorkflowCollectionAlignmentSubscription.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowCollectionAlignmentSubscription.to_json())

# convert the object into a dict
billing_workflow_collection_alignment_subscription_dict = billing_workflow_collection_alignment_subscription_instance.to_dict()
# create an instance of BillingWorkflowCollectionAlignmentSubscription from a dict
billing_workflow_collection_alignment_subscription_from_dict = BillingWorkflowCollectionAlignmentSubscription.from_dict(billing_workflow_collection_alignment_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


