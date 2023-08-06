import requests
import json

class SlackMessage:
    def __init__(self, webhook_url, channel):
        """
        Initiate SlackMessage with webhook_url and channel.
        Args:
          webhook_url (str): The Slack Incoming Webhook URL.
          channel (str): The Slack channel to send the messages to (e.g., "#your-channel").
        """
        self.webhook_url = webhook_url
        self.channel = channel

    def send_messages(self, messages):
        """
        Sends a list of messages to Slack using the provided webhook URL.
        Args:
          messages (list): A list of message content to send to Slack.
        """

        blocks = []
        for message in messages:
            block = {"type": "section", "text": {"type": "mrkdwn", "text": message}}
            blocks.append(block)
        payload = {"channel": self.channel, "blocks": blocks}
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.webhook_url, json=payload, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Error sending Slack messages: {response.text}")
