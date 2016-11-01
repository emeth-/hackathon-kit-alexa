Hackathon-kit
===========

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

##### SETUP
```
- Install heroku toolbelt (https://toolbelt.heroku.com/)
- Install git
- Install python 2.7.6
- Install pip (e.g. sudo easy_install pip)
```

```
<clone our app to a local git repository>
$ sudo pip install -r requirements.txt
$ heroku apps:create hackathon-demo
$ heroku config:set IS_HEROKU_SERVER=1
$ heroku config:set ALEXA_APP_ID_topopps=amzn1.ask.skill.b9b3ac07-6eeb-4534-bc3f-b0b2073363e5
(replace the above ID with your own)
$ git push heroku master
```

##### Alexa SETUP
To setup app:
https://developer.amazon.com/edw/home.html

Follow screenshots in setup_screenshots folder. Important part is that the contents of intent_schema.json, opp_name_list.txt, and utterances_schema.txt are uploaded into the appropriate spots on #2 Interaction Model screen.

##### Notes

A skill can have a total of 50,000 custom slot values, totaled across all custom slots used in the interaction model.

Note that a custom slot type is not the equivalent of an enumeration. Values outside the list may still be returned if recognized by the spoken language understanding system. Although input to a custom slot type is weighted towards the values in the list, it is not constrained to just the items on the list.