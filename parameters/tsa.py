import random

from utils import DataGenerator

dg = DataGenerator()

test_01_ind_get = [({},
                    {'result': True,
                     'code': 0,
                     'msg': ''},
                    'ind_list')]

test_01_qua_get = [({},
                    {'result': True,
                     'code': 0,
                     'msg': ''},
                    'qua_list')]

test_01_adcreative_templates_get = [({'account_id': 100006180, 'page': '', 'page_size': '', 'site_set': '', 'promoted_object_type': '', 'filtering': ''},
                                     {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                     'get_adcreative_templates')]

test_01_advertiser_add = [({'corporation_name': 'test_corportaion_name_{}'.format(dg.randint()), 'certification_image_id': '3670', 'system_industry_id': 21474836581, 'introduction_url': '', 'individual_qualification': '', 'corporate_image_name': '', 'contact_person_telephone': '', 'contact_person_mobile': '', 'certification_number': '', 'sndo_ader_id': ''},
                           {'result': True,
                            'code': 0,
                            'msg': ''},
                           'add_advertiser')]

test_02_advertiser_update = [({'account_id': 'global variable', 'daily_budget': '', 'corporation_name': 'update_corportaion_name_{}'.format(dg.randint()), 'certification_image_id': '', 'system_industry_id': '', 'introduction_url': '', 'individual_qualification': '', 'corporate_image_name': '', 'contact_person_telephone': '', 'contact_person_mobile': '', 'wechat_spec': '', 'websites': ''},
                              {'result': True,
                               'code': 0,
                               'msg': ''},
                              'update_advertiser')]

test_03_advertiser_get = [({'account_id': 100006180, 'page': '', 'page_size': '', 'filtering': ''},
                           {'result': True,
                            'code': 0,
                            'msg': ''},
                           'get_advertiser'),
                          ({},
                           {'result': True,
                            'code': 0,
                            'msg': ''},
                           'get_all_advertiser')]

test_01_qualifications_add = [({'account_id': 100006180, 'qualification_type': 'INDUSTRY_QUALIFICATION', 'qualification_spec': {'industry_spec': {'system_industry_id': 21474836586,
                                                                                                                                                  'qualification_code': 'A150', 'image_id_list': ['3512']}}},
                               {'result': True,
                                'code': 0,
                                'msg': ''},
                               'add_qualification')]

test_02_qualifications_update = [({'account_id': 100006180, 'qualification_type': 'INDUSTRY_QUALIFICATION', 'qualification_id': 'global variable', 'image_id_list': ['3517']},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'update_qualification')]

test_03_qualifications_get = [({
    'account_id': 100006180,
    'qualification_type': 'INDUSTRY_QUALIFICATION',
    'filtering': '',
    'fields': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_qualification')]

test_04_qualifications_delete = [({
            'account_id': 100006180,
            'qualification_type': 'INDUSTRY_QUALIFICATION',
            'qualification_id': 'global variable'},
    {'result': True,
     'code': 0,
     'msg': ''},
    'delete_qualification')]    

test_01_campaigns_add = [({
            'account_id': 100006180,
            'campaign_name': 'test_campaign_name_{}'.format(dg.randint()),
            'campaign_type': 'CAMPAIGN_TYPE_NORMAL',
            'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
            'daily_budget': 100000,
            'configured_status': 'AD_STATUS_SUSPEND',
            'speed_mode': '',
            'sndo_ader_id': ''},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'add_campaign')]   

test_02_campaigns_update = [({
            'account_id': 100006180,
            'campaign_id': 'global variable',
            'campaign_name': 'update_campaign_name_{}'.format(dg.randint()),
            'daily_budget': '',
            'configured_status': '',
            'speed_mode': '',
            'promoted_object_type': ''},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'update_campaign')]

test_03_campaigns_get = [({
            'account_id': 100006180,
            'filtering': '',
            'page': '',
            'page_size': ''
        },
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'get_campaign')]

test_04_campaigns_delete = [({
            'account_id': 100006180,
            'campaign_id': 'global variable'
        },
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'delete_campaign')]

test_01_adgroups_add = [({
            'account_id': 100006180,
            'campaign_id': 'global variable',
            'adgroup_name': 'test_adgroup_name_{}'.format(dg.randint()),
            'site_set': ['SITE_SET_QZONE'],
            'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
            'begin_date': '2019-03-07',
            'end_date': '',
            'billing_event': 'BILLINGEVENT_CLICK',
            'bid_amount': 1000,
            'optimization_goal': 'OPTIMIZATIONGOAL_CLICK',
            'targeting_id': 97522,
            'time_series': ''.join([str(random.randint(0, 1)) for x in range(336)])},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'add_adgroup')]

test_02_adgroups_update = [({
            'account_id': 100006180,
            'adgroup_id':'global variable',
            'adgroup_name': 'update_adgroup_name_{}'.format(dg.randint()),
            'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
            'begin_date': '2019-03-07',
            'end_date': '',
            'billing_event': 'BILLINGEVENT_CLICK',
            'bid_amount': 1000,
            'optimization_goal': 'OPTIMIZATIONGOAL_CLICK',
            'targeting_id': 97522,
            'time_series': ''.join([str(random.randint(0, 1)) for x in range(336)])},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'update_adgroup')] 

test_03_adgroups_get = [({
            'account_id': 100006180,
            'filtering': '',
            'page': '',
            'page_size': ''
        },
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'get_adgroup')]

test_04_adgroups_delete = [({
            'account_id': 100006180,
            'adgroup_id': 'global variable'
        },
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'delete_adgroup')]

test_01_ads_add = [({
            'account_id': 100006180,
            'adgroup_id': 'global variable',
            'adcreative_id': 'global variable',
            'ad_name': 'test_ad_name_{}'.format(gd.randint()),
            'configured_status': '',
            'impression_tracking_url': '',
            'click_tracking_url': '',
            'feeds_interaction_enabled': '',
            'sndo_ader_id': ''},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'add_ad')]



test_01_adcreatives_add = [({
            'account_id': 100006180,
            'campaign_id': 'global variable',
            'adcreative_name': 'test_adcreative_name_{}'.format(gd.randint()),
            'adcreative_template_id': 529,
            'adcreative_elements': {'image': '3519', 'title': 'test_title_'.format(gd.randint())},
            'site_set': ['SITE_SET_QQCLIENT'],
            'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
            'page_type': 'PAGE_TYPE_DEFAULT',
            'page_spec': '',
            'deep_link_url':'',
            'promoted_object_id':'',
            'share_content_spec':'',
            'dynamic_adcreative_spec':'',
            'multi_share_optimization_enabled':'',
            'sndo_ader_id':''},
                                  {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                  'add_adcreative')]

test_01_images_add = [
    (100006180, 'C:/Users/SNQU/Pictures/github200x200Discount.jpg',
     True, 0, '', 'create_image')
]

test_02_advertiser_add = [
    ('test0326001', '3670', 21474836581, '', '', '',
     '', '', '', '', '', True, 0, '', 'create_account')
]

test_03_campaigns_add = [
    (100006180, 'api_test_plan', 'CAMPAIGN_TYPE_NORMAL', 'PROMOTED_OBJECT_TYPE_LINK', 100000,
     'AD_STATUS_SUSPEND', '', '', True, 0, '', 'create_campaign')
]

test_04_adgroups_add = [
    (100006180, 29131, 'test_group', ['SITE_SET_QZONE'], 'PROMOTED_OBJECT_TYPE_LINK', '2019-03-07', '', 'BILLINGEVENT_CLICK', 1000, 'OPTIMIZATIONGOAL_CLICK', 97522,
     ''.join([str(random.randint(0, 1)) for x in range(336)]), True, 0, '', 'create_adgroup')
]

test_05_adcreatives2_add = [
    (100006180, 29131, 'test_adcreative_name', 529, {'image': '3519', 'title': 'test title'}, ['SITE_SET_QQCLIENT'], {
     'page_id': 0, 'page_url': 'https://www.qq.com'}, 'PROMOTED_OBJECT_TYPE_LINK', 'PAGE_TYPE_DEFAULT', 41887, 'test_ad_name', 'AD_STATUS_SUSPEND', True, 0, '', 'create_adcreatives')
]

test_06_promoted_objects_add = [
    (100006180, 'PROMOTED_OBJECT_TYPE_APP_IOS',
     '1456102515', True, 0, '', 'create_promoted_objects')
]

test_07_targeting_add = [
    (100006180, 'targeting_name_{}'.format(random.randint(
        1000, 9999)), True, 0, '', 'create_targeting')
]

test_08_advertiser_get = [
    ('', '', '', '', True, 0, '', 'get_advertiser_all'),
    (100006180, '', '', '', True, 0, '', 'get_advertiser_by_account_id'),
]

test_09_campaigns_get = [
    (100006180, '', '', '', True, 0, '', 'get_campaigns_by_account_id'),
]

test_10_images_get = [
    (100006180, '', '', '', True, 0, '', 'get_images_by_account_id'),
]

test_11_targeting_get = [
    (100006180, '', '', '', True, 0, '', 'get_targeting_by_account_id'),
]

test_12_estimation_get = [
    (100006180, '', '', {'geo_location': {'location_types': [
     'RECENTLY_IN'], 'regions':[510100]}}, True, 0, '', 'get_estimation_by_account_id_and_targeting'),
]

test_13_ads_add = [
    (100006180, 41869, 64019, 'test_ad_{}'.format(random.randint(
        1000, 9999)), '', '', '', '', '', True, 0, '', 'create_add'),
]

test_14_adgroups_get = [
    (100006180, '', '', '', True, 0, '', 'get_adgroups_by_account_id'),
]

test_15_adcreatives_get = [
    (100006180, '', '', '', True, 0, '', 'get_adcreatives_by_account_id'),
]

test_16_adcreative_templates_get = [
    (100006180, '', '', '', '', '', True, 0, '',
     'get_adcreative_templates_by_account_id'),
]

test_17_funds_get = [
    (100006180, True, 0, '', 'get_adcreatives_by_account_id'),
]

test_18_fund_transfer_add = [
    (100006180, 'FUND_TYPE_CASH', 5000, 'AGENCY_TO_ADVERTISER',
     '', '', True, 0, '', 'fund_transfer_add')
]

test_19_ads_get = [
    (100006180, True, 0, '', 'get_ads_by_account_id'),
]

test_20_qualifications_get = [
    (1553568843, 'INDUSTRY_QUALIFICATION', '', '',
     True, 0, '', 'get_qualifications_by_account_id')
]

test_21_qualifications_delete = [
    (1553568843, 'INDUSTRY_QUALIFICATION', 10009282,
     True, 0, '', 'delete_qualifications')
]

test_22_qualifications_add = [
    (1553568843, 'INDUSTRY_QUALIFICATION', {'industry_spec': {'system_industry_id': 21474836586,
                                                              'qualification_code': 'A150', 'image_id_list': ['3512']}}, True, 0, '', 'delete_qualifications')
]

test_23_adcreatives2_delete = [
    (100006180, 63651, 35997, True, 0, '', 'delete_adcreatives')
]

test_24_qualifications_update = [
    (1553568843, 'INDUSTRY_QUALIFICATION', 10009283,
     ["3517"], True, 0, '', 'delete_adcreatives')
]
