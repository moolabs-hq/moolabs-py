# AccountTeamMemberIn

Request body for creating an internal team member.  Note: ``user_id`` is intentionally NOT a body field — it's resolved server-side from the authenticated request context (``X-User-Id`` header / future JWT claim) to prevent forgery of the team-member identity (Issue C3 — mass-assignment guard). Callers register *themselves* on the account team; admin workflows that need to register on behalf of others should use a future ``POST /admin/...`` endpoint that explicitly checks admin role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AccountTeamRole**](AccountTeamRole.md) |  | 
**name** | **str** |  | 
**email** | **str** |  | [optional] 
**is_primary** | **bool** |  | [optional] [default to False]
**notify_on_escalation** | **bool** |  | [optional] [default to True]

## Example

```python
from moolabs.models.account_team_member_in import AccountTeamMemberIn

# TODO update the JSON string below
json = "{}"
# create an instance of AccountTeamMemberIn from a JSON string
account_team_member_in_instance = AccountTeamMemberIn.from_json(json)
# print the JSON string representation of the object
print(AccountTeamMemberIn.to_json())

# convert the object into a dict
account_team_member_in_dict = account_team_member_in_instance.to_dict()
# create an instance of AccountTeamMemberIn from a dict
account_team_member_in_from_dict = AccountTeamMemberIn.from_dict(account_team_member_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


