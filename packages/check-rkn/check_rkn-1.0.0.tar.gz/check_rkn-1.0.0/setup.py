# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_rkn']

package_data = \
{'': ['*']}

install_requires = \
['anticaptchaofficial>=1.0.53,<2.0.0', 'selenium>=4.10.0,<5.0.0']

setup_kwargs = {
    'name': 'check-rkn',
    'version': '1.0.0',
    'description': 'Library that check blocked website on blocklist.rkn.gov.ru',
    'long_description': '# Check_rkn\n\n[![PyPI](https://img.shields.io/pypi/v/check-rkn)](https://pypi.org/project/check-rkn/)\n\nThis is library, that check blocked websites on [blocklist.rkn.gov.ru](https://blocklist.rkn.gov.ru/). Library uses [Selenium](https://pypi.org/project/selenium/) and [anticaptchaofficial](https://pypi.org/project/anticaptchaofficial/). *WARNING!*  You need to register on [anti-captcha.com](https://anti-captcha.com/) to get the api key and top up your balance (For residents of the Russian federation: MIR cards are available, you can also pay with cryptocurrency)\n\n## How to use\n\n```python \nfrom check_rkn.check_rkn import check_website\n\nresult = check_website("your_url", "your_api_key")\nprint(result) # True if website is blocked or False if no\n\n```\n\n## License - [Apache 2.0](NOTICE)\n',
    'author': 'IvanyaK',
    'author_email': 'ivanrus200519@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/IvanyaK/check-rkn',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
