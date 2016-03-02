#!/usr/bin/env python
# coding: utf-8
# Created on: 24.02.2016
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from __future__ import print_function
import os
from subprocess import call

gh_token = os.environ['GH_TOKEN']
repo_slug= os.environ['TRAVIS_REPO_SLUG']
gh_repo_url = 'https://{gh_token}@github.com/{repo_slug}.git'.format(gh_token=gh_token,
                                                                     repo_slug=repo_slug)
devnull = open(os.devnull, 'w')


def execute(args, silent=False):
    if silent:
        stdout = stderr = devnull
    else:
        stdout = stderr = None
    res = call(args, stdout=stdout, stderr=stderr)
    if res:
        raise RuntimeError('Call {call} returned error code {res}'.format(
            call=str(args).replace(gh_token, '*****'),
            res=res))


base_dir = os.path.dirname(os.path.abspath(__file__))
docs_dir = os.path.join(base_dir, 'docs')
html_dir = os.path.join(docs_dir, '_build', 'html')
os.chdir(docs_dir)
execute(['make', 'html'])
os.chdir(html_dir)
execute(['git', 'init'])
execute(['git', 'config', 'user.name', '"Roman Miroshnychenko"'])
execute(['git', 'config', 'user.email', '"romanvm@yandex.ua"'])
open('.nojekyll', 'w').close()
execute(['git', 'add', '--all', '.'])
execute(['git', 'commit', '-m' '"Updates docs"'])
execute(['git', 'push', '--force', '--quiet', gh_repo_url, 'HEAD:gh-pages'], silent=True)
print('Docs published to GitHub Pages.')
