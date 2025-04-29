# https://github.com/zerwes/hiyapyco
import os

import hiyapyco
import yaml
from loguru import logger

PIPELINE_TENANT = os.getenv('PIPELINE_TENANT')
PIPELINE_ENV = os.getenv('PIPELINE_ENV')
PIPELINE_ZONE = os.getenv('PIPELINE_ZONE')
GITHUB_WORKSPACE = os.getenv('GITHUB_WORKSPACE')
ARGOCD_FOLDER = os.getenv('ARGOCD_FOLDER')
DEPLOYMENT_FOLDER = os.getenv('DEPLOYMENT_FOLDER')
DEPLOYMENT_TAG = os.getenv('DEPLOYMENT_TAG')

# get the service name (expected input example microservices/ci-demo)
# microservices/ should be a constant

split_string = str(DEPLOYMENT_FOLDER).split('/', 1)
service_name = split_string[1]

logger.debug(
    f'PIPELINE_TENANT: {PIPELINE_TENANT}, \
      PIPELINE_ENV: {PIPELINE_ENV}, \
      PIPELINE_ZONE: {PIPELINE_ZONE}, \
      GITHUB_WORKSPACE: {GITHUB_WORKSPACE}, \
      DEPLOYMENT_FOLDER: {DEPLOYMENT_FOLDER}, \
      service_name: {service_name}',
)

# this is diff when testing local vs in github actions

common_yaml = f'{GITHUB_WORKSPACE}/configs/common.yaml'
env_yaml = f'{GITHUB_WORKSPACE}/configs/{PIPELINE_TENANT}/values.yaml'

logger.info(f'looking at common.yaml file from {common_yaml}')
logger.info(f'looking at values.yaml file from {env_yaml}')

conf = hiyapyco.load(
    f'{common_yaml}',
    f'{env_yaml}',
    method=hiyapyco.METHOD_MERGE, interpolate=True, failonmissingfiles=True,
)

conf[service_name]['image']['tag'] = DEPLOYMENT_TAG

if "flywayImage" in conf[service_name]:
    conf[service_name]['flywayImage']['tag'] = DEPLOYMENT_TAG

output = yaml.safe_load(hiyapyco.dump(conf, default_flow_style=False))

logger.debug(output)

# {GITHUB_WORKSPACE}/bb-argocd-microservices-deployment/microservices/ci-demo/bbtd/np/main01/values.yaml
deployment_file = f'{GITHUB_WORKSPACE}/{ARGOCD_FOLDER}/{DEPLOYMENT_FOLDER}/{PIPELINE_TENANT}/{PIPELINE_ENV}/{PIPELINE_ZONE}/values.yaml'

logger.info(f'this file is been updated with default_style: {deployment_file}')
# if locally testing
# deployment_file = 'values.yaml'

with open(deployment_file, 'w') as file:
    yaml.dump(output, file, default_style='"')
