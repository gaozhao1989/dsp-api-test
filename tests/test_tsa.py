import json
import urllib.parse
import requests
import pytest
from parameters import tsa
from utils import Log


@pytest.mark.usefixtures('base')
class TestTsaApi(object):

    addr = 'http://test.sndo.com/sdk/tsa/'

    log = Log.getlog('tsaTest')

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
        response = json.loads(requests.post(urllib.parse.urljoin(self.addr, 'adcreatives2/add'),json={
            'account_id': account_id,
            'campaign_id': 29131,
            'adcreative_name': 'test_delete_adcreative',
            'adcreative_template_id': 529,
            'adcreative_elements': {'image': '3519', 'title': 'test title'},
            'site_set': ['SITE_SET_QQCLIENT'],
            'page_spec': {'page_id': 0, 'page_url': 'https://www.qq.com'},
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
            qualification_type,qualification_id,image_id_list,
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
            'image_id_list':image_id_list
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