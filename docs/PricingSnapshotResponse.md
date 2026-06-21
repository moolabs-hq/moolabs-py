# PricingSnapshotResponse

Read-only projection of a persisted ``QuotePricingSnapshot``.  Served by ``GET /v1/quotes/pricing-snapshots/{snapshot_id}`` so the UI's Pricing tab can render totals + the rule trace after a quote is priced. Deliberately omits ``normalized_input`` (the pre-pricing input payload) — the UI never needs it and it can carry redaction-sensitive context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**pricing_snapshot_id** | **str** |  | 
**priced_output** | **Dict[str, object]** |  | 
**pricing_trace** | **Dict[str, object]** |  | 
**pricing_trace_digest** | **str** |  | 
**source_versions** | **Dict[str, object]** |  | 
**currency** | **str** |  | [optional] [default to 'USD']
**subtotal_micros** | **int** |  | 
**discount_micros** | **int** |  | 
**total_micros** | **int** |  | 

## Example

```python
from moolabs.models.pricing_snapshot_response import PricingSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSnapshotResponse from a JSON string
pricing_snapshot_response_instance = PricingSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(PricingSnapshotResponse.to_json())

# convert the object into a dict
pricing_snapshot_response_dict = pricing_snapshot_response_instance.to_dict()
# create an instance of PricingSnapshotResponse from a dict
pricing_snapshot_response_from_dict = PricingSnapshotResponse.from_dict(pricing_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


