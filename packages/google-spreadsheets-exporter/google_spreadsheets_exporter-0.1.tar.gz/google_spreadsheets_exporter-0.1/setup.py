from setuptools import setup

setup(
    name='google_spreadsheets_exporter',
    version='0.1',
    packages=['google_spreadsheets_exporter'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
    ],
)