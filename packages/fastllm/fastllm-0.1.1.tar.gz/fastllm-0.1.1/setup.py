# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastllm']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.2.1,<3.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'jsonschema>=4.18.4,<5.0.0',
 'openai>=0.27.8,<0.28.0']

setup_kwargs = {
    'name': 'fastllm',
    'version': '0.1.1',
    'description': 'Fast and easy wrapper around LLMs.',
    'long_description': '# FastLLM\n\nFast and simple wrapper around LLMs. The package aims to be simply, precise and allows for fast prototyping of agents and applications around LLMs. At the moment focus around OpenAI\'s chat models.\n\n**Warning - experimental package and subject to change.** For features and plans see the [roadmap](#roadmap).\n\n## Samples\n\nRequire an openai api key in `OPENAI_API_KEY` environment variable or `.env` file.\n\n```bash\nexport OPENAI_API_KEY=...\n```\n\n### Agents\n\n```python\nfrom fastllm import Agent\n\nfind_cities = Agent("List {{ n }} cities comma separated in {{ country }}.")\ncities = find_cities(n=3, country="Austria").split(",")\n\nprint(cities)\n```\n\n```bash\n[\'Vienna\', \'Salzburg\', \'Graz\']\n```\n\n```python\nfrom fastllm import Agent, Message, Model, Prompt, Role\n\ns = ";"\n\ncreative_name_finder = Agent(\n    Message("You are an expert name finder.", Role.SYSTEM),\n    Prompt("Find {{ n }} names.", temperature=2.0),\n    Prompt("Print names {{ s }} separated, nothing else!"),\n    model=Model("gpt-4"),\n)\n\nnames = creative_name_finder(n=3, s=s).split(s)\n\nprint(names)\n```\n\n```bash\n[\'Ethan Gallagher, Samantha Cheng, Max Thompson\']\n```\n\n#### Functions\n\nFunctions can be added to Agents, Models or Prompts. Either as initial arguments or as decorator. Functions type hints, documentation and name are inferred from the function and added to the model call.\n\n```python\nfrom typing import Literal\n\nfrom fastllm import Agent, Prompt\n\ncalculator_agent = Agent(\n    Prompt("Calculate the result for task: {{ task }}"),\n    Prompt("Only give the result number as result without anything else!"),\n)\n\n\n@calculator_agent.function\ndef calculator(a, b, operator: Literal["+", "-", "*", "/"]):\n    """A basic calculator using various operators."""\n\n    match operator:\n        case "+":\n            return a + b\n        case "-":\n            return a - b\n        case "*":\n            return a * b\n        case "/":\n            return a / b\n        case _:\n            raise ValueError(f"Unknown operator {operator}")\n\n\nresult = calculator_agent(task="give the final result for (11 + 14) * (6 - 2)")\n\nprint(result)\n\nanother_result = calculator_agent(\n    task="if I have 114 apples and 3 children, how many apples will each child get?"\n)\n\nprint(another_result)\n```\n\n```bash\n100\n38\n```\n\n## Roadmap\n\n### Features\n\n- [x] Prompts using jinja2 templates\n- [x] LLM calling with backoff and retry\n- [x] Able to register functions to agents, models and prompts using decorators\n- [x] Possible to register functions on multiple levels (agent, model, prompt). The function call is only available on the level it was registered.\n- [x] Conversation history. The Model class keeps track of the conversation history.\n- [x] Function schema is inferred from python function type hints, documentation and name\n- [x] Function calling is handled by the Model class itself. Meaning if a LLM response indicate a function call, the Model class will call the function and return the result back to the LLM\n- [ ] Function calling can result in an infinite loop if LLM can not provide function name or arguments properly. This needs to be handled by the Model class.\n- [ ] Prompts with pattern using logit bias to guide LLM completion.\n- [ ] Handling of multiple response messages from LLMs in a single call. At the moment only the first response is kept.\n- [ ] Supporting non chat based LLMs (e.g. OpenAI\'s completion LLMs).\n- [ ] Supporting other LLMs over APIs except OpenAI\'s. (e.g. google, anthropics, etc.)\n- [ ] Supporting local LLMs (e.g. llama-1, llama-2, mpt, etc.)\n\n### Package\n\n- [x] Basic package structure and functionality\n- [x] Test cases and high test coverage\n- [ ] Tests against multiple python versions\n- [ ] 100% test coverage (at the moment around 90%)\n- [ ] Better documentation including readthedocs site.\n- [ ] Better error handling and logging\n- [ ] Better samples using jupyter notebooks\n- [ ] Set up of pre-commit\n- [ ] CI using github actions\n- [ ] Prober release and versioning\n\n## Development\n\nUsing [poetry](https://python-poetry.org/docs/#installation).\n\n```bash\npoetry install\n```\n\n### Tests\n\n```bash\npoetry run pytest\n``` ',
    'author': 'Clemens Kriechbaumer',
    'author_email': 'clemens.kriechbaumer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/clemens33/fastllm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
