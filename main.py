import os
import requests
import json


def main():
    webhook = os.environ['INPUT_WEBHOOK']
    title = os.environ['INPUT_TITLE']
    subtitle = os.environ['INPUT_SUBTITLE']
    message = os.environ['INPUT_MESSAGE']
    status = os.environ['INPUT_STATUS']

    if title == '_REPO_NAME_':
        title = os.environ['GITHUB_REPOSITORY']

    if subtitle == '_REPO_BRANCH_':
        subtitle = os.environ['GITHUB_REF']

    if status.upper() == "SUCCESS":
        status = ':heavy_check_mark:'
    else:
        status = ':x:'

    encoded_message = {
        'text': f'''*{title}* {status}\n{subtitle}''',
        'attachments': [
            {
                'text': message
            }
        ]
    }

    response = requests.post(webhook, data=json.dumps(encoded_message), headers={'Content-Type': 'application/json'})

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
