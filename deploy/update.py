"""
├── deploy
│   ├── config.json
│   └── update.py (this file)
└── src
    └── lambda_function.py
"""

import os
from pathlib import Path
import shutil
import json
from pprint import pprint

AWS_CMD_PATH = '/usr/local/bin/aws'

TARGET_SOURCE_DIR = Path.cwd().parent / 'src'
DEPLOY_DIR = Path.cwd()
BUILD_FILE_PREFIX = 'lambda'
BUILD_FILE = DEPLOY_DIR / '{}.zip'.format(BUILD_FILE_PREFIX)
CONFIG_FILE = 'config.json'
AWS_PROFILE = os.environ['AWS_PROFILE']

with open(CONFIG_FILE, 'r') as F:
    CONFIG = json.load(F)
    CONFIG.update({'AWS_PROFILE': AWS_PROFILE})


def main():
    pprint(CONFIG)
    BUILD_FILE.unlink(missing_ok=True)

    args = CONFIG
    args.update({'cmd': AWS_CMD_PATH, 'source': str(BUILD_FILE), 'file': str(BUILD_FILE.name)})

    shutil.make_archive(os.path.join(DEPLOY_DIR, BUILD_FILE_PREFIX), 'zip', root_dir=TARGET_SOURCE_DIR)

    aws_s3_cp = "{cmd} s3 cp {source} s3://{bucket}/{module}/{function_name}/{file}".format(**args)
    print(aws_s3_cp)

    # アップロードを実行し、zipファイルを削除する
    os.system(aws_s3_cp)
    BUILD_FILE.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
