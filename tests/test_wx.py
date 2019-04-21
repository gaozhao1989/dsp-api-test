import json
import urllib.parse

import allure
import pytest

from parameters import wx

from utils import AssertUtils
from utils import ConfigParser
from utils import DataGenerator
from utils import Log
from utils import Requests

au = AssertUtils()
cp = ConfigParser()
dg = DataGenerator()
log = Log.getlog('WxTest')
r = Requests()
addr = cp.get_wx_addr()
# global variables
qualification_id = None
transfter_order_id = None
campaign_id = None
adgroup_id = None
adcreative_id = None
ad_id = None
image_id = None
audience_id = None
custom_audience_file_id = None


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


def get_ad_id(glo=True, payload={'ad_id': 'global variable'}):
    if payload['ad_id'] == 'global variable':
        global ad_id
        if ad_id is None:
            add_ad_payload = wx.test_01_ads_add[0][0]
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


def get_image_id(glo=True, payload={'image_id': 'global variable'}):
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


def get_audience_id(glo=True, payload={'audience_id': 'global variable'}):
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            au.assertnotfound(cursor, payload['appid'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            au.assertnotfound(cursor, payload['appid'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': payload['appid']})
            au.assertnotfound(cursor, payload['appid'])


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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.account.qualification'].find_one(
                {'qualification_id': response['data']['qualification_id']})
            au.assertnotfound(cursor, response['data']['qualification_id'])
            global qualification_id
            qualification_id = response['data']['qualification_id']
            au.assertgroup(cursor,
                           payload,
                           ['appid',
                            'qualification_name',
                            'qualification_image_id',
                            'qualification_type'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.account.qualification'].find_one(
                    {'qualification_id': tag['qualification_id']})
                au.assertnotfound(cursor, tag['qualification_id'])
                au.assertgroup(cursor,
                               payload,
                               ['qualification_name',
                                'qualification_image',
                                'qualification_type',
                                'qualification_status',
                                'valid_date'])

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
        au.assertgroup(res, response, ['code', 'message'])
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
        au.assertgroup(res, response, ['code', 'message'])

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
        au.assertgroup(res, response, ['code', 'message'])


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
        au.assertgroup(res, response, ['code', 'message'])
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
        au.assertgroup(res, response, ['code', 'message'])


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
        au.assertgroup(res, response, ['code', 'message'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            au.assertnotfound(cursor, response['data']['campaign_id'])
            global campaign_id
            campaign_id = response['data']['campaign_id']
            au.assertgroup(cursor,
                           payload,
                           ['campaign_name',
                            'campaign_type',
                            'product_type',
                            'configured_status',
                            'daily_budget',
                            'sndo_ader_id'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['lit']:
                cursor = mongodb.sndo['wx.campaign'].find_one(
                    {'campaign_id': tag['campaign_id']})
                au.assertnotfound(cursor, tag['campaign_id'])
                au.assertgroup(cursor,
                               payload,
                               ['campaign_name',
                                'campaign_type',
                                'product_type',
                                'configured_status',
                                'daily_budget',
                                'created_time',
                                'budget_reach_date',
                                'last_modified_time'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            af_cursor = mongodb.sndo['wx.campaign'].find_one(
                {'campaign_id': payload['campaign_id']})
            au.assertnotfound(af_cursor, payload['campaign_id'])
            au.assertnotfound(af_cursor, payload, [
                              'campaign_name', 'configured_status'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'campaign_id': payload['campaign_id']})
            au.assertnotfound(cursor, payload['campaign_id'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            au.assertnotfound(cursor, response['data']['adgroup_id'])
            global adgroup_id
            adgroup_id = response['data']['adgroup_id']
            au.assertgroup(cursor,
                           payload,
                           ['appid',
                            'campaign_id',
                            'adgroup_name',
                            'site_set',
                            'product_type',
                            'targeting',
                            'optimization_goal',
                            'billing_event',
                            'bid_amount',
                            'begin_date',
                            'end_date',
                            'time_series',
                            'daily_budget',
                            'product_refs_id',
                            'configured_status',
                            'sndo_ader_id'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            au.assertnotfound(cursor, response['data']['adgroup_id'])
            au.assertgroup(cursor,
                           payload,
                           ['adgroup_name',
                            'targeting',
                            'bid_amount',
                            'begin_date',
                            'end_date',
                            'time_series',
                            'daily_budget',
                            'configured_status'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.adgroup'].find_one(
                    {'adgroup_id': tag['adgroup_id']})
                au.assertnotfound(cursor, tag['adgroup_id'])
                au.assertgroup(cursor,
                               payload,
                               ['campaign_id',
                                'adgroup_name',
                                'site_set',
                                'product_type',
                                'targeting',
                                'optimization_goal',
                                'billing_event',
                                'bid_amount',
                                'begin_date',
                                'end_date',
                                'time_series',
                                'daily_budget',
                                'product_refs_id',
                                'configured_status',
                                'system_status',
                                'reject_message',
                                'created_time',
                                'last_modified_time'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': payload['adgroup_id']})
            au.assertnotfound(cursor, payload['adgroup_id'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(cursor, response['data']['adcreative_id'])
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            au.assertgroup(cursor,
                           payload,
                           ['appid',
                            'campaign',
                            'adcreative_name',
                            'adcreative_template_id',
                            'adcreative_elements',
                            'destination_url',
                            'site_set',
                            'product_type',
                            'product_refs_id',
                            'share_info',
                            'sndo_ader_id'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(cursor, response['data']['adcreative_id'])
            au.assertgroup(
                cursor, payload, [
                    'adcreative_name', 'adcreative_elements', 'destination_url'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.adcreative'].find_one(
                    {'adcreative_id': tag['adcreative_id']})
                au.assertnotfound(cursor, tag['adcreative_id'])
                au.assertgroup(cursor,
                               payload,
                               ['campaign_id',
                                'adcreative_name',
                                'adcreative_template_id',
                                'adcreative_elements',
                                'destination_url',
                                'site_set',
                                'product_type',
                                'product_refs_id',
                                'created_time',
                                'last_modified_time'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(cursor, response['data']['adcreative_id'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
            global ad_id
            ad_id = response['data']['ad_id']
            au.assertgroup(cursor,
                           payload,
                           ['appid',
                            'adgroup_id',
                            'adcreative_id',
                            'ad_name',
                            'configured_status',
                            'sndo_ader_id'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
            au.assertgroup(cursor, payload, ['ad_name', 'configured_status'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.ad'].find_one(
                    {'ad_id': tag['ad_id']})
                au.assertnotfound(cursor, tag['ad_id'])
                au.assertgroup(cursor,
                               tag,
                               ['campaign_id',
                                'adgroup_id',
                                'adcreative',
                                'ad_name',
                                'configured_status',
                                'system_status',
                                'reject_message',
                                'created_time',
                                'last_modified_time'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(cursor, response['data']['ad_id'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            cursor = mongodb.sndo['wx.image'].find_one(
                {'image_id': response['data']['image_id']})
            au.assertnotfound(cursor, response['data']['image_id'])
            global image_id
            image_id = response['data']['image_id']
            au.assertgroup(
                cursor, payload, [
                    'signature', 'preview_url', 'type', 'width', 'height', 'size'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                cursor = mongodb.sndo['wx.image'].find_one(
                    {'image_id': tag['image_id']})
                image_id = tag['image_id']
                au.assertnotfound(cursor, tag['image_id'])
                au.assertgroup(
                    cursor, tag, [
                        'signature', 'preview_url', 'type', 'width', 'height', 'size'])


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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            # NOTICES: the db structure not exists now
            cursor = mongodb.sndo['wx.audience'].find_one(
                {'audience_id': response['data']['audience_id']})
            au.assertnotfound(cursor, response['data']['audience_id'])
            global audience_id
            audience_id = response['data']['audience_id']
            au.assertgroup(cursor, payload, ['name', 'type', 'description'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            # NOTICES: the db structure not exists now
            cursor = mongodb.sndo['wx.audience'].find_one(
                {'audience_id': response['data']['audience_id']})
            au.assertnotfound(cursor, response['data']['audience_id'])
            audience_id = response['data']['audience_id']
            au.assertgroup(cursor, payload, ['name', 'type', 'description'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            for tag in response['data']['list']:
                # NOTICES: the db structure not exists now
                cursor = mongodb.sndo['wx.audience'].find_one(
                    {'audience_id': tag['audience_id']})
                au.assertnotfound(cursor, tag['audience_id'])
                au.assertgroup(cursor,
                               tag,
                               ['name',
                                'type',
                                'description',
                                'status',
                                'error_code',
                                'user_count',
                                'created_time',
                                'last_modified_time'])


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
        au.assertgroup(res, response, ['code', 'message'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            assert payload['custom_audience_file_id'] == response['data']['list'][
                0]['custom_audience_file_id'], 'custom_audience_file_id not equal'


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
        au.assertgroup(res, response, ['code', 'message'])


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
        au.assertgroup(res, response, ['code', 'message'])


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
        au.assertgroup(res, response, ['code', 'message'])
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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(ad_cursor, response['data']['ad_id'])
            global ad_id
            ad_id = response['data']['ad_id']
            au.assertgroup(
                ad_cursor, payload, [
                    'appid', 'adgroup_id', 'ad_name', 'configured_status', 'sndo_ader_id'])
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(adcreative_cursor,
                              response['data']['adcreative_id'])
            global adcreative_id
            adcreative_id = response['data']['adcreative_id']
            au.assertgroup(ad_cursor,
                           payload,
                           ['appid',
                            'campaign_id',
                            'adcreative_name',
                            'adcreative_template_id',
                            'adcreative_elements',
                            'destination_url',
                            'site_set',
                            'product_type',
                            'product_refs_id',
                            'share_info',
                            'sndo_ader_id'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(ad_cursor, response['data']['ad_id'])
            au.assertgroup(ad_cursor, payload, [
                           'appid', 'ad_name', 'configured_status'])
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(adcreative_cursor,
                              response['data']['adcreative_id'])
            au.assertgroup(
                adcreative_cursor, payload, [
                    'adcreative_name', 'adcreative_elements', 'destination_url'])

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
        au.assertgroup(res, response, ['code', 'message'])
        if res['result']:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            au.assertnotfound(ad_cursor, response['data']['ad_id'])
            assert ad_cursor['is_deleted'], 'delete fail'
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            au.assertnotfound(adcreative_cursor,
                              response['data']['adcreative_id'])
            assert adcreative_cursor['is_deleted'], 'delete fail'
