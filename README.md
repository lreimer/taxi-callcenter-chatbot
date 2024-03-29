# Taxi Call Center Chatbot

A PoC implementation for a GenAI based taxi call center chatbot.

## Usage

```bash
# setup your local Python environment
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

# create cloud storage and run
$ gcloud storage buckets create gs://taxi-callcenter-bucket --location=eu
$ python chatbot.py
$ gsutil ls gs://taxi-callcenter-bucket
$ gsutil cp gs://taxi-callcenter-bucket/hello_callcenter.mp3 .
```

## Maintainer

M.-Leander Reimer (@lreimer), <mario-leander.reimer@qaware.de>

## License

This software is provided under the MIT open source license, read the `LICENSE`
file for details.
