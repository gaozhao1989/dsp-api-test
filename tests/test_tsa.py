import json
import urllib.parse
import requests
import pytest
from parameters import tsa
from utils import Log, Requests, ConfigParser, DataGenerator

cp = ConfigParser()
addr = cp.get_tsa_addr()
log = Log.getlog('TsaTest')
r = Requests()
dg = DataGenerator()
# global varibales
account_id = None
qualification_id = None
campaign_id = None
adgroup_id = None
adcreative_id = None
ad_id = None
targeting_id = None
external_bill_no = None


def get_account_id(glo=True, payload={}):
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


def get_qualification_id(glo=True, payload={}):
    if payload['qualification_id'] == 'global variable':
        global qualification_id
        if qualification_id is None:
            add_qua_payload = tsa.test_01_qualifications_add[0][0]
            add_qua_payload['account_id'] = get_account_id()
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


def get_campaign_id(glo=True, payload={}):
    if payload['campaign_id'] == 'global variable':
        global campaign_id
        if campaign_id is None:
            add_cam_payload = tsa.test_01_campaigns_add[0][0]
            add_cam_payload['account_id'] = get_account_id()
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


def get_targeting_id(glo=True, payload={}):
    if payload['targeting_id'] == 'globale variable':
        global targeting_id
        if targeting_id is None:
            add_targeting_payload = tsa.test_01_targeting_add[0][0]
            add_targeting_payload['account_id'] = get_account_id()
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


def get_adgroup_id(glo=True, payload={}):
    if payload['adgroup_id'] == 'global variable':
        global adgroup_id
        if adgroup_id is None:
            add_adgroup_payload = tsa.test_01_adgroups_add[0][0]
            add_adgroup_payload['account_id'] = get_account_id()
            add_adgroup_payload['campaign_id'] = get_campaign_id()
            add_adgroup_payload['targeting_id'] = get_targeting_id()
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


def get_adcreative_id(glo=True, payload={}):
    if payload['adcreative_id'] == 'global variable':
        global adcreative_id
        if adcreative_id is None:
            add_adcreative_payload = tsa.test_01_adcreatives_add[0][0]
            add_adcreative_payload['account_id'] = get_account_id()
            add_adcreative_payload['campaign_id'] = get_campaign_id()
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


def get_ad_id(glo=True, payload={}):
    if payload['ad_id'] == 'global variable':
        global ad_id
        if ad_id is None:
            add_ad_payload = tsa.test_01_ads_add[0][0]
            add_ad_payload['account_id'] = get_account_id()
            add_ad_payload['adgroup_id'] = get_adgroup_id()
            add_ad_payload['adcreative_id'] = get_adcreative_id()
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


@pytest.mark.userfixtures('base')
class TestTsaInd(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_ind_get)
    def test_01_ind_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'ind/list')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']:
                cursor = mongodb.sndo['tsa.industry'].find_one(
                    {'_id': tag['_id']})
                assert cursor, 'industry not found'
                assert cursor['describe'] == tag['describe'], 'describe not equal'
                assert cursor['name'] == tag['name'], 'name not equal'
                assert cursor['pid'] == tag['pid'], 'pid not equal'


@pytest.mark.userfixtures('base')
class TestTsaQua(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_qua_get)
    def test_01_qua_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'qua/list')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.userfixtures('base')
class TestTsaADCreativeTemplates(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adcreative_templates_get)
    def test_01_adcreative_templates_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreative_templates/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        assert response['data']['list'], 'adcreative templates empty'


@pytest.mark.userfixtures('base')
class TestTsaAdvertiser(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_advertiser_add)
    def test_01_advertiser_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.account'].find_one(
                {'account_id': response['data']['account_id']})
            assert cursor, 'advertiser not found'
            global account_id
            account_id = response['data']['account_id']
            assert cursor['corporation_name'] == payload['corporation_name'], 'corporation_name not equal'
            assert cursor['certification_image_id'] == payload['certification_image_id'], 'certification_image_id not equal'
            assert cursor['system_industry_id'] == payload['system_industry_id'], 'system_industry_id not equal'
            assert cursor['introduction_url'] == payload['introduction_url'], 'introduction_url not equal'
            assert cursor['individual_qualification'] == payload['individual_qualification'], 'individual_qualification not equal'
            assert cursor['corporate_image_name'] == payload['corporate_image_name'], 'corporate_image_name not equal'
            assert cursor['contact_person_telephone'] == payload['contact_person_telephone'], 'contact_person_telephone not equal'
            assert cursor['contact_person_mobile'] == payload['contact_person_mobile'], 'contact_person_mobile not equal'
            assert cursor['certification_number'] == payload['certification_number'], 'certification_number not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'individual_qualification not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_advertiser_update)
    def test_02_advertiser_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'advertiser/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.account'].find_one(
                {'account_id': response['data']['account_id']})
            assert cursor, 'advertiser not found'
            assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
            assert cursor['corporation_name'] == payload['corporation_name'], 'corporation_name not equal'
            assert cursor['certification_image_id'] == payload['certification_image_id'], 'certification_image_id not equal'
            assert cursor['system_industry_id'] == payload['system_industry_id'], 'system_industry_id not equal'
            assert cursor['introduction_url'] == payload['introduction_url'], 'introduction_url not equal'
            assert cursor['individual_qualification'] == payload['individual_qualification'], 'individual_qualification not equal'
            assert cursor['corporate_image_name'] == payload['corporate_image_name'], 'corporate_image_name not equal'
            assert cursor['contact_person_telephone'] == payload['contact_person_telephone'], 'contact_person_telephone not equal'
            assert cursor['contact_person_mobile'] == payload['contact_person_mobile'], 'contact_person_mobile not equal'
            assert cursor['certification_number'] == payload['certification_number'], 'certification_number not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'individual_qualification not equal'
            assert cursor['wechat_spec'] == payload['wechat_spec'], 'wechat_spec not equal'
            assert cursor['websites'] == payload['websites'], 'websites not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_advertiser_get)
    def test_03_advertiser_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/get')
        if 'account' in payload:
            payload['account_id'] = get_account_id(payload=payload)
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.account'].find_one(
                    {'account_id': tag['account_id']})
                assert cursor, 'advertiser not found'
                assert cursor['daily_budget'] == tag['daily_budget'], 'daily_budget not equal'
                assert cursor['system_status'] == tag['system_status'], 'system_status not equal'
                assert cursor['corporation_name'] == tag['corporation_name'], 'corporation_name not equal'
                assert cursor['certification_image_id'] == tag['certification_image_id'], 'certification_image_id not equal'
                assert cursor['individual_qualification'] == tag['individual_qualification'], 'individual_qualification not equal'
                assert cursor['system_industry_id'] == tag['system_industry_id'], 'system_industry_id not equal'
                assert cursor['wechat_spec'] == tag['wechat_spec'], 'wechat_spec not equal'


@pytest.mark.userfixtures('base')
class TestTsaQualifications(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_qualifications_add)
    def test_01_qualifications_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor, 'qualification not found'
            global qualification_id
            qualification_id = response['data']['qualification_id']
            assert cursor['qualification_type'] == payload['qualification_type'], 'qualification_type not equal'
            assert cursor['system_industry_id'] == payload['qualification_spec'][
                'industry_spec']['system_industry_id'], 'system_industry_id not equal'
            assert cursor['business_scope_id'] == payload['qualification_spec'][
                'industry_spec']['business_scope_id'], 'business_scope_id not equal'
            assert cursor['qualification_code'] == payload['qualification_spec'][
                'industry_spec']['qualification_code'], 'qualification_code not equal'
            assert cursor['image_id_list'] == payload['qualification_spec']['industry_spec']['image_id_list'], 'qualification_code not equal'
            assert cursor['qualification_status'] == payload['qualification_spec'][
                'industry_spec']['qualification_status'], 'qualification_status not equal'
            assert cursor['reject_message'] == payload['qualification_spec']['industry_spec']['reject_message'], 'reject_message not equal'
            assert cursor['created_time'] == payload['qualification_spec']['industry_spec']['created_time'], 'created_time not equal'
            assert cursor['last_modified_time'] == payload['qualification_spec'][
                'industry_spec']['last_modified_time'], 'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_qualifications_update)
    def test_02_qualifications_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['qualification_id'] = get_qualification_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor, 'qualification not found'
            assert cursor['qualification_type'] == payload['qualification_type'], 'qualification_type not equal'
            assert cursor['system_industry_id'] == payload['qualification_spec'][
                'industry_spec']['system_industry_id'], 'system_industry_id not equal'
            assert cursor['business_scope_id'] == payload['qualification_spec'][
                'industry_spec']['business_scope_id'], 'business_scope_id not equal'
            assert cursor['qualification_code'] == payload['qualification_spec'][
                'industry_spec']['qualification_code'], 'qualification_code not equal'
            assert cursor['image_id_list'] == payload['qualification_spec']['industry_spec']['image_id_list'], 'qualification_code not equal'
            assert cursor['qualification_status'] == payload['qualification_spec'][
                'industry_spec']['qualification_status'], 'qualification_status not equal'
            assert cursor['reject_message'] == payload['qualification_spec']['industry_spec']['reject_message'], 'reject_message not equal'
            assert cursor['created_time'] == payload['qualification_spec']['industry_spec']['created_time'], 'created_time not equal'
            assert cursor['last_modified_time'] == payload['qualification_spec'][
                'industry_spec']['last_modified_time'], 'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_qualifications_get)
    def test_03_qualifications_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_qualifications_delete)
    def test_04_qualifications_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['qualification_id'] = get_qualification_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'qualifications/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor is None, 'delete fail'


@pytest.mark.userfixtures('base')
class TestTsaCampaigns(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_campaigns_add)
    def test_01_campaigns_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            assert cursor, 'campaign not found'
            global campaign_id
            campaign_id = response['data']['campaign_id']
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['campaign_name'] == payload['campaign_name'], 'campaign_name not equal'
            assert cursor['campaign_type'] == payload['campaign_type'], 'campaign_type not equal'
            assert cursor['promoted_object_type'] == payload['promoted_object_type'], 'promoted_object_type not equal'
            assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
            assert cursor['configured_status'] == payload['configured_status'] if payload[
                'configured_status'] else 'AD_STATUS_NORMAL', 'configured_status not equal'
            assert cursor['speed_mode'] == payload['speed_mode'] if payload['speed_mode'] else 'SPEED_MODE_STANDARD', 'speed_mode not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'
            assert cursor['is_deleted'] == False, 'is_deleted not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_campaigns_update)
    def test_02_campaigns_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            assert cursor, 'campaign not found'
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['campaign_name'] == payload['campaign_name'], 'campaign_name not equal'
            assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
            assert cursor['configured_status'] == payload['configured_status'] if payload[
                'configured_status'] else 'AD_STATUS_NORMAL', 'configured_status not equal'
            assert cursor['speed_mode'] == payload['speed_mode'] if payload['speed_mode'] else 'SPEED_MODE_STANDARD', 'speed_mode not equal'
            assert cursor['promoted_object_type'] == payload['promoted_object_type'], 'promoted_object_type not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_campaigns_get)
    def test_03_campaigns_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.campaign'].find_one(
                    {'campaign_id': tag['campaign_id']})
                assert cursor, 'campaign not found'
                assert cursor['campaign_name'] == tag['campaign_name'], 'campaign_name not equal'
                assert cursor['configured_status'] == tag['configured_status'], 'configured_status not equal'
                assert cursor['campaign_type'] == tag['campaign_type'], 'campaign_type not equal'
                assert cursor['promoted_object_type'] == tag['promoted_object_type'], 'promoted_object_type not equal'
                assert cursor['daily_budget'] == tag['daily_budget'], 'daily_budget not equal'
                assert cursor['budget_reach_date'] == tag['budget_reach_date'], 'budget_reach_date not equal'
                assert cursor['created_time'] == tag['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'], 'last_modified_time not equal'
                assert cursor['speed_mode'] == tag['speed_mode'], 'speed_mode not equal'
                assert cursor['is_deleted'] == tag['is_deleted'], 'is_deleted not equal'
                assert cursor['account_id'] == payload['account_id'], 'account_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_campaigns_delete)
    def test_04_campaigns_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'campaigns/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': payload['campaign_id']})
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaAdgroups(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adgroups_add)
    def test_01_adgroups_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor, 'adgroup not found'
            global adgroup_id
            adgroup_id = response['data']['adgroup_id']
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert cursor['adgroup_name'] == payload['adgroup_name'], 'adgroup_name not equal'
            assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert cursor['promoted_object_type'] == payload['promoted_object_type'], 'promoted_object_type not equal'
            assert cursor['begin_date'] == payload['begin_date'], 'begin_date not equal'
            assert cursor['end_date'] == payload['end_date'], 'end_date not equal'
            assert cursor['billing_event'] == payload['billing_event'], 'billing_event not equal'
            assert cursor['bid_amount'] == payload['bid_amount'], 'bid_amount not equal'
            assert cursor['optimization_goal'] == payload['optimization_goal'], 'optimization_goal not equal'
            assert cursor['targeting_id'] == payload['targeting_id'], 'targeting_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_adgroups_update)
    def test_02_adgroups_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor, 'adgroup not found'
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert cursor['adgroup_name'] == payload['adgroup_name'], 'adgroup_name not equal'
            assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert cursor['promoted_object_type'] == payload['promoted_object_type'], 'promoted_object_type not equal'
            assert cursor['begin_date'] == payload['begin_date'], 'begin_date not equal'
            assert cursor['end_date'] == payload['end_date'], 'end_date not equal'
            assert cursor['billing_event'] == payload['billing_event'], 'billing_event not equal'
            assert cursor['bid_amount'] == payload['bid_amount'], 'bid_amount not equal'
            assert cursor['optimization_goal'] == payload['optimization_goal'], 'optimization_goal not equal'
            assert cursor['targeting_id'] == payload['targeting_id'], 'targeting_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_adgroups_get)
    def test_03_adgroups_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.adgroup'].find_one(
                    {'adgroup_id': tag['adgroup_id']})
                assert cursor, 'adgroup not found'
                assert cursor['account_id'] == tag['account_id'], 'account_id not equal'
                assert cursor['campaign_id'] == tag['campaign_id'], 'campaign_id not equal'
                assert cursor['adgroup_name'] == tag['adgroup_name'], 'adgroup_name not equal'
                assert cursor['site_set'] == tag['site_set'], 'site_set not equal'
                assert cursor['promoted_object_type'] == tag['promoted_object_type'], 'promoted_object_type not equal'
                assert cursor['begin_date'] == tag['begin_date'], 'begin_date not equal'
                assert cursor['end_date'] == tag['end_date'], 'end_date not equal'
                assert cursor['billing_event'] == tag['billing_event'], 'billing_event not equal'
                assert cursor['bid_amount'] == tag['bid_amount'], 'bid_amount not equal'
                assert cursor['optimization_goal'] == tag['optimization_goal'], 'optimization_goal not equal'
                assert cursor['time_series'] == tag['time_series'], 'time_series not equal'
                assert cursor['daily_budget'] == tag['daily_budget'], 'daily_budget not equal'
                assert cursor['promoted_object_id'] == tag['promoted_object_id'], 'promoted_object_id not equal'
                assert cursor['app_android_channel_package_id'] == tag[
                    'app_android_channel_package_id'], 'app_android_channel_package_id not equal'
                assert cursor['targeting_id'] == tag['targeting_id'], 'targeting_id not equal'
                assert cursor['targeting'] == tag['targeting'], 'targeting not equal'
                assert cursor['scene_spec'] == tag['scene_spec'], 'scene_spec not equal'
                assert cursor['configured_status'] == tag['configured_status'], 'configured_status not equal'
                assert cursor['customized_category'] == tag['customized_category'], 'customized_category not equal'
                assert cursor['frequency_capping'] == tag['frequency_capping'], 'frequency_capping not equal'
                assert cursor['dynamic_ad_spec'] == tag['dynamic_ad_spec'], 'dynamic_ad_spec not equal'
                assert cursor['ocpa_expand_enabled'] == tag['ocpa_expand_enabled'], 'ocpa_expand_enabled not equal'
                assert cursor['ocpa_expand_targeting'] == tag['ocpa_expand_targeting'], 'ocpa_expand_targeting not equal'
                assert cursor['user_action_sets'] == tag['user_action_sets'], 'user_action_sets not equal'
                assert cursor['created_time'] == tag['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'], 'last_modified_time not equal'
                assert cursor['is_deleted'] == tag['is_deleted'], 'is_deleted not equal'
                assert cursor['cpc_expand_enabled'] == tag['cpc_expand_enabled'], 'cpc_expand_enabled not equal'
                assert cursor['cpc_expand_targeting'] == tag['cpc_expand_targeting'], 'cpc_expand_targeting not equal'
                assert cursor['account_id'] == tag['account_id'], 'account_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_adgroups_delete)
    def test_04_adgroups_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': payload['adgroup_id']})
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.userfixtures('base')
class TestTsaAds(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_ads_add)
    def test_01_ads_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            global ad_id
            ad_id = response['data']['ad_id']
            assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert cursor['adgroup_id'] == payload['adgroup_id'], 'adgroup_id not equal'
            assert cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor['impression_tracking_url'] == payload['impression_tracking_url'], 'impression_tracking_url not equal'
            assert cursor['click_tracking_url'] == payload['click_tracking_url'], 'click_tracking_url not equal'
            assert cursor['feeds_interaction_enabled'] == payload['feeds_interaction_enabled'], 'feeds_interaction_enabled not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_ads_update)
    def test_02_ads_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': payload['ad_id']})
            assert cursor, 'ad not found'
            assert cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor['impression_tracking_url'] == payload['impression_tracking_url'], 'impression_tracking_url not equal'
            assert cursor['click_tracking_url'] == payload['click_tracking_url'], 'click_tracking_url not equal'
            assert cursor['feeds_interaction_enabled'] == payload['feeds_interaction_enabled'], 'feeds_interaction_enabled not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_ads_get)
    def test_03_ads_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.ad'].find_one(
                    {'ad_id': tag['ad_id']})
                assert cursor['campaign_id'] == tag['campaign_id'], 'campaign_id not equal'
                assert cursor['adgroup_id'] == tag['adgroup_id'], 'adgroup_id not equal'
                assert cursor['ad_name'] == tag['ad_name'], 'ad_name not equal'
                assert cursor['adcreative'] == tag['adcreative'], 'adcreative not equal'
                assert cursor['configured_status'] == tag['configured_status'], 'configured_status not equal'
                assert cursor['system_status'] == tag['system_status'], 'system_status not equal'
                assert cursor['impression_tracking_url'] == tag['impression_tracking_url'], 'impression_tracking_url not equal'
                assert cursor['click_tracking_url'] == tag['click_tracking_url'], 'click_tracking_url not equal'
                assert cursor['feeds_interaction_enabled'] == tag['feeds_interaction_enabled'], 'feeds_interaction_enabled not equal'
                assert cursor['reject_message'] == tag['reject_message'], 'reject_message not equal'
                assert cursor['conversion_tracking_enabled'] == tag['conversion_tracking_enabled'], 'conversion_tracking_enabled not equal'
                assert cursor['is_deleted'] == tag['is_deleted'], 'is_deleted not equal'
                assert cursor['created_time'] == tag['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'], 'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_ads_delete)
    def test_04_ads_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaAdcreatives(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_adcreatives_add)
    def test_01_adcreatives_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor, 'adcreative not found'
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            assert cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert cursor['adcreative_template_id'] == payload['adcreative_template_id'], 'adcreative_template_id not equal'
            assert cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert cursor['promoted_object_type'] == payload['promoted_object_type'], 'promoted_object_type not equal'
            assert cursor['page_type'] == payload['page_type'], 'page_type not equal'
            assert cursor['page_spec'] == payload['page_spec'], 'page_spec not equal'
            assert cursor['deep_link_url'] == payload['deep_link_url'], 'deep_link_url not equal'
            assert cursor['promoted_object_id'] == payload['promoted_object_id'], 'promoted_object_id not equal'
            assert cursor['share_content_spec'] == payload['share_content_spec'], 'share_content_spec not equal'
            assert cursor['dynamic_adcreative_spec'] == payload['dynamic_adcreative_spec'], 'dynamic_adcreative_spec not equal'
            assert cursor['multi_share_optimization_enabled'] == payload[
                'multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_adcreatives_update)
    def test_02_adcreatives_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            assert cursor, 'adcreative not found'
            assert cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert cursor['page_type'] == payload['page_type'], 'page_type not equal'
            assert cursor['page_spec'] == payload['page_spec'], 'page_spec not equal'
            assert cursor['deep_link_url'] == payload['deep_link_url'], 'deep_link_url not equal'
            assert cursor['share_content_spec'] == payload['share_content_spec'], 'share_content_spec not equal'
            assert cursor['dynamic_adcreative_spec'] == payload['dynamic_adcreative_spec'], 'dynamic_adcreative_spec not equal'
            assert cursor['multi_share_optimization_enabled'] == payload[
                'multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_adcreatives_get)
    def test_03_adcreatives_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.adcreative'].find_one(
                    {'adcreative_id': tag['adcreative_id']})
                assert cursor, 'adcreative not found'
                assert cursor['account_id'] == tag['account_id'], 'account_id not equal'
                assert cursor['campaign_id'] == tag['campaign_id'], 'campaign_id not equal'
                assert cursor['adcreative_name'] == tag['adcreative_name'], 'adcreative_name not equal'
                assert cursor['adcreative_template_id'] == tag['adcreative_template_id'], 'adcreative_template_id not equal'
                assert cursor['adcreative_elements'] == tag['adcreative_elements'], 'adcreative_elements not equal'
                assert cursor['site_set'] == tag['site_set'], 'site_set not equal'
                assert cursor['promoted_object_type'] == tag['promoted_object_type'], 'promoted_object_type not equal'
                assert cursor['page_type'] == tag['page_type'], 'page_type not equal'
                assert cursor['page_spec'] == tag['page_spec'], 'page_spec not equal'
                assert cursor['deep_link_url'] == tag['deep_link_url'], 'deep_link_url not equal'
                assert cursor['promoted_object_id'] == tag['promoted_object_id'], 'promoted_object_id not equal'
                assert cursor['share_content_spec'] == tag['share_content_spec'], 'share_content_spec not equal'
                assert cursor['dynamic_adcreative_spec'] == tag['dynamic_adcreative_spec'], 'dynamic_adcreative_spec not equal'
                assert cursor['multi_share_optimization_enabled'] == tag[
                    'multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'
                assert cursor['created_time'] == tag['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'], 'last_modified_time not equal'
                assert cursor['is_deleted'] == tag['is_deleted'], 'is_deleted not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_04_adcreatives_delete)
    def test_04_adcreatives_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            assert cursor, 'adcreative not found'
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestTsaTargeting(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_targeting_add)
    def test_01_targeting_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': response['data']['targeting_id']})
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['targeting_name'] == payload['targeting_name'], 'targeting_name not equal'
            assert cursor['targeting'] == payload['targeting'], 'targeting not equal'
            assert cursor['description'] == payload['description'], 'description not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_targeting_update)
    def test_02_targeting_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['targeting_id'] = get_targeting_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': payload['targeting_id']})
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['targeting_name'] == payload['targeting_name'], 'targeting_name not equal'
            assert cursor['targeting'] == payload['targeting'], 'targeting not equal'
            assert cursor['description'] == payload['description'], 'description not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_03_targeting_get)
    def test_03_targeting_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'targeting/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['tsa.targeting'].find_one(
                    {'targeting_id': tag['targeting_id']})
                assert cursor, 'targeting not found'
                assert cursor['targeting_name'] == tag['targeting_name'], 'targeting_name not equal'
                assert cursor['targeting'] == tag['targeting'], 'targeting not equal'
                assert cursor['description'] == tag['description'], 'description not equal'


@pytest.mark.usefixtures('base')
class TestTsaTargetingTags(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_targeting_tags_get)
    def test_01_targeting_tags_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'targeting_tags/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = ongodb.sndo['tsa.targeting_tag'].find_one(
                    {
                        'id': tag['id'],
                        'name': tag['name'],
                        'parent_id': tag['parent_id'],
                        'parent_name': tag['parent_name'],
                        'city_level': tag['city_level']})
                assert cursor, 'targeting_tag not found'
                assert cursor['type'] == payload['type'], 'type not equal'


@pytest.mark.usefixtures('base')
class TestTsaCapabilities(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_capabilities_get)
    def test_01_capabilities_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'capabilities/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.usefixtures('base')
class TestTsaEstimation(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_estimation_get)
    def test_01_estimation_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'estimation/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            assert response['data']['approximate_count'], 'approximate_count error'
            assert response['data']['impression'], 'impression error'
            assert response['data']['min_bid_amount'], 'min_bid_amount error'
            assert response['data']['max_bid_amount'], 'max_bid_amount error'


@pytest.mark.usefixtures('base')
class TestTsaRealtimeCost(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_realtime_cost_get)
    def test_01_realtime_cost_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'realtime_cost/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.usefixtures('base')
class TestTsaImages(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_images_add)
    def test_01_images_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'images/add')
        files = {'image': open(payload['image'], 'rb')
                 if payload['image'] else ''}
        payload = {'account_id': get_account_id(payload=payload)}
        response = r.req('POST', url, data=payload, files=files)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.image'].find_one(
                {'image_id': response['data']['image_id']})
            assert cursor, 'image not found'
            assert cursor['signature'] == response['data']['signature'], 'signature not equal'
            assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
            assert cursor['type'] == response['data']['type'], 'type not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_images_get)
    def test_02_images_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'images/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = ongodb.sndo['tsa.image'].find_one(
                    {'image_id': tag['image_id']})
                assert cursor, 'image not found'
                assert cursor['signature'] == response['data']['signature'], 'signature not equal'
                assert cursor['preview_url'] == response['data']['preview_url'], 'preview_url not equal'
                assert cursor['width'] == response['data']['width'], 'width not equal'
                assert cursor['height'] == response['data']['height'], 'height not equal'
                assert cursor['file_size'] == response['data']['file_size'], 'file_size not equal'
                assert cursor['type'] == response['data']['type'], 'type not equal'


@pytest.mark.usefixtures('base')
class TestTsaVideo(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_video_add)
    def test_01_video_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'video/add')
        files = {'video': open(payload['video'], 'rb')
                 if payload['video'] else ''}
        payload = {'account_id': get_account_id(payload=payload)}
        response = r.req('POST', url, data=payload, files=files)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.video'].find_one(
                {'video_id': response['data']['video_id']})
            assert cursor, 'video not found'
            assert cursor['signature'] == response['data']['signature'], 'signature not equal'
            assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
            assert cursor['type'] == response['data']['type'], 'type not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_02_video_get)
    def test_02_video_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'video/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = ongodb.sndo['tsa.video'].find_one(
                    {'video_id': tag['video_id']})
                assert cursor, 'video not found'
                assert cursor['signature'] == response['data']['signature'], 'signature not equal'
                assert cursor['preview_url'] == response['data']['preview_url'], 'preview_url not equal'
                assert cursor['width'] == response['data']['width'], 'width not equal'
                assert cursor['height'] == response['data']['height'], 'height not equal'
                assert cursor['file_size'] == response['data']['file_size'], 'file_size not equal'
                assert cursor['type'] == response['data']['type'], 'type not equal'


@pytest.mark.usefixtures('base')
class TestTsaFundTransfer(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_transfer_add)
    def test_01_fund_transfer_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_transfer/add')
        # TODO verify variable is_repeated
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            assert response['data']['fund_type'] == payload['fund_type'], 'fund_type not equal'
            assert response['data']['amount'] == payload['amount'], 'amount not equal'
            assert response['data']['external_bill_no'] == payload['external_bill_no'], 'external_bill_no not equal'


@pytest.mark.usefixtures('base')
class TestTsaFunds(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_funds_get)
    def test_01_funds_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'funds/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.usefixtures('base')
class TestTsaFundStatementsDaily(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_statements_daily_get)
    def test_01_fund_statements_daily_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_statements_daily/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.usefixtures('base')
class TestTsaFundStatementsDetailed(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        tsa.test_01_fund_statements_detailed_get)
    def test_01_fund_statements_detailed_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'fund_statements_detailed/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'


@pytest.mark.usefixtures('base')
class TestTsAadcreatives2(object):

    @Log.logtestcase()
    @pytest.mark.parametrize('payload, res, test_title',
                             tsa.test_01_adcreatives2_add)
    def test_01_adcreatives2_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['campaign_id'] = get_campaign_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor_adcreative, 'adcreative not found'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor_ad, 'ad not found'

    @Log.logtestcase()
    @pytest.mark.parametrize('payload, res, test_title',
                             tsa.test_02_adcreatives2_update)
    def test_02_adcreatives2_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            assert cursor_adcreative, 'adcreative not found'
            assert cursor_adcreative['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert cursor_adcreative['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert cursor_adcreative['page_type'] == payload['page_type'], 'page_type not equal'
            assert cursor_adcreative['page_spec'] == payload['page_spec'], 'page_spec not equal'
            assert cursor_adcreative['deep_link_url'] == payload['deep_link_url'], 'deep_link_url not equal'
            assert cursor_adcreative['share_content_spec'] == payload['share_content_spec'], 'share_content_spec not equal'
            assert cursor_adcreative['dynamic_adcreative_spec'] == payload[
                'dynamic_adcreative_spec'], 'dynamic_adcreative_spec not equal'
            assert cursor_adcreative['multi_share_optimization_enabled'] == payload[
                'multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': payload['ad_id']})
            assert cursor_ad, 'ad not found'
            assert cursor_ad['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert cursor_ad['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor_ad['impression_tracking_url'] == payload['impression_tracking_url'], 'impression_tracking_url not equal'
            assert cursor_ad['click_tracking_url'] == payload['click_tracking_url'], 'click_tracking_url not equal'
            assert cursor_ad['feeds_interaction_enabled'] == payload['feeds_interaction_enabled'], 'feeds_interaction_enabled not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize('payload, res, test_title',
                             tsa.test_03_adcreatives2_delete)
    def test_03_adcreatives2_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['account_id'] = get_account_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            assert cursor_adcreative, 'adcreative not found'
            assert cursor_adcreative['is_deleted'], 'delete fail'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': payload['ad_id']})
            assert cursor_ad, 'ad not found'
            assert cursor_ad['is_deleted'], 'delete fail'
