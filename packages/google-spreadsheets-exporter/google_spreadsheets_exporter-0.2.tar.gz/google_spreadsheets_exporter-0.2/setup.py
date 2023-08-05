from setuptools import setup

setup(
    name='google_spreadsheets_exporter',
    version='0.2',
    packages=['google_spreadsheets_exporter'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
    ],
    exclude_package_data={'google_spreadsheets_exporter': ['creds.json', 'test.py']}
)