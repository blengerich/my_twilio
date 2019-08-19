# my_twilio

Used to text myself when training has finished.

## Usage
Sign up for an account on twilio.com. The free trial includes $25 of credit. At a price of about 1c per text, this is about 2500 notifications.

### Install
```bash
git clone https://github.com/blengerich/my_twilio
cd my_twilio
pip install -e .
```

Copy the config file to a private file that will contain the information from your Twilio account:
```
cp config_template.py config.py
vim config.py
```
Do NOT share config.py (it is ignored by .gitignore by default).

### Use the Available Dicts in Python
```python
>>> import my_twilio
>>> my_twilio.text_me("Training Finished!")