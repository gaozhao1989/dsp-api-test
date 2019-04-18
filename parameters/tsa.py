import random

from utils import DataGenerator
from utils import PathParser

dg = DataGenerator()
pp = PathParser()

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

test_01_adcreative_templates_get = [({'account_id': 'global variable',
                                      'page': '',
                                      'page_size': '',
                                      'site_set': '',
                                      'promoted_object_type': '',
                                      'filtering': ''},
                                     {'result': True,
                                      'code': 0,
                                      'msg': ''},
                                     'get_adcreative_templates')]

test_01_advertiser_add = [
    ({
        'corporation_name': 'test_corportaion_name_{}'.format(
            dg.randint()),
        'certification_image_id': '2873',
        'system_industry_id': 21474836581,
        'introduction_url': '',
        'individual_qualification': '',
        'corporate_image_name': '',
        'contact_person_telephone': '',
        'contact_person_mobile': '',
        'certification_number': '',
        'sndo_ader_id': ''},
     {
        'result': True,
        'code': 0,
        'msg': ''},
     'add_advertiser')]

test_02_advertiser_update = [({'account_id': 'global variable',
                               'daily_budget': '',
                               'corporation_name': 'update_corportaion_name_{}'.format(dg.randint()),
                               'certification_image_id': '',
                               'system_industry_id': '',
                               'introduction_url': '',
                               'individual_qualification': '',
                               'corporate_image_name': '',
                               'contact_person_telephone': '',
                               'contact_person_mobile': '',
                               'wechat_spec': '',
                               'websites': ''},
                              {'result': True,
                               'code': 0,
                               'msg': ''},
                              'update_advertiser')]

test_03_advertiser_get = [
    ({
        'account_id': 'global variable', 'page': '', 'page_size': '', 'filtering': ''}, {
            'result': True, 'code': 0, 'msg': ''}, 'get_advertiser'), ({}, {
                'result': True, 'code': 0, 'msg': ''}, 'get_all_advertiser')]

test_01_qualifications_add = [
    ({
        'account_id': 'global variable',
        'qualification_type': 'INDUSTRY_QUALIFICATION',
        'qualification_spec': {
            'industry_spec': {
                'system_industry_id': 21474836581,
                'qualification_code': 'A150',
                'image_id_list': ['global variable']}}},
     {
        'result': True,
        'code': 0,
        'msg': ''},
     'add_qualification')]

test_02_qualifications_update = [({'account_id': 'global variable',
                                   'qualification_type': 'INDUSTRY_QUALIFICATION',
                                   'qualification_id': 'global variable',
                                   'image_id_list': ['global variable']},
                                  {'result': True,
                                   'code': 0,
                                   'msg': ''},
                                  'update_qualification')]

test_03_qualifications_get = [({
    'account_id': 'global variable',
    'qualification_type': 'INDUSTRY_QUALIFICATION',
    'filtering': '',
    'fields': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_qualification')]

test_04_qualifications_delete = [({
    'account_id': 'global variable',
    'qualification_type': 'INDUSTRY_QUALIFICATION',
    'qualification_id': 'global variable'},
    {'result': True,
     'code': 0,
     'msg': ''},
    'delete_qualification')]

test_01_campaigns_add = [({
    'account_id': 'global variable',
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
    'account_id': 'global variable',
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
    'account_id': 'global variable',
    'filtering': '',
    'page': '',
            'page_size': ''
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_campaign')]

test_04_campaigns_delete = [({
    'account_id': 'global variable',
    'campaign_id': 'global variable'
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'delete_campaign')]

test_01_adgroups_add = [({
    'account_id': 'global variable',
    'campaign_id': 'global variable',
    'adgroup_name': 'test_adgroup_name_{}'.format(dg.randint()),
    'site_set': ['SITE_SET_QZONE'],
    'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
    'begin_date': '2019-03-07',
    'end_date': '',
    'billing_event': 'BILLINGEVENT_CLICK',
    'bid_amount': 1000,
    'optimization_goal': 'OPTIMIZATIONGOAL_CLICK',
    'targeting_id': 'global variable',
    'time_series': ''.join([str(random.randint(0, 1)) for x in range(336)])},
    {'result': True,
     'code': 0,
     'msg': ''},
    'add_adgroup')]

test_02_adgroups_update = [({
    'account_id': 'global variable',
    'adgroup_id': 'global variable',
    'adgroup_name': 'update_adgroup_name_{}'.format(dg.randint()),
    'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
    'begin_date': '2019-03-07',
    'end_date': '',
    'billing_event': 'BILLINGEVENT_CLICK',
    'bid_amount': 1000,
    'optimization_goal': 'OPTIMIZATIONGOAL_CLICK',
    'targeting_id': 'global variable',
    'time_series': ''.join([str(random.randint(0, 1)) for x in range(336)])},
    {'result': True,
     'code': 0,
     'msg': ''},
    'update_adgroup')]

test_03_adgroups_get = [({
    'account_id': 'global variable',
    'filtering': '',
    'page': '',
            'page_size': ''
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_adgroup')]

test_04_adgroups_delete = [({
    'account_id': 'global variable',
    'adgroup_id': 'global variable'
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'delete_adgroup')]

test_01_ads_add = [({
    'account_id': 'global variable',
    'adgroup_id': 'global variable',
    'adcreative_id': 'global variable',
    'ad_name': 'test_ad_name_{}'.format(dg.randint()),
    'configured_status': '',
    'impression_tracking_url': '',
    'click_tracking_url': '',
    'feeds_interaction_enabled': '',
    'sndo_ader_id': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'add_ad')]

test_02_ads_update = [({
    'account_id': 'global variable',
    'ad_id': 'global variable',
    'ad_name': 'update_ad_name_{}'.format(dg.randint()),
    'configured_status': '',
    'impression_tracking_url': '',
    'click_tracking_url': '',
    'feeds_interaction_enabled': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'update_ad')]

test_03_ads_get = [({
    'account_id': 'global variable',
    'filtering': '',
    'page': '',
            'page_size': ''
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_ad')]

test_04_ads_delete = [({
    'account_id': 'global variable',
    'ad_id': 'global variable'
},
    {'result': True,
     'code': 0,
     'msg': ''},
    'delete_ad')]

test_01_adcreatives_add = [({
    'account_id': 'global variable',
    'campaign_id': 'global variable',
    'adcreative_name': 'test_adcreative_name_{}'.format(dg.randint()),
    'adcreative_template_id': 529,
    'adcreative_elements': {'image': '3519', 'title': 'test_title_'.format(dg.randint())},
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

test_02_adcreatives_update = [({
    'account_id': 'global variable',
    'adcreative_id': 'global variable',
    'adcreative_name': 'update_adcreative_name_{}'.format(dg.randint()),
    'adcreative_elements': {'image': '3519', 'title': 'update_title_'.format(dg.randint())},
    'page_type': 'PAGE_TYPE_DEFAULT',
    'page_spec': '',
    'deep_link_url': '',
    'share_content_spec': '',
    'dynamic_adcreative_spec': '',
    'multi_share_optimization_enabled': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'update_adcreative')]

test_03_adcreatives_get = [({
    'account_id': 'global variable',
    'filtering': '',
    'page': '',
    'page_size': ''},
    {'result': True,
     'code': 0,
     'msg': ''},
    'get_adcreative')]

test_04_adcreatives_delete = [
    ({
        'account_id': 'global variable', 'adcreative_id': 'global variable'}, {
            'result': True, 'code': 0, 'msg': ''}, 'delete_advertiser')]

test_01_targeting_add = [
    ({
        'account_id': 'global variable', 'targeting_name': 'test_targeting_name_{}'.format(
            dg.randint()), 'targeting': '', 'description': 'test_description_{}'.format(
                dg.randint())}, {
        'result': True, 'code': 0, 'msg': ''}, 'add_targeting')]

test_02_targeting_update = [({'account_id': 'global variable',
                              'targeting_id': 'gloabl variable',
                              'targeting_name': 'update_targeting_name_{}'.format(dg.randint()),
                              'targeting': '',
                              'description': 'update_description_{}'.format(dg.randint())},
                             {'result': True,
                              'code': 0,
                              'msg': ''},
                             'update_targeting')]

test_03_targeting_get = [
    ({
        'account_id': 'global variable',
        'filtering': '',
        'page': '',
        'page_size': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_targeting')]

test_01_targeting_tags_get = [
    ({
        'type': 'REGION',
        'tag_spec': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_targeting_tags')]

test_01_capabilities_get = [
    ({
        'account_id': 'global variable',
        'capability': 'CAPABILITY_WECHAT_ECOMMERCE_PRODUCT',
        'query_spec': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_capabilities')]

test_01_estimation_get = [
    ({
        'account_id': 'global variable',
        'adgroup': '',
        'adcreative': '',
        'targeting': {
            'geo_location': {
                'location_types': ['RECENTLY_IN'],
                'regions':[510100]
            }
        }
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'get_estimation')]

test_01_realtime_cost_get = [
    ({
        'account_id': 'global variable',
        'level': 'ADVERTISER',
        'date': '2019-4-10',
        'filtering': '',
        'page': '',
        'page_size': ''
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'get_realtime_cost')]

test_01_images_add = [
    ({
        'account_id': 'global variable',
        'image': dg.drawimage()
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'add_image')]

test_02_images_get = [
    ({
        'account_id': 'global variable',
        'filtering': '',
        'page': '',
        'page_size': ''
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'get_image')]

test_01_video_add = [
    ({
        'account_id': 'global variable',
        'video': pp.path_join(pp.current_path(),'misc/video.webm')
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'add_video')]

test_02_video_get = [
    ({
        'account_id': 'global variable',
        'filtering': '',
        'page': '',
        'page_size': ''
    }, {
        'result': True, 'code': 0, 'msg': ''}, 'get_video')]

test_01_fund_transfer_add = [
    ({
        'account_id': 'global variable',
        'fund_type': 'FUND_TYPE_CASH',
        'amount': 5000,
        'transfer_type': 'AGENCY_TO_ADVERTISER',
        'external_bill_no': 'test_external_bill_{}'.format(dg.randchr()),
        'memo': 'test_memo_{}'.format(dg.randint())}, {
        'result': True, 'code': 0, 'msg': ''}, 'add_fund_transfer')]

test_01_funds_get = [
    ({
        'account_id': 'global variable'}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_funds')
]

test_01_fund_statements_daily_get = [
    ({
        'account_id': 'global variable',
        'fund_type': 'FUND_TYPE_CASH',
        'date_range': {
            'start_date': '2019-03-10',
            'end_date': '2019-03-15'
        },
        'trade_type': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_fund_statements_daily')
]

test_01_fund_statements_detailed_get = [
    ({
        'account_id': 'global variable',
        'fund_type': 'FUND_TYPE_CASH',
        'date_range': {
            'start_date': '2019-03-10',
            'end_date': '2019-03-15'
        },
        'page': '',
        'page_size': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'get_fund_statements_detailed')
]

test_01_adcreatives2_add = [
    ({
        'account_id': 'global variable',
        'campaign_id': 'global variable',
        'adcreative_name': 'test_adcreative_name_{}'.format(dg.randint()),
        'adcreative_template_id': 529,
        'adcreative_elements': {'image': '3519', 'title': 'test_title_{}'.format(dg.randint())},
        'site_set': ['SITE_SET_QQCLIENT'],
        'page_spec': {'page_id': 0,
                      'page_url': 'https://www.example.com'},
        'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
        'page_type': 'PAGE_TYPE_DEFAULT',
        'adgroup_id': 'global variable',
        'ad_name': 'test_ad_name_{}'.format(dg.randint()),
        'configured_status': 'AD_STATUS_SUSPEND',
        'deep_link_url': '',
        'promoted_object_id': '',
        'share_content_spec': '',
        'dynamic_adcreative_spec': '',
        'multi_share_optimization_enabled': '',
        'adcreative_id': '',
        'impression_tracking_url': '',
        'click_tracking_url': '',
        'feeds_interaction_enabled': '',
        'sndo_ader_id': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'add_adcreatives2')
]

test_02_adcreatives2_update = [
    ({
        'account_id': 'global variable',
        'adcreative_id': 'global variable',
        'adcreative_name': 'update_adcreative_name_{}'.format(dg.randint()),
        'adcreative_elements': {'image': '3519', 'title': 'update_title_{}'.format(dg.randint())},
        'page_spec': {'page_id': 0,
                      'page_url': 'https://www.example.com'},
        'page_type': 'PAGE_TYPE_DEFAULT',
        'deep_link_url': '',
        'share_content_spec': '',
        'dynamic_adcreative_spec': '',
        'multi_share_optimization_enabled': '',
        'ad_id': 'global variable',
        'ad_name': 'update_ad_name_{}'.format(dg.randint()),
        'configured_status': 'AD_STATUS_SUSPEND',
        'impression_tracking_url': '',
        'click_tracking_url': '',
        'feeds_interaction_enabled': ''}, {
        'result': True, 'code': 0, 'msg': ''}, 'update_adcreatives2')
]

test_03_adcreatives2_delete = [
    ({
        'account_id': 'global variable',
        'adcreative_id': 'global variable',
        'ad_id': 'global variable'}, {
        'result': True, 'code': 0, 'msg': ''}, 'delete_adcreatives2')
]
