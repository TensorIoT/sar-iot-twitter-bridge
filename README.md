# AWS IOT - Twitter Bridge

Have you devices tweet on your behalf. This service provides a bridge between AWS IOT and Twitter. Now using this service, the text messages sent by devices via aws iot can be forwarded to Twitter.

## Input Format from the IOT Topic

~~~~
{
    "deviceID": "deviceID123",
    "incomingText": "Text From Device"
}

~~~~

## Needed configuration

The following items needs to be configured in the template

~~~~
1.) CONSUMERKEY - Twitter app Consumer key.
2.) CONSUMERSECRET - Twitter app Consumer secret.
3.) IncomingTopic - The topic that will be used as the trigger for the lambda.
4.) TOKEN - Twitter app Token.
5.) TOKENSECRET - Twitter app Token secret.




