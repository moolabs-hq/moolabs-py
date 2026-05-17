# AccountTeamMemberPatch

Partial update body.  ``user_id`` is intentionally NOT updatable via this endpoint — it's a server-resolved field (Issue C3).  Re-registering with a different user requires DELETE + POST.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AccountTeamRole**](AccountTeamRole.md) |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_primary** | **bool** |  | [optional] 
**notify_on_escalation** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.account_team_member_patch import AccountTeamMemberPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTeamMemberPatch from a JSON string
account_team_member_patch_instance = AccountTeamMemberPatch.from_json(json)
# print the JSON string representation of the object
print(AccountTeamMemberPatch.to_json())

# convert the object into a dict
account_team_member_patch_dict = account_team_member_patch_instance.to_dict()
# create an instance of AccountTeamMemberPatch from a dict
account_team_member_patch_from_dict = AccountTeamMemberPatch.from_dict(account_team_member_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


