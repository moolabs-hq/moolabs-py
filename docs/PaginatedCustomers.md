# PaginatedCustomers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**items** | [**List[CustomerItem]**](CustomerItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from moolabs.models.paginated_customers import PaginatedCustomers

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCustomers from a JSON string
paginated_customers_instance = PaginatedCustomers.from_json(json)
# print the JSON string representation of the object
print(PaginatedCustomers.to_json())

# convert the object into a dict
paginated_customers_dict = paginated_customers_instance.to_dict()
# create an instance of PaginatedCustomers from a dict
paginated_customers_from_dict = PaginatedCustomers.from_dict(paginated_customers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


