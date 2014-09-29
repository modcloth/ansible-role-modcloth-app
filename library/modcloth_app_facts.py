#!/usr/bin/env python
# vim:fileencoding=utf-8

import os
import sys

import requests


GITHUB_API = os.environ.get('GITHUB_API', 'https://api.github.com')


def main(sysargs=sys.argv[:]):
    module = AnsibleModule(
        argument_spec=dict(
            github_token=dict(required=True),
            repo=dict(required=True),
            revision=dict(required=True),
        )
    )
    module.exit_json(
        changed=False,
        ansible_facts=dict(
            modcloth_app_deployer=_get_deployer(),
            modcloth_app_tag_annotation=_get_tag_annotation(
                module.params['repo'],
                module.params['revision'],
                module.params['github_token']
            ),
            modcloth_app_hipchat_html=_get_hipchat_html(),
            modcloth_app_facted=True,
        )
    )
    return 0


def _get_hipchat_html():
    return os.path.join(
        tempfile.gettempdir(),
        '.modcloth_app_hipchat_notification.frag.html'
    )


def _get_deployer():
    return subprocess.check_output(
        ['git', 'config', 'user.name']
    ).strip()


def _get_tag_annotation(repo, revision, github_token, api=GITHUB_API):
    url = '{api}/repos/{repo}/git/refs/tags/{revision}'.format(
        api=api, repo=repo, revision=revision
    )
    response_json = requests.get(
        url, auth=(github_token, 'x-oauth-basic')
    ).json()

    commit_url = response_json.get('object', {}).get('url')
    if not commit_url:
        return ''

    message = requests.get(
        commit_url, auth=(github_token, 'x-oauth-basic')
    ).json().get('message', '').strip()

    if message:
        return ' ({}) '.format(message)
    return ''


from ansible.module_utils.basic import *
main()
