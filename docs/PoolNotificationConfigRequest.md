# PoolNotificationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_emails** | **List[str]** | List of email addresses to notify on pool-level alerts | 

## Example

```python
from moolabs.models.pool_notification_config_request import PoolNotificationConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PoolNotificationConfigRequest from a JSON string
pool_notification_config_request_instance = PoolNotificationConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PoolNotificationConfigRequest.to_json())

# convert the object into a dict
pool_notification_config_request_dict = pool_notification_config_request_instance.to_dict()
# create an instance of PoolNotificationConfigRequest from a dict
pool_notification_config_request_from_dict = PoolNotificationConfigRequest.from_dict(pool_notification_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


