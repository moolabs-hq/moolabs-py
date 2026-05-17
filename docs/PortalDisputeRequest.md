# PortalDisputeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**disputed_amount_micros** | **int** |  | 
**description** | **str** |  | 
**case_id** | **str** | Case ID to disambiguate when invoice_id exists in multiple cases | [optional] 

## Example

```python
from moolabs.models.portal_dispute_request import PortalDisputeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortalDisputeRequest from a JSON string
portal_dispute_request_instance = PortalDisputeRequest.from_json(json)
# print the JSON string representation of the object
print(PortalDisputeRequest.to_json())

# convert the object into a dict
portal_dispute_request_dict = portal_dispute_request_instance.to_dict()
# create an instance of PortalDisputeRequest from a dict
portal_dispute_request_from_dict = PortalDisputeRequest.from_dict(portal_dispute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


