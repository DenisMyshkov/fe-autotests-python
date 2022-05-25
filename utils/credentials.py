user_name = ''
user_password = ''
bearer = ''
ae_buyer_id = {"gw0": {"id": , "cart": },
               "gw1": {"id": , "cart": },
               "gw2": {"id": , "cart": },
               "gw3": {"id": , "cart": },
               "gw4": {"id": , "cart": }}
ae_buyer_id_for_one_store = ''
belyuga_test_card = ['']
test_card = ['']
random_card = ['']
test_url = ''
pepsi_address = '{"place_id":"ChIJPS7JY8-0SkERRPAdgiVJud0","address":{"country":"Россия","region":"Москва",' \
                '"city":"Москва","street":"улица Трофимова","house":"25","geo_point":{"latitude":55.70283120000001,' \
                '"longitude":37.6782566}}}'
novatorov_address = '{"place_id":"ElbQsdGD0LvRjNCy0LDRgCDQndC-0LLQsNGC0L7RgNC' \
                    '-0LIsINC0LiAxMCwg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LMsINCg0L7RgdGB0LjRjyJQEk4KNAoyCY94f' \
                    '-ToOpZGEcWNcSZxy1ONGh4LEO7B7qEBGhQKEglB1oJTlTqWRhHJAX5VU16TFAwQCioUChIJG8QQx-U6lkYR2mp35gpJc5c",' \
                    '"address":{"country":"Россия","region":"Санкт-Петербург",' \ 
                    '"city":"Санкт-Петербург","street":"бульвар Новаторов","house":"10","geo_point":{' \
                    '"latitude":59.84954911,"longitude":30.26949}}}'
only_pharma_address = '{"place_id":"ChIJq2iwbqtz7kARdAEP-5FwrNo","address":{"country":"Россия",' \
                      '"region":"Краснодарский край",' \ 
                      '"city":"Витязево","street":"Центральная улица","house":"Витязево","geo_point":{' \
                      '"latitude":44.98354,"longitude":37.2696037}}}'
clear_cart = {
    'url': '',
    'data': f"{{'cart_id':,'ae_buyer_id':{ae_buyer_id}}}",
    'headers': {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json'}
}

is_not_adult = {
    'url': '',
    'data': '{\"is_adult\":false}',
    'headers': {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json',
        'x-user-id': f'{ae_buyer_id}'}
}
