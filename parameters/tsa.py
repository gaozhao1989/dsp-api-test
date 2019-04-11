import random

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
    (100006180, 29131, 'test_group', ["SITE_SET_QZONE"], 'PROMOTED_OBJECT_TYPE_LINK', '2019-03-07', '', 'BILLINGEVENT_CLICK', 1000, 'OPTIMIZATIONGOAL_CLICK', 97522,
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
    (100006180,63651,35997, True, 0, '', 'delete_adcreatives')
]

test_24_qualifications_update = [
    (1553568843,'INDUSTRY_QUALIFICATION',10009283,["3517"],True, 0, '', 'delete_adcreatives')
]