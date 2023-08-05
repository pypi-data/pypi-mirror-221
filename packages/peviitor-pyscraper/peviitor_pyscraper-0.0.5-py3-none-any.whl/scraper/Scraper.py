from bs4 import BeautifulSoup
import requests
import io
import subprocess

class Scraper(BeautifulSoup):
    
    def __init__(self, markup="", features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, element_classes=None, **kwargs):
        """
        Initialize Scraper class.

        Attributes:
            markup (str): HTML markup to be parsed.
            features (str): HTML parser to be used.
            builder (TreeBuilder): TreeBuilder to be used.
            parse_only (SoupStrainer): SoupStrainer to be used.
            from_encoding (str): Encoding to be used.
            exclude_encodings (list): Encodings to be excluded.
            element_classes (dict): Dictionary of element classes.
            **kwargs: Keyword arguments.
        """
        self.headers = self.set_headers()
        super().__init__(markup, features, builder, parse_only, from_encoding, exclude_encodings, element_classes, **kwargs)

    def set_headers(self, *args):
        """
        Set headers for requests.

        Attributes:
            **kwargs: Keyword arguments.
        Sets:
            self.headers (dict): Headers for requests.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        if args:
            headers.update(*args)

        self.headers = headers

    def session(self):
        """
        Create a session for requests.

        Returns:
            requests.Session: Session for requests.
        """
        return requests.Session()
    
    def get_from_url(self, url:str, type:str="HTML", **kwargs):
        """
        Set markup from URL.

        Attributes:
            url (str): URL to get data from.
            type (str): Type of data to get.
            params (dict): Parameters to be used.
            **kwargs: Keyword arguments.

        Sets:
            self.markup (str): Markup from URL.
        """
        session = self.session()
        response = session.get(url, headers=self.headers, **kwargs)

        if type == "HTML":
            self.markup = response.text
            self.__init__(self.markup, 'html.parser')
        elif type == "JSON":
            self.markup = response.json()
        else:
            self.markup = response.text
        
    def post(self, url: str, data: dict):
        """
        Post data to URL.

        Attributes:
            url (str): URL to post data to.
            data (dict): Data to be posted.

        Returns:
            requests.Response: Response from post request.
        """
        session = self.session()
        return session.post(url, data=data, headers=self.headers)
    
    def render_page(self, url: str):
        """
        Render page using JavaScript.

        Attributes:
            url (str): URL to render.

        """
        session = self.session()
        response = session.get(url, headers=self.headers)

        """
        This is the JavaScript code that will be executed in Node.js.
        It will render the page using JavaScript and return the markup.
        """

        js = f"""const {{ Scraper }} = require('peviitor_jsscraper');

            async function main() {{
                const scraper = new Scraper("{url}");
                soup = await scraper.render_page();
                console.log(soup.prettify());
            }}

            main();"""

        """
        Create a file-like object from the response content.
        """
        file = io.BytesIO()
        file.write(response.content)
        file.seek(0)

        process = subprocess.run(["node", "-e", js], input=file.read(), capture_output=True)
        if process.returncode != 0:
            raise Exception("Failed to render page, make sure you have node and peviitor_jsscraper installed")
        
        self.markup = process.stdout.decode("utf-8")
        self.__init__(self.markup, 'html.parser')
        return self.markup