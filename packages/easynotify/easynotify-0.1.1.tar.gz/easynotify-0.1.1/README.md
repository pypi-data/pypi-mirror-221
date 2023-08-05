# EasyNotify
This package allows you to post messages with bots easily.

## Install
Install this package:

```pip install easynotify```

If it does not work, try:

```pip install git+https://github.com/CauchyComplete/EasyNotify```

## SlackBot
In your slack workspace, click the top left menu > Settings & administartion > Manage apps.

Search for "Incomming Webhooks" and click "Add to Slack".

Choose a channel you want to use and click "Add Incoming Webhooks integration".

Now you can post onto this workspace using this library.

```angular2html
import easynotify
bot = easynotify.SlackBot("https://hooks.slack.com/services/...")  # Your Webhook URL
bot.post("Test Message", username="SlackBot", icon_emoji=":ghost:", print_also=True)
```
