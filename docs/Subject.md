# Subject

A subject is a unique identifier for a usage attribution by its key. Subjects only exist in the concept of metering. Subjects are optional to create and work as an enrichment for the subject key like displayName, metadata, etc. Subjects are useful when you are reporting usage events with your own database ID but want to enrich the subject with a human-readable name or metadata. For most use cases, a subject is equivalent to a customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | A unique identifier for the subject. | [readonly] 
**key** | **str** | A unique, human-readable identifier for the subject. This is typically a database ID or a customer key. | 
**display_name** | **str** | A human-readable display name for the subject. | [optional] 
**metadata** | **Dict[str, object]** | Metadata for the subject. | [optional] 
**current_period_start** | **datetime** | The start of the current period for the subject. | [optional] 
**current_period_end** | **datetime** | The end of the current period for the subject. | [optional] 
**stripe_customer_id** | **str** | The Stripe customer ID for the subject. | [optional] 

## Example

```python
from moolabs.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print(Subject.to_json())

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_from_dict = Subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


