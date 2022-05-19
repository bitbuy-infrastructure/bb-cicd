# bb-cicd

- [bb-cicd](#bb-cicd)
  - [Requirements](#requirements)
  - [Dev](#dev)
    - [running locally](#running-locally)
    - [Linting](#linting)

## Requirements

1. python
1. setup pre-commit for this repo

## Dev

### running locally

1. assuming that you are running your dev from withing `bb-cicd` folder
1. setup env vars:
    ```bash
      export PIPELINE_TENANT='bbtd'
      export PIPELINE_ENV='np'
      export PIPELINE_ZONE='main01'
      export GITHUB_WORKSPACE='../'
      export DEPLOYMENT_FOLDER='ci-demo'
    ```
1. run
    ```bash
    └> python src/pipeline.py
    2022-05-18 13:48:01.376 | DEBUG    | __main__:<module>:13 - PIPELINE_TENANT: bbtd, PIPELINE_ENV: np, PIPELINE_ZONE: main01, GITHUB_WORKSPACE: ../, DEPLOYMENT_FOLDER: ci-demo
    2022-05-18 13:48:01.376 | INFO     | __main__:<module>:20 - looking at common.yaml file from ..//ci-demo/configs/common.yaml
    2022-05-18 13:48:01.376 | INFO     | __main__:<module>:21 - looking at values.yaml file from ..//ci-demo/configs/bbtd/values.yaml
    2022-05-18 13:48:01.380 | INFO     | __main__:<module>:29 - ci-demo:
      image:
        repository: 972594475906.dkr.ecr.ca-central-1.amazonaws.com/test/bitbuy-infrastructure/ci-demo
        tag: PIPELINE_TAG
      configMaps:
        envVars:
        - PORT: 8080
      ingress:
        enable: true
        annotations:
          kubernetes.io/ingress.class: nginx
        rules:
        - host: PIPELINE_DNS_PREFIX-ci-demo.teod.bitbuy.private
          pathType: Prefix
          paths:
          - /
      service:
        name: ci-demo-dev
      env:
      - NAME: HELL0
        VALUE: World
    ```

### Linting

-run these commands on the root of the repository-

```bash
pip install pre-commit-hooks
pre-commit install
pre-commit run --all-files
```
