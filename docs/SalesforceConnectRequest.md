# SalesforceConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** |  | 
**sync_direction** | **str** |  | 
**sync_frequency** | **str** |  | 
**owner** | **str** |  | [optional] 

## Example

```python
from moolabs.models.salesforce_connect_request import SalesforceConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceConnectRequest from a JSON string
salesforce_connect_request_instance = SalesforceConnectRequest.from_json(json)
# print the JSON string representation of the object
print(SalesforceConnectRequest.to_json())

# convert the object into a dict
salesforce_connect_request_dict = salesforce_connect_request_instance.to_dict()
# create an instance of SalesforceConnectRequest from a dict
salesforce_connect_request_from_dict = SalesforceConnectRequest.from_dict(salesforce_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


