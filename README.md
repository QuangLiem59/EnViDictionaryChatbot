## Installation

- [Installing Rasa Open Source](https://rasa.com/docs/rasa/installation/installing-rasa-open-source)

* Rasa version

```bash
Rasa Version      :         3.6.20
Minimum Compatible Version: 3.5.0
Rasa SDK Version  :         3.6.2
Python Version    :         3.8.10
Operating System  :         Linux-5.10.16.3-microsoft-standard-WSL2-x86_64-with-glibc2.29
Python Path       :         /usr/bin/python3
```

- Rasa SDK version

```bash
Name: rasa-sdk
Version: 3.6.2
Summary: Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants
Home-page: https://rasa.com
Author: Rasa Technologies GmbH
Author-email: hi@rasa.com
License: Apache-2.0
Location: /home/liem/.local/lib/python3.8/site-packages
Requires: coloredlogs, pluggy, prompt-toolkit, ruamel.yaml, sanic, Sanic-Cors, setuptools, typing-extensions, websockets, wheel
Required-by: rasa
```

- Train the Bot

```bash
rasa init
```

- Run Rasa Action Server

```bash
rasa run actions
```

- Run the Rasa Shell (test your bot in the terminal)

```bash
rasa shell
```

- Connect to a Frontend
  Integrate the bot with platforms like Slack, Facebook Messenger, or a custom website using `credentials.yml`. To run on a web interface:

```bash
rasa run --enable-api
```

## Modify and Extend

- **Define Intents and Entities**: Update `nlu.yml` with more intents and entities.
- **Stories**: Update `stories.yml` with conversation paths.
- **Responses**: Update `domain.yml` with appropriate responses.
- **Custom Actions**: Implement Python-based logic in `actions.py` and define them in `domain.yml`.

## Demo

[![Demo Video](https://i9.ytimg.com/vi_webp/zFHxeZwN6qw/mq2.webp?sqp=CNDAiLwG-oaymwEmCMACELQB8quKqQMa8AEB-AGACYAC0AWKAgwIABABGBogZShPMA8=&rs=AOn4CLA3QSJwe7bVK0JkEEsyyOx9r6HY7Q)](https://www.youtube.com/watch?v=zFHxeZwN6qw)
