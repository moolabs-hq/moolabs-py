# EmailConfigOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**sender_domain** | **str** |  | 
**from_address** | **str** |  | 
**resend_domain_id** | **str** |  | 
**verification_status** | **str** |  | 
**reply_domain** | **str** |  | 
**reply_resend_domain_id** | **str** |  | 
**reply_verification_status** | **str** |  | 
**inbound_secret_last4** | **str** |  | 
**dns_records** | **List[Dict[str, object]]** |  | [optional] 
**reply_dns_records** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from moolabs.models.email_config_out import EmailConfigOut

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfigOut from a JSON string
email_config_out_instance = EmailConfigOut.from_json(json)
# print the JSON string representation of the object
print(EmailConfigOut.to_json())

# convert the object into a dict
email_config_out_dict = email_config_out_instance.to_dict()
# create an instance of EmailConfigOut from a dict
email_config_out_from_dict = EmailConfigOut.from_dict(email_config_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


