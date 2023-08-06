from setuptools import setup

setup(
    name='Edgar13F',
    version='0.1.0',
    author='Jack Brown',
    author_email='jackabrown21@gmail.com',
    packages=['Edgar13F'],
    description='A Python package for scraping 13F filings from the SEC Edgar database.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'beautifulsoup4',
        'python-dotenv'
    ],
)
