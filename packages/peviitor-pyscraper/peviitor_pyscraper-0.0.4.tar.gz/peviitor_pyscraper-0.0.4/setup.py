from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='peviitor_pyscraper',
    version='0.0.4',
    description='A simple scraper',
    url="https://github.com/lalalaurentiu/peviitor_pyscraper",
    author='Laurentiu Baluta',
    author_email="contact@laurentiumarian.ro",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=find_packages(),

    install_requires=[
        'beautifulsoup4==4.9.3',
        'bs4==0.0.1',
        'certifi==2020.12.5',
        'chardet==4.0.0',
        'idna==2.10',
        'lxml==4.9.2',
        'requests==2.25.1',
        'soupsieve==2.2',
        'urllib3==1.26.3',
    ],
    python_requires='>=3.6',
)


