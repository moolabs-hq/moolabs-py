# PTPCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promised_amount_micros** | **int** |  | 
**promised_date** | **date** |  | 
**captured_from_channel** | **str** |  | 
**captured_by** | **str** |  | 
**currency_code** | **str** |  | [optional] [default to 'USD']
**contact_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from moolabs.models.ptp_create_request import PTPCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PTPCreateRequest from a JSON string
ptp_create_request_instance = PTPCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PTPCreateRequest.to_json())

# convert the object into a dict
ptp_create_request_dict = ptp_create_request_instance.to_dict()
# create an instance of PTPCreateRequest from a dict
ptp_create_request_from_dict = PTPCreateRequest.from_dict(ptp_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


