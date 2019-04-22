import json
import urllib.parse

import allure
import pytest

from parameters import tsa

from utils import AssertUtils
from utils import ConfigParser
from utils import DataGenerator
from utils import Log
from utils import Requests

au = AssertUtils()
cp = ConfigParser()
dg = DataGenerator()
log = Log.getlog('TsaTest')
r = Requests()
addr = cp.get_tsa_addr()
# global varibales
account_id = None
ad_id = None
adcreative_id = None
adgroup_id = None
campaign_id = None
external_bill_no = None
image_id = None
qualification_id = None
targeting_id = None


@allure.step('step for get the account_id')
def get_account_id(glo=True, payload={'account_id': 'global variable'}):
    """Get variable 'account_id' value.
    
    Get the value of variable 'account_id'. 
    Condition 1:Check the 'account_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'account_id'.
    Condition 2:If the variable value set to None, it will create new advertiser by api 
    'advertiser/add' and get the 'account_id'in response.

    Args:
        glo: The toggle for set global variable 'account_id'. Default set as 'True'
        payload: a dict contains 'account_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'account_id'. For example:

        100006180
    """
    if payload['account_id'] == 'global variable':
        global account_id
        if account_id is None:
            url = urllib.parse.urljoin(addr, 'advertiser/add')
            response = r.req(
                'POST',
                url,
                json=tsa.test_01_advertiser_add[0][0])
            if glo:
                account_id = response['data']['account_id']
        return account_id
    else:
        return payload['account_id']


@allure.step('step for get the qualification_id')
def get_qualification_id(
    glo=True, payload={
        'qualification_id': 'global variable'}):
    """Get variable 'qualification_id' value.
    
    Get the value of variable 'qualification_id'. 
    Condition 1:Check the 'qualification_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'qualification_id'.
    Condition 2:If the variable value set to None, it will create new qualification by api 
    'qualifications/add' and get the 'qualification_id'in response. Need get the 'account_id' 
    before create.

    Args:
        glo: The toggle for set global variable 'qualification_id'. Default set as 'True'
        payload: a dict contains 'qualification_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'qualification_id'. For example:

        10261234
    """    
    if payload['qualification_id'] == 'global variable':
        global qualification_id
        if qualification_id is None:
            add_qua_payload = tsa.test_01_qualifications_add[0][0]
            add_qua_payload['account_id'] = get_account_id(
                payload=add_qua_payload)
            url = urllib.parse.urljoin(addr, 'qualifications/add')
            response = r.req(
                'POST',
                url,
                json=add_qua_payload)
            if glo:
                qualification_id = response['data']['qualification_id']
        return qualification_id
    else:
        return payload['qualification_id']


@allure.step('step for get the campaign_id')
def get_campaign_id(glo=True, payload={'campaign_id': 'global variable'}):
    """Get variable 'campaign_id' value.
    
    Get the value of variable 'campaign_id'. 
    Condition 1:Check the 'campaign_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'campaign_id'.
    Condition 2:If the variable value set to None, it will create new campaign by api 
    'campaigns/add' and get the 'campaign_id'in response. Need get the 'account_id' 
    before create.

    Args:
        glo: The toggle for set global variable 'campaign_id'. Default set as 'True'
        payload: a dict contains 'campaign_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'campaign_id'. For example:

        29847
    """    
    if payload['campaign_id'] == 'global variable':
        global campaign_id
        if campaign_id is None:
            add_cam_payload = tsa.test_01_campaigns_add[0][0]
            add_cam_payload['account_id'] = get_account_id(
                payload=add_cam_payload)
            url = urllib.parse.urljoin(addr, 'campaigns/add')
            response = r.req(
                'POST',
                url,
                json=add_cam_payload)
            if glo:
                campaign_id = response['data']['campaign_id']
        return campaign_id
    else:
        return payload['campaign_id']


@allure.step('step for get the targeting_id')
def get_targeting_id(glo=True, payload={'targeting_id': 'global variable'}):
    """Get variable 'targeting_id' value.
    
    Get the value of variable 'targeting_id'. 
    Condition 1:Check the 'targeting_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'targeting_id'.
    Condition 2:If the variable value set to None, it will create new targeting by api 
    'targeting/add' and get the 'targeting_id'in response. Need get the 'account_id' 
    before create.

    Args:
        glo: The toggle for set global variable 'targeting_id'. Default set as 'True'
        payload: a dict contains 'targeting_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'targeting_id'. For example:

        99252
    """   
    if payload['targeting_id'] == 'global variable':
        global targeting_id
        if targeting_id is None:
            add_targeting_payload = tsa.test_01_targeting_add[0][0]
            add_targeting_payload['account_id'] = get_account_id(
                payload=add_targeting_payload)
            url = urllib.parse.urljoin(addr, 'targeting/add')
            response = r.req(
                'POST',
                url,
                json=add_targeting_payload)
            if glo:
                targeting_id = response['data']['targeting_id']
        return targeting_id
    else:
        return payload['targeting_id']


@allure.step('step for get the adgroup_id')
def get_adgroup_id(glo=True, payload={'adgroup_id': 'global variable'}):
    """Get variable 'adgroup_id' value.
    
    Get the value of variable 'adgroup_id'. 
    Condition 1:Check the 'adgroup_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'adgroup_id'.
    Condition 2:If the variable value set to None, it will create new adgroup by api 
    'adgroups/add' and get the 'adgroup_id'in response. Need get the 'account_id', 
    'campaign_id', 'targeting_id' before create.

    Args:
        glo: The toggle for set global variable 'adgroup_id'. Default set as 'True'
        payload: a dict contains 'adgroup_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'adgroup_id'. For example:

        41869
    """  
    if payload['adgroup_id'] == 'global variable':
        global adgroup_id
        if adgroup_id is None:
            add_adgroup_payload = tsa.test_01_adgroups_add[0][0]
            add_adgroup_payload['account_id'] = get_account_id(
                payload=add_adgroup_payload)
            add_adgroup_payload['campaign_id'] = get_campaign_id(
                payload=add_adgroup_payload)
            add_adgroup_payload['targeting_id'] = get_targeting_id(
                payload=add_adgroup_payload)
            url = urllib.parse.urljoin(addr, 'adgroups/add')
            response = r.req(
                'POST',
                url,
                json=add_adgroup_payload)
            if glo:
                adgroup_id = response['data']['adgroup_id']
        return adgroup_id
    else:
        return payload['adgroup_id']


@allure.step('step for get the adcreative_id')
def get_adcreative_id(glo=True, payload={'adcreative_id': 'global variable'}):
    """Get variable 'adcreative_id' value.
    
    Get the value of variable 'adcreative_id'. 
    Condition 1:Check the 'adcreative_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'adcreative_id'.
    Condition 2:If the variable value set to None, it will create new adcreative by api 
    'adcreatives/add' and get the 'adcreative_id'in response. Need get the 'account_id', 
    'campaign_id' before create.

    Args:
        glo: The toggle for set global variable 'adcreative_id'. Default set as 'True'
        payload: a dict contains 'adcreative_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'adcreative_id'. For example:

        64019
    """  
    if payload['adcreative_id'] == 'global variable':
        global adcreative_id
        if adcreative_id is None:
            add_adcreative_payload = tsa.test_01_adcreatives_add[0][0]
            add_adcreative_payload['account_id'] = get_account_id(
                payload=add_adcreative_payload)
            add_adcreative_payload['campaign_id'] = get_campaign_id(
                payload=add_adcreative_payload)
            url = urllib.parse.urljoin(addr, 'adcreatives/add')
            response = r.req(
                'POST',
                url,
                json=add_adcreative_payload)
            if glo:
                adcreative_id = response['data']['adcreative_id']
        return adcreative_id
    else:
        return payload['adcreative_id']


@allure.step('step for get the ad_id')
def get_ad_id(glo=True, payload={'ad_id': 'global variable'}):
    """Get variable 'ad_id' value.
    
    Get the value of variable 'ad_id'. 
    Condition 1:Check the 'ad_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'ad_id'.
    Condition 2:If the variable value set to None, it will create new ad by api 
    'ads/add' and get the 'ad_id'in response. Need get the 'account_id', 
    'adgroup_id', 'adcreative_id' before create.

    Args:
        glo: The toggle for set global variable 'ad_id'. Default set as 'True'
        payload: a dict contains 'ad_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'ad_id'. For example:

        36312
    """      
    if payload['ad_id'] == 'global variable':
        global ad_id
        if ad_id is None:
            add_ad_payload = tsa.test_01_ads_add[0][0]
            add_ad_payload['account_id'] = get_account_id(
                payload=add_ad_payload)
            add_ad_payload['adgroup_id'] = get_adgroup_id(
                payload=add_ad_payload)
            add_ad_payload['adcreative_id'] = get_adcreative_id(
                payload=add_ad_payload)
            url = urllib.parse.urljoin(addr, 'ads/add')
            response = r.req(
                'POST',
                url,
                json=add_ad_payload)
            if glo:
                ad_id = response['data']['ad_id']
        return ad_id
    else:
        return payload['ad_id']


@allure.step('step for get the image_id')
def get_image_id(glo=True, payload={'image_id': 'global variable'}):
    """Get variable 'image_id' value.
    
    Get the value of variable 'image_id'. 
    Condition 1:Check the 'image_id' in parameters, replace the value from global 
    variable if 'global variable' as the value of 'image_id'.
    Condition 2:If the variable value set to None, it will create new ad by api 
    'images/add' and get the 'image_id'in response. Need get the 'account_id' before create.

    Args:
        glo: The toggle for set global variable 'image_id'. Default set as 'True'
        payload: a dict contains 'image_id' key value pairs. Default set value as 'global variable'

    Returns:
        A int value of 'image_id'. For example:

        36312
    """   
    if payload['image_id'] == 'global variable':
        global image_id
        if image_id is None:
            add_image_payload = tsa.test_01_images_add[0][0]
            add_image_payload['account_id'] = get_account_id(
                payload=add_image_payload)
            url = urllib.parse.urljoin(addr, 'images/add')
            op = open(add_image_payload['image'], 'rb')
            files = {'image': op}
            del add_image_payload['image']
            response = r.req(
                'POST',
                url,
                data=add_image_payload,
                files=files
            )
            op.close()
            if glo:
                image_id = response['data']['image_id']
        return image_id
    else:
        return payload['image_id']


@pytest.mark.userfixtures('base')
class TestTsaInd(object):
    """Test cases for TSA industry check.
    
    Include: get the industry list.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_01_ind_get)
    def test_01_ind_get(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'ind/list')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']:
                cursor = mongodb.sndo['tsa.industry'].find_one(
                    {'_id': tag['_id']})
                au.assertnotfound(cursor, tag['_id'])
                au.assertgroup(cursor, tag, ['describe', 'name', 'pid'])


@pytest.mark.userfixtures('base')
class TestTsaQua(object):
    """Test cases for TSA qualification check.
    
    Include: get the qualification information.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_01_qua_get)
    def test_01_qua_get(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'qua/list')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.userfixtures('base')
class TestTsaADCreativeTemplates(object):
    """Test cases for TSA adcreative templates check.
    
    Include: get the adcreative templates information.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adcreative_templates_get)
    def test_01_adcreative_templates_get(
            self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreative_templates/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.userfixtures('base')
class TestTsaAdvertiser(object):
    """Test cases for TSA advertiser check.
    
    Include: 01.add an advertiser.
    02.update an advertiser.
    03.get the advertiser list.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_advertiser_add)
    def test_01_advertiser_add(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.account'].find_one(
                {'account_id': response['data']['account_id']})
            au.assertnotfound(cursor, response['data']['account_id'])
            global account_id
            account_id = response['data']['account_id']
            au.assertgroup(cursor,
                           payload,
                           ['corporation_name',
                            'certification_image_id',
                            'system_industry_id',
                            'introduction_url',
                            'corporate_image_name',
                            'contact_person_telephone',
                            'contact_person_mobile',
                            'certification_number',
                            'sndo_ader_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_advertiser_update)
    def test_02_advertiser_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'advertiser/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.account'].find_one(
                {'account_id': response['data']['account_id']})
            au.assertnotfound(cursor, response['data']['account_id'])
            au.assertgroup(cursor,
                           payload,
                           ['daily_budget',
                            'corporation_name',
                            'certification_image_id',
                            'system_industry_id',
                            'introduction_url',
                            'individual_qualification',
                            'corporate_image_name',
                            'contact_person_telephone',
                            'contact_person_mobile',
                            'sndo_ader_id',
                            'wechat_spec',
                            'websites'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_advertiser_get)
    def test_03_advertiser_get(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/get')
        if 'account_id' in payload:
            payload['account_id'] = get_account_id(payload=payload)
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.account'].find_one(
                    {'account_id': tag['account_id']})
                au.assertnotfound(cursor, tag['account_id'])
                au.assertgroup(cursor,
                               tag,
                               ['daily_budget',
                                'system_status',
                                'corporation_name',
                                'certification_image_id',
                                'individual_qualification',
                                'system_industry_id',
                                'wechat_spec'])


@pytest.mark.userfixtures('base')
class TestTsaQualifications(object):
    """Test cases for TSA qualification check.
    
    Include: 01.add a qualification.
    02.update a qualification.
    03.get the qualification list.
    04.delete a qualification.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_qualifications_add)
    def test_01_qualifications_add(self, payload, res, test_title, mongodb):
        # account_id and image_id should be associated
        # add qualification will failed if the account's system_status is 'CUSTOMER_STATUS_NORMAL'
        payload['account_id'] = get_account_id(payload=payload)
        payload_qua_spec = payload['qualification_spec'][next(
            iter(payload['qualification_spec']))]
        if 'image_id_list' in payload_qua_spec:
            if 'global variable' in payload_qua_spec['image_id_list']:
                payload_qua_spec['image_id_list'][0] = get_image_id()
        url = urllib.parse.urljoin(addr, 'qualifications/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            au.assertnotfound(cursor, response['data']['qualification_id'])
            global qualification_id
            qualification_id = response['data']['qualification_id']
            au.assertgroup(
                cursor, payload, [
                    'account_id', 'qualification_type'])
            if payload['qualification_type'] == 'INDUSTRY_QUALIFICATION':
                au.assertgroup(cursor,
                               payload['qualification_spec']['industry_spec'],
                               ['system_industry_id',
                                'business_scope_id',
                                'qualification_code',
                                'image_id_list',
                                'qualification_id',
                                'qualification_status',
                                'reject_message'])
            elif payload['qualification_type'] == 'AD_QUALIFICATION':
                au.assertgroup(cursor,
                               payload['qualification_spec']['ad_spec'],
                               ['qualification_code',
                                'image_id_list',
                                'qualification_id',
                                'qualification_status',
                                'reject_message'])
            elif payload['qualification_type'] == 'ADDITIONAL_INDUSTRY_QUALIFICATION':
                au.assertgroup(cursor,
                               payload['qualification_spec']['additional_industry_spec'],
                               ['system_industry_id',
                                'business_scope_id',
                                'qualification_code',
                                'image_id_list',
                                'qualification_id',
                                'qualification_status',
                                'reject_message'])
            elif payload['qualification_type'] == 'INDUSTRY_QUALIFICATION_WECHAT':
                au.assertgroup(cursor,
                               payload['qualification_spec']['industry_wechat_spec'],
                               ['qualification_name',
                                'image_id',
                                'qualification_id',
                                'qualification_status',
                                'reject_message',
                                'image_url',
                                'expired_date'])
            elif payload['qualification_type'] == 'AD_QUALIFICATION_WECHAT':
                au.assertgroup(cursor,
                               payload['qualification_spec']['ad_wechat_spec'],
                               ['qualification_name',
                                'image_id',
                                'qualification_id',
                                'qualification_status',
                                'reject_message',
                                'image_url',
                                'expired_date'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_qualifications_update)
    def test_02_qualifications_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        if 'image_id_list' in payload:
            if 'global variable' in payload['image_id_list']:
                payload['image_id_list'][0] = get_image_id()
        payload['qualification_id'] = get_qualification_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': payload['qualification_id']})
            au.assertnotfound(cursor, payload['qualification_id'])
            au.assertgroup(
                cursor, payload, [
                    'qualification_type', 'qualification_id', 'image_id_list'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_qualifications_get)
    def test_03_qualifications_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_qualifications_delete)
    def test_04_qualifications_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['qualification_id'] = get_qualification_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor is None, 'delete fail'


@pytest.mark.userfixtures('base')
class TestTsaCampaigns(object):
    """Test cases for TSA campaign check.
    
    Include: 01.add a campaign.
    02.update a campaign.
    03.get the campaign list.
    04.delete a campaign.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_campaigns_add)
    def test_01_campaigns_add(self, payload, res, test_title, mongodb):
        # account inactive can not add campaign
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            au.assertnotfound(cursor, response['data']['campaign_id'])
            global campaign_id
            campaign_id = response['data']['campaign_id']
            au.assertgroup(cursor,
                           payload,
                           ['account_id',
                            'campaign_name',
                            'campaign_type',
                            'promoted_object_type',
                            'daily_budget',
                            'configured_status',
                            'speed_mode',
                            'sndo_ader_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_campaigns_update)
    def test_02_campaigns_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            au.assertnotfound(cursor, response['data']['campaign_id'])
            au.assertgroup(cursor,
                           payload,
                           ['account_id',
                            'campaign_name',
                            'daily_budget',
                            'configured_status',
                            'speed_mode',
                            'promoted_object_type'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_campaigns_get)
    def test_03_campaigns_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.campaign'].find_one(
                    {'campaign_id': tag['campaign_id']})
                au.assertnotfound(cursor, tag['campaign_id'])
                au.assertgroup(cursor,
                               tag,
                               ['campaign_name',
                                'configured_status',
                                'campaign_type',
                                'promoted_object_type',
                                'daily_budget',
                                'budget_reach_date',
                                'created_time',
                                'last_modified_time',
                                'speed_mode',
                                'is_deleted',
                                'account_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_campaigns_delete)
    def test_04_campaigns_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': payload['campaign_id']})
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaAdgroups(object):
    """Test cases for TSA adgroup check.
    
    Include: 01.add an adgroup.
    02.update an adgroup.
    03.get the adgroup list.
    04.delete an adgroup.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adgroups_add)
    def test_01_adgroups_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            au.assertnotfound(cursor, response['data']['adgroup_id'])
            global adgroup_id
            adgroup_id = response['data']['adgroup_id']
            au.assertgroup(cursor,
                           payload,
                           ['account_id',
                            'campaign_id',
                            'adgroup_name',
                            'site_set',
                            'promoted_object_type',
                            'begin_date',
                            'end_date',
                            'billing_event',
                            'bid_amount',
                            'optimization_goal',
                            'targeting_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_adgroups_update)
    def test_02_adgroups_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            au.assertnotfound(cursor, response['data']['adgroup_id'])
            au.assertgroup(cursor,
                           payload,
                           ['account_id',
                            'campaign_id',
                            'adgroup_name',
                            'site_set',
                            'promoted_object_type',
                            'begin_date',
                            'end_date',
                            'billing_event',
                            'bid_amount',
                            'optimization_goal',
                            'targeting_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_adgroups_get)
    def test_03_adgroups_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.adgroup'].find_one(
                    {'adgroup_id': tag['adgroup_id']})
                au.assertnotfound(cursor, tag['adgroup_id'])
                assert cursor['cpc_expand_targeting'] == tag['cpc_expand_targeting'], 'cpc_expand_targeting not equal'
                au.assertgroup(cursor,
                               tag,
                               ['account_id',
                                'campaign_id',
                                'adgroup_name',
                                'site_set',
                                'promoted_object_type',
                                'begin_date',
                                'end_date',
                                'billing_event',
                                'bid_amount',
                                'optimization_goal',
                                'time_series',
                                'daily_budget',
                                'promoted_object_id',
                                'app_android_channel_package_id',
                                'targeting_id',
                                'targeting',
                                'scene_spec',
                                'configured_status',
                                'customized_category',
                                'frequency_capping',
                                'dynamic_ad_spec',
                                'ocpa_expand_enabled',
                                'ocpa_expand_targeting',
                                'user_action_sets',
                                'created_time',
                                'last_modified_time',
                                'is_deleted',
                                'cpc_expand_enabled',
                                ''])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_adgroups_delete)
    def test_04_adgroups_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': payload['adgroup_id']})
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.userfixtures('base')
class TestTsaAds(object):
    """Test cases for TSA ad check.
    
    Include: 01.add an ad.
    02.update an ad.
    03.get the ad list.
    04.delete an ad.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_01_ads_add)
    def test_01_ads_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
            global ad_id
            ad_id = response['data']['ad_id']
            au.assertgroup(cursor,
                           payload,
                           ['campaign_id',
                            'adgroup_id',
                            'ad_name',
                            'configured_status',
                            'impression_tracking_url',
                            'click_tracking_url',
                            'feeds_interaction_enabled',
                            'sndo_ader_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_ads_update)
    def test_02_ads_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
            au.assertgroup(cursor,
                           payload,
                           ['ad_name',
                            'configured_status',
                            'impression_tracking_url',
                            'click_tracking_url',
                            'feeds_interaction_enabled'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_03_ads_get)
    def test_03_ads_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.ad'].find_one(
                    {'ad_id': tag['ad_id']})
                au.assertgroup(cursor,
                               tag,
                               ['campaign_id',
                                'adgroup_id',
                                'ad_name',
                                'adcreative',
                                'configured_status',
                                'system_status',
                                'impression_tracking_url',
                                'click_tracking_url',
                                'feeds_interaction_enabled',
                                'reject_message',
                                'conversion_tracking_enabled',
                                'is_deleted',
                                'created_time',
                                'last_modified_time'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_ads_delete)
    def test_04_ads_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaAdcreatives(object):
    """Test cases for TSA adcreative check.
    
    Include: 01.add an adcreative.
    02.update an adcreative.
    03.get the adcreative list.
    04.delete an adcreative.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adcreatives_add)
    def test_01_adcreatives_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(cursor, response['data']['adcreative_id'])
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            au.assertgroup(cursor,
                           payload,
                           ['adcreative_name',
                            'adcreative_template_id',
                            'adcreative_elements',
                            'site_set',
                            'promoted_object_type',
                            'page_type',
                            'page_spec',
                            'deep_link_url',
                            'promoted_object_id',
                            'share_content_spec',
                            'dynamic_adcreative_spec',
                            'multi_share_optimization_enabled',
                            'sndo_ader_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_adcreatives_update)
    def test_02_adcreatives_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            au.assertnotfound(cursor, payload['adcreative_id'])
            au.assertgroup(cursor,
                           payload,
                           ['adcreative_name',
                            'adcreative_elements',
                            'page_type',
                            'page_spec',
                            'deep_link_url',
                            'share_content_spec',
                            'dynamic_adcreative_spec',
                            'multi_share_optimization_enabled'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_adcreatives_get)
    def test_03_adcreatives_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.adcreative'].find_one(
                    {'adcreative_id': tag['adcreative_id']})
                au.assertnotfound(cursor, tag['adcreative_id'])
                au.assertgroup(cursor,
                               tag,
                               ['campaign_id',
                                'adcreative_name',
                                'adcreative_template_id',
                                'adcreative_elements',
                                'site_set',
                                'promoted_object_type',
                                'page_type',
                                'page_spec',
                                'deep_link_url',
                                'promoted_object_id',
                                'share_content_spec',
                                'dynamic_adcreative_spec',
                                'multi_share_optimization_enabled',
                                'created_time',
                                'last_modified_time',
                                'is_deleted'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_adcreatives_delete)
    def test_04_adcreatives_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            au.assertnotfound(cursor, payload['adcreative_id'])
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaTargeting(object):
    """Test cases for TSA targeting check.
    
    Include: 01.add a targeting.
    02.update a targeting.
    03.get the targeting list.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_targeting_add)
    def test_01_targeting_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': response['data']['targeting_id']})
            au.assertnotfound(cursor, response['data']['targeting_id'])
            au.assertgroup(
                cursor, payload, [
                    'account_id', 'targeting_name', 'targeting', 'description'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_targeting_update)
    def test_02_targeting_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': payload['targeting_id']})
            au.assertnotfound(cursor, payload['targeting_id'])
            au.assertgroup(
                cursor, payload, [
                    'account_id', 'targeting_name', 'targeting', 'description'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_targeting_get)
    def test_03_targeting_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.targeting'].find_one(
                    {'targeting_id': tag['targeting_id']})
                au.assertnotfound(cursor, tag['targeting_id'])
                au.assertgroup(
                    cursor, tag, [
                        'account_id', 'targeting_name', 'targeting', 'description'])


@pytest.mark.usefixtures('base')
class TestTsaTargetingTags(object):
    """Test cases for TSA targeting tag check.
    
    Include: 01.get the targeting tag list.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_targeting_tags_get)
    def test_01_targeting_tags_get(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'targeting_tags/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.targeting_tag'].find_one(
                    {
                        'id': tag['id'],
                        'name': tag['name'],
                        'parent_id': tag['parent_id'],
                        'parent_name': tag['parent_name'],
                        'city_level': tag['city_level']})
                au.assertnotfound(cursor, tag['targeting_id'])
                au.assertgroup(cursor, payload, ['type'])


@pytest.mark.usefixtures('base')
class TestTsaCapabilities(object):
    """Test cases for TSA capability check.
    
    Include: 01.get the capability information.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_capabilities_get)
    def test_01_capabilities_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'capabilities/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.usefixtures('base')
class TestTsaEstimation(object):
    """Test cases for TSA estimation check.
    
    Include: 01.get the estimation information.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_estimation_get)
    def test_01_estimation_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'estimation/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            assert response['data']['approximate_count'], 'approximate_count error'
            assert response['data']['impression'], 'impression error'
            assert response['data']['min_bid_amount'], 'min_bid_amount error'
            assert response['data']['max_bid_amount'], 'max_bid_amount error'


@pytest.mark.usefixtures('base')
class TestTsaRealtimeCost(object):
    """Test cases for TSA real time cost check.
    
    Include: 01.get the real time cost information.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_realtime_cost_get)
    def test_01_realtime_cost_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'realtime_cost/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.usefixtures('base')
class TestTsaImages(object):
    """Test cases for TSA images check.
    
    Include: 01.add a image.
    02.get the image list.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_images_add)
    def test_01_images_add(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'images/add')
        op = open(payload['image'], 'rb') if payload['image'] else ''
        files = {'image': op}
        del payload['image']
        response = r.req('POST', url, data=payload, files=files)
        op.close()
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.image'].find_one(
                {'image_id': response['data']['image_id']})
            au.assertnotfound(cursor, response['data']['image_id'])
            au.assertgroup(
                cursor, response['data'], [
                    'signature', 'preview_url', 'type'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_images_get)
    def test_02_images_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'images/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.image'].find_one(
                    {'image_id': tag['image_id']})
                au.assertnotfound(cursor, tag['image_id'])
                au.assertgroup(
                    cursor, tag, [
                        'signature', 'preview_url', 'width', 'height', 'file_size', 'type'])


@pytest.mark.usefixtures('base')
class TestTsaVideo(object):
    """Test cases for TSA videos check.
    
    Include: 01.add a video.
    02.get the video list.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_01_video_add)
    def test_01_video_add(self, payload, res, test_title, mongodb):
        url = urllib.parse.urljoin(addr, 'video/add')
        op = open(payload['video'], 'rb') if payload['video'] else ''
        files = {'video': op}
        del payload['video']
        response = r.req('POST', url, data=payload, files=files)
        op.close()
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['tsa.video'].find_one(
                {'video_id': response['data']['video_id']})
            au.assertnotfound(cursor, response['data']['video_id'])
            au.assertgroup(
                cursor, response['data'], [
                    'signature', 'preview_url', 'type'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_02_video_get)
    def test_02_video_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'video/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.video'].find_one(
                    {'video_id': tag['video_id']})
                au.assertnotfound(cursor, tag['video_id'])
                au.assertgroup(
                    cursor, tag, [
                        'signature', 'preview_url', 'width', 'height', 'file_size', 'type'])


@pytest.mark.usefixtures('base')
class TestTsaFundTransfer(object):
    """Test cases for TSA fund transfer check.
    
    Include: 01.get the fund transfer information.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_transfer_add)
    def test_01_fund_transfer_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_transfer/add')
        # TODO verify variable is_repeated
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            au.assertgroup(
                response['data'], payload, [
                    'fund_type', 'amount', 'external_bill_no'])


@pytest.mark.usefixtures('base')
class TestTsaFunds(object):
    """Test cases for TSA fund check.
    
    Include: 01.get the fund information.
    """  

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize('payload, res, test_title', tsa.test_01_funds_get)
    def test_01_funds_get(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'funds/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.usefixtures('base')
class TestTsaFundStatementsDaily(object):
    """Test cases for TSA fund statement daily check.
    
    Include: 01.get the fund statement daily information.
    """   

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_statements_daily_get)
    def test_01_fund_statements_daily_get(
            self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_statements_daily/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.usefixtures('base')
class TestTsaFundStatementsDetailed(object):
    """Test cases for TSA fund statement detailed check.
    
    Include: 01.get the fund statement detailed information.
    """    

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_statements_detailed_get)
    def test_01_fund_statements_detailed_get(
            self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_statements_detailed/get')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])


@pytest.mark.usefixtures('base')
class TestTsAadcreatives2(object):
    """Test cases for TSA ad and adcreative in signle action.
    
    Include: 01.add an ad and adcreative.
    02.update an ad and adcreative.
    03.delete an ad and advertiser.
    """

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adcreatives2_add)
    def test_01_adcreatives2_add(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/add')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(
                cursor_adcreative,
                response['data']['adcreative_id'])
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor_ad, response['data']['ad_id'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_adcreatives2_update)
    def test_02_adcreatives2_update(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/update')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            au.assertnotfound(cursor_adcreative, payload['adcreative_id'])
            au.assertgroup(cursor_adcreative,
                           payload,
                           ['adcreative_name',
                            'adcreative_elements',
                            'page_type',
                            'page_spec',
                            'deep_link_url',
                            'share_content_spec',
                            'dynamic_adcreative_spec',
                            'multi_share_optimization_enabled'])
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': payload['ad_id']})
            au.assertnotfound(cursor_ad, payload['ad_id'])
            au.assertgroup(cursor_ad,
                           payload,
                           ['ad_name',
                            'configured_status',
                            'impression_tracking_url',
                            'click_tracking_url',
                            'feeds_interaction_enabled'])

    @Log.logtestcase()
    @allure.title('{test_title}')
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_adcreatives2_delete)
    def test_03_adcreatives2_delete(self, payload, res, test_title, mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/delete')
        response = r.req('POST', url, json=payload)
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            au.assertnotfound(cursor_adcreative, payload['adcreative_id'])
            assert cursor_adcreative['is_deleted'], 'delete fail'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': payload['ad_id']})
            au.assertnotfound(cursor_ad, payload['ad_id'])
            assert cursor_ad['is_deleted'], 'delete fail'
