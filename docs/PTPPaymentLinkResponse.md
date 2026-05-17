# PTPPaymentLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**session_id** | **str** |  | 

## Example

```python
from moolabs.models.ptp_payment_link_response import PTPPaymentLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PTPPaymentLinkResponse from a JSON string
ptp_payment_link_response_instance = PTPPaymentLinkResponse.from_json(json)
# print the JSON string representation of the object
print(PTPPaymentLinkResponse.to_json())

# convert the object into a dict
ptp_payment_link_response_dict = ptp_payment_link_response_instance.to_dict()
# create an instance of PTPPaymentLinkResponse from a dict
ptp_payment_link_response_from_dict = PTPPaymentLinkResponse.from_dict(ptp_payment_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


