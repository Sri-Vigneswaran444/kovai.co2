import requests
from config import DOCUMENT360_API_URL, API_KEY, USER_ID, PROJECT_VERSION_ID, CATEGORY_ID

def upload_to_document360(html_body):

    headers = {
        "api_token": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "title": "Migrated Article",
        "content": html_body,
        "categoryId": CATEGORY_ID,
        "projectVersionId": PROJECT_VERSION_ID,
        "userId": USER_ID
    }

    response = requests.post(
        DOCUMENT360_API_URL,
        headers=headers,
        json=payload
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    return response.text