from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

address = '360 HENDERSON DRIVE,SAN JOSE,CA'
zipcode = '95123'

zillow_data = ZillowWrapper("X1-ZWz1ewrfwub6rv_aj9j5")
deep_search_response = zillow_data.get_deep_search_results('360 HENDERSON DRIVE,SAN JOSE,CA', '95123')
result = GetDeepSearchResults(deep_search_response)
result

result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails
