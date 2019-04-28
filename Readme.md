# Zappa and Docker Example

This repo shows how to use docker with zappa to deploy multiple lambdas that have dependencies on third party libraries that need to be built in the AWS Linux Python 3.6 environment.


## Environment Variables
export AWS_SECRET_ACCESS_KEY=
export AWS_ACCESS_KEY_ID=
export AWS_DEFAULT_REGION=us-east-1

## Docker
execute: `run_aws_docker.sh`

## In Docker shell

python -m venv aws_venv

source aws_venv/bin/activate

## Install libraries
pip install -r aws_requirements.txt

## Zappa
zappa deploy comp1

## Tricky part

make sure to exclude the directories you do not want to include for each of the subdirectories components.

For example in the comp1 configuration we do not want code from comp2:

```json
        "exclude": [
            "comp2"
        ]

```

## Test SFTP Server
Part of the this sample app is to see that we can pull in Paramiko which is a library
that needs to be build for the AWS Linux environment.

To do that comp1.SqsSubcriberComp1.py connects to the test SFTP server.

https://www.wftpserver.com/onlinedemo.htm