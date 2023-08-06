# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['megaladon']

package_data = \
{'': ['*']}

install_requires = \
['datasets', 'deepspeed', 'openai', 'transformers']

setup_kwargs = {
    'name': 'megaladon',
    'version': '0.0.1',
    'description': 'Megalodon - Pytorch',
    'long_description': '# Megalodon\nSail the Seas of Data and Dive into the Depths of Computation!  \n![Megalodon](megaladon.jpeg)\n\n## _Megalodon: The Orca is no match._\n\nWelcome aboard, shipmates! Let Megalodon be your steadfast vessel on the uncharted ocean of Big Data and Machine Learning. With our rich datasets and detailed mathematical models, there\'s no computational storm we can\'t weather together! \n\n> "We didn\'t name it \'Megalodon\' for nothing. It\'s big, it\'s powerful, and it\'s got a heck of a bite when it comes to data crunching!" - Captain Codebeard\n\n## Navigation Chart\n\n```python\nDataset Sample (Row by Row) [Input] --(Feeds into)--> [Model] --(Outputs)--> Dataset Sample (Row by Row)\n```\n\n# Deck Logs (Changelog)\n\n- **v2.0.0 - The Leviathan Update** - We\'ve surfaced some serious computational power in this one! Modular integration of HuggingFace and OpenAI models.\n- **v1.5.0 - The Kraken Patch** - Tightened up the tentacles of the code. Fewer bugs will be slipping through!\n- **v1.0.0 - Maiden Voyage** - Initial launch! The Megalodon sets sail!\n\n# Shipwright\'s Guide (Installation)\n\nBatten down the hatches and ready your terminal, it\'s time to summon the Megalodon:\n\n```bash\ngit clone https://github.com/megalodon-ds/megalodon.git\ncd megalodon\npip install -r requirements.txt\n```\n\n# Navigational Tools (Usage)\n\n1. **Start your voyage with a good map.** (Load your dataset)\n\n```python\nfrom megalodon import Megalodon\n\n# Using OpenAI model\nmegalodon = Megalodon(model_id="gpt-3", api_key="your-api-key", dataset="flax-sentence-embeddings/stackexchange_math_jsonl")\n\n# Using Hugging Face model\nmegalodon = Megalodon(model_id="gpt2", dataset="flax-sentence-embeddings/stackexchange_math_jsonl")\n```\n\n2. **Set sail!** (Generate explanations)\n\n```python\nexplanations = megalodon.run()\n```\n\n3. **Return to port.** (Save your results)\n\n```python\nmegalodon.save_to_huggingface(explanations, \'hf_output_dir\')\n```\n\nPlease replace `"your-api-key"` with your actual OpenAI API key, and `\'hf_output_dir\'` with your desired output directory for the Hugging Face datasets.\n\n# Lifeboats (Support)\n\nIf you find yourself overboard in a sea of confusion, don\'t panic! Shoot a flare to our issue tracker on Github, and our dedicated crew will row to your rescue. \n\n[Create New Issue](https://github.com/megalodon-ds/megalodon/issues/new)\n\n# Crow\'s Nest (Future Plans)\n\n1. **New Species Detection** - We\'re constantly exploring unknown waters to find and integrate new algorithms and data models into Megalodon. \n2. **Crew Training** - Comprehensive documentation and examples are on the horizon to help you get the most out of your voyage with Megalodon.\n\nThank you for choosing to sail with Megalodon. May fair winds and calm seas guide your data journey!\n\nHappy Sailing!\n\nThe Megalodon Team\n\n\n\n# Todo:\n\n* Better prompt\n* More seamless model handling, plug and play with any model from OpenAI or HuggingFace.\n* Save to HuggingFace after each iteration is labeled\n* Potentially use Parquet for optimized storage\n* Add in polymorphic or shape shifting preprocessing logic\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Agora-X/Megalodon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
