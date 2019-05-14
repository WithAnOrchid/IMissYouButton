# IMissYouButton
Easiest way to send "I miss you" message during meeting, using Amazon IoT Button

| File | Usage |
| ------ | ------ |
| handler.py | handle incoming signal from the button, and invoke other Lambda functions accordingly |
| getToken.js | retetive a session token from WeChat |
| sendMsg.js | compose message body |
| handler.js | call getToken and sendMsg |
