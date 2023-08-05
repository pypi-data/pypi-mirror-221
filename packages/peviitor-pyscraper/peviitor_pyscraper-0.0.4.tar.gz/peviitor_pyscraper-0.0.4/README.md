# Peviitor Scraper

![Pe Viitor logo](https://peviitor.ro/static/media/peviitor_logo.df4cd2d4b04f25a93757bb59b397e656.svg)

## Description

**peviitor_pyscraper** is a Python-based scraping library that relies on HTML parsing libraries, Beautiful Soup, and Requests. It allows you to extract the required data from web pages and save them in an easily usable format such as CSV or JSON. With **peviitor_pyscraper**, you can select specific HTML elements from a web page and extract necessary information like text, links, images, etc.

Features of **peviitor_pyscraper**:

 - Utilizes popular Python libraries, BeautifulSoup and Requests, to facilitate web scraping.
 - Extracts the required data from a web page using specific HTML selections.
 - Provides a variety of storage options for the scraped data, including JSON.
 - Is easy to use and integrate into existing Python projects.
 - It can render pages with dynamically generated elements.

**peviitor_pyscraper** is an excellent choice for Python developers seeking a powerful and flexible web scraping library. With **peviitor_pyscraper**, you can automate the process of extracting data from web pages, saving time and effort.

## Installation

1. You need to have Python 3.6 or higher installed on your computer.
`pip install peviitor-pyscraper`
2. Node JS is required for rendering pages with dynamically generated elements.
`npm i peviitor_jsscraper`

## Usage Examples

1. Downloading the content from a specific URL:
   ```py
    from scraper import Scraper
    scraper = Scraper()
    html = scraper.get_from_url('https://www.example.ro')
    print(html.prettify())
    ```
    The two lines of code create a Scraper object with the URL https://www.example.ro and then download the HTML code from that URL using the `get_from_url()` method, which returns a BeautifulSoup object that can be later used to search for specific elements within the web page.

    To extract all "a" tags that contain an "href" attribute starting with "https://" from the downloaded HTML code, you can use the following code:
    ```py
    from scraper import Scraper
    scraper = Scraper()
    html = scraper.get_from_url('https://www.example.ro')
    links = html.find_all('a', href=re.compile('^https://'))
    for link in links:
        print(link.get('href'))
    ```

    To extract the first "h1" tag from the page:
    ```py
    from scraper import Scraper
    scraper = Scraper()
    html = scraper.get_from_url('https://www.example.ro')
    h1 = html.find('h1')
    print(h1.text)
    ```

2. Downloading JSON content from a specific URL:

    ```py
    from scraper import Scraper
    scraper = Scraper()
    json = scraper.get_from_url('https://api.example.ro', type='JSON')
    print(json)
    ```

    These lines of code create a Scraper object with the URL https://api.example.ro and then download the JSON content from that URL using the `get_from_url()` method, which returns a JSON object that can be later used to search for specific elements within the web page.

    To make a POST request to a specific URL:
    ```py
    from scraper import Scraper
    scraper = Scraper()
    data = {'key1': 'value1', 'key2': 'value2'}
    response = scraper.post('https://api.example.ro', data=data, type='JSON')
    json = response.json()
    print(json)
    ```

3. The **peviitor_pyscraper** can render pages with dynamically generated elements.
    ```py
    from scraper import Scraper
    scraper = Scraper()
    html = scraper.render_page('https://www.example.ro')
    print(html.prettify())
    ```

4. Contains all BeautifulSoup methods and attributes.
    
## Contributing

If you want to contribute to the development of the scraper, there are several ways you can do so. First, you can help by contributing to the source code by adding new features or fixing existing issues. Second, you can contribute to improving the documentation or translating it into other languages. Additionally, if you want to help but are unsure how to get started, you can check our list of open issues and ask us how you can assist. For more information, please refer to the "Contribute" section in our documentation.

## License
    
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
    
If you have any questions or suggestions, please contact us at

- Email: contact@laurentiumarian.ro
- Website: https://laurentiumarian.ro
- GitHub: https://github.com/lalalaurentiu

## Acknowledgements
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/master/)
    
    
