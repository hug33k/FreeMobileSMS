# Free Mobile SMS

[![Build Status](https://travis-ci.org/hug33k/FreeMobileSMS.svg?branch=master)](https://travis-ci.org/hug33k/FreeMobileSMS)
[![PyPI version](https://badge.fury.io/py/freemobilesms.svg)](https://badge.fury.io/py/freemobilesms)
<img src="http://www.universfreebox.com/UserFiles/image/freemobile(1).png" alt="Logo Free Mobile" height="50px;"/>

## Description

Python client to send SMS via french mobile operator Free Mobile.

## Configuration

### With environment variables

You need to set ___SMS_LOGIN___ and ___SMS_TOKEN___ variables.

### With configuration file

You have to write your infos in a file like this :

```json
{
    "login": YOUR_FREE_MOBILE_LOGIN,
    "token": TOKEN_GIVEN_BY_FREE_MOBILE
}
```

Now, you can have to use it with specific flag (--config=_FILE_).

## Usage

#### Python

````python
from freemobilesms import SMS


service = SMS()
service.send("Message")
````

#### Command Line

```shell
$>./sms.py "Hello World"
200 Message send

$>./sms.py --config=my_config.json "Hello world"
200 Message send

$>echo "Foo" | ./sms.py
200 Message send

$>echo "Bar" > tmp && ./sms.py < tmp
200 Message send
```

## Status values

* 200 : Message send
* 400 : Missing parameter
* 402 : Too much messages send
    * You have to wait a little to reuse it.
* 403 : Service not enable
    * You can enable the service in your [Free Mobile panel](https://mobile.free.fr/moncompte/)
* 500 : Server not available
    * You have to try later.
