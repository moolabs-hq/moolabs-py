# LinkNetSuiteAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**netsuite_customer_id** | **str** |  | 

## Example

```python
from moolabs.models.link_net_suite_account_request import LinkNetSuiteAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkNetSuiteAccountRequest from a JSON string
link_net_suite_account_request_instance = LinkNetSuiteAccountRequest.from_json(json)
# print the JSON string representation of the object
print(LinkNetSuiteAccountRequest.to_json())

# convert the object into a dict
link_net_suite_account_request_dict = link_net_suite_account_request_instance.to_dict()
# create an instance of LinkNetSuiteAccountRequest from a dict
link_net_suite_account_request_from_dict = LinkNetSuiteAccountRequest.from_dict(link_net_suite_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


