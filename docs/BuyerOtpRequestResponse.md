# BuyerOtpRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**otp_id** | **str** |  | 
**expires_at** | **str** |  | 

## Example

```python
from moolabs.models.buyer_otp_request_response import BuyerOtpRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerOtpRequestResponse from a JSON string
buyer_otp_request_response_instance = BuyerOtpRequestResponse.from_json(json)
# print the JSON string representation of the object
print(BuyerOtpRequestResponse.to_json())

# convert the object into a dict
buyer_otp_request_response_dict = buyer_otp_request_response_instance.to_dict()
# create an instance of BuyerOtpRequestResponse from a dict
buyer_otp_request_response_from_dict = BuyerOtpRequestResponse.from_dict(buyer_otp_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


