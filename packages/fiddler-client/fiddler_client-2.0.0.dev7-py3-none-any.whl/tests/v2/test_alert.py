import json
import unittest
from http import HTTPStatus
from typing import Optional
from unittest import mock

from responses import matchers

from fiddler.exceptions import NotFound
from fiddler.v2.schema.alert import (
    AlertCondition,
    AlertRule,
    AlertType,
    BinSize,
    ComparePeriod,
    CompareTo,
    Metric,
    Priority,
    TriggeredAlerts,
)
from fiddler.v2.schema.server_info import ServerInfo
from tests.v2.base import BaseTestCase


class TestAlert(BaseTestCase):
    def setUp(self):
        super(TestAlert, self).setUp()
        self._project_name = 'test_project'
        self._model_name = 'test_model'
        self._alert_rule_uuid = 'test_alert_rule_uuid'

    def _get_url(
        self,
        alert_rule_uuid: Optional[str] = None,
    ) -> str:
        base_url = f'{self._url}/alert-configs'

        if alert_rule_uuid:
            return f'{base_url}/{alert_rule_uuid}'

        return base_url

    def test_get_alert_rules_before_metadb_filtering(self):
        response = {
            'data': {
                'page_size': 100,
                'total': 84,
                'item_count': 84,
                'page_count': 1,
                'page_index': 1,
                'offset': 0,
                'items': [
                    {
                        'critical_threshold': 0.5,
                        'organization_name': self._org,
                        'id': 1,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'greater',
                        'time_bucket': 3600000,
                        'compare_period': 86400000,
                        'details': 'New Alert',
                        'model_name': self._model_name,
                        'name': 'alert_name_1',
                        'feature_names': ['probability_churned', 'age'],
                        'baseline_name': 'baseline_name',
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': '932bb123-3fc6-4ee5-a48c-1f96bb29f7ee',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:26.889000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.2,
                        'compare_to': 'time_period',
                        'alert_log_time': '2022-09-08T18:47:28.034165+00:00',
                        'priority': 'LOW',
                    },
                    {
                        'critical_threshold': 0.7,
                        'organization_name': self._org,
                        'id': 2,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'lesser',
                        'time_bucket': 3600000,
                        'compare_period': 86400000,
                        'details': 'New Alert',
                        'model_name': self._model_name,
                        'name': 'alert_name_2',
                        'feature_names': ['probability_churned'],
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': 'e7c7f891-53ba-4246-b691-53b6efda332b',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:27.923000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.1,
                        'compare_to': 'time_period',
                        'alert_log_time': '2022-09-08T18:47:29.087871+00:00',
                        'priority': 'LOW',
                    },
                    {
                        'critical_threshold': 0.8,
                        'organization_name': self._org,
                        'id': 3,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'greater',
                        'time_bucket': 3600000,
                        'compare_period': 0,
                        'model_name': self._model_name,
                        'name': 'alert_name_3',
                        'feature_names': ['probability_churned'],
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': '320060fa-abeb-4cae-9718-17d6f917b414',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:28.975000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.4,
                        'compare_to': 'raw_value',
                        'alert_log_time': '2022-09-08T18:47:30.100808+00:00',
                        'priority': 'LOW',
                    },
                ],
            },
            'api_version': '2.0',
            'kind': 'PAGINATED',
        }

        url = self._get_url()

        query_params = {'organization_name': 'test_organization', 'offset': 0, 'limit': 20, 'ordering': 'alert_type,metric', 'filter': '{"condition": "AND", "rules": [{"field": "project_name", "operator": "equal", "value": "test_project"}, {"field": "model_name", "operator": "equal", "value": "test_model"}, {"field": "alert_type", "operator": "equal", "value": "drift"}, {"field": "metric", "operator": "equal", "value": "jsd"}, {"field": "baseline_name", "operator": "equal", "value": "test_baseline"}]}'}

        self.requests_mock.get(
            url, json=response, match=[matchers.query_param_matcher(query_params)]
        )

        server_info = ServerInfo(**{'feature_flags': {}, 'server_version': '23.3.0'})

        with mock.patch.object(
            self.client, 'server_info', server_info
        ) as mock_server_info:
            alert_rules = self.client.get_alert_rules(
                project_name='test_project',
                model_name='test_model',
                alert_type='drift',
                metric='jsd',
                baseline_name='test_baseline',
                ordering=['alert_type', 'metric'],
            )

        self.assertIsInstance(alert_rules[0], AlertRule)
        self.assertEqual(alert_rules[0].alert_type, 'drift')
        self.assertEqual(alert_rules[0].critical_threshold, 0.5)
        self.assertEqual(alert_rules[0].name, 'alert_name_1')
        self.assertEqual(alert_rules[0].compare_period, ComparePeriod.ONE_DAY)
        self.assertEqual(alert_rules[0].columns, ['probability_churned', 'age'])
        self.assertEqual(
            alert_rules[0].alert_rule_uuid, '932bb123-3fc6-4ee5-a48c-1f96bb29f7ee'
        )
        self.assertEqual(alert_rules[0].baseline_name, 'baseline_name')
        self.assertIsInstance(alert_rules[2], AlertRule)
        self.assertEqual(alert_rules[2].alert_type, 'drift')
        self.assertEqual(alert_rules[2].critical_threshold, 0.8)
        self.assertEqual(alert_rules[2].name, 'alert_name_3')
        self.assertEqual(alert_rules[2].columns, ['probability_churned'])
        self.assertEqual(alert_rules[2].project_name, self._project_name)
        self.assertEqual(alert_rules[2].model_name, self._model_name)
        self.assertEqual(alert_rules[2].model_name, self._model_name)
        self.assertEqual(
            alert_rules[2].alert_rule_uuid, '320060fa-abeb-4cae-9718-17d6f917b414'
        )
        self.assertIsNone(alert_rules[2].compare_period)
        self.assertEqual(len(alert_rules), 3)

        response_items = self.requests_mock.calls[0].response.json()['data']['items']

        self.assertEqual(response_items[0]['organization_name'], self._org)
        self.assertEqual(response_items[0]['model_name'], self._model_name)
        self.assertEqual(response_items[0]['project_name'], self._project_name)
        self.assertEqual(response_items[0]['alert_type'], 'drift')
        self.assertEqual(response_items[0]['name'], 'alert_name_1')

    def test_get_alert_rules_after_metadb_filtering(self):
        response = {
            'data': {
                'page_size': 100,
                'total': 84,
                'item_count': 84,
                'page_count': 1,
                'page_index': 1,
                'offset': 0,
                'items': [
                    {
                        'critical_threshold': 0.5,
                        'organization_name': self._org,
                        'id': 1,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'greater',
                        'time_bucket': 3600000,
                        'compare_period': 86400000,
                        'details': 'New Alert',
                        'model_name': self._model_name,
                        'name': 'alert_name_1',
                        'feature_names': ['probability_churned'],
                        'baseline_name': 'baseline_name',
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': '932bb123-3fc6-4ee5-a48c-1f96bb29f7ee',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:26.889000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.2,
                        'compare_to': 'time_period',
                        'alert_log_time': '2022-09-08T18:47:28.034165+00:00',
                        'priority': 'LOW',
                    },
                    {
                        'critical_threshold': 0.7,
                        'organization_name': self._org,
                        'id': 2,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'lesser',
                        'time_bucket': 3600000,
                        'compare_period': 86400000,
                        'details': 'New Alert',
                        'model_name': self._model_name,
                        'name': 'alert_name_2',
                        'feature_names': ['probability_churned'],
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': 'e7c7f891-53ba-4246-b691-53b6efda332b',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:27.923000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.1,
                        'compare_to': 'time_period',
                        'alert_log_time': '2022-09-08T18:47:29.087871+00:00',
                        'priority': 'LOW',
                    },
                    {
                        'critical_threshold': 0.8,
                        'organization_name': self._org,
                        'id': 3,
                        'sub_metric': 'jsd',
                        'metric': 'jsd',
                        'condition': 'greater',
                        'time_bucket': 3600000,
                        'compare_period': 0,
                        'model_name': self._model_name,
                        'name': 'alert_name_3',
                        'feature_names': ['probability_churned'],
                        'created_by': 'admin@fiddler.ai',
                        'alert_type': 'drift',
                        'uuid': '320060fa-abeb-4cae-9718-17d6f917b414',
                        'is_active': True,
                        'created_at': '2022-09-08T18:47:28.975000+00:00',
                        'project_name': self._project_name,
                        'warning_threshold': 0.4,
                        'compare_to': 'raw_value',
                        'alert_log_time': '2022-09-08T18:47:30.100808+00:00',
                        'priority': 'LOW',
                    },
                ],
            },
            'api_version': '2.0',
            'kind': 'PAGINATED',
        }

        url = self._get_url()
        query_params = {
            'organization_name': self._org,
            'filter': json.dumps(
                {
                    'condition': 'AND',
                    'rules': [
                        {
                            'field': 'project_name',
                            'operator': 'equal',
                            'value': 'test_project',
                        },
                        {
                            'field': 'model_name',
                            'operator': 'equal',
                            'value': 'test_model',
                        },
                        {'field': 'alert_type', 'operator': 'equal', 'value': 'drift'},
                        {'field': 'metric', 'operator': 'equal', 'value': 'jsd'},
                        {
                            'field': 'feature_names',
                            'operator': 'contains',
                            'value': ['test_column'],
                        },
                        {
                            'field': 'baseline_name',
                            'operator': 'equal',
                            'value': 'test_baseline',
                        },
                    ],
                }
            ),
            'ordering': 'alert_type,metric',
            'limit': 20,
            'offset': 0,
        }
        self.requests_mock.get(
            url, json=response, match=[matchers.query_param_matcher(query_params)]
        )

        server_info = ServerInfo(**{'feature_flags': {}, 'server_version': '23.3.0'})

        with mock.patch.object(
            self.client, 'server_info', server_info
        ) as mock_server_info:
            alert_rules = self.client.get_alert_rules(
                project_name='test_project',
                model_name='test_model',
                alert_type='drift',
                metric='jsd',
                columns=['test_column'],
                baseline_name='test_baseline',
                ordering=['alert_type', 'metric'],
            )

        self.assertIsInstance(alert_rules[0], AlertRule)
        self.assertEqual(alert_rules[0].alert_type, 'drift')
        self.assertEqual(alert_rules[0].critical_threshold, 0.5)
        self.assertEqual(alert_rules[0].name, 'alert_name_1')
        self.assertEqual(alert_rules[0].compare_period, ComparePeriod.ONE_DAY)
        self.assertEqual(alert_rules[0].columns, ['probability_churned'])

        self.assertEqual(
            alert_rules[0].alert_rule_uuid, '932bb123-3fc6-4ee5-a48c-1f96bb29f7ee'
        )
        self.assertEqual(alert_rules[0].baseline_name, 'baseline_name')
        self.assertIsInstance(alert_rules[2], AlertRule)
        self.assertEqual(alert_rules[2].alert_type, 'drift')
        self.assertEqual(alert_rules[2].critical_threshold, 0.8)
        self.assertEqual(alert_rules[2].name, 'alert_name_3')
        self.assertEqual(alert_rules[2].project_name, self._project_name)
        self.assertEqual(alert_rules[2].model_name, self._model_name)
        self.assertEqual(
            alert_rules[2].alert_rule_uuid, '320060fa-abeb-4cae-9718-17d6f917b414'
        )
        self.assertIsNone(alert_rules[2].compare_period)
        self.assertEqual(len(alert_rules), 3)

        response_items = self.requests_mock.calls[0].response.json()['data']['items']

        self.assertEqual(response_items[0]['organization_name'], self._org)
        self.assertEqual(response_items[0]['model_name'], self._model_name)
        self.assertEqual(response_items[0]['project_name'], self._project_name)
        self.assertEqual(response_items[0]['alert_type'], 'drift')
        self.assertEqual(response_items[0]['name'], 'alert_name_1')

    def test_delete_alert_rule(self):
        url = self._get_url(alert_rule_uuid=self._alert_rule_uuid)
        self.requests_mock.delete(url)
        response = self.client.delete_alert_rule(self._alert_rule_uuid)
        self.assertIsNone(response)

    def test_delete_alert_rule_404(self):
        url = self._get_url(alert_rule_uuid=self._alert_rule_uuid)
        message = "AlertConfig({'uuid': " + self._alert_rule_uuid + '}) not found'
        response_body = {
            'error': {
                'code': 404,
                'message': message,
                'errors': [
                    {'reason': 'ObjectNotFound', 'message': message, 'help': ''}
                ],
            },
            'api_version': '2.0',
            'kind': 'ERROR',
        }
        self.requests_mock.delete(url, json=response_body, status=HTTPStatus.NOT_FOUND)
        with self.assertRaises(NotFound) as e:
            _ = self.client.delete_alert_rule(self._alert_rule_uuid)

        self.assertEqual(e.exception.message, message)

    def test_create_alert_rule_compare_one_month(self):
        response = {
            'data': {
                'organization_name': self._org,
                'project_name': self._project_name,
                'model_name': self._model_name,
                'baseline_name': 'baseline_name',
                'name': 'alert_name_com',
                'id': 86,
                'uuid': 'e7c7f891-53ba-4246-b691-53b6efda332b',
                'alert_type': 'drift',
                'metric': 'jsd',
                'sub_metric': 'jsd',
                'feature_names': ['probability_churned'],
                'time_bucket': 3600000,
                'compare_period': 2592000000,
                'compare_to': 'time_period',
                'warning_threshold': 0.7,
                'critical_threshold': 0.2,
                'condition': 'lesser',
                'details': 'New Alert',
                'created_by': 'admin@fiddler.ai',
                'priority': 'LOW',
                'is_active': True,
                'created_at': '2022-09-08T18:47:27.923000+00:00',
                'alert_log_time': '2022-09-08T18:47:29.087871+00:00',
            },
            'api_version': '2.0',
            'kind': 'NORMAL',
        }

        url = self._get_url()

        self.requests_mock.post(
            url,
            json=response,
        )

        # columns parameter is supported from 23.3.0
        server_info = ServerInfo(**{'feature_flags': {}, 'server_version': '23.3.0'})
        with mock.patch.object(
            self.client, 'server_info', server_info
        ) as mock_server_info:
            alert_rule = self.client.add_alert_rule(
                project_name=self._project_name,
                model_name=self._model_name,
                name='alert_name_com',
                priority=Priority.LOW,
                alert_type=AlertType.DATA_DRIFT,
                metric=Metric.JSD,
                columns=['probability_churned'],
                baseline_name='baseline_name',
                bin_size=BinSize.ONE_HOUR,
                compare_period= ComparePeriod.ONE_MONTH,
                compare_to=CompareTo.RAW_VALUE,
                warning_threshold=0.7,
                critical_threshold=0.2,
                condition=AlertCondition.LESSER,
                notifications_config={
                    'emails': {'email': 'nikhil@fiddler.ai, admin@fiddler.ai'},
                    'pagerduty': {
                        'service': 'pd_test_1, pd_test_2',
                        'severity': 'critical',
                    },
                    'webhooks': [{
                        'uuid' : '5e4eceae-0387-44fe-b726-7516c33e33fe'
                    }]
                },
            )

        self.assertEqual(
            alert_rule.alert_rule_uuid, 'e7c7f891-53ba-4246-b691-53b6efda332b'
        )
        self.assertEqual(alert_rule.project_name, self._project_name)
        self.assertEqual(alert_rule.model_name, self._model_name)
        self.assertEqual(alert_rule.alert_type, 'drift')
        self.assertEqual(alert_rule.critical_threshold, 0.2)
        self.assertEqual(alert_rule.name, 'alert_name_com')
        self.assertEqual(alert_rule.baseline_name, 'baseline_name')
        self.assertEqual(alert_rule.bin_size, BinSize.ONE_HOUR)
        self.assertEqual(alert_rule.columns, ['probability_churned'])
        self.assertEqual(alert_rule.compare_period, ComparePeriod.ONE_MONTH)

        request_body = json.loads(self.requests_mock.calls[0].request.body)

        self.assertEqual(len(self.requests_mock.calls), 1)
        self.assertEqual(request_body['model_name'], self._model_name)
        self.assertEqual(request_body['project_name'], self._project_name)
        self.assertEqual(request_body['organization_name'], self._org)
        self.assertEqual(request_body['name'], 'alert_name_com')
        self.assertEqual(request_body['alert_type'], 'drift')
        self.assertEqual(request_body['time_bucket'], 3600000)
        self.assertEqual(request_body['compare_period'], 2592000000)

    def test_create_alert_rule(self):
        response = {
            'data': {
                'created_by': 'admin@fiddler.ai',
                'priority': 'LOW',
                'alert_type': 'performance',
                'compare_period': 0,
                'time_bucket': 2592000000,
                'metric': 'r2',
                'model_name': self._model_name,
                'organization_name': self._org,
                'baseline_name': 'baseline_name',
                'created_at': '2022-09-15T18:10:38.286686+00:00',
                'critical_threshold': 0.2,
                'feature_names': ['age', 'gender'],
                'is_active': True,
                'uuid': '9f8180d3-3fa0-40c4-8656-b9b1d2de1b69',
                'compare_to': 'raw_value',
                'warning_threshold': 0.7,
                'condition': 'lesser',
                'project_name': self._project_name,
                'id': 86,
                'name': 'new_name',
            },
            'api_version': '2.0',
            'kind': 'NORMAL',
        }

        url = self._get_url()

        self.requests_mock.post(
            url,
            json=response,
        )

        # columns parameter is supported from 23.3.0
        server_info = ServerInfo(**{'feature_flags': {}, 'server_version': '23.3.0'})
        with mock.patch.object(
            self.client, 'server_info', server_info
        ) as mock_server_info:
            alert_rule = self.client.add_alert_rule(
                project_name=self._project_name,
                model_name=self._model_name,
                name='new_name',
                priority=Priority.HIGH,
                alert_type=AlertType.PERFORMANCE,
                metric=Metric.R2,
                columns=['age', 'gender'],
                baseline_name='baseline_name',
                bin_size=BinSize.ONE_MONTH,
                compare_to=CompareTo.RAW_VALUE,
                warning_threshold=0.7,
                critical_threshold=0.2,
                condition=AlertCondition.LESSER,
                notifications_config={
                    'emails': {'email': 'nikhil@fiddler.ai, admin@fiddler.ai'},
                    'pagerduty': {
                        'service': 'pd_test_1, pd_test_2',
                        'severity': 'critical',
                    },
                    'webhooks': [{
                        'uuid' : '5e4eceae-0387-44fe-b726-7516c33e33fe'
                    }]
                },
            )

        self.assertEqual(
            alert_rule.alert_rule_uuid, '9f8180d3-3fa0-40c4-8656-b9b1d2de1b69'
        )
        self.assertEqual(alert_rule.project_name, self._project_name)
        self.assertEqual(alert_rule.model_name, self._model_name)
        self.assertEqual(alert_rule.alert_type, 'performance')
        self.assertEqual(alert_rule.critical_threshold, 0.2)
        self.assertEqual(alert_rule.name, 'new_name')
        self.assertEqual(alert_rule.baseline_name, 'baseline_name')
        self.assertEqual(alert_rule.bin_size, BinSize.ONE_MONTH)
        self.assertEqual(alert_rule.columns, ['age', 'gender'])

        request_body = json.loads(self.requests_mock.calls[0].request.body)

        self.assertEqual(len(self.requests_mock.calls), 1)
        self.assertEqual(request_body['model_name'], self._model_name)
        self.assertEqual(request_body['project_name'], self._project_name)
        self.assertEqual(request_body['organization_name'], self._org)
        self.assertEqual(request_body['name'], 'new_name')
        self.assertEqual(request_body['alert_type'], 'performance')
        self.assertEqual(request_body['time_bucket'], 2592000000)

    def test_create_alert_rule_time_period(self):
        response = {
            'data': {
                'created_by': 'admin@fiddler.ai',
                'priority': 'LOW',
                'alert_type': 'drift',
                'compare_period': 86400000,
                'time_bucket': 3600000,
                'metric': 'jsd',
                'model_name': self._model_name,
                'organization_name': self._org,
                'created_at': '2022-09-15T18:10:38.286686+00:00',
                'critical_threshold': 0.2,
                'feature_names': ['age'],
                'is_active': True,
                'uuid': '9f8180d3-3fa0-40c4-8656-b9b1d2de1b69',
                'compare_to': 'time_period',
                'warning_threshold': 0.7,
                'condition': 'lesser',
                'project_name': self._project_name,
                'id': 86,
                'name': 'new_name',
            },
            'api_version': '2.0',
            'kind': 'NORMAL',
        }

        url = self._get_url()

        self.requests_mock.post(
            url,
            json=response,
        )

        # columns parameter is supported from 23.3.0
        server_info = ServerInfo(**{'feature_flags': {}, 'server_version': '23.3.0'})
        with mock.patch.object(
            self.client, 'server_info', server_info
        ) as mock_server_info:
            alert_rule = self.client.add_alert_rule(
                project_name=self._project_name,
                model_name=self._model_name,
                name='new_name',
                priority=Priority.HIGH,
                alert_type=AlertType.DATA_DRIFT,
                metric=Metric.JSD,
                columns=['age'],
                bin_size=BinSize.ONE_HOUR,
                compare_to=CompareTo.TIME_PERIOD,
                compare_period=ComparePeriod.ONE_DAY,
                warning_threshold=0.7,
                critical_threshold=0.2,
                condition=AlertCondition.LESSER,
                notifications_config={
                    'emails': {'email': 'nikhil@fiddler.ai, admin@fiddler.ai'},
                    'pagerduty': {
                        'service': 'pd_test_1, pd_test_2',
                        'severity': 'critical',
                    },
                    'webhooks': [{
                        'uuid' : '5e4eceae-0387-44fe-b726-7516c33e33fe'
                    }]
                },
            )

        self.assertEqual(
            alert_rule.alert_rule_uuid, '9f8180d3-3fa0-40c4-8656-b9b1d2de1b69'
        )
        self.assertEqual(alert_rule.alert_type, AlertType.DATA_DRIFT)
        self.assertEqual(alert_rule.critical_threshold, 0.2)
        self.assertEqual(alert_rule.name, 'new_name')
        self.assertEqual(alert_rule.columns, ['age'])
        self.assertEqual(alert_rule.compare_period, ComparePeriod.ONE_DAY)
        self.assertIsNone(alert_rule.baseline_name)
        request_body = json.loads(self.requests_mock.calls[0].request.body)

        self.assertEqual(len(self.requests_mock.calls), 1)
        self.assertEqual(request_body['model_name'], self._model_name)
        self.assertEqual(request_body['project_name'], self._project_name)
        self.assertEqual(request_body['organization_name'], self._org)
        self.assertEqual(request_body['name'], 'new_name')
        self.assertEqual(request_body['alert_type'], AlertType.DATA_DRIFT)

    def test_get_triggered_alerts(self):
        response = {
            'data': {
                'page_size': 100,
                'total': 151,
                'item_count': 100,
                'page_count': 2,
                'page_index': 1,
                'offset': 0,
                'items': [
                    {
                        'id': 285,
                        'uuid': 'ea45ff98-96de-4015-817d-00e571b3fac7',
                        'alert_config_uuid': self._alert_rule_uuid,
                        'alert_run_start_time': 1658481873833,
                        'alert_time_bucket': 1657710000000,
                        'alert_value': {'__DEFAULT__':0.789176795308359},
                        'baseline_time_bucket': None,
                        'baseline_value': None,
                        'is_alert': True,
                        'severity': None,
                        'failure_reason': 'NA',
                        'message': 'In project bank_churn and model  bank_churn, during the time period of one hour  starting |2022-07-13 11:00:00 (UTC time)|, the prediction drift score was 0.789,   greater than 0.1.',
                    },
                    {
                        'id': 287,
                        'uuid': '9cc8df42-73f4-4f5d-aea9-d8a5ab5b195e',
                        'alert_config_uuid': self._alert_rule_uuid,
                        'alert_run_start_time': 1658481873991,
                        'alert_time_bucket': 1657720800000,
                        'alert_value': {'__DEFAULT__':0.789176795308359},
                        'baseline_time_bucket': None,
                        'baseline_value': None,
                        'is_alert': True,
                        'severity': None,
                        'failure_reason': 'NA',
                        'message': 'In project bank_churn and model  bank_churn, during the time period of one hour  starting |2022-07-13 14:00:00 (UTC time)|, the prediction drift score was 0.789,   greater than 0.1.',
                    },
                    {
                        'id': 288,
                        'uuid': '5d2868cf-0321-46cd-af36-b784710b2295',
                        'alert_config_uuid': self._alert_rule_uuid,
                        'alert_run_start_time': 1658481874167,
                        'alert_time_bucket': 1657724400000,
                        'alert_value': {'__DEFAULT__':0.789176795308359},
                        'baseline_time_bucket': None,
                        'baseline_value': None,
                        'is_alert': True,
                        'severity': None,
                        'failure_reason': 'NA',
                        'message': 'In project bank_churn and model  bank_churn, during the time period of one hour  starting |2022-07-13 15:00:00 (UTC time)|, the prediction drift score was 0.789,   greater than 0.1.',
                    },
                ],
            }
        }
        url = self._get_url(alert_rule_uuid=self._alert_rule_uuid) + '/records'

        self.requests_mock.get(url, json=response)

        triggered_alerts = self.client.get_triggered_alerts(
            alert_rule_uuid=self._alert_rule_uuid,
            start_time='2022-07-12',
            end_time='2022-07-14',
        )

        self.assertIsInstance(triggered_alerts[0], TriggeredAlerts)
        self.assertEqual(triggered_alerts[0].alert_rule_uuid, self._alert_rule_uuid)
        self.assertEqual(triggered_alerts[0].alert_value, {'__DEFAULT__':0.789176795308359})
        self.assertEqual(triggered_alerts[0].failure_reason, 'NA')
        self.assertEqual(triggered_alerts[0].is_alert, True)

        response_items = self.requests_mock.calls[0].response.json()['data']['items']

        self.assertEqual(response_items[0]['is_alert'], True)
        self.assertEqual(response_items[0]['id'], 285)
        self.assertEqual(response_items[0]['alert_time_bucket'], 1657710000000)
        self.assertEqual(response_items[0]['alert_config_uuid'], self._alert_rule_uuid)


if __name__ == '__main__':
    unittest.main()
