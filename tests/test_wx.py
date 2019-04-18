import json
import random
import urllib.parse
import requests
import pytest
from parameters import wx
from utils import Log, Requests, ConfigParser

cp = ConfigParser()
addr = cp.get_wx_addr()
log = Log.getlog('wxTest')
r = Requests()
# global variables
qualification_id = None
transfter_order_id = None
campaign_id = None
adgroup_id = None
adcreative_id = None
ad_id = None
image_id = None
audience_id =None
custom_audience_file_id=None


def get_campaign_id(glo=True, payload={'campaign_id': 'global variable'}):
    if payload['campaign_id'] == 'global variable':
        global campaign_id
        if campaign_id is None:
            add_cam_payload = wx.test_01_campaigns_add[0][0]
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


def get_adgroup_id(glo=True, payload={'adgroup_id': 'global variable'}):
    if payload['adgroup_id'] == 'global variable':
        global adgroup_id
        if adgroup_id is None:
            add_adgroup_payload = wx.test_01_adgroups_add[0][0]
            add_adgroup_payload['campaign_id'] = get_campaign_id(
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


def get_adcreative_id(glo=True, payload={'adcreative_id': 'global variable'}):
    if payload['adcreative_id'] == 'global variable':
        global adcreative_id
        if adcreative_id is None:
            add_adcreative_payload = wx.test_01_adcreatives_add[0][0]
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

def get_ad_id(glo=True,payload={'ad_id':'global variable'}):
    if payload['ad_id'] == 'global variable':
        global ad_id
        if ad_id is None:
            add_ad_payload = wx.test_01_ads_add[0][0]
            add_ad_payload['adgroup_id'] = get_adgroup_id(
                payload=add_ad_payload)
            add_ad_payload['adcreative_id'] = get_adcreative_id(payload=add_ad_payload)
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

def get_image_id(glo=True,payload={'image_id':'global variable'}):
    if payload['image_id'] == 'global variable':
        global image_id
        if image_id is None:
            add_image_payload = wx.test_01_images_add[0][0]
            url = urllib.parse.urljoin(addr, 'images/add')
            response = r.req(
                'POST',
                url,
                json=add_image_payload)
            if glo:
                image_id = response['data']['image_id']
    else:
        return payload['image_id']

def get_audience_id(glo=True,payload={'audience_id':'global variable'}):
    if payload['audience_id'] == 'global variable':
        global audience_id
        if audience_id is None:
            add_audience_payload = wx.test_01_custom_audiences_add[0][0]
            url = urllib.parse.urljoin(addr, 'custom_audiences/add')
            response = r.req(
                'POST',
                url,
                json=add_audience_payload)
            if glo:
                audience_id = response['data']['audience_id']
    else:
        return payload['audience_id']

@pytest.mark.userfixtures('base')
class TestWxApiAdvertiser(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_advertiser_add)
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
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            assert cursor, 'advertiser not found'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_advertiser_update)
    def test_02_advertiser_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            assert cursor, 'advertiser not found'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_advertiser_get)
    def test_03_advertiser_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'advertiser/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            assert cursor, 'advertiser not found'


@pytest.mark.userfixtures('base')
class TestWxApiQualifications(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_qualifications_add)
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
            cursor = mongodb.sndo['wx.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            assert cursor, 'qualification not found'
            global qualification_id
            qualification_id = response['data']['qualification_id']
            assert cursor['appid'] == payload['appid'], 'appid not equal'
            assert cursor['qualification_name'] == payload['qualification_name'], 'qualification_name not equal'
            assert cursor['qualification_image_id'] == payload['qualification_image_id'], 'qualification_image_id not equal'
            assert cursor['qualification_type'] == payload['qualification_type'], 'qualification_type not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_qualifications_get)
    def test_02_qualifications_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'qualifications/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.account.qualification'].find_one(
                    {'qualification_id': tag['qualification_id']})
                assert cursor, 'qualification not found'
                assert cursor['qualification_name'] == tag['qualification_name'], 'qualification_name not equal'
                assert cursor['qualification_type'] == tag['qualification_type'], 'qualification_type not equal'
                assert cursor['qualification_image'] == tag['qualification_image'], 'qualification_image not equal'
                assert cursor['qualification_status'] == tag['qualification_status'], 'qualification_status not equal'
                assert cursor['valid_date'] == tag['valid_date'], 'valid_date not equal'

    # Notice: qualification in STATUS_PENDING status not allowed to be deleted.
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_qualifications_delete)
    def test_03_qualifications_delete(
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
            cursor = mongodb.sndo['wx.account.qualification'].find_one(
                {'qualification_id': qualification_id})
            assert cursor is None, 'delete failed'


@pytest.mark.userfixtures('base')
class TestWxApiSpEntrustment(object):

    # Notice: no resources now
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_sp_entrustment_add)
    @pytest.mark.skip(reason='no resources')
    def test_01_sp_entrustment_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'sp_entrustment/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_sp_entrustment_get)
    def test_02_sp_entrustment_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'sp_entrustment/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            assert cursor, 'sp_entrustment not found'


@pytest.mark.userfixtures('base')
class TestWxApiFundTransfer(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_fund_transfer_add)
    def test_01_fund_transfer_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'fund_transfer/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            global transfter_order_id
            transfter_order_id = response['data']['external_bill_no']
            assert payload['amount'] == response['data']['amount']
            assert payload['external_bill_no'] in response['data']['external_bill_no']
            assert response['data']['is_repeated'] == False


@pytest.mark.userfixtures('base')
class TestWxApiFunds(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_funds_get)
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


@pytest.mark.userfixtures('base')
class TestWxApiFundStatementsDetailed(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_fund_statements_detailed_get)
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
        if res['result']:
            key, value = 'order_id', transfter_order_id
            assert str(response).find(
                "'{}': '{}'".format(
                    key, value)), 'not found'


@pytest.mark.userfixtures('base')
class TestWxApiCampaigns(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_campaigns_add)
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
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            assert cursor, 'campaign not found'
            global campaign_id
            campaign_id = response['data']['campaign_id']
            assert cursor['campaign_name'] == payload['campaign_name'], 'campaign_name not equal'
            assert cursor['campaign_type'] == payload['campaign_type'], 'campaign_type not equal'
            assert cursor['product_type'] == payload['product_type'], 'product_type not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor['daily_budget'] == (
                payload['daily_budget'] if payload['daily_budget'] else 0), 'daily_budget not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_campaigns_get)
    def test_02_campaigns_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'campaigns/get')
        payload['campaign_id'] = campaign_id if payload['campaign_id'] == 'global variable' else payload['campaign_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['lit']:
                cursor = mongodb.sndo['wx.campaign'].find_one(
                    {'campaign_id': tag['campaign_id']})
                assert cursor, 'campaign not found'
                assert cursor['campaign_name'] == tag['campaign_name'], 'campaign_name not equal'
                assert cursor['configured_status'] == tag['configured_status'], 'configured_status not equal'
                assert cursor['campaign_type'] == tag['campaign_type'], 'campaign_type not equal'
                assert cursor['product_type'] == tag['product_type'], 'product_type not equal'
                assert cursor['daily_budget'] == tag['daily_budget'], 'daily_budget not equal'
                assert cursor['budget_reach_date'] == tag['budget_reach_date'], 'budget_reach_date not equal'
                assert cursor['created_time'] == tag['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'], 'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_campaigns_update)
    def test_03_campaigns_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        bf_cursor = mongodb.sndo['wx.campaign'].find_one(
            {'appid': payload['appid'], 'campaign_id': campaign_id})
        url = urllib.parse.urljoin(addr, 'campaigns/update')
        payload['campaign_id'] = campaign_id if payload['campaign_id'] == 'global variable' else payload['campaign_id']
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            af_cursor = mongodb.sndo['wx.campaign'].find_one(
                {'appid': payload['appid'], 'campaign_id': payload['campaign_id']})
            assert af_cursor, 'campaign not found'
            assert af_cursor['campaign_name'] == payload['campaign_name'] if payload['campaign_name'] else bf_cursor['campaign_name']
            assert af_cursor['configured_status'] == payload['configured_status'] if payload[
                'configured_status'] else bf_cursor['configured_status']
            assert str(
                af_cursor['daily_budget']) == str(
                payload['daily_budget']) if str(
                payload['daily_budget']) else str(
                bf_cursor['daily_budget'])

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_04_campaigns_delete)
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
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'appid': payload['appid'], 'campaign_id': payload['campaign_id']})
            assert cursor, 'campaign not found'
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.userfixtures('base')
class TestWxApiAdgroups(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_adgroups_add)
    def test_01_adgroups_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor, 'adgroup not found'
            global adgroup_id
            adgroup_id = response['data']['adgroup_id']
            assert cursor['appid'] == payload['appid'], 'appid not equal'
            assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert cursor['adgroup_name'] == payload['adgroup_name'], 'adgroup_name not equal'
            assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert cursor['product_type'] == payload['product_type'], 'product_type not equal'
            assert cursor['targeting'] == payload['targeting'], 'targeting not equal'
            assert cursor['optimization_goal'] == payload['optimization_goal'], 'optimization_goal not equal'
            assert cursor['billing_event'] == payload['billing_event'], 'billing_event not equal'
            assert cursor['bid_amount'] == payload['bid_amount'], 'bid_amount not equal'
            assert cursor['begin_date'] == payload['begin_date'], 'begin_date not equal'
            assert cursor['end_date'] == payload['end_date'], 'end_date not equal'
            assert cursor['time_series'] == payload['time_series'], 'time_series not equal'
            assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
            assert cursor['product_refs_id'] == payload['product_refs_id'], 'product_refs_id not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_adgroups_update)
    def test_02_adgroups_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor, 'adgroup not found'
            assert cursor['adgroup_name'] == payload['adgroup_name'], 'adgroup_name not equal'
            assert cursor['targeting'] == payload['targeting'], 'targeting not equal'
            assert cursor['bid_amount'] == payload['bid_amount'], 'bid_amount not equal'
            assert cursor['begin_date'] == payload['begin_date'], 'begin_date not equal'
            assert cursor['end_date'] == payload['end_date'], 'end_date not equal'
            assert cursor['time_series'] == payload['time_series'], 'time_series not equal'
            assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_adgroups_get)
    def test_03_adgroups_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        if 'adgroup_id' in payload:
            payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.adgroup'].find_one(
                    {'adgroup_id': tag['adgroup_id']})
                assert cursor, 'adgroup not found'
                assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
                assert cursor['adgroup_name'] == payload['adgroup_name'], 'adgroup_name not equal'
                assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
                assert cursor['product_type'] == payload['product_type'], 'product_type not equal'
                assert cursor['targeting'] == payload['targeting'], 'targeting not equal'
                assert cursor['optimization_goal'] == payload['optimization_goal'], 'optimization_goal not equal'
                assert cursor['billing_event'] == payload['billing_event'], 'billing_event not equal'
                assert cursor['bid_amount'] == payload['bid_amount'], 'bid_amount not equal'
                assert cursor['begin_date'] == payload['begin_date'], 'begin_date not equal'
                assert cursor['end_date'] == payload['end_date'], 'end_date not equal'
                assert cursor['time_series'] == payload['time_series'], 'time_series not equal'
                assert cursor['daily_budget'] == payload['daily_budget'], 'daily_budget not equal'
                assert cursor['product_refs_id'] == payload['product_refs_id'], 'product_refs_id not equal'
                assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
                assert cursor['system_status'] == payload['system_status'], 'system_status not equal'
                assert cursor['reject_message'] == payload['reject_message'], 'reject_message not equal'
                assert cursor['created_time'] == payload['created_time'], 'created_time not equal'
                assert cursor['last_modified_time'] == payload['last_modified_time'], 'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_04_adgroups_delete)
    def test_04_adgroups_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adgroups/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': payload['adgroup_id']})
            assert cursor, 'adgroup not found'
            assert cursor['is_deleted'], 'delete fail'


@pytest.mark.usefixtures('base')
class TestWxApiAdcreatives(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_adcreatives_add)
    def test_01_adcreatives_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['campaign_id'] = get_campaign_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor, 'adcreative not found'
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            assert cursor['appid'] == payload['appid'], 'appid not equal'
            assert cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert cursor['adcreative_template_id'] == payload['adcreative_template_id'], 'adcreative_template_id not equal'
            assert cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert cursor['destination_url'] == payload['destination_url'], 'destination_url not equal'
            assert cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert cursor['product_type'] == payload['product_type'], 'product_type not equal'
            assert cursor['product_refs_id'] == payload['product_refs_id'], 'product_refs_id not equal'
            assert cursor['share_info'] == payload['share_info'], 'share_info not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_adcreatives_update)
    def test_02_adcreatives_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor, 'adcreative not found'
            assert cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert cursor['destination_url'] == payload['destination_url'], 'destination_url not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_adcreatives_get)
    def test_03_adcreatives_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        if 'adcreative_id' in payload:
            payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.adcreative'].find_one(
                    {'adcreative_id': tag['adcreative_id']})
                assert cursor, 'adcreative not found'
                assert cursor['campaign_id'] == tag['campaign_id'],'campaign_id not equal'
                assert cursor['adcreative_name'] == tag['adcreative_name'],'adcreative_name not equal'
                assert cursor['adcreative_template_id'] == tag['adcreative_template_id'],'adcreative_template_id not equal'
                assert cursor['adcreative_elements'] == tag['adcreative_elements'],'adcreative_elements not equal'
                assert cursor['destination_url'] == tag['destination_url'],'destination_url not equal'
                assert cursor['site_set'] == tag['site_set'],'site_set not equal'
                assert cursor['product_type'] == tag['product_type'],'product_type not equal'
                assert cursor['product_refs_id'] == tag['product_refs_id'],'product_refs_id not equal'
                assert cursor['created_time'] == tag['created_time'],'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'],'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_04_adcreatives_delete)
    def test_04_adcreatives_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert cursor, 'adcreative not found'
            assert cursor['is_deleted'], 'delete fail'

@pytest.mark.usefixtures('base')
class TestWxApiAds(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_ads_add)
    def test_01_ads_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            global ad_id
            ad_id = response['data']['ad_id']
            assert cursor['appid'] == payload['appid'], 'appid not equal'
            assert cursor['adgroup_id'] == payload['adgroup_id'], 'adgroup_id not equal'
            assert cursor['adcreative_id'] == payload['adcreative_id'], 'adcreative_id not equal'
            assert cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_ads_update)
    def test_02_ads_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            assert cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_ads_get)
    def test_03_ads_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        if 'ad_id' in payload:
            payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.ad'].find_one(
                    {'ad_id': tag['ad_id']})
                assert cursor, 'ad not found'
                assert cursor['campaign_id'] == tag['campaign_id'],'campaign_id not equal'
                assert cursor['adgroup_id'] == tag['adgroup_id'],'adgroup_id not equal'
                assert cursor['ad_name'] == tag['ad_name'],'ad_name not equal'
                assert cursor['adcreative'] == tag['adcreative'],'adcreative not equal'
                assert cursor['configured_status'] == tag['configured_status'],'configured_status not equal'
                assert cursor['system_status'] == tag['system_status'],'system_status not equal'
                assert cursor['reject_message'] == tag['reject_message'],'reject_message not equal'
                assert cursor['created_time'] == tag['created_time'],'created_time not equal'
                assert cursor['last_modified_time'] == tag['last_modified_time'],'last_modified_time not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_04_ads_delete)
    def test_04_ads_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'ads/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert cursor, 'ad not found'
            assert cursor['is_deleted'], 'delete fail'

@pytest.mark.usefixtures('base')
class TestWxApiImages(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_images_add)
    def test_01_images_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        files = {'image': open(payload['image'], 'rb')
                 if payload['image'] else ''}
        payload = {'appid': payload['appid']}
        url = urllib.parse.urljoin(addr, 'images/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            cursor = mongodb.sndo['wx.image'].find_one(
                {'image_id': response['data']['image_id']})
            assert cursor, 'image not found'
            global image_id
            image_id = response['data']['image_id']
            assert cursor['signature'] == response['data']['signature'], 'signature not equal'
            assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
            assert cursor['type'] == response['data']['type'], 'type not equal'
            assert cursor['width'] == response['data']['width'], 'width not equal'
            assert cursor['height'] == response['data']['height'], 'height not equal'
            assert cursor['size'] == response['data']['size'], 'size not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_images_get)
    def test_02_images_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        if 'image_id' in payload:
            payload['image_id'] = get_image_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'images/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.image'].find_one(
                {'image_id': tag['image_id']})
                assert cursor, 'image not found'
                assert cursor['signature'] == response['data']['signature'], 'signature not equal'
                assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
                assert cursor['type'] == response['data']['type'], 'type not equal'
                assert cursor['width'] == response['data']['width'], 'width not equal'
                assert cursor['height'] == response['data']['height'], 'height not equal'
                assert cursor['size'] == response['data']['size'], 'size not equal'

@pytest.mark.usefixtures('base')
class TestWxApiCustomAudiences(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_custom_audiences_add)
    def test_01_custom_audiences_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'custom_audiences/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            #NOTICES: the db structure not exists now
            cursor = mongodb.sndo['wx.audience'].find_one(
                {'audience_id': response['data']['audience_id']})
            assert cursor,'audience not found'
            global audience_id
            audience_id = response['data']['audience_id']
            assert cursor['name'] == payload['name'],'name not equal'
            assert cursor['type'] == payload['type'],'type not equal'
            assert cursor['description'] == payload['description'],'description not equal'
    
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_custom_audiences_update)
    def test_02_custom_audiences_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['audience_id'] = get_audience_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'custom_audiences/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            #NOTICES: the db structure not exists now
            cursor = mongodb.sndo['wx.audience'].find_one(
                {'audience_id': response['data']['audience_id']})
            assert cursor,'audience not found'
            assert cursor['name'] == payload['name'],'name not equal'
            assert cursor['type'] == payload['type'],'type not equal'
            assert cursor['description'] == payload['description'],'description not equal'
    
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_custom_audiences_get)
    def test_03_custom_audiences_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        if 'audience_id' in payload:
            payload['audience_id'] = get_audience_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'custom_audiences/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            for tag in response['data']['list']:
                #NOTICES: the db structure not exists now
                cursor = mongodb.sndo['wx.audience'].find_one(
                {'audience_id': tag['audience_id']})
                assert cursor, 'audience not found'
                assert cursor['name'] == payload['name'],'name not equal'
                assert cursor['type'] == payload['type'],'type not equal'
                assert cursor['description'] == payload['description'],'description not equal'
                assert cursor['status'] == payload['status'],'status not equal'
                assert cursor['error_code'] == payload['error_code'],'error_code not equal'
                assert cursor['user_count'] == payload['user_count'],'user_count not equal'
                assert cursor['created_time'] == payload['created_time'],'created_time not equal'
                assert cursor['last_modified_time'] == payload['last_modified_time'],'last_modified_time not equal'

@pytest.mark.usefixtures('base')
class TestWxApiCustomAudienceFiles(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_custom_audience_files_add)
    def test_01_custom_audience_files_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['audience_id'] = get_audience_id(payload=payload)
        files = {'file': open(payload['file'], 'rb')
                 if payload['file'] else ''}
        del payload['file']
        url = urllib.parse.urljoin(addr, 'custom_audience_files/add')
        response = r.req('POST', url, data=payload, files=files)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            assert response['data']['custom_audience_file_id'], 'custom_audience_file_id fail'
            global custom_audience_file_id
            custom_audience_file_id = response['data']['custom_audience_file_id']
    
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_custom_audience_files_get)
    def test_02_custom_audience_files_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['custom_audience_file_id'] = custom_audience_file_id
        url = urllib.parse.urljoin(addr, 'custom_audience_files/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            assert payload['custom_audience_file_id'] == response['data']['list'][0]['custom_audience_file_id'],'custom_audience_file_id not equal'

@pytest.mark.uesfixtures('base')            
class TestWxApiDailyReports(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_daily_reports_get)
    def test_01_daily_reports_get(
            self,
            payload,
            res,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(addr, 'daily_reports/get')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'

@pytest.mark.uesfixtures('base')            
class TestWxApiRealtimeCost(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_realtime_cost_get)
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

@pytest.mark.uesfixtures('base')            
class TestWxApiEstimation(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_estimation_get)
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

@pytest.mark.uesfixtures('base')            
class TestWxApiAdcreatives2(object):
    
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_adcreatives2_add)
    def test_01_adcreatives2_add(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['campaign_id'] = get_campaign_id(payload=payload)
        payload['adgroup_id'] = get_adgroup_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/add')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert ad_cursor,'ad not found'
            global ad_id
            ad_id = response['data']['ad_id']
            assert ad_cursor['appid'] == payload['appid'], 'appid not equal'
            assert ad_cursor['adgroup_id'] == payload['adgroup_id'], 'adgroup_id not equal'
            assert ad_cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert ad_cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            assert ad_cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert adcreative_cursor,'adcreative not found'  
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            assert adcreative_cursor['appid'] == payload['appid'], 'appid not equal'
            assert adcreative_cursor['campaign_id'] == payload['campaign_id'], 'campaign_id not equal'
            assert adcreative_cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert adcreative_cursor['adcreative_template_id'] == payload['adcreative_template_id'], 'adcreative_template_id not equal'
            assert adcreative_cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert adcreative_cursor['destination_url'] == payload['destination_url'], 'destination_url not equal'
            assert adcreative_cursor['site_set'] == payload['site_set'], 'site_set not equal'
            assert adcreative_cursor['product_type'] == payload['product_type'], 'product_type not equal'
            assert adcreative_cursor['product_refs_id'] == payload['product_refs_id'], 'product_refs_id not equal'
            assert adcreative_cursor['share_info'] == payload['share_info'], 'share_info not equal'
            assert adcreative_cursor['sndo_ader_id'] == payload['sndo_ader_id'], 'sndo_ader_id not equal'
    
    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_02_adcreatives2_update)
    def test_02_adcreatives2_update(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/update')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert ad_cursor,'ad not found'
            assert ad_cursor['appid'] == payload['appid'], 'appid not equal'
            assert ad_cursor['ad_name'] == payload['ad_name'], 'ad_name not equal'
            assert ad_cursor['configured_status'] == payload['configured_status'], 'configured_status not equal'
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert adcreative_cursor,'adcreative not found'  
            assert adcreative_cursor['adcreative_name'] == payload['adcreative_name'], 'adcreative_name not equal'
            assert adcreative_cursor['adcreative_elements'] == payload['adcreative_elements'], 'adcreative_elements not equal'
            assert adcreative_cursor['destination_url'] == payload['destination_url'], 'destination_url not equal'
    

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_03_adcreatives2_delete)
    def test_03_adcreatives2_delete(
            self,
            payload,
            res,
            test_title,
            mongodb):
        payload['adcreative_id'] = get_adcreative_id(payload=payload)
        payload['ad_id'] = get_ad_id(payload=payload)
        url = urllib.parse.urljoin(addr, 'adcreatives2/delete')
        response = r.req('POST', url, json=payload)
        assert res['code'] == response['code'], 'code not equal'
        assert res['msg'] == response['message'], 'message not equal'
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert ad_cursor,'ad not found'
            assert ad_cursor['is_deleted'],'delete fail'
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert adcreative_cursor,'adcreative not found' 
            assert adcreative_cursor['is_deleted'],'delete fail'