# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['activity_tracking']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'activity-tracking',
    'version': '0.0.1',
    'description': 'Utility functions for desktop activity tracking',
    'long_description': '# activity tracking library\n\nThis library contains utility functions for recording desktop activity on windows and linux\n\nI created this for my productivity tool [Activity Monitor](https://github.com/elpachongco/activity-monitor)\n\n## Features \n- Cross platform [windows, linux(ubuntu, X window system)]\n\n## Functions \n\n- Get foreground window name, process, pid\n- is user active\n\n',
    'author': 'elpachongco',
    'author_email': 'earlsiachongco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elpachongco/activity-tracking-lib',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
