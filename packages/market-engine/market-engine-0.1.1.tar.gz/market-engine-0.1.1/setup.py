from setuptools import setup, find_packages

setup(
    name='market-engine',
    version='0.1.1',
    description='Engine for easily getting the orders, statistics, and other stats from warframe.market.',
    author='Jacob McBride',
    author_email='jake55111@gmail.com',
    packages=find_packages(),
    install_requires=[
        'aiohttp~=3.8.4',
        'redis~=4.6.0',
        'beautifulsoup4~=4.12.2',
        'PyMySQL~=1.1.0',
        'fuzzywuzzy~=0.18.0',
        'pytz~=2023.3',
        'aiolimiter~=1.1.0',
        'tenacity~=8.2.2'
    ],
)