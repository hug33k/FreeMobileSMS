#Free Mobile SMS
[![Build Status](https://travis-ci.org/hug33k/FreeMobileSMS.svg?branch=master)](https://travis-ci.org/hug33k/FreeMobileSMS)
![Logo Free Mobile](http://www.universfreebox.com/UserFiles/image/freemobile(1).png)

##Description

Python client to send SMS via french mobile operator Free Mobile.

##Configuration

###With environment variables

You need to set ___SMS_LOGIN___ and ___SMS_TOKEN___ variables.

###With configuratino file
You have to write your informations in a file like this :
````json
{
    "login": YOUR_FREE_MOBILE_LOGIN,
    "token": TOKEN_GIVEN_BY_FREE_MOBILE
}
````

Now, you can have to use it with specific flag (--config=_FILE_).

##Usage

````shell
$>./sms.py "Hello World"
200 Message send

$>./sms.py --config=my_config.json "Hello world"
200 Message send

$>echo "Foo" | ./sms.py
200 Message send

$>echo "Bar" > tmp && ./sms.py < tmp
200 Message send
````

##Possible return values

* 200 : Message send
* 400 : Missing parameter
* 402 : Too much messages send
    * You have to wait a little to reuse it.
* 403 : Service not enable
    * You can enable the service in your [Free Mobile panel](https://mobile.free.fr/moncompte/)
* 500 : Server not available
    * You have to try later.

##Want to use this service with an other Python project?

You just have to reuse the FreeMobileSMS class, it is easy to use ;)
