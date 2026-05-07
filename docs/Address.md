# Address

Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country code in [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html) alpha-2 format. | [optional] 
**postal_code** | **str** | Postal code. | [optional] 
**state** | **str** | State or province. | [optional] 
**city** | **str** | City. | [optional] 
**line1** | **str** | First line of the address. | [optional] 
**line2** | **str** | Second line of the address. | [optional] 
**phone_number** | **str** | Phone number. | [optional] 

## Example

```python
from moolabs.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


