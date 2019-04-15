import random
from utils import DataGenerator

dg = DataGenerator()

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

test_03_qualifications_delete = [({'appid': 'wxd1de6b7bf1d874f9', 'qualification_id': 'global_var'},
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
                          ({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global_var', 'filtering': '', 'page': '', 'page_size': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'get_campaign')
                          ]    

test_03_campaigns_update = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global_var', 'campaign_name': 'update_campaign_name_{}'.format(dg.randint()), 'configured_status': '', 'daily_budget': ''},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'update_campaign')]

test_04_campaigns_delete =[({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global_var'},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'update_campaign')]

test_01_adgroups_add = [({'appid': 'wxd1de6b7bf1d874f9', 'campaign_id': 'global_var'},
                          {'result': True,
                           'code': 0,
                           'msg': ''},
                          'update_campaign')]                          

test_03_advertiser_get = [
    ({'appid': 'wxd1de6b7bf1d874f9'},
     {'result': True, 'code': 0, 'msg': ''},
     'get_advertiser_by_appid')
]

test_01_advertiser_get = [
    ({'appid': 'wxd1de6b7bf1d874f9'},
     {'result': True, 'code': 0, 'msg': ''},
     'get_advertiser_by_appid')
]

test_02_ads_get = [
    ('wxd1de6b7bf1d874f9',
     True, 0, '', 'get_ads_by_appid')
]

test_03_sp_entrustment_add = [
    ('wxd1de6b7bf1d874f9',
     True, 0, '', 'create_sp_entrustment')
]

test_04_sp_entrustment_get = [
    ('wxd1de6b7bf1d874f9',
     True, 0, '', 'get_sp_entrustment_by_appid')
]

test_05_campaigns_add = [
    ('wxd1de6b7bf1d874f9',
     'test_campaign_name_{}'.format(
         random.randint(
             1000,
             9999)),
     'CAMPAIGN_TYPE_WECHAT_MOMENTS',
     'PRODUCT_TYPE_LINK_WECHAT',
     'AD_STATUS_SUSPEND',
     '',
     '',
     True,
     0,
     '',
     'create_campaign')]

test_06_campaigns_get = [
    ('wxd1de6b7bf1d874f9', 41704869, '', '', '',
     True, 0, '', 'get_all_campaign'),
    ('wxd1de6b7bf1d874f9', '', '', '', '',
     True, 0, '', 'get_all_campaign')
]

test_07_campaigns_update = [
    ('wxd1de6b7bf1d874f9', 41704869, '', '', '',
     True, 0, '', 'update_campaign')
]

test_08_campaigns_delete = [
    ('wxd1de6b7bf1d874f9', 41703265,
     True, 0, '', 'delete_campaigns')
]

test_09_adgroups_add = [('wxd1de6b7bf1d874f9',
                         41704869,
                         'test_adgroup_name_{}'.format(random.randint(1000,
                                                                      9999)),
                         ["SITE_SET_WECHAT"],
                         'PRODUCT_TYPE_LINK_WECHAT',
                         {'age': ['15~25'],
                          'geo_location':{'regions': [110000,
                                                      310000],
                                          'location_types':['LIVE_IN']}},
                         'OPTIMIZATIONGOAL_IMPRESSION',
                         'BILLINGEVENT_IMPRESSION',
                         12000,
                         '2019-03-27',
                         '2019-04-25',
                         ''.join([str(random.randint(0,
                                                     1)) for x in range(48)]) * 7,
                         500000,
                         '',
                         'AD_STATUS_SUSPEND',
                         '',
                         True,
                         0,
                         '',
                         'create_adgroup')]

test_10_images_add = [
    ('wxd1de6b7bf1d874f9', 'C:/Users/SNQU/Pictures/github200x200Discount.jpg',
     True, 0, '', 'create_image')
]

test_11_images_get = [
    ('wxd1de6b7bf1d874f9', '', '', '',
     True, 0, '', 'get_image')
]

test_12_adcreatives2_add = [
    ('wxd1de6b7bf1d874f9',
     41704869,
     'test_adcreative_name_{}'.format(
         random.randint(
             1000,
             9999)),
     263,
     {
         'title': 'test_title',
         'image_list': ['9738853:93308213c445916a2acfa81425a643be']},
     'https://www.example.com',
     ["SITE_SET_WECHAT"],
     'PRODUCT_TYPE_LINK_WECHAT',
     '',
     '',
     113228326,
     'test_ad_name_{}'.format(
         random.randint(
             1000,
             9999)),
     'AD_STATUS_SUSPEND',
     '',
     True,
     0,
     '',
     'create_adcreatives2')]

test_13_funds_get = [
    ('wxd1de6b7bf1d874f9',
     True, 0, '', 'get_funds_by_appid')
]


test_14_fund_statements_detailed_get = [
    ('wxd1de6b7bf1d874f9',
     'TRANSACTION_RECHARGE',
     {
         'start_date': '2019-03-29',
         'end_date': '2019-03-29'},
        True,
        0,
        '',
     'get_fund_statements_detailed_by_appid')]

test_15_daily_reports_get = [('wxd1de6b7bf1d874f9',
                              'MOMENTS_REPORT',
                              'CAMPAIGN',
                              {'start_date': '2019-03-29',
                               'end_date': '2019-03-31'},
                              '',
                              '',
                              True,
                              0,
                              '',
                              'get_daily_report_by_appid')]

test_16_fund_transfer_add = [
    ('wxd1de6b7bf1d874f9', 'GENERAL_CASH', 1, 'test_transfer', 'test_transfer',
     True, 0, '', 'get_funds_by_appid')
]
