import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def lambda_handler(event, context):
    logger.info('this is blank lambda to set lambda function on Terraform')


def test():
    deploy_path = os.path.join(os.pardir, 'deploy')
    invocation_file = os.path.join(deploy_path, 'input_for_invocation.json')
    if os.path.exists(invocation_file):
        event = json.load(open(invocation_file, 'r'))
        context = {}
        lambda_handler(event, context)
    else:
        print('No invocation file found')


if __name__ == '__main__':
    test()
