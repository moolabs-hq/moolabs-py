# StripeAppReadOrCreateOrUpdateOrDeleteOrQuery

A installed Stripe app object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**listing** | [**MarketplaceListing**](MarketplaceListing.md) | The marketplace listing that this installed app is based on. | [readonly] 
**status** | [**AppStatus**](AppStatus.md) | Status of the app connection. | [readonly] 
**type** | **str** | The app&#39;s type is Stripe. | 
**stripe_account_id** | **str** | The Stripe account ID. | [readonly] 
**livemode** | **bool** | Livemode, true if the app is in production mode. | [readonly] 
**masked_api_key** | **str** | The masked API key. Only shows the first 8 and last 3 characters. | [readonly] 
**secret_api_key** | **str** | The Stripe API key. | [optional] 

## Example

```python
from moolabs.models.stripe_app_read_or_create_or_update_or_delete_or_query import StripeAppReadOrCreateOrUpdateOrDeleteOrQuery

# TODO update the JSON string below
json = "{}"
# create an instance of StripeAppReadOrCreateOrUpdateOrDeleteOrQuery from a JSON string
stripe_app_read_or_create_or_update_or_delete_or_query_instance = StripeAppReadOrCreateOrUpdateOrDeleteOrQuery.from_json(json)
# print the JSON string representation of the object
print(StripeAppReadOrCreateOrUpdateOrDeleteOrQuery.to_json())

# convert the object into a dict
stripe_app_read_or_create_or_update_or_delete_or_query_dict = stripe_app_read_or_create_or_update_or_delete_or_query_instance.to_dict()
# create an instance of StripeAppReadOrCreateOrUpdateOrDeleteOrQuery from a dict
stripe_app_read_or_create_or_update_or_delete_or_query_from_dict = StripeAppReadOrCreateOrUpdateOrDeleteOrQuery.from_dict(stripe_app_read_or_create_or_update_or_delete_or_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


