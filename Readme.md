# Zappa with subdirectories for deployable components

Repo to show how to break up zappa code and settings across directories with a zappa_settings instead of multiple repos.

## Setup

`pip install zappa`

## Comp1 build

`zappa deploy comp1`

`zappa undeploy -f comp1`

## Comp2 build

`zappa deploy comp2`

`zappa undeploy -f comp2`

## Tricky part

make sure to exclude the directories you do not want to include for each of the subdirectories components.

For example in the comp1 configuration we do not want code from comp2:

```json
        "exclude": [
            "comp2"
        ]

```
