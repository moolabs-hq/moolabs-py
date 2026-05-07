# Alignment

Alignment configuration for a plan or subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billables_must_align** | **bool** | Whether all Billable items and RateCards must align. Alignment means the Price&#39;s BillingCadence must align for both duration and anchor time. | [optional] 

## Example

```python
from moolabs.models.alignment import Alignment

# TODO update the JSON string below
json = "{}"
# create an instance of Alignment from a JSON string
alignment_instance = Alignment.from_json(json)
# print the JSON string representation of the object
print(Alignment.to_json())

# convert the object into a dict
alignment_dict = alignment_instance.to_dict()
# create an instance of Alignment from a dict
alignment_from_dict = Alignment.from_dict(alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


