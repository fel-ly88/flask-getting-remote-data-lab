import requests


class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response_body(self):
        """Send an HTTP GET request to the URL and store the raw response bytes."""
        self.response = requests.get(self.url)
        return self.response.content  # return bytes to match test expectations

    def load_json(self):
        """Parse the stored response as JSON and return it."""
        if self.response is None:
            self.response = requests.get(self.url)
        try:
            return self.response.json()
        except ValueError:
            return None