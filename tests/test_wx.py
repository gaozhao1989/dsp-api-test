import json
import random
import urllib.parse
import requests
import pytest
from parameters import wx
from utils import Log, Requests


addr = 'http://test.sndo.com/sdk/wx/'
log = Log.getlog('wxTest')
r = Requests()


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


@pytest.mark.usefixtures('base')
class TestWxApi(object):

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'payload, res, test_title',
        wx.test_01_advertiser_get)
    def test_01_advertiser_get(
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

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid, res_result, result_code, result_message, test_title',
        wx.test_02_ads_get)
    def test_02_ads_get(
            self,
            appid,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'ads/get')
        payload = {'appid': appid}
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.ad'].find(
                {'appid': appid, 'is_deleted': False})
            assert cursor.count() == len(
                response['data']['list']), 'ads not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid, res_result, result_code, result_message, test_title',
        wx.test_03_sp_entrustment_add)
    @pytest.mark.skip(reason='no resources')
    def test_03_sp_entrustment_add(
            self,
            appid,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'sp_entrustment/add')
        payload = {'appid': appid}
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid, res_result, result_code, result_message, test_title',
        wx.test_04_sp_entrustment_get)
    def test_04_sp_entrustment_get(
            self,
            appid,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'sp_entrustment/get')
        payload = {'appid': appid}
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.account'].find_one(
                {'appid': appid})
            assert cursor

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_name,campaign_type,product_type,configured_status,daily_budget,sndo_ader_id, res_result, result_code, result_message, test_title',
        wx.test_05_campaigns_add)
    def test_05_campaigns_add(
            self,
            appid,
            campaign_name,
            campaign_type,
            product_type,
            configured_status,
            daily_budget,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'campaigns/add')
        payload = {
            'appid': appid,
            'campaign_name': campaign_name,
            'campaign_type': campaign_type,
            'product_type': product_type,
            'configured_status': configured_status,
            'daily_budget': daily_budget,
            'sndo_ader_id': sndo_ader_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'campaign_id': response['data']['campaign_id']})
            assert cursor
            assert cursor['campaign_name'] == campaign_name
            assert cursor['campaign_type'] == campaign_type
            assert cursor['product_type'] == product_type
            assert cursor['configured_status'] == configured_status
            assert cursor['daily_budget'] == (
                daily_budget if daily_budget else 0)
            assert cursor['sndo_ader_id'] == sndo_ader_id

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_id,filtering,page,page_size, res_result, result_code, result_message, test_title',
        wx.test_06_campaigns_get)
    def test_06_campaigns_get(
            self,
            appid,
            campaign_id,
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
            'appid': appid,
            'campaign_id': campaign_id,
            'filtering': filtering,
            'page': page,
            'page_size': page_size,
        }
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            if campaign_id:
                cursor = mongodb.sndo['wx.campaign'].find_one(
                    {'appid': appid, 'campaign_id': campaign_id})
                assert cursor, 'campaign not found'
            else:
                cursor = mongodb.sndo['wx.campaign'].find(
                    {'appid': appid})
                assert cursor, 'campaign not found'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_id,campaign_name,configured_status,daily_budget, res_result, result_code, result_message, test_title',
        wx.test_07_campaigns_update)
    def test_07_campaigns_update(
            self,
            appid,
            campaign_id,
            campaign_name,
            configured_status,
            daily_budget,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'campaigns/update')
        payload = {
            'appid': appid,
            'campaign_id': campaign_id,
            'campaign_name': campaign_name,
            'configured_status': configured_status,
            'daily_budget': daily_budget}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        bf_cursor = mongodb.sndo['wx.campaign'].find_one(
            {'appid': appid, 'campaign_id': campaign_id})
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            af_cursor = mongodb.sndo['wx.campaign'].find_one(
                {'appid': appid, 'campaign_id': campaign_id})
            assert af_cursor
            assert af_cursor['campaign_name'] == campaign_name if campaign_name else bf_cursor['campaign_name']
            assert af_cursor['configured_status'] == configured_status if configured_status else bf_cursor['configured_status']
            assert str(af_cursor['daily_budget']) == str(daily_budget) if str(
                daily_budget) else str(bf_cursor['daily_budget'])

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_id, res_result, result_code, result_message, test_title',
        wx.test_08_campaigns_delete)
    def test_08_campaigns_delete(
            self,
            appid,
            campaign_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'campaigns/delete')
        payload = {'appid': appid, 'campaign_id': campaign_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.campaign'].find_one(
                {'appid': appid, 'campaign_id': campaign_id})
            assert cursor['is_deleted']

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_id,adgroup_name,site_set,product_type,targeting,optimization_goal,billing_event,bid_amount,begin_date,end_date,time_series,daily_budget,product_refs_id,configured_status,sndo_ader_id, res_result, result_code, result_message, test_title',
        wx.test_09_adgroups_add)
    def test_09_adgroups_add(
            self,
            appid,
            campaign_id,
            adgroup_name,
            site_set,
            product_type,
            targeting,
            optimization_goal,
            billing_event,
            bid_amount,
            begin_date,
            end_date,
            time_series,
            daily_budget,
            product_refs_id,
            configured_status,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adgroups/add')
        payload = {
            'appid': appid,
            'campaign_id': campaign_id,
            'adgroup_name': adgroup_name,
            'site_set': site_set,
            'product_type': product_type,
            'targeting': targeting,
            'optimization_goal': optimization_goal,
            'billing_event': billing_event,
            'bid_amount': bid_amount,
            'begin_date': begin_date,
            'end_date': end_date,
            'time_series': time_series,
            'daily_budget': daily_budget,
            'product_refs_id': product_refs_id,
            'configured_status': configured_status,
            'sndo_ader_id': sndo_ader_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.adgroup'].find_one(
                {'adgroup_id': response['data']['adgroup_id']})
            assert cursor

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,image, res_result, result_code, result_message, test_title',
        wx.test_10_images_add)
    def test_10_images_add(
            self,
            appid,
            image,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'images/add')
        payload = {'appid': appid}
        files = {'image': open(image, 'rb') if image else ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, data=payload, files=files).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.image'].find_one(
                {'signature': response['data']['signature']})
            assert cursor, 'image not found'
            assert cursor['signature'] == response['data']['signature'], 'signature not equal'
            assert cursor['preview_url'] == response['data']['preview_url'], 'image url not equal'
            assert cursor['image_id'] == response['data']['image_id'], 'image id not equal'
            assert cursor['type'] == response['data']['type'], 'type not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,filtering,page,page_size, res_result, result_code, result_message, test_title',
        wx.test_11_images_get)
    def test_11_images_get(
            self,
            appid,
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
            'appid': appid,
            'filtering': filtering,
            'page': page,
            'page_size': page_size}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            cursor = mongodb.sndo['wx.image'].find(
                {'appid': appid})
            assert cursor

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,campaign_id,adcreative_name,adcreative_template_id,adcreative_elements,destination_url,site_set,product_type,product_refs_id,share_info,adgroup_id,ad_name,configured_status,sndo_ader_id, res_result, result_code, result_message, test_title',
        wx.test_12_adcreatives2_add)
    def test_12_adcreatives2_add(
            self,
            appid,
            campaign_id,
            adcreative_name,
            adcreative_template_id,
            adcreative_elements,
            destination_url,
            site_set,
            product_type,
            product_refs_id,
            share_info,
            adgroup_id,
            ad_name,
            configured_status,
            sndo_ader_id,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'adcreatives2/add')
        # create new ad_campaign
        campaign_id = json.loads(
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'campaigns/add'),
                json={
                    'appid': appid,
                    'campaign_name': 'test_campaign_name_{}'.format(
                        random.randint(
                            1000,
                            9999)),
                    'campaign_type': 'CAMPAIGN_TYPE_WECHAT_MOMENTS',
                    'product_type': product_type,
                    'configured_status': configured_status}).content)['data']['campaign_id']
        # create new ad_group
        adgroup_id = json.loads(
            requests.post(
                urllib.parse.urljoin(
                    self.addr,
                    'adgroups/add'),
                json={
                    'appid': appid,
                    'campaign_id': campaign_id,
                    'adgroup_name': 'test_adgroup_name_{}'.format(
                        random.randint(
                            1000,
                            9999)),
                    'site_set': site_set,
                    'product_type': product_type,
                    'targeting': {
                        'age': ['15~25'],
                        'geo_location': {
                            'regions': [
                                110000,
                                310000],
                            'location_types': ['LIVE_IN']}},
                    'daily_budget': 500000,
                    'optimization_goal': 'OPTIMIZATIONGOAL_IMPRESSION',
                    'billing_event': 'BILLINGEVENT_IMPRESSION',
                    'bid_amount': 12000,
                    'begin_date': '2019-03-27',
                    'end_date': '2019-04-20',
                    'time_series': ''.join(
                        [
                            str(
                                random.randint(
                                    0,
                                    1)) for x in range(48)]) * 7,
                    'configured_status': configured_status}).content)['data']['adgroup_id']
        payload = {
            'appid': appid,
            'campaign_id': campaign_id,
            'adcreative_name': adcreative_name,
            'adcreative_template_id': adcreative_template_id,
            'adcreative_elements': adcreative_elements,
            'destination_url': destination_url,
            'site_set': site_set,
            'product_type': product_type,
            'product_refs_id': product_refs_id,
            'share_info': share_info,
            'adgroup_id': adgroup_id,
            'ad_name': ad_name,
            'configured_status': configured_status,
            'sndo_ader_id': sndo_ader_id}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
        if res_result:
            ad_cursor = mongodb.sndo['wx.ad'].find_one(
                {'ad_id': response['data']['ad_id']})
            assert ad_cursor
            adcreative_cursor = mongodb.sndo['wx.adcreative'].find_one(
                {'adcreative_id': response['data']['adcreative_id']})
            assert adcreative_cursor

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid, res_result, result_code, result_message, test_title',
        wx.test_13_funds_get)
    def test_13_funds_get(
            self,
            appid,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'funds/get')
        payload = {'appid': appid}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,transaction_type,date_range, res_result, result_code, result_message, test_title',
        wx.test_14_fund_statements_detailed_get)
    def test_14_fund_statements_detailed_get(
            self,
            appid,
            transaction_type,
            date_range,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'fund_statements_detailed/get')
        payload = {
            'appid': appid,
            'transaction_type': transaction_type,
            'date_range': date_range}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,report_type,level,date_range,page,page_size, res_result, result_code, result_message, test_title',
        wx.test_15_daily_reports_get)
    def test_15_daily_reports_get(
            self,
            appid,
            report_type,
            level,
            date_range,
            page,
            page_size,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'daily_reports/get')
        payload = {
            'appid': appid,
            'report_type': report_type,
            'level': level,
            'date_range': date_range,
            'page': page,
            'page_size': page_size}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'

    @Log.logtestcase()
    @pytest.mark.parametrize(
        'appid,fund_type,amount,external_bill_no,memo, res_result, result_code, result_message, test_title',
        wx.test_16_fund_transfer_add)
    def test_16_fund_transfer_add(
            self,
            appid,
            fund_type,
            amount,
            external_bill_no,
            memo,
            res_result,
            result_code,
            result_message,
            test_title,
            mongodb):
        url = urllib.parse.urljoin(self.addr, 'fund_transfer/add')
        payload = {
            'appid': appid,
            'fund_type': fund_type,
            'amount': amount,
            'external_bill_no': external_bill_no,
            'memo': memo}
        payload = {k: v for k, v in payload.items() if v is not ''}
        self.log.info(payload)
        try:
            response = json.loads(requests.post(
                url, json=payload).content)
        except Exception as e:
            assert False, 'request fail'
        self.log.info(response)
        assert result_code == response['code'], 'code not equal'
        assert result_message == response['message'], 'message not equal'
