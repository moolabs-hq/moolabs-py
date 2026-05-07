# GrantUsageRecord

Usage Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_id** | **str** | The id of the grant | 
**usage** | **float** | The usage in the period | 

## Example

```python
from moolabs.models.grant_usage_record import GrantUsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of GrantUsageRecord from a JSON string
grant_usage_record_instance = GrantUsageRecord.from_json(json)
# print the JSON string representation of the object
print(GrantUsageRecord.to_json())

# convert the object into a dict
grant_usage_record_dict = grant_usage_record_instance.to_dict()
# create an instance of GrantUsageRecord from a dict
grant_usage_record_from_dict = GrantUsageRecord.from_dict(grant_usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


