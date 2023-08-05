# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geo', 'lyft_bikes', 'lyft_bikes.geo', 'lyft_bikes.historical']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['pandas', 'requests']

extras_require = \
{'boundary': ['geopandas'], 'index': ['lxml']}

setup_kwargs = {
    'name': 'lyft-bikes',
    'version': '0.1.0',
    'description': 'Python Client for Lyft Bike Sharing Data.',
    'long_description': '# Lyft Bike Share Data\n\nPython client for Lyft bike share data.\n\n## Features \n\n- Support for [cities](https://www.lyft.com/bikes#cities) with Lyft bike share\n- [Historical trips](https://wd60622.github.io/lyft-bikes/examples/historical-trips/)\n- Live station and bike / scooter availability\n- [Applying pricing to trips](https://wd60622.github.io/lyft-bikes/examples/new-pricing/)\n    - Unlock Fees\n    - Minute Rates\n\n## Installation \n\nInstall from `pip` \n\n```shell \n$ pip install lyft-bikes\n```\n\n## Documentation\n\nThe documentation is hosted on [GitHub Pages](https://wd60622.github.io/lyft-bikes/).\n\n## Development\n\nThe development environment was created with [`poetry`](https://python-poetry.org/docs/). The `pyproject.toml` file is the main configuration file for the project.\n\n```bash\npoetry install . \n```\n\n## Contributing\n\nIf you would like to contribute or find some issue in the code, please [open an Issue](https://github.com/wd60622/divvy/issues/new) or a PR on GitHub. Thanks!',
    'author': 'Will Dean',
    'author_email': 'wd60622@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://wd60622.github.io/divvy/',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
