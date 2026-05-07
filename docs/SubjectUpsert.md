# SubjectUpsert

A subject is a unique identifier for a user or entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique, human-readable identifier for the subject. This is typically a database ID or a customer key. | 
**display_name** | **str** | A human-readable display name for the subject. | [optional] 
**metadata** | **Dict[str, object]** | Metadata for the subject. | [optional] 
**current_period_start** | **datetime** | The start of the current period for the subject. | [optional] 
**current_period_end** | **datetime** | The end of the current period for the subject. | [optional] 
**stripe_customer_id** | **str** | The Stripe customer ID for the subject. | [optional] 

## Example

```python
from moolabs.models.subject_upsert import SubjectUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectUpsert from a JSON string
subject_upsert_instance = SubjectUpsert.from_json(json)
# print the JSON string representation of the object
print(SubjectUpsert.to_json())

# convert the object into a dict
subject_upsert_dict = subject_upsert_instance.to_dict()
# create an instance of SubjectUpsert from a dict
subject_upsert_from_dict = SubjectUpsert.from_dict(subject_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


