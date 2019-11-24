#!/usr/bin/env python
# coding: utf-8
import os
import json
import yaml
from dotenv import load_dotenv
from urllib.parse import urljoin
import requests

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
TOKEN = os.environ.get('TOKEN', '')
BASE_PATH = os.environ.get('BASE_PATH', '')


def get_jobs():
    project = 'test01'
    path = 'project/{}/jobs'.format(project)
    api = urljoin(BASE_PATH, path)

    print(api)

    headers = {
        'X-Rundeck-Auth-Token': TOKEN,
        'Accept': 'application/json'
    }

    res = requests.get(api, headers=headers)
    print(res)
    print(json.dumps(res.json(), indent=2))
    # 073d3026-9887-4d44-8504-ecec0fee9cbc


def import_job():
    project = 'test01'
    path = 'project/{}/jobs/import?dupeOption=update'.format(project)
    api = urljoin(BASE_PATH, path)

    print(api)

    headers = {
        'X-Rundeck-Auth-Token': TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/yaml'
    }

    job_data = [
        {
            "defaultTab": "nodes",
            "description": "",
            "executionEnabled": True,
            # "id": "073d3026-9887-4d44-8504-ecec0fee9cbc",
            "loglevel": "INFO",
            "name": "job01",
            "nodeFilterEditable": True,
            "scheduleEnabled": True,
            "sequence": {
                "commands": [
                    {
                        "exec": "ifconfig"
                    }
                ],
                "keepgoing": True,
                "strategy": "node-first"
            },
            "uuid": "073d3026-9887-4d44-8504-ecec0fee9cbc"
        }
    ]

    job_yaml = yaml.safe_dump(job_data)
    print(job_yaml)

    res = requests.post(api, data=job_yaml, headers=headers)
    print(res)
    print(json.dumps(res.json(), indent=2))


if __name__ == '__main__':
    get_jobs()
    # import_job()
