# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grid',
 'grid.cli',
 'grid.client',
 'grid.client.routing',
 'grid.models',
 'grid.models.bloom',
 'grid.models.llama',
 'grid.server',
 'grid.utils']

package_data = \
{'': ['*']}

install_requires = \
['Dijkstar>=2.6.0',
 'accelerate>=0.20.3,<0.21.0',
 'async-timeout>=4.0.2',
 'bitsandbytes==0.40.1.post1',
 'cpufeature>=0.2.0',
 'hivemind==1.1.9',
 'huggingface-hub>=0.11.1,<1.0.0',
 'humanfriendly',
 'packaging>=20.9',
 'peft>=0.4.0',
 'pydantic>=1.10,<2.0',
 'safetensors>=0.3.1',
 'sentencepiece>=0.1.99',
 'speedtest-cli==2.1.3',
 'tensor_parallel==1.0.23',
 'tokenizers>=0.13.3',
 'torch>=1.12',
 'transformers>=4.31.0,<5.0.0']

setup_kwargs = {
    'name': 'the-grid',
    'version': '0.1.0',
    'description': 'Easy way to efficiently run 100B+ language models without high-end GPUs',
    'long_description': 'None',
    'author': 'Grid Developers',
    'author_email': 'https://discord.gg/qUtxnK2NMf',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/thegrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
