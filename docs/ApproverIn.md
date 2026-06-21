# ApproverIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level_key** | **str** |  | 
**display_name** | **str** |  | [optional] 
**manager_user_ref** | **str** |  | [optional] 
**territory_key** | **str** |  | [optional] 

## Example

```python
from moolabs.models.approver_in import ApproverIn

# TODO update the JSON string below
json = "{}"
# create an instance of ApproverIn from a JSON string
approver_in_instance = ApproverIn.from_json(json)
# print the JSON string representation of the object
print(ApproverIn.to_json())

# convert the object into a dict
approver_in_dict = approver_in_instance.to_dict()
# create an instance of ApproverIn from a dict
approver_in_from_dict = ApproverIn.from_dict(approver_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


