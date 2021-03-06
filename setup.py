from setuptools import setup

setup(
    name='salesforce-fetcher',
    version='0.1.0',
    py_modules=['fetcher'],
    python_requires='>=2.7',
    install_requires=[
        'Click',
        'simple-salesforce',
        'salesforce-bulk',
        'pyOpenSSL>=0.14',
        'pyyaml>=3.12',
        'pyjson==1.3.0',
        'pytz==2019.2',
    ],
    data_files = [('salesforce-fetcher/queries',[
      'queries/contact_history.soql',
      'queries/foundation_signups.soql',
      'queries/petition_signups.soql',
    ])],
    author='Aaron Wirick',
    author_email='awirick@mozilla.com',
    description='Python tool for fetching bulk queries and reports from Salesforce',
    entry_points='''
        [console_scripts]
        salesforce-fetcher=fetcher:run
    ''',
)

