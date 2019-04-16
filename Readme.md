# Zappa with subdirectories for deployable components

Repo to show how to break up zappa code and settings across directories with a zappa_settings instead of multiple repos.

## Setup

`pip install zappa`

## Comp1 build

`cd comp1`

`zappa deploy comp1`

`zappa undeploy -f comp1`

## Comp2 build

`cd comp2`

`zappa deploy comp2`

`zappa undeploy -f comp2`

## Tricky part

The includes when building from an IDE are pathed differently AFAIK.

```python
import platform

if 'Linux' in platform.platform():
    from sqs_service import send_message_to_queue
else:
    from .sqs_service import send_message_to_queue

```

It is my understanding that Zappa will 'zip' everything in directory, unless excluded so any shared files will need to be in each subdirectory from the parent.  For example *sqs_service.py*

