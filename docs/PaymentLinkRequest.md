# PaymentLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**ptp_id** | **str** |  | 
**invoice_id** | **str** |  | 
**amount_usd** | **float** |  | 

## Example

```python
from moolabs.models.payment_link_request import PaymentLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkRequest from a JSON string
payment_link_request_instance = PaymentLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkRequest.to_json())

# convert the object into a dict
payment_link_request_dict = payment_link_request_instance.to_dict()
# create an instance of PaymentLinkRequest from a dict
payment_link_request_from_dict = PaymentLinkRequest.from_dict(payment_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


