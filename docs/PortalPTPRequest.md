# PortalPTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**promised_amount_micros** | **int** |  | 
**promised_date** | **date** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']

## Example

```python
from moolabs.models.portal_ptp_request import PortalPTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortalPTPRequest from a JSON string
portal_ptp_request_instance = PortalPTPRequest.from_json(json)
# print the JSON string representation of the object
print(PortalPTPRequest.to_json())

# convert the object into a dict
portal_ptp_request_dict = portal_ptp_request_instance.to_dict()
# create an instance of PortalPTPRequest from a dict
portal_ptp_request_from_dict = PortalPTPRequest.from_dict(portal_ptp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


