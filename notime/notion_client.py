import requests
import os
from dotenv import load_dotenv

load_dotenv()


class NotionAPIClient:
    """
    A client for interacting with the Notion API.
    """

    def __init__(self):
        """
        Initializes the client with the Notion token and database ID,
        and sets up the headers required for API requests.
        """
        self.notion_token = os.getenv(
            "NOTION_TOKEN"
        )  # Retrieve the Notion API token from environment variables
        self.database_id = os.getenv(
            "DATABASE_ID"
        )  # Retrieve the Notion Database ID from environment variables

        # Define the headers
        self.headers = {
            "Authorization": f"Bearer {self.notion_token}",  # Bearer token for authorization
            "Content-Type": "application/json",  # JSON content type for requests
            "Notion-Version": "2022-06-28",  # Specify the version of the Notion API
        }

    def get_data(self):
        """
        Sends a POST request to retrieve data from the Notion database.

        Returns:
            dict: The response from the API, parsed as JSON.
        """

        # Endpoint for querying the database
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        response = requests.post(
            url, headers=self.headers
        )  # Send the POST request with headers
        return response.json()  # Return the response data as JSON

    def update_page(self, page_id, data):
        """
        Sends a PATCH request to update a specific page in the Notion database.

        Args:
            page_id (str): The ID of the page to update.
            data (dict): The new data to update the page with.

        Returns:
            dict: The response from the API, parsed as JSON.
        """

        # Endpoint for updating a page
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = requests.patch(
            url, headers=self.headers, json=data
        )  # Send the PATCH request with headers and JSON data
        return response.json()  # Return the response data as JSON

    def get_sprint(self, sprint_number):
        """
        Sends a POST request to get all cards from a specific sprint.

        Args:
            sprint_number (int): The sprint number to pull.

        Returns:
            dict: The response from the API, parsed as JSON.
        """
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        payload = {
            "filter": {
                "property": "Sprint",
                "multi_select": {"contains": f"Sprint {sprint_number}"},
            }
        }

        response = requests.post(
            url, headers=self.headers, json=payload
        )  # Send the PATCH request with headers and JSON data
        return response.json()  # Return the response data as JSON
