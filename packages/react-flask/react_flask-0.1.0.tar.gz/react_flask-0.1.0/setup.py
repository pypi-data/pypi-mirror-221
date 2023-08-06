# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src',
 'src.beckett',
 'src.beckett.renderer',
 'src.beckett.renderer.html',
 'src.beckett.renderer.typescript_react',
 'src.beckett.types',
 'src.views']

package_data = \
{'': ['*'],
 'src': ['js/*',
         'js/api/*',
         'js/components/*',
         'js/template/people/*',
         'static/*',
         'template/*',
         'template/index/*']}

install_requires = \
['Flask>=2.2.3,<3.0.0',
 'Jinja2>=3.1.2,<4.0.0',
 'black>=23.3.0,<24.0.0',
 'click>=8.1.3,<9.0.0',
 'inflection>=0.5.1,<0.6.0',
 'isort>=5.12.0,<6.0.0',
 'mkdocs-material>=9.1.13,<10.0.0',
 'mkdocs>=1.4.3,<2.0.0',
 'mypy>=1.1.1,<2.0.0',
 'pydantic>=2.0.3,<3.0.0',
 'ruff>=0.0.267,<0.0.268',
 'structlog>=22.3.0,<23.0.0',
 'typing-extensions>=4.7.1,<5.0.0']

setup_kwargs = {
    'name': 'react-flask',
    'version': '0.1.0',
    'description': 'Fully typed Flask and React applications',
    'long_description': "# 💫 React Flask (RF)\n\n### Fully typed Flask and React applications\n\n![maze](/docs/banner.jpg)\n\nWelcome to RF, a _strongly-linked_ Flask and React application template.\n\nRF combines a [Flask](https://flask.palletsprojects.com/en/2.3.x/) server, with a [React TypeScript](https://www.typescriptlang.org/docs/handbook/react.html) UI into a comprehensive full-stack framework for building modern web applications.\n\nRF features a sophisticated types manager that automatically synchronizes [Python Type hints](https://docs.python.org/3/library/typing.html) and [TypeScript interfaces](https://www.typescriptlang.org/docs/handbook/interfaces.html). This means that as you make changes to your API code in the server, RF diligently keeps the API Client up to date.\n\n## Built on popular tools\n\nWe use cutting edge Python tools including:\n\n* [Pydantic 2.0](https://docs.pydantic.dev/latest/)\n* [Flask 2.3](https://flask.palletsprojects.com/en/2.3.x/)\n\nAnd our TypeScript is modern too:\n\n* [Node 18.17.0](https://nodejs.org/en)\n* [React 18](https://react.dev/)\n* [TypeScript 5.1](https://www.typescriptlang.org/)\n\nBoth TypeScript and Python hold their positions as two of the [most widely used programming languages globally](https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/). As a result, they are frequently combined in various projects.\n\nHowever, setting up a smooth and efficient development environment that integrates these languages can be a cumbersome and time-consuming process, often leading to a subpar developer experience. Thankfully, RF steps in to solve this challenge by through it's sophisticated types manager.\n\n## Type-safe productivity boost\n\nRF provides:\n\n* A types manager which keeps the API interface type-safe.\n* React: A collection of type-safe API hooks for querying the HTTP API.\n* React: No single page app, so bundled JS for the client loads faster.\n* Flask: A manager for generating new React pages without any manual effort.\n* Flask: View-based routing to reduce the bundle size of JS on page loads.\n\n## Currently in development\n\nBefore this becomes a fully fledged package, it exists as a decent template that can be forked when you start a new project and worked on from there.\n\n## Set up\n\nFork the code, then run the build and dev command to get started:\n\n```bash\ngit clone git@github.com:beckett-software/react-flask.git\ncd react-flask\nmake build\nmake dev\n```\n",
    'author': 'Paul Hallett',
    'author_email': 'paulandrewhallett@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11.2,<4.0.0',
}


setup(**setup_kwargs)
