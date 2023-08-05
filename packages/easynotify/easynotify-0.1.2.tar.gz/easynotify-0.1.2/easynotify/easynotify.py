"""
2023-07-24
Myung-Joon Kwon (CauchyComplete)
corundum240@gmail.com
"""
import requests


class SlackBot:
    def __init__(self, url, username=None, channel=None, icon_emoji=None, print_also=False):
        self.url = url
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji
        self.print_also = print_also

    def post(self, text, username=None, channel=None, icon_emoji=None, print_also=None):
        if username is None:
            username = self.username
        if channel is None:
            channel = self.channel
        if icon_emoji is None:
            icon_emoji = self.icon_emoji
        if print_also is None:
            print_also = self.print_also
        payload = {
            "channel": channel,
            "username": username,
            "icon_emoji": icon_emoji,
            "text": text,
        }
        if username is None:
            payload.pop("username")
        if channel is None:
            payload.pop("channel")
        if icon_emoji is None:
            payload.pop("icon_emoji")
        if print_also:
            print_username = username if username is not None else "SlackBot"
            print(f"{print_username}: {text}")

        # Send POST request
        if self.url is not None:
            requests.post(self.url, json=payload)

