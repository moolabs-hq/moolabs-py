# EmailConfigUpsert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_domain** | **str** |  | 
**from_address** | **str** |  | [optional] 
**reply_domain** | **str** |  | [optional] 
**inbound_secret** | **str** |  | [optional] 

## Example

```python
from moolabs.models.email_config_upsert import EmailConfigUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfigUpsert from a JSON string
email_config_upsert_instance = EmailConfigUpsert.from_json(json)
# print the JSON string representation of the object
print(EmailConfigUpsert.to_json())

# convert the object into a dict
email_config_upsert_dict = email_config_upsert_instance.to_dict()
# create an instance of EmailConfigUpsert from a dict
email_config_upsert_from_dict = EmailConfigUpsert.from_dict(email_config_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


