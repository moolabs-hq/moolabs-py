# PortalPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**amount_micros** | **int** |  | 
**payment_method** | **str** |  | [optional] [default to 'stripe']

## Example

```python
from moolabs.models.portal_payment_request import PortalPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortalPaymentRequest from a JSON string
portal_payment_request_instance = PortalPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PortalPaymentRequest.to_json())

# convert the object into a dict
portal_payment_request_dict = portal_payment_request_instance.to_dict()
# create an instance of PortalPaymentRequest from a dict
portal_payment_request_from_dict = PortalPaymentRequest.from_dict(portal_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


