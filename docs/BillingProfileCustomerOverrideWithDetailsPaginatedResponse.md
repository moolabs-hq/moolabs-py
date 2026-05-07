# BillingProfileCustomerOverrideWithDetailsPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[BillingProfileCustomerOverrideWithDetails]**](BillingProfileCustomerOverrideWithDetails.md) | The items in the current page. | 

## Example

```python
from moolabs.models.billing_profile_customer_override_with_details_paginated_response import BillingProfileCustomerOverrideWithDetailsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCustomerOverrideWithDetailsPaginatedResponse from a JSON string
billing_profile_customer_override_with_details_paginated_response_instance = BillingProfileCustomerOverrideWithDetailsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCustomerOverrideWithDetailsPaginatedResponse.to_json())

# convert the object into a dict
billing_profile_customer_override_with_details_paginated_response_dict = billing_profile_customer_override_with_details_paginated_response_instance.to_dict()
# create an instance of BillingProfileCustomerOverrideWithDetailsPaginatedResponse from a dict
billing_profile_customer_override_with_details_paginated_response_from_dict = BillingProfileCustomerOverrideWithDetailsPaginatedResponse.from_dict(billing_profile_customer_override_with_details_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


