# BuyerOtpVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from moolabs.models.buyer_otp_verify_request import BuyerOtpVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerOtpVerifyRequest from a JSON string
buyer_otp_verify_request_instance = BuyerOtpVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(BuyerOtpVerifyRequest.to_json())

# convert the object into a dict
buyer_otp_verify_request_dict = buyer_otp_verify_request_instance.to_dict()
# create an instance of BuyerOtpVerifyRequest from a dict
buyer_otp_verify_request_from_dict = BuyerOtpVerifyRequest.from_dict(buyer_otp_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


