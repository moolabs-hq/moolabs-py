# CustomerUpsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netsuite_customer_id** | **str** |  | 
**moometer_customer_id** | **str** |  | 
**company_name** | **str** |  | 
**customer_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] [default to 'USD']
**status** | **str** |  | [optional] [default to 'active']
**source_updated_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.customer_upsert_request import CustomerUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerUpsertRequest from a JSON string
customer_upsert_request_instance = CustomerUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerUpsertRequest.to_json())

# convert the object into a dict
customer_upsert_request_dict = customer_upsert_request_instance.to_dict()
# create an instance of CustomerUpsertRequest from a dict
customer_upsert_request_from_dict = CustomerUpsertRequest.from_dict(customer_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


