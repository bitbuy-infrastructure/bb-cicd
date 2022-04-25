# bb-template-helm-repos

<!-- TOC -->

- [bb-template-helm-repos](#bb-template-helm-repos)
  - [Requirements](#requirements)
  - [Helm commands](#helm-commands)
    - [Install](#install)
    - [Update](#update)
    - [Delete](#delete)
  - [Dev](#dev)
    - [Linting](#linting)
  - [Doco](#doco)

<!-- /TOC -->

## Requirements

1. helm
1. python
1. setup pre-commit for this repo

## Helm commands

### Install

*NOTE:* this example is for new-qa cluster
1. `export HELM_ENV=new-qa`
1. `helm upgrade --install <deployment name> <helm chart repo> -f configs/${HELM_ENV}/values.yaml --namespace <namespace> --create-namespace --wait`

### Update

1. `helm upgrade --install <deployment name> <helm chart repo> -f configs/${HELM_ENV}/values.yaml --namespace <namespace> --create-namespace --wait`

### Delete

1. `helm delete <deployment name> --namespace <namespace>`

## Dev

### Linting

-run these commands on the root of the repository-

```bash
pip install pre-commit-hooks
pre-commit install
pre-commit run --all-files
```

## Doco

main helm repo url
