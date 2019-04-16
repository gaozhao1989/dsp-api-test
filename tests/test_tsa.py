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
# global varibales
account_id = None
qualification_id = None
campaign_id = None
adgroup_id = None
adcreative_id = None
ad_id = None
targeting_id = None
external_bill_no = None


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
        assert response['data'], 'ind empty'


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
        url = urllib.parse.urljoin(addr, 'advertiser/update')
        payload['account_id'] = account_id if payload['account_id'] == 'global variable' else payload['account_id']
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
        payload['account_id'] = account_id if payload['account_id'] == 'global variable' else payload['account_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            if payload['account_id']:
                cursor = mongodb.sndo['tsa.account'].find_one(
                    {'account_id': payload['account_id']})
                assert cursor, 'advertiser not found'
                assert cursor['account_id'] == response['data']['list'][0]['account_id']
                assert cursor['daily_budget'] == response['data']['list'][0]['daily_budget'], 'daily_budget not equal'
                assert cursor['corporation_name'] == response['data']['list'][0]['corporation_name'], 'corporation_name not equal'
                assert cursor['certification_image_id'] == response['data']['list'][
                    0]['certification_image_id'], 'certification_image_id not equal'
                assert cursor['system_industry_id'] == response['data']['list'][0]['system_industry_id'], 'system_industry_id not equal'
                assert cursor['introduction_url'] == response['data']['list'][0]['introduction_url'], 'introduction_url not equal'
                assert cursor['individual_qualification'] == response['data']['list'][
                    0]['individual_qualification'], 'individual_qualification not equal'
                assert cursor['corporate_image_name'] == response['data']['list'][
                    0]['corporate_image_name'], 'corporate_image_name not equal'
                assert cursor['contact_person_telephone'] == response['data']['list'][
                    0]['contact_person_telephone'], 'contact_person_telephone not equal'
                assert cursor['contact_person_mobile'] == response['data']['list'][
                    0]['contact_person_mobile'], 'contact_person_mobile not equal'
                assert cursor['certification_number'] == response['data']['list'][
                    0]['certification_number'], 'certification_number not equal'
                assert cursor['sndo_ader_id'] == response['data']['list'][0]['sndo_ader_id'], 'individual_qualification not equal'
                assert cursor['wechat_spec'] == response['data']['list'][0]['wechat_spec'], 'wechat_spec not equal'
                assert cursor['websites'] == response['data']['list'][0]['websites'], 'websites not equal'
            else:
                cursor = mongodb.sndo['tsa.account'].find({})
                assert cursor, 'advertiser empty'


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
        url = urllib.parse.urljoin(addr, 'qualifications/update')
        payload['qualification_id'] = qualification_id if payload['qualification_id'] == 'global variable' else payload['qualification_id']
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
        url = urllib.parse.urljoin(addr, 'qualifications/delete')
        payload['qualification_id'] = qualification_id if payload['qualification_id'] == 'global variable' else payload['qualification_id']
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
        url = urllib.parse.urljoin(addr, 'campaigns/update')
        payload['campaign_id'] = campaign_id if payload['campaign_id'] == 'global variable' else payload['campaign_id']
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
        url = urllib.parse.urljoin(addr, 'campaigns/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'

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
        url = urllib.parse.urljoin(addr, 'campaigns/delete')
        payload['campaign_id'] = campaign_id if payload['campaign_id'] == 'global variable' else payload['campaign_id']
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
        # add new campaign
        if payload['campaign_id'] == 'global variable':
            response = r.req(
                'POST',
                'campaigns/add',
                json=tsa.test_01_campaigns_add[0][0])
            global campaign_id
            campaign_id = response['data']['campaign_id']
            payload['campaign_id'] == campaign_id
        # add new targeting
        if payload['targeting_id'] == 'global variable':
            response = r.req(
                'POST',
                'targeting/add',
                json=tsa.test_01_targeting_add[0][0])
            global targeting_id
            targeting_id = response['data']['targeting_id']
            payload['targeting_id'] == targeting_id
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
        url = urllib.parse.urljoin(addr, 'adgroups/add')
        payload['adgroup_id'] = adgroup_id if payload['adgroup_id'] == 'global variable' else payload['adgroup_id']
        # add new targeting
        if payload['targeting_id'] == 'global variable':
            response = r.req(
                'POST',
                'targeting/add',
                json=tsa.test_01_targeting_add[0][0])
            global targeting_id
            targeting_id = response['data']['targeting_id']
            payload['targeting_id'] == targeting_id
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
        url = urllib.parse.urljoin(addr, 'adgroups/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find({})
            assert cursor, 'adgroup empty'

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
        url = urllib.parse.urljoin(addr, 'adgroups/delete')
        payload['adgroup_id'] = adgroup_id if payload['adgroup_id'] == 'global variable' else payload['adgroup_id']
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
        if payload['adgroup_id'] == 'global variable':
            # add new campaign
            response = r.req(
                'POST',
                'campaigns/add',
                json=tsa.test_01_campaigns_add[0][0])
            campaign_id = response['data']['campaign_id']
            # add new adgroup
            payload_adgroup = tsa.test_01_adgroups_add[0][0]
            payload_adgroup['campaign_id'] = campaign_id
            response = r.req('POST', 'adgroups/add', json=payload_adgroup)
            global adgroup_id
            adgroup_id = response['data']['adgroup_id']
            # add new adcreative
            payload_adcreative = tsa.test_01_adcreatives_add[0][0]
            payload_adcreative['campaign_id'] = campaign_id
            response = r.req('POST', 'adgroups/add', json=payload_adcreative)
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
        url = urllib.parse.urljoin(addr, 'ads/add')
        payload['adgroup_id'] = adgroup_id if payload['adgroup_id'] == 'global variable' else payload['adgroup_id']
        payload['adcreative_id'] = adcreative_id if payload['adcreative_id'] == 'global variable' else payload['adcreative_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['ad_id']})
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
        url = urllib.parse.urljoin(addr, 'ads/update')
        payload['ad_id'] = ad_id if payload['ad_id'] == 'global variable' else payload['ad_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': payload['ad_id']})
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
        url = urllib.parse.urljoin(addr, 'ads/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            key, value = 'ad_id', ad_id
            assert str(response).find(
                "'{}': '{}'".format(
                    key, value)), 'ad not found'

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
        url = urllib.parse.urljoin(addr, 'ads/delete')
        payload['ad_id'] = ad_id if payload['ad_id'] == 'global variable' else payload['ad_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            assert cursor['is_deleted'] == True, 'delete fail'
            
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
        # add new campaign
        if payload['campaign_id'] == 'global variable':
            response = r.req(
                'POST',
                'campaigns/add',
                json=tsa.test_01_campaigns_add[0][0])
            global campaign_id
            campaign_id = response['data']['campaign_id']
            payload['campaign_id'] == campaign_id
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
            assert cursor['multi_share_optimization_enabled'] == payload['multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'
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
        url = urllib.parse.urljoin(addr, 'adcreatives/update')
        payload['adcreative_id'] = adcreative_id if payload['adcreative_id'] == 'global variable' else payload['adcreative_id']

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
            assert cursor['multi_share_optimization_enabled'] == payload['multi_share_optimization_enabled'], 'multi_share_optimization_enabled not equal'

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
        url = urllib.parse.urljoin(addr, 'adcreatives/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            if adcreative_id:
                key, value = 'adcreative_id', adcreative_id
                assert str(response).find(
                    "'{}': '{}'".format(
                        key, value)), 'adcreatives not found' 
            else:
                cursor = mongodb.sndo['tsa.adcreative'].find({'account':tsa.test_03_adcreatives_get[0][0]['account_id']})
                assert  cursor.count() == response['data']['page_info']['total_number'], 'total number not equal'
    
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
        url = urllib.parse.urljoin(addr, 'adcreatives/delete')
        payload['adcreative_id'] = adcreative_id if payload['adcreative_id'] == 'global variable' else payload['adcreative_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:    
            cursor = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': payload['adcreative_id']})
            assert cursor, 'adcreative not found'
            assert cursor['is_deleted'] == True, 'delete fail'
    
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
        url = urllib.parse.urljoin(addr, 'targeting/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:  
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': response['data']['targeting_id']})
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['targeting_name'] == payload['targeting_name'], 'targeting_name not equal'
            assert cursor['targeting'] == payload['targeting'],'targeting not equal'
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
        url = urllib.parse.urljoin(addr, 'targeting/update')
        payload['targeting_id'] = targeting_id if payload['targeting_id'] == 'global variable' else payload['targeting_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:  
            cursor = mongodb.sndo['tsa.targeting'].find_one(
                {'targeting_id': payload['targeting_id']})
            assert cursor['account_id'] == payload['account_id'], 'account_id not equal'
            assert cursor['targeting_name'] == payload['targeting_name'], 'targeting_name not equal'
            assert cursor['targeting'] == payload['targeting'],'targeting not equal'
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
        url = urllib.parse.urljoin(addr, 'targeting/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:  
            if targeting_id:
                key, value = 'targeting_id', targeting_id
                assert str(response).find(
                    "'{}': '{}'".format(
                        key, value)), 'targeting not found' 
            else:
                cursor = mongodb.sndo['tsa.targeting'].find({'account':tsa.test_03_targeting_get[0][0]['account_id']})
                assert  cursor.count() == response['data']['page_info']['total_number'], 'total number not equal'

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
                {'id': tag['id'],'name':tag['name'],'parent_id':tag['parent_id'],'parent_name':tag['parent_name'],'city_level':tag['city_level']})
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
        files = {'image': open(payload['image'], 'rb') if payload['image'] else ''}
        payload = {'account_id':payload['account_id']}
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
        files = {'video': open(payload['video'], 'rb') if payload['video'] else ''}
        payload = {'account_id':payload['account_id']}
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
        url = urllib.parse.urljoin(addr, 'fund_transfer/add')
        # set global variable external_bill_no
        global external_bill_no
        if payload['external_bill_no'] == 'global variable':
            payload['external_bill_no'] = external_bill_no
            is_repeated = True
        else:
            external_bill_no = payload['external_bill_no']
            is_repeated = False
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            assert response['data']['fund_type'] == payload['fund_type'], 'fund_type not equal'
            assert response['data']['amount'] == payload['amount'], 'amount not equal'
            assert response['data']['external_bill_no'] == payload['external_bill_no'], 'external_bill_no not equal'
            assert response['data']['is_repeated'] == is_repeated, 'is_repeated not equal'

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
        url = urllib.parse.urljoin(addr, 'funds/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        #TODO verify response

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
        url = urllib.parse.urljoin(addr, 'fund_statements_daily/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        #TODO verify response

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
        url = urllib.parse.urljoin(addr, 'fund_statements_detailed/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        #TODO verify response

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
        url = urllib.parse.urljoin(addr, 'adcreatives2/add')
        payload = {
            'account_id': account_id,
            'campaign_id': campaign_id,
            'adcreative_name': adcreative_name,
            'adcreative_template_id': adcreative_template_id,
            'adcreative_elements': adcreative_elements,
            'site_set': site_set,
            'page_spec': page_spec,
            'promoted_object_type': promoted_object_type,
            'page_type': page_type,
            'adgroup_id': adgroup_id,
            'ad_name': ad_name,
            'configured_status': configured_status}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor_adcreative, 'can not found adcreative'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor_ad, 'can not found ad'
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'adcreatives2/delete'),
                headers=headers,
                json={
                    'account_id': account_id,
                    'adcreative_id': response['data']['adcreative_id'],
                    'ad_id': response['data']['ad_id']})
            mongodb.sndo['tsa.adcreative'].delete_one(
                {'adcreative_id': response['data']['adcreative_id']})
            mongodb.sndo['tsa.ad'].delete_one(
                {'ad_id': response['data']['ad_id']})

@pytest.mark.usefixtures('base')
class TestTsaApi(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id, file_path, res_result, result_code, result_message, test_title',
        tsa.test_01_images_add)
    def test_01_images_add(
            self,
            account_id,
            file_path,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'images/add')
        payload = {'account_id': account_id}
        files = {'image': open(file_path, 'rb') if file_path else ''}
        try:
            response = json.loads(requests.post(
                url, data=payload, files=files).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['tsa.image'].find_one(
                {'signature': response['data']['signature']})
            assert cursor, 'can not found image'
            assert cursor['signature'] == response['data']['signature'], 'signature not equal'
            assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
            assert cursor['image_id'] == response['data']['image_id'], 'image id not equal'
            assert cursor['type'] == response['data']['type'], 'type not equal'
            mongodb.sndo['tsa.image'].delete_one(
                {'signature': response['data']['signature']})

    @Log.logtestcase()
    @pytest.mark.parametrize('corporation_name,\
    certification_image_id, system_industry_id, introduction_url,\
    identification_front_image_id, identification_back_image_id,\
    corporate_image_name, contact_person_telephone,\
    contact_person_mobile, certification_number, sndo_ader_id,\
    res_result, result_code, result_message, test_title', tsa.test_02_advertiser_add)
    def test_02_advertiser_add(
            self,
            corporation_name,
            certification_image_id,
            system_industry_id,
            introduction_url,
            identification_front_image_id,
            identification_back_image_id,
            corporate_image_name,
            contact_person_telephone,
            contact_person_mobile,
            certification_number,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'advertiser/add')
        idv_params = {
            'identification_front_image_id': identification_front_image_id,
            'identification_back_image_id': identification_back_image_id
        }
        idv_params = {k: v for k, v in idv_params.items() if v is not ''}
        payload = {
            'corporation_name': corporation_name,
            'certification_image_id': certification_image_id,
            'system_industry_id': system_industry_id,
            'introduction_url': introduction_url,
            'individual_qualification': idv_params if bool(idv_params) else '',
            'corporate_image_name': corporate_image_name,
            'contact_person_telephone': contact_person_telephone,
            'contact_person_mobile': contact_person_mobile,
            'certification_number': certification_number,
            'sndo_ader_id': sndo_ader_id
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor = mongodb.sndo['tsa.account'].find_one(
                {'account_id': response['data']['account_id']})
            assert curosr, 'can not found account'
            # TODO db variables verify
            mongodb.sndo['tsa.account'].delete_one(
                {'account_id': response['data']['account_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize('account_id, campaign_name,\
    campaign_type, promoted_object_type, daily_budget,\
    configured_status, speed_mode, sndo_ader_id,\
    res_result, result_code, result_message, test_title',
                             tsa.test_03_campaigns_add)
    def test_03_campaigns_add(
            self,
            account_id,
            campaign_name,
            campaign_type,
            promoted_object_type,
            daily_budget,
            configured_status,
            speed_mode,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'campaigns/add')
        payload = {
            'account_id': account_id,
            'campaign_name': campaign_name,
            'campaign_type': campaign_type,
            'promoted_object_type': promoted_object_type,
            'daily_budget': daily_budget,
            'configured_status': configured_status,
            'speed_mode': speed_mode,
            'sndo_ader_id': sndo_ader_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor = mongodb.sndo['tsa.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            assert cursor, 'can not found campaign'
            assert cursor['account_id'] == account_id, 'account_id not equal'
            assert cursor['campaign_name'] == campaign_name, 'campaign_name not equal'
            assert cursor['campaign_type'] == campaign_type, 'campaign_type not equal'
            assert cursor['promoted_object_type'] == promoted_object_type, 'promoted_object_type not equal'
            assert cursor['daily_budget'] == daily_budget, 'daily_budget not equal'
            assert cursor['configured_status'] == configured_status if configured_status else 'AD_STATUS_NORMAL', 'configured_status not equal'
            assert cursor['speed_mode'] == speed_mode if speed_mode else 'SPEED_MODE_STANDARD', 'speed_mode not equal'
            assert cursor['sndo_ader_id'] == sndo_ader_id, 'sndo_ader_id not equal'
            assert cursor['is_deleted'] == False, 'is_deleted not equal'
            # delete campaign
            if configured_status == 'AD_STATUS_NORMAL':
                requests.post(
                    urllib.parse.urljoin(
                        self.addr,
                        'campaigns/update'),
                    headers=headers,
                    json={
                        'account_id': account_id,
                        'campaign_id': response['data']['campaign_id'],
                        'configured_status': 'AD_STATUS_SUSPEND'})
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'campaigns/delete'),
                headers=headers,
                json={
                    'account_id': account_id,
                    'campaign_id': response['data']['campaign_id']})
            mongodb.sndo['tsa.campaign'].delete_one(
                {'campaign_id': response['data']['campaign_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize('account_id, campaign_id, adgroup_name,\
    site_set, promoted_object_type, begin_date, end_date,\
    billing_event, bid_amount, optimization_goal, targeting_id,\
    time_series, res_result, result_code, result_message, test_title',
                             tsa.test_04_adgroups_add)
    def test_04_adgroups_add(
            self,
            account_id,
            campaign_id,
            adgroup_name,
            site_set,
            promoted_object_type,
            begin_date,
            end_date,
            billing_event,
            bid_amount,
            optimization_goal,
            targeting_id,
            time_series,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adgroups/add')
        payload = {
            'account_id': account_id,
            'campaign_id': campaign_id,
            'adgroup_name': adgroup_name,
            'site_set': site_set,
            'promoted_object_type': promoted_object_type,
            'begin_date': begin_date,
            'end_date': end_date,
            'billing_event': billing_event,
            'bid_amount': bid_amount,
            'optimization_goal': optimization_goal,
            'targeting_id': targeting_id,
            'time_series': time_series}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor = mongodb.sndo['tsa.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor, 'can not found adgroup'
            assert cursor['account_id'] == account_id, 'account_id not equal'
            assert cursor['campaign_id'] == campaign_id, 'campaign_id not equal'
            assert cursor['adgroup_name'] == adgroup_name, 'adgroup_name not equal'
            assert cursor['site_set'] == site_set, 'site_set not equal'
            assert cursor['promoted_object_type'] == promoted_object_type, 'promoted_object_type not equal'
            assert cursor['begin_date'] == begin_date, 'begin_date not equal'
            assert cursor['end_date'] == end_date, 'end_date not equal'
            assert cursor['billing_event'] == billing_event, 'billing_event not equal'
            assert cursor['bid_amount'] == bid_amount, 'bid_amount not equal'
            assert cursor['optimization_goal'] == optimization_goal, 'optimization_goal not equal'
            assert cursor['targeting_id'] == targeting_id, 'targeting_id not equal'
            assert len(cursor['time_series']
                       ) == 336, 'time_series length incorrect'
            # delete adgroup
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'adgroups/delete'),
                headers=headers,
                json={
                    'account_id': account_id,
                    'adgroup_id': response['data']['adgroup_id']})
            mongodb.sndo['tsa.adgroup'].delete_one(
                {'adgroup_id': response['data']['adgroup_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize('account_id, campaign_id, adcreative_name,\
    adcreative_template_id, adcreative_elements, site_set, page_spec,\
    promoted_object_type, page_type, adgroup_id, ad_name, configured_status,\
    res_result, result_code, result_message, test_title', tsa.test_05_adcreatives2_add)
    def test_05_adcreatives2_add(
            self,
            account_id,
            campaign_id,
            adcreative_name,
            adcreative_template_id,
            adcreative_elements,
            site_set,
            page_spec,
            promoted_object_type,
            page_type,
            adgroup_id,
            ad_name,
            configured_status,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adcreatives2/add')
        payload = {
            'account_id': account_id,
            'campaign_id': campaign_id,
            'adcreative_name': adcreative_name,
            'adcreative_template_id': adcreative_template_id,
            'adcreative_elements': adcreative_elements,
            'site_set': site_set,
            'page_spec': page_spec,
            'promoted_object_type': promoted_object_type,
            'page_type': page_type,
            'adgroup_id': adgroup_id,
            'ad_name': ad_name,
            'configured_status': configured_status}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor_adcreative, 'can not found adcreative'
            cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor_ad, 'can not found ad'
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'adcreatives2/delete'),
                headers=headers,
                json={
                    'account_id': account_id,
                    'adcreative_id': response['data']['adcreative_id'],
                    'ad_id': response['data']['ad_id']})
            mongodb.sndo['tsa.adcreative'].delete_one(
                {'adcreative_id': response['data']['adcreative_id']})
            mongodb.sndo['tsa.ad'].delete_one(
                {'ad_id': response['data']['ad_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id, promoted_object_type, promoted_object_id, res_result,result_code,result_message,test_title',
        tsa.test_06_promoted_objects_add)
    def test_06_promoted_objects_add(
            self,
            account_id,
            promoted_object_type,
            promoted_object_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'promoted_objects/add')
        payload = {
            'account_id': account_id,
            'promoted_object_type': promoted_object_type,
            'promoted_object_id': promoted_object_id}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            assert response['data']['promoted_object_id'] == promoted_object_id

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id, targeting_name, res_result,result_code,result_message,test_title',
        tsa.test_07_targeting_add)
    def test_07_targeting_add(
            self,
            account_id,
            targeting_name,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'targeting/add')
        payload = {
            'account_id': account_id,
            'targeting_name': targeting_name}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert response['data']['targeting_id']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_08_advertiser_get)
    def test_08_advertiser_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'advertiser/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_09_campaigns_get)
    def test_09_campaigns_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'campaigns/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_10_images_get)
    def test_10_images_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'images/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_11_targeting_get)
    def test_11_targeting_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'targeting/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,adgroup,adcreative,targeting, res_result,result_code,result_message,test_title',
        tsa.test_12_estimation_get)
    def test_12_estimation_get(
            self,
            account_id,
            adgroup,
            adcreative,
            targeting,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'estimation/get')
        payload = {
            'account_id': account_id,
            'adgroup': adgroup,
            'adcreative': adcreative,
            'targeting': targeting
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,adgroup_id,adcreative_id,ad_name,configured_status,impression_tracking_url,click_tracking_url,feeds_interaction_enabled,sndo_ader_id, res_result,result_code,result_message,test_title',
        tsa.test_13_ads_add)
    def test_13_ads_add(
            self,
            account_id,
            adgroup_id,
            adcreative_id,
            ad_name,
            configured_status,
            impression_tracking_url,
            click_tracking_url,
            feeds_interaction_enabled,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'ads/add')
        payload = {
            'account_id': account_id,
            'adgroup_id': adgroup_id,
            'adcreative_id': adcreative_id,
            'ad_name': ad_name,
            'configured_status': configured_status,
            'impression_tracking_url': impression_tracking_url,
            'click_tracking_url': click_tracking_url,
            'feeds_interaction_enabled': feeds_interaction_enabled,
            'sndo_ader_id': sndo_ader_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_14_adgroups_get)
    def test_14_adgroups_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adgroups/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size, res_result,result_code,result_message,test_title',
        tsa.test_15_adcreatives_get)
    def test_15_adcreatives_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adcreatives/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        assert len(response['data']['list']
                   ) == response['data']['page_info']['total_number']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,filtering,page,page_size,site_set,promoted_object_type, res_result,result_code,result_message,test_title',
        tsa.test_16_adcreative_templates_get)
    def test_16_adcreative_templates_get(
            self,
            account_id,
            filtering,
            page,
            page_size,
            site_set, promoted_object_type,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adcreative_templates/get')
        payload = {
            'account_id': account_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size,
            'site_set': site_set, 'promoted_object_type': promoted_object_type
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id, res_result,result_code,result_message,test_title',
        tsa.test_17_funds_get)
    def test_17_funds_get(
            self,
            account_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'funds/get')
        payload = {
            'account_id': account_id
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,fund_type,amount,transfer_type,external_bill_no,memo, res_result,result_code,result_message,test_title',
        tsa.test_18_fund_transfer_add)
    def test_18_fund_transfer_add(
            self,
            account_id,
            fund_type, amount, transfer_type, external_bill_no, memo,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'fund_transfer/add')
        payload = {
            'account_id': account_id,
            'fund_type': fund_type,
            'amount': amount,
            'transfer_type': transfer_type,
            'external_bill_no': external_bill_no,
            'memo': memo}
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            assert fund_type == response['data']['fund_type']
            assert amount == response['data']['amount']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id, res_result,result_code,result_message,test_title',
        tsa.test_19_ads_get)
    def test_19_ads_get(
            self,
            account_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'ads/get')
        payload = {
            'account_id': account_id
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,qualification_type,filtering,fields, res_result,result_code,result_message,test_title',
        tsa.test_20_qualifications_get)
    def test_20_qualifications_get(
            self,
            account_id,
            qualification_type, filtering, fields,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'qualifications/get')
        payload = {
            'account_id': account_id,
            'qualification_type': qualification_type,
            'filtering': filtering,
            'fields': fields}
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,qualification_type,qualification_id, res_result,result_code,result_message,test_title',
        tsa.test_21_qualifications_delete)
    def test_21_qualifications_delete(
            self,
            account_id,
            qualification_type, qualification_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        response = json.loads(requests.post(
            urllib.parse.urljoin(
                self.addr,
                'qualifications/add'),
            json={
                'account_id': account_id,
                'qualification_type': qualification_type,
                'qualification_spec': {
                    'industry_spec': {
                        'system_industry_id': 21474836586,
                        'qualification_code': 'A150',
                        'image_id_list': ['3512']}}}).content)
        self.log.info(response)
        url = urllib.parse.urljoin(self.addr, 'qualifications/delete')
        payload = {
            'account_id': account_id,
            'qualification_type': qualification_type,
            'qualification_id': response['data']['qualification_id']}
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor is None

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,qualification_type,qualification_spec, res_result,result_code,result_message,test_title',
        tsa.test_22_qualifications_add)
    def test_22_qualifications_add(
            self,
            account_id,
            qualification_type, qualification_spec,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'qualifications/add')
        payload = {
            'account_id': account_id,
            'qualification_type': qualification_type,
            'qualification_spec': qualification_spec
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            cursor = mongodb.sndo['tsa.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor, 'qualification not found'
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'qualifications/delete'),
                headers=headers,
                json={
                    'account_id': account_id,
                    'qualification_type': qualification_type,
                    'qualification_id': response['data']['qualification_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,adcreative_id, ad_id, res_result,result_code,result_message,test_title',
        tsa.test_23_adcreatives2_delete)
    def test_23_adcreatives2_delete(
            self,
            account_id,
            adcreative_id, ad_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        response = json.loads(
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'adcreatives2/add'),
                json={
                    'account_id': account_id,
                    'campaign_id': 29131,
                    'adcreative_name': 'test_delete_adcreative',
                    'adcreative_template_id': 529,
                    'adcreative_elements': {
                        'image': '3519',
                        'title': 'test title'},
                    'site_set': ['SITE_SET_QQCLIENT'],
                    'page_spec': {
                        'page_id': 0,
                        'page_url': 'https://www.qq.com'},
                    'promoted_object_type': 'PROMOTED_OBJECT_TYPE_LINK',
                    'page_type': 'PAGE_TYPE_DEFAULT',
                    'adgroup_id': 41887,
                    'ad_name': 'test_delete_ad',
                    'configured_status': 'AD_STATUS_SUSPEND'}).content)
        url = urllib.parse.urljoin(self.addr, 'adcreatives2/delete')
        payload = {
            'account_id': account_id,
            'adcreative_id': response['data']['adcreative_id'],
            'ad_id': response['data']['ad_id']
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
        if res_result:
            if res_result:
                cursor_adcreative = mongodb.sndo['tsa.adcreative'].find_one(
                    {'adcreative_id': response['data']['adcreative_id']})
                assert cursor_adcreative, 'can not found adcreative'
                cursor_ad = mongodb.sndo['tsa.ad'].find_one(
                    {'ad_id': response['data']['ad_id']})
                assert cursor_ad, 'can not found ad'
                mongodb.sndo['tsa.adcreative'].delete_one(
                    {'adcreative_id': response['data']['adcreative_id']})
                mongodb.sndo['tsa.ad'].delete_one(
                    {'ad_id': response['data']['ad_id']})

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'account_id,qualification_type,qualification_id,image_id_list, res_result,result_code,result_message,test_title',
        tsa.test_24_qualifications_update)
    def test_24_qualifications_update(
            self,
            account_id,
            qualification_type, qualification_id, image_id_list,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'qualifications/update')
        payload = {
            'account_id': account_id,
            'qualification_type': qualification_type,
            'qualification_id': qualification_id,
            'image_id_list': image_id_list
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        headers = {
            'Content-Type': 'application/json'
        }
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, headers=headers, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code']
        assert result_message in response['message']
