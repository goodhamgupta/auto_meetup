# Auto Meetup

**auto_meetup** is a library to automatically RSVP for your favorite events on [Meetup](https://meetup.com). 

## Installation

We will install the dependencies using a virtual environment and pip3.

```bash
cd auto_meetup/
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
```

## Usage

- First set your `API_KEY` in the Meetup class. You can obtain this key from [here](https://secure.meetup.com/meetup_api/key/).
- Set your public `GROUP_NAME` in the `EVENT_URL` attribute. This refers to the events from the group you want to automatically RSVP.
- Set your `slack_token` in the `send_message` function. This token will be used to send updates of the API to slack.
- Set the slack channel to which you want to send the updates. Update the attributes `channel` in the `_send_message` function.
- Setup a cronjob to periodically run the script. My current cronjob has the following syntax:
```bash
0-5 11 * * 5 python3 /home/ubuntu/meetup_script.py >> /home/ubuntu/cron.log 2>&1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
