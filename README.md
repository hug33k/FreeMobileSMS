#Free Mobile SMS

##Description

Python client to send SMS via french mobile operator Free Mobile.

##Configuration

You have to write your informations in config.json like this :
````json
{
    "login": YOUR_FREE_MOBILE_LOGIN,
    "token": TOKEN_GIVEN_BY_FREE_MOBILE
}
````

You can use a different name for config file but you have to launch script with specific flag (--config=FILE).

##Usage

````shell
$>./sms.py "Hello World"
200 Message send

$>./sms.py --config=my_config.json "Hello world"
200 Message send
````

##Possible return values

* 200 : Message send
* 400 : Missing parameter
* 402 : Too much messages send
    You have to wait a little to reuse it.
* 403 : Service not enable
    You can enable the service in your [Free Mobile panel](https://mobile.free.fr/moncompte/)
* 500 : Server not available
    You have to try later.

##Want to use this service with an other Python project?

You just have to reuse the FreeMobileSMS class, it is easy to use ;)
