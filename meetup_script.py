import requests
import json
import sys
from slackclient import SlackClient


class Meetup():

    API_KEY = 'YOUR_API_KEY'
    EVENT_URL = "https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=GROUP_NAME&page=2&key={}&format=json"
    RSVP_URL = "https://api.meetup.com/2/rsvp?event_id={}&rsvp=yes&key={}"

    def __init__(self):
        pass

    def _send_message(self, content, success=False):
        """
        Function to send a message to slack with the status flag i.e if the API was successful or not.

        :param content: JSON payload containing API response.
        :type content: json string

        :param success: Boolean flag indicating if the API was successful or not.
        :type success: boolean

        :return: None
        :rtype: None
        """
        slack_token = "slack_token"
        sc = SlackClient(slack_token)
        if success:
            message = "RSVP Successful! {}".format(content['tallies'])
                sc.api_call(
                        "chat.postMessage",
                        channel="your_channel_or_username",
                        text=message
                        )
        else:
            message = "RSVP Failed! {}".format(content)
                sc.api_call(
                        "chat.postMessage",
                        channel="your_channel_or_username",
                        text=message
                        )
                print("Sent message to slack!")

    def _get_event_id(self):
        """
        Function to get the event ID for the given meetup group. The event ID is needed as part of the API.

        :return event_id: String containing the event_id if successful, exits the program if not successful.
        :rtype event_id: string
        """
        response = requests.get(self.EVENT_URL.format(self.API_KEY))
            try:
                data = response.json()['results'][0]
            except Exception as e:
                print("Failed to parse json")
                    print(response.content)
                    sys.exit(1)

            # This part helps identify if 'Sunday' is present in the meetup title, as I wanted to go only for the sunday events.
            # Feel free to remove this condition if needed.
            if 'Sunday' in data['name']:
                event_id = data['id']
            else:
                print("Event ID not found!")
                    print("Response: ".format(response.json()))
                    sys.exit(1)
            return event_id

    def make_request(self):
        """
        Function to make the API request.
        """
        event_id = self._get_event_id()
            rsvp_url = self.RSVP_URL.format(event_id, self.API_KEY)
            response = requests.post(rsvp_url)
            if response.status_code in [201, 202]:
                self._send_message(response.json(), True)
            else:
                print("RSVP Failed")
                print(response.json())
                self._send_message(response.json(), False)


if __name__ == "__main__":
    Meetup().make_request()
