# moolabs.AccountTeamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_team_member**](AccountTeamApi.md#create_account_team_member) | **POST** /v1/arc/accounts/{account_id}/team | Create Account Team Member
[**delete_account_team_member**](AccountTeamApi.md#delete_account_team_member) | **DELETE** /v1/arc/accounts/{account_id}/team/{member_id} | Delete Account Team Member
[**list_account_team**](AccountTeamApi.md#list_account_team) | **GET** /v1/arc/accounts/{account_id}/team | List Account Team
[**update_account_team_member**](AccountTeamApi.md#update_account_team_member) | **PATCH** /v1/arc/accounts/{account_id}/team/{member_id} | Update Account Team Member


# **create_account_team_member**
> AccountTeamMemberOut create_account_team_member(account_id, account_team_member_in, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id)

Create Account Team Member

Add an internal stakeholder to the account's team.  The ``user_id`` column is populated from the authenticated request context, never from the body (Issue C3).

### Example


```python
import moolabs
from moolabs.models.account_team_member_in import AccountTeamMemberIn
from moolabs.models.account_team_member_out import AccountTeamMemberOut
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AccountTeamApi(api_client)
    account_id = 'account_id_example' # str | 
    account_team_member_in = moolabs.AccountTeamMemberIn() # AccountTeamMemberIn | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)

    try:
        # Create Account Team Member
        api_response = api_instance.create_account_team_member(account_id, account_team_member_in, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id)
        print("The response of AccountTeamApi->create_account_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTeamApi->create_account_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **account_team_member_in** | [**AccountTeamMemberIn**](AccountTeamMemberIn.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 

### Return type

[**AccountTeamMemberOut**](AccountTeamMemberOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_team_member**
> delete_account_team_member(account_id, member_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Delete Account Team Member

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AccountTeamApi(api_client)
    account_id = 'account_id_example' # str | 
    member_id = 'member_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Delete Account Team Member
        api_instance.delete_account_team_member(account_id, member_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
    except Exception as e:
        print("Exception when calling AccountTeamApi->delete_account_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **member_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_team**
> List[AccountTeamMemberOut] list_account_team(account_id, notify_only=notify_only, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Account Team

List internal team members for an account.  ``notify_only=true`` returns only members with ``notify_on_escalation=true`` — used by the escalation agent when assembling a tier-N notification list.

### Example


```python
import moolabs
from moolabs.models.account_team_member_out import AccountTeamMemberOut
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AccountTeamApi(api_client)
    account_id = 'account_id_example' # str | 
    notify_only = False # bool |  (optional) (default to False)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Account Team
        api_response = api_instance.list_account_team(account_id, notify_only=notify_only, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountTeamApi->list_account_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTeamApi->list_account_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **notify_only** | **bool**|  | [optional] [default to False]
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**List[AccountTeamMemberOut]**](AccountTeamMemberOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_team_member**
> AccountTeamMemberOut update_account_team_member(account_id, member_id, account_team_member_patch, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Account Team Member

### Example


```python
import moolabs
from moolabs.models.account_team_member_out import AccountTeamMemberOut
from moolabs.models.account_team_member_patch import AccountTeamMemberPatch
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AccountTeamApi(api_client)
    account_id = 'account_id_example' # str | 
    member_id = 'member_id_example' # str | 
    account_team_member_patch = moolabs.AccountTeamMemberPatch() # AccountTeamMemberPatch | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Account Team Member
        api_response = api_instance.update_account_team_member(account_id, member_id, account_team_member_patch, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountTeamApi->update_account_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountTeamApi->update_account_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **member_id** | **str**|  | 
 **account_team_member_patch** | [**AccountTeamMemberPatch**](AccountTeamMemberPatch.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountTeamMemberOut**](AccountTeamMemberOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

