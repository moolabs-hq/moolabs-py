# BuyerOtpVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**otp_id** | **str** |  | 

## Example

```python
from moolabs.models.buyer_otp_verify_response import BuyerOtpVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerOtpVerifyResponse from a JSON string
buyer_otp_verify_response_instance = BuyerOtpVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(BuyerOtpVerifyResponse.to_json())

# convert the object into a dict
buyer_otp_verify_response_dict = buyer_otp_verify_response_instance.to_dict()
# create an instance of BuyerOtpVerifyResponse from a dict
buyer_otp_verify_response_from_dict = BuyerOtpVerifyResponse.from_dict(buyer_otp_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


