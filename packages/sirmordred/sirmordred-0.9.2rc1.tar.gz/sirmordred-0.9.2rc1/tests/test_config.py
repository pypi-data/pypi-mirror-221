#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Valerio Cosentino <valcos@bitergia.com>
#     Miguel Ángel Fernández <mafesan@bitergia.com>

import sys
import tempfile
import unittest

# Hack to make sure that tests import the right packages
# due to setuptools behaviour
sys.path.insert(0, '..')

from sirmordred.config import (Config, logger)

CONF_FULL = 'test.cfg'
CONF_SLIM = 'test_studies.cfg'
CONF_WRONG = 'test_wrong.cfg'


class TestConfig(unittest.TestCase):
    """Config tests"""

    def test_init(self):
        """Test whether attributes are initializated"""

        config = Config(CONF_FULL)

        self.assertIsNotNone(config.conf)
        self.assertIsNone(config.raw_conf)
        self.assertEqual(config.conf_list, [CONF_FULL])
        self.assertEqual(len(config.conf.keys()), 47)

    def test_init_studies(self):
        """Test whether studies' attributes are initialized"""

        config = Config(CONF_SLIM)

        self.assertIsNotNone(config.conf)
        self.assertIsNone(config.raw_conf)
        self.assertEqual(config.conf_list, [CONF_SLIM])

        top_sections = config.conf.keys()
        demography_params = config.conf['enrich_demography:git'].keys()
        enrich_areas_of_code_params = config.conf['enrich_areas_of_code:git'].keys()
        enrich_onion_git_params = config.conf['enrich_onion:git'].keys()
        enrich_extra_data_git_params = config.conf['enrich_extra_data:git'].keys()
        enrich_onion_github_params = config.conf['enrich_onion:github'].keys()
        enrich_onion_gerrit_params = config.conf['enrich_onion:gerrit'].keys()
        enrich_demography_gerrit_params = config.conf['enrich_demography:gerrit'].keys()
        enrich_demography_contribution_gerrit_params = config.conf['enrich_demography_contribution:gerrit'].keys()

        self.assertIn('general', top_sections)
        self.assertIn('projects', top_sections)
        self.assertIn('es_collection', top_sections)
        self.assertIn('es_enrichment', top_sections)
        self.assertIn('sortinghat', top_sections)
        self.assertIn('panels', top_sections)
        self.assertIn('phases', top_sections)

        self.assertIn('git', top_sections)
        self.assertIn('enrich_demography:git', top_sections)
        self.assertIn('date_field', demography_params)
        self.assertIn('author_field', demography_params)

        self.assertIn('enrich_areas_of_code:git', top_sections)
        self.assertIn('in_index', enrich_areas_of_code_params)
        self.assertIn('out_index', enrich_areas_of_code_params)
        self.assertIn('sort_on_field', enrich_areas_of_code_params)
        self.assertIn('no_incremental', enrich_areas_of_code_params)

        self.assertIn('enrich_onion:git', top_sections)
        self.assertIn('in_index', enrich_onion_git_params)
        self.assertIn('out_index', enrich_onion_git_params)
        self.assertIn('data_source', enrich_onion_git_params)
        self.assertIn('contribs_field', enrich_onion_git_params)
        self.assertIn('timeframe_field', enrich_onion_git_params)
        self.assertIn('sort_on_field', enrich_onion_git_params)
        self.assertIn('no_incremental', enrich_onion_git_params)
        self.assertIn('seconds', enrich_onion_git_params)

        self.assertIn('enrich_extra_data:git', top_sections)
        self.assertIn('json_url', enrich_extra_data_git_params)
        self.assertIn('target_index', enrich_extra_data_git_params)

        self.assertIn('github:issue', top_sections)
        self.assertIn('github:pull', top_sections)
        self.assertIn('enrich_onion:github', top_sections)
        self.assertIn('in_index_iss', enrich_onion_github_params)
        self.assertIn('in_index_prs', enrich_onion_github_params)
        self.assertIn('out_index_iss', enrich_onion_github_params)
        self.assertIn('in_index_prs', enrich_onion_github_params)
        self.assertIn('data_source_iss', enrich_onion_github_params)
        self.assertIn('data_source_prs', enrich_onion_github_params)
        self.assertIn('contribs_field', enrich_onion_github_params)
        self.assertIn('timeframe_field', enrich_onion_github_params)
        self.assertIn('sort_on_field', enrich_onion_github_params)
        self.assertIn('no_incremental', enrich_onion_github_params)
        self.assertIn('seconds', enrich_onion_github_params)

        self.assertIn('gerrit', top_sections)
        self.assertIn('enrich_demography_contribution:gerrit', top_sections)
        self.assertIn('date_field', enrich_demography_contribution_gerrit_params)
        self.assertIn('author_field', enrich_demography_contribution_gerrit_params)

        self.assertIn('gerrit', top_sections)
        self.assertIn('enrich_demography:gerrit', top_sections)
        self.assertIn('date_field', enrich_demography_gerrit_params)
        self.assertIn('author_field', enrich_demography_gerrit_params)

        self.assertIn('enrich_onion:gerrit', top_sections)
        self.assertIn('in_index', enrich_onion_gerrit_params)
        self.assertIn('out_index', enrich_onion_gerrit_params)
        self.assertIn('data_source', enrich_onion_gerrit_params)
        self.assertIn('contribs_field', enrich_onion_gerrit_params)
        self.assertIn('timeframe_field', enrich_onion_gerrit_params)
        self.assertIn('sort_on_field', enrich_onion_gerrit_params)
        self.assertIn('no_incremental', enrich_onion_gerrit_params)
        self.assertIn('seconds', enrich_onion_gerrit_params)

        self.assertIn('githubql', top_sections)
        self.assertIn('enrich_reference_analysis', top_sections)

    def test_create_config_file(self):
        """Test whether a config file is correctly created"""

        tmp_path = tempfile.mktemp(prefix='mordred_')

        config = Config(CONF_FULL)
        config.create_config_file(tmp_path)
        copied_config = Config(tmp_path)
        # TODO create_config_file produces a config different from the original one
        # self.assertDictEqual(config.conf, copied_config.conf)

    def test_check_config(self):
        """Test whether the config is properly checked"""

        with self.assertRaises(Exception):
            Config(CONF_WRONG)

    def test_get_data_sources(self):
        """Test whether all data sources are properly retrieved"""

        config = Config(CONF_FULL)

        expected = ['askbot', 'bugzilla', 'bugzillarest', 'confluence', 'discourse', 'dockerhub', 'functest',
                    'gerrit', 'git', 'gitlab', 'github', 'google_hits', 'groupsio', 'hyperkitty', 'jenkins', 'jira',
                    'mbox', 'meetup', 'mediawiki', 'mozillaclub', 'nntp', 'phabricator', 'pipermail', 'puppetforge',
                    'redmine', 'remo', 'rss', 'stackexchange', 'slack', 'supybot', 'telegram', 'twitter']
        data_sources = config.get_data_sources()

        self.assertEqual(len(data_sources), len(expected))
        self.assertEqual(data_sources.sort(), expected.sort())

    def test_set_param(self):
        """Test whether a param is correctly modified"""

        config = Config(CONF_FULL)

        self.assertFalse(config.conf['twitter']['collect'])
        config.set_param("twitter", "collect", "true")
        self.assertTrue(config.conf['twitter']['collect'])

    def test_set_param_not_found(self):
        """Test whether an error is logged if a param does not exist"""

        config = Config(CONF_FULL)

        with self.assertLogs(logger, level='ERROR') as cm:
            config.set_param("twitter", "acme", "true")
            self.assertEqual(cm.output[-1], 'ERROR:sirmordred.config:Config section twitter and param acme not exists')

    def test_backend_composition_by_get_backend_section(self):
        """Test the ability to parameterize backends as in the docs for get_backend_section"""

        config = Config(CONF_FULL)
        config.conf = {
            'backend:param1': {
                'shared_param': 'value 1',
                'unique_to_1': 'value 2',
            },
            'backend:param2': {
                'shared_param': 'value 3',
                'unique_to_2': 'value 4',
            },
            'backend:param1:param2': {
                'param_combo': 'value 5',
            }
        }

        self.assertEqual(config.get_backend_section('backend'), dict())
        self.assertEqual(config.get_backend_section('backend', 'param1'), {
            'shared_param': 'value 1',
            'unique_to_1': 'value 2',
        })
        self.assertEqual(config.get_backend_section('backend', 'param2'), {
            'shared_param': 'value 3',
            'unique_to_2': 'value 4',
        })
        self.assertEqual(config.get_backend_section('backend', 'param2', 'param1'), {
            'shared_param': 'value 1',  # Param1 takes priority
            'unique_to_1': 'value 2',
            'unique_to_2': 'value 4',
        })
        self.assertEqual(config.get_backend_section('backend', 'param1', 'param2'), {
            'shared_param': 'value 3',  # Param2 takes priority
            'unique_to_1': 'value 2',
            'unique_to_2': 'value 4',
            'param_combo': 'value 5',  # This shows up because its an exact match
        })

        config.conf['backend'] = {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        }

        self.assertEqual(config.get_backend_section('backend'), {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        })
        self.assertEqual(config.get_backend_section('backend', 'nonexistant'), {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        })
        self.assertEqual(config.get_backend_section('backend', 'param1'), {
            'unique_to_base': 'value 6',
            'unique_to_1': 'value 2',
            'shared_param': 'value 1',
        })

    def test_backend_composition_by_get_item(self):
        """Test the ability to parameterize backends as in the docs for get_backend_section"""

        # This code is p much copy-pasted from the above test case, save the way that the
        # backends are accessed

        config = Config(CONF_FULL)
        config.conf = {
            'backend:param1': {
                'shared_param': 'value 1',
                'unique_to_1': 'value 2',
            },
            'backend:param2': {
                'shared_param': 'value 3',
                'unique_to_2': 'value 4',
            },
            'backend:param1:param2': {
                'param_combo': 'value 5',
            }
        }

        self.assertEqual(config['backend'], dict())
        self.assertEqual(config['backend:param1'], {
            'shared_param': 'value 1',
            'unique_to_1': 'value 2',
        })
        self.assertEqual(config['backend:param2'], {
            'shared_param': 'value 3',
            'unique_to_2': 'value 4',
        })
        self.assertEqual(config['backend:param2:param1'], {
            'shared_param': 'value 1',  # Param1 takes priority
            'unique_to_1': 'value 2',
            'unique_to_2': 'value 4',
        })
        self.assertEqual(config['backend:param1:param2'], {
            'shared_param': 'value 3',  # Param2 takes priority
            'unique_to_1': 'value 2',
            'unique_to_2': 'value 4',
            'param_combo': 'value 5',  # This shows up because its an exact match
        })

        config.conf['backend'] = {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        }

        self.assertEqual(config['backend'], {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        })
        self.assertEqual(config['backend:nonexistant'], {
            'unique_to_base': 'value 6',
            'shared_param': 'value 7',
        })
        self.assertEqual(config['backend:param1'], {
            'unique_to_base': 'value 6',
            'unique_to_1': 'value 2',
            'shared_param': 'value 1',
        })

    def test_contains(self):

        config = Config(CONF_FULL)
        config.conf = {
            'backend:param1': {
                'shared_param': 'value 1',
                'unique_to_1': 'value 2',
            },
            'backend:param2': {
                'shared_param': 'value 3',
                'unique_to_2': 'value 4',
            },
            'backend:param1:param2': {
                'param_combo': 'value 5',
            }
        }

        # Directly contained
        self.assertIn('backend:param1', config)
        self.assertIn('backend:param2', config)
        self.assertIn('backend:param1:param2', config)

        # Implicitly contained
        self.assertIn('backend:param2:param1', config)
        self.assertIn('backend:fake:param1', config)
        self.assertIn('backend:param1:fake', config)

        # Not contained
        self.assertNotIn('backend', config)
        self.assertNotIn('backend:fake', config)
        self.assertNotIn('fake-backend:param1', config)

        # Set the previously missing backend param
        config.conf['backend'] = {
            'arbitrary_data': 'idc',
        }

        # Contained after backend specified
        self.assertIn('backend', config)
        self.assertIn('backend:fake', config)
        self.assertIn('backend:param1', config)

        # Still not contained
        self.assertNotIn('fake-backend:param1', config)
        self.assertNotIn('fake-backend', config)

    def test_get(self):

        config = Config(CONF_FULL)
        config.conf = {
            'backend:param1': {
                'dummy': 'data',
            },
        }

        self.assertEqual(config.get('backend'), None)
        self.assertEqual(config.get('backend', 'hiya!'), 'hiya!')
        self.assertEqual(config.get('backend:param1'), config['backend:param1'])
        self.assertEqual(config.get('backend:param1', 'inspecific string'), config['backend:param1'])


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
