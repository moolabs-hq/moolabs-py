# BillingWorkflowCollectionSettings

Workflow collection specifies how to collect the pending line items for an invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | [**BillingWorkflowCollectionAlignment**](BillingWorkflowCollectionAlignment.md) | The alignment for collecting the pending line items into an invoice. | [optional] 
**interval** | **str** | This grace period can be used to delay the collection of the pending line items specified in alignment.  This is useful, in case of multiple subscriptions having slightly different billing periods. | [optional] [default to 'PT1H']

## Example

```python
from moolabs.models.billing_workflow_collection_settings import BillingWorkflowCollectionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowCollectionSettings from a JSON string
billing_workflow_collection_settings_instance = BillingWorkflowCollectionSettings.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowCollectionSettings.to_json())

# convert the object into a dict
billing_workflow_collection_settings_dict = billing_workflow_collection_settings_instance.to_dict()
# create an instance of BillingWorkflowCollectionSettings from a dict
billing_workflow_collection_settings_from_dict = BillingWorkflowCollectionSettings.from_dict(billing_workflow_collection_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


