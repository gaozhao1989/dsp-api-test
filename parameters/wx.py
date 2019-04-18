import random
from utils import DataGenerator
from utils import PathParser

dg = DataGenerator()
pp = PathParser()

test_01_advertiser_add = [({'appid': 'wxd1de6b7bf1d874f9',
                            'system_industry_id': 2102,
                            'contact_person': 'test_contact_person',
                            'contact_person_telephone': '15880000001',
                            'business_type': '',
                            'business_content': '',
                            'sndo_ader_id': ''},
                           {'result': True,
                            'code': 0,
                            'msg': ''},
                           'add_advertiser')]

test_02_advertiser_update = [({'appid': 'wxd1de6b7bf1d874f9',
                               'system_industry_id': 2102,
                               'contact_person': 'test_contact_person',
                               'contact_person_telephone': '15880000001',
                               'business_type': '',
                               'business_content': ''},
                              {'result': True,
                               'code': 0,
                               'msg': ''},
                              'update_advertiser')]

test_01_qualifications_add = [({'appid': 'wxd1de6b7bf1d874f9',
                                'qualification_type': 'INDUSTRY_QUALIFICATION',
                                'qualification_name': 'test_qualification_name_{}'.format(dg.randint()),
                                'qualification_image_id': '9738853:93308213c445916a2acfa81425a643be'},
                               {'result': True,
                                'code': 0,
                                'msg': ''},
                               'add_qualification')]

test_02_qualifications_get = [({'appid': 'wxd1de6b7bf1d874f9'},
                               {'result': True,
                                'code': 0,
                                'msg': ''},
                               'get_qualification')]

test_03_qualifications_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'qualification_id': 'global variable'},
                                  {'result': True,
                                   'code': 0,
                                   'msg': ''},
                                  'delete_qualification')]

test_01_sp_entrustment_add = [({'appid': 'wxd1de6b7bf1d874f9'},
                               {'result': True,
                                'code': 0,
                                'msg': ''},
                               'add_sp_entrustment')]

test_02_sp_entrustment_get = [({'appid': 'wxd1de6b7bf1d874f9'},
                               {'result': True,
                                'code': 0,
                                'msg': ''},
                               'add_sp_entrustment')]

test_01_fund_transfer_add = [({'appid': 'wxd1de6b7bf1d874f9', 'fund_type': 'GENERAL_CASH', 'amount': 1, 'external_bill_no': 'sndo_test_{}{}'.format(dg.getdate(), dg.randint()), 'memo': 'test_transfer'},
                              {'result': True,
                               'code': 0,
                               'msg': ''},
                              'add_sp_entrustment')]

test_01_funds_get = [({'appid': 'wxd1de6b7bf1d874f9'},
                      {'result': True,
                       'code': 0,
                       'msg': ''},
                      'add_sp_entrustment')]

test_01_fund_statements_detailed_get = [({'appid': 'wxd1de6b7bf1d874f9', 'date_range': {'start_date': '2019-03-29',
                                                                                        'end_date': '2019-04-29'}, 'transaction_type': 'TRANSACTION_RECHARGE'},
                                         {'result': True,
                                          'code': 0,
                                          'msg': ''},
                                         'get_fund_statements_detailed')]

test_01_campaigns_add = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_name': 'test_campaign_name_{}'.format(dg.randint()), 'campaign_type': 'CAMPAIGN_TYPE_WECHAT_MOMENTS', 'product_type': 'PRODUCT_TYPE_LINK_WECHAT', 'configured_status': 'AD_STATUS_SUSPEND', 'daily_budget': '', 'sndo_ader_id': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'add_campaign')]

test_02_campaigns_get = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 41704869, 'filtering': '', 'page': '', 'page_size': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'get_campaign'),
                         ({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': '', 'filtering': '', 'page': '', 'page_size': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'get_all_campaign'),
                         ({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global variable', 'filtering': '', 'page': '', 'page_size': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'get_campaign')
                         ]

test_03_campaigns_update = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global variable', 'campaign_name': 'update_campaign_name_{}'.format(dg.randint()), 'configured_status': '', 'daily_budget': ''},
                             {'result': True,
                              'code': 0,
                              'msg': ''},
                             'update_campaign')]

test_04_campaigns_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global variable'},
                             {'result': True,
                              'code': 0,
                              'msg': ''},
                             'update_campaign')]

test_01_adgroups_add = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global variable',
                          'adgroup_name': 'test_adgroup_name_{}'.format(dg.randint()),
                          'site_set': ['SITE_SET_WECHAT'],
                          'product_type': 'PRODUCT_TYPE_LINK_WECHAT',
                          'targeting': {'age': ['15~25'],
                                        'geo_location':{'regions': [110000,
                                                                    310000],
                                                        'location_types':['LIVE_IN']}},
                          'optimization_goal': 'OPTIMIZATIONGOAL_IMPRESSION',
                          'billing_event': 'BILLINGEVENT_IMPRESSION',
                          'bid_amount': 12000,
                          'begin_date': '2019-03-27',
                          'end_date': '2019-04-25',
                          'time_series': ''.join([str(random.randint(0,
                                                                     1)) for x in range(48)]) * 7,
                          'daily_budget': 500000,
                          'product_refs_id': '',
                          'configured_status': 'AD_STATUS_SUSPEND',
                          'sndo_ader_id': ''},
                         {'result': True,
                          'code': 0,
                          'msg': ''},
                         'add_adgroup')]

test_02_adgroups_update = [({'appid': 'wxd1de6b7bf1d874f9', 'adgroup_id': 'global variable',
                             'adgroup_name': 'test_adgroup_name_{}'.format(dg.randint()),
                             'targeting': {'age': ['15~25'],
                                           'geo_location':{'regions': [110000,
                                                                       310000],
                                                           'location_types':['LIVE_IN']}},
                             'bid_amount': 12000,
                             'begin_date': '2019-03-27',
                             'end_date': '2019-04-25',
                             'time_series': ''.join([str(random.randint(0,
                                                                        1)) for x in range(48)]) * 7,
                             'daily_budget': 500000,
                             'configured_status': 'AD_STATUS_SUSPEND'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'update_adgroup')]

test_03_adgroups_get = [({'appid': 'wxd1de6b7bf1d874f9', 'adgroup_id': 'global variable',
                          'filtering': '',
                          'page': '',
                          'page_size': ''},
                         {'result': True,
                          'code': 0,
                          'msg': ''},
                         'get_adgroup')]

test_04_adgroups_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'adgroup_id': 'global variable'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'delete_adgroup')]

test_01_adcreatives_add = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global variable',
                             'adcreative_name': 'test_adcreative_name_{}'.format(dg.randint()),
                             'adcreative_template_id': 263,
                             'adcreative_elements': {
                                 'title': 'test_title_{}'.format(dg.randint()),
                                 'image_list': ['9738853:93308213c445916a2acfa81425a643be']},
                             'destination_url':'https://www.example.com',
                             'site_set':['SITE_SET_WECHAT'],
                             'product_type':'PRODUCT_TYPE_LINK_WECHAT',
                             'product_refs_id':'',
                             'share_info':'',
                             'sndo_ader_id':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_adcreative')]

test_02_adcreatives_update = [({'appid': 'wxd1de6b7bf1d874f9', 'adcreative_id': 'global variable',
                             'adcreative_name': 'update_adcreative_name_{}'.format(dg.randint()),
                             'adcreative_elements': {
                                 'title': 'update_title_{}'.format(dg.randint()),
                                 'image_list': ['9738853:93308213c445916a2acfa81425a643be']},
                             'destination_url':'https://www.example.com'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'update_adcreative')]

test_03_adcreatives_get = [({'appid': 'wxd1de6b7bf1d874f9', 'adcreative_id': 'global variable',
                             'filtering': '',
                             'page': '',
                             'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_adcreative'),
                            ({'appid': 'wxd1de6b7bf1d874f9',
                             'filtering': '',
                             'page': '',
                             'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_all_adcreative')]

test_04_adcreatives_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'adcreative_id': 'global variable'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'delete_adcreative')]

test_01_ads_add = [({'appid': 'wxd1de6b7bf1d874f9', 'adgroup_id': 'global variable',
                             'adcreative_id': 'global variable',
                             'ad_name': 'test_ad_name_{}'.format(dg.randint()),
                             'configured_status': 'AD_STATUS_SUSPEND',
                             'sndo_ader_id':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_ad')]
test_02_ads_update = [({'appid': 'wxd1de6b7bf1d874f9', 'ad_id': 'global variable',
                             'ad_name': 'update_ad_name_{}'.format(dg.randint()),
                             'configured_status': 'AD_STATUS_SUSPEND'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'update_ad')]
test_03_ads_get = [({'appid': 'wxd1de6b7bf1d874f9', 'ad_id': 'global variable',
                             'filtering': '',
                             'page': '',
                             'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_ad'),
                            ({'appid': 'wxd1de6b7bf1d874f9',
                             'filtering': '',
                             'page': '',
                             'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_all_ad')]                                                        
test_04_ads_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'ad_id': 'global variable'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'delete_ad')]
test_01_images_add = [({'appid': 'wxd1de6b7bf1d874f9', 'image': dg.drawimage()},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_image')]

test_02_images_get = [({'appid': 'wxd1de6b7bf1d874f9', 'image_id': 'global variable',
'filtering':'','page':'','page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_image'),
                            ({'appid': 'wxd1de6b7bf1d874f9', 
'filtering':'','page':'','page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_all_image')]

test_01_custom_audiences_add = [({'appid': 'wxd1de6b7bf1d874f9', 'name': 'test_name_{}'.format(dg.randint()),
'type':'CUSTOMER_FILE','description':'test_description_{}'.format(dg.randint())},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_custom_audiences')]

test_02_custom_audiences_update = [({'appid': 'wxd1de6b7bf1d874f9','audience_id':'global variable', 'name': 'update_name_{}'.format(dg.randint()),
'type':'CUSTOMER_FILE','description':'update_description_{}'.format(dg.randint())},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'update_custom_audiences')]       
test_03_custom_audiences_get = [({'appid': 'wxd1de6b7bf1d874f9','audience_id':'global variable', 'page': '',
'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_custom_audiences'),
                            ({'appid': 'wxd1de6b7bf1d874f9', 'page': '',
'page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_all_custom_audiences')]  
test_01_custom_audience_files_add = [({'appid': 'wxd1de6b7bf1d874f9', 'file': pp.path_join(pp.current_path(),'misc/audiencefile.zip'),'user_id_type':'QQ','operation_type':'APPEND','audience_id':'global variable'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_custom_audience_file')]    
test_02_custom_audience_files_get = [({'appid': 'wxd1de6b7bf1d874f9', 'custom_audience_file_id': 'global variable','audience_id':'','page':'','page_size':''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_custom_audience_file')]                                                                                                        
test_01_daily_reports_get = [
    ({
            'appid': 'wxd1de6b7bf1d874f9',
            'report_type': 'MOMENTS_REPORT',
            'level': 'CAMPAIGN',
            'date_range': {'start_date': '2019-03-29',
                               'end_date': '2019-03-31'},
            'page': '',
            'page_size': ''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_daily_report')
]

test_01_realtime_cost_get=[
        ({
            'appid': 'wxd1de6b7bf1d874f9',
            'level': 'ADGROUP',
            'date': '2019-03-25',
            'filtering': ''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_realtime_cost')
]

test_01_estimation_get =[
    ({
            'appid': 'wxd1de6b7bf1d874f9',
            'campaign_type': 'CAMPAIGN_TYPE_WECHAT_MOMENTS',
            'targeting': {
            'geo_location': {
                'location_types': ['RECENTLY_IN'],
                'regions':[510100]
            }
        }},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'get_estimation')
]

test_01_adcreatives2_add =[
    ({
            'appid': 'wxd1de6b7bf1d874f9',
            'campaign_id': 'global variable',
            'adcreative_name': 'test_adcreative_name_{}'.format(dg.randint()),
            'adcreative_template_id': 263,
            'adcreative_elements': {
                                 'title': 'test_title_{}'.format(dg.randint()),
                                 'image_list': ['9738853:93308213c445916a2acfa81425a643be']},
            'destination_url': 'https://www.testexample.com',
            'site_set':['SITE_SET_WECHAT'],
            'product_type':'PRODUCT_TYPE_LINK_WECHAT',
            'product_refs_id': '',
            'share_info': '',
            'adgroup_id': 'global variable',
            'ad_name': 'test_ad_name_{}'.format(dg.randint()),
            'configured_status': 'AD_STATUS_SUSPEND',
            'sndo_ader_id': ''},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'add_adcreatives2')
]

test_02_adcreatives2_update =[
    ({
            'appid': 'wxd1de6b7bf1d874f9',
            'adcreative_id': 'global variable',
            'adcreative_name': 'update_adcreative_name_{}'.format(dg.randint()),
            'adcreative_elements': {
                                 'title': 'test_title_{}'.format(dg.randint()),
                                 'image_list': ['9738853:93308213c445916a2acfa81425a643be']},
            'destination_url': 'https://www.updateexample.com',
            'ad_id': 'global variable',
            'ad_name': 'update_ad_name_{}'.format(dg.randint()),
            'configured_status': 'AD_STATUS_SUSPEND'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'update_adcreatives2')
]

test_03_adcreatives2_delete =[
    ({
            'appid': 'wxd1de6b7bf1d874f9',
            'adcreative_id': 'global variable',
            'ad_id': 'global variable'},
                            {'result': True,
                             'code': 0,
                             'msg': ''},
                            'delete_adcreatives2')
]