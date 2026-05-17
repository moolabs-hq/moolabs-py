# AccountTeamMemberOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**role** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**user_id** | **str** |  | 
**is_primary** | **bool** |  | 
**notify_on_escalation** | **bool** |  | 

## Example

```python
from moolabs.models.account_team_member_out import AccountTeamMemberOut

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTeamMemberOut from a JSON string
account_team_member_out_instance = AccountTeamMemberOut.from_json(json)
# print the JSON string representation of the object
print(AccountTeamMemberOut.to_json())

# convert the object into a dict
account_team_member_out_dict = account_team_member_out_instance.to_dict()
# create an instance of AccountTeamMemberOut from a dict
account_team_member_out_from_dict = AccountTeamMemberOut.from_dict(account_team_member_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


