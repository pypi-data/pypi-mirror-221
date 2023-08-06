# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oceandb',
 'oceandb.api',
 'oceandb.api.models',
 'oceandb.db',
 'oceandb.db.index',
 'oceandb.server',
 'oceandb.server.fastapi',
 'oceandb.telemetry',
 'oceandb.test',
 'oceandb.test.property',
 'oceandb.utils',
 'oceandb.utils.ImageBind',
 'oceandb.utils.ImageBind.models']

package_data = \
{'': ['*'], 'oceandb.utils.ImageBind': ['.assets/*']}

install_requires = \
['clickhouse_connect>=0.5.7,<0.6.0',
 'duckdb>=0.7.1,<0.8.0',
 'fastapi>=0.85.1,<0.86.0',
 'hnswlib>=0.7,<0.8',
 'numpy>=1.21.6,<2.0.0',
 'pandas>=1.3,<2.0',
 'posthog>=2.4.0,<3.0.0',
 'pydantic>=1.9,<2.0',
 'requests>=2.28,<3.0',
 'sentence-transformers>=2.2.2,<3.0.0',
 'typing_extensions>=4.5.0,<5.0.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'oceandb',
    'version': '0.1.0',
    'description': 'Ocean.',
    'long_description': '\n# Ocean 🌊🐠\n\nOcean is a powerful, flexible, and easy-to-use library for cross-modal and modality-specific searching. It provides a unified interface for embedding and querying text, images, and audio. Ocean leverages the latest advancements in deep learning and the power of the ImageBind Embedding model to deliver unparalleled search accuracy and performance.\n\n<p align="center">\n  <a href="https://discord.gg/qUtxnK2NMf" target="_blank">\n      <img src="https://img.shields.io/discord/1073293645303795742" alt="Discord">\n  </a> |\n  <a href="https://github.com/ocean-core/ocean/blob/master/LICENSE" target="_blank">\n      <img src="https://img.shields.io/static/v1?label=license&message=Apache 2.0&color=white" alt="License">\n  </a> |\n  <a href="https://docs.tryocean.com/" target="_blank">\n      Docs\n  </a> |\n  <a href="https://www.tryocean.com/" target="_blank">\n      Homepage\n  </a>\n</p>\n\n<p align="center">\n  <a href="https://github.com/ocean-core/ocean/actions/workflows/ocean-integration-test.yml" target="_blank">\n    <img src="https://github.com/ocean-core/ocean/actions/workflows/ocean-integration-test.yml/badge.svg?branch=main" alt="Integration Tests">\n  </a> |\n  <a href="https://github.com/ocean-core/ocean/actions/workflows/ocean-test.yml" target="_blank">\n    <img src="https://github.com/ocean-core/ocean/actions/workflows/ocean-test.yml/badge.svg?branch=main" alt="Tests">\n  </a>\n</p>\n\n```bash\npip install https://github.com/kyegomez/Ocean.git # python client\n# for javascript, npm install oceandb!\n# for client-server mode, docker-compose up -d --build\n```\n\nThe core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing) or [Replit template](https://replit.com/@swyx/BasicOceanStarter?v=1)):\n\n```python\nimport oceandb\napi = oceandb.Client()\nprint(api.heartbeat())\n\nfrom oceandb.utils.embedding_functions import MultiModalEmbeddingFunction\n\n\n# setup Ocean in-memory, for easy prototyping. Can add persistence easily!\nclient = oceandb.Client()\n\n#text\ntext_embedding_function = MultiModalEmbeddingFunction(modality="text")\n\n\n#vision\n#vision_embedding_function = MultiModalEmbeddingFunction(modality="vision")\n\n#audio\n#audio_embedding_function = MultiModalEmbeddingFunction(modality="audio")\n\n# # Create collection. get_collection, get_or_create_collection, delete_collection also available and add embedding function\ncollection = client.create_collection("all-my-documents", embedding_function=text_embedding_function)\n\n\n\ntext_data = [\'This is a query about artificial intelligence\']\n\n#test\ntest = collection.add(\n    documents=text_data,\n    ids=[\'doc1\']\n)\n\nprint(test)\n\n#query result\nresults = collection.query(\n    query_texts=[query_text],\n    n_results=1\n)\n\nprint(f"Query texts {query_text}")\nprint("Most similar document:", results[\'documents\'][0][0])\n\n\n```\n\n## Features\n\n- **Simple**: Fully-typed, fully-tested, fully-documented == happiness\n- **Integrations**: [`🦜️🔗 LangChain`](https://blog.langchain.dev/langchain-ocean/) (python and js), [`🦙 LlamaIndex`](https://twitter.com/atroyn/status/1628557389762007040) and more soon\n- **Dev, Test, Prod**: the same API that runs in your python notebook, scales to your cluster\n- **Feature-rich**: Queries, filtering, density estimation and more\n- **Free & Open Source**: Apache 2.0 Licensed\n\n## Use case: ChatGPT for **\\_\\_**\n\nFor example, the `"Chat your data"` use case:\n\n1. Add documents to your database. You can pass in your own embeddings, embedding function, or let Ocean embed them for you.\n2. Query relevant documents with natural language.\n3. Compose documents into the context window of an LLM like `GPT3` for additional summarization or analysis.\n\n## Embeddings?\n\nWhat are embeddings?\n\n- [Read the guide from OpenAI](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)\n- **Literal**: Embedding something turns it from image/text/audio into a list of numbers. 🖼️ or 📄 => `[1.2, 2.1, ....]`. This process makes documents "understandable" to a machine learning model.\n- **By analogy**: An embedding represents the essence of a document. This enables documents and queries with the same essence to be "near" each other and therefore easy to find.\n- **Technical**: An embedding is the latent-space position of a document at a layer of a deep neural network. For models trained specifically to embed data, this is the last layer.\n- **A small example**: If you search your photos for "famous bridge in San Francisco". By embedding this query and comparing it to the embeddings of your photos and their metadata - it should return photos of the Golden Gate Bridge.\n\nEmbeddings databases (also known as **vector databases**) store embeddings and allow you to search by nearest neighbors rather than by substrings like a traditional database. By default, Ocean uses [ImageBind](https://github.com/facebookresearch/ImageBind) to embed for you but you can also use OpenAI embeddings, Cohere (multilingual) embeddings, or your own.\n\n## Roadmap 🗺️\n\n- [ ] Integrate the new 3 loss functions (conditional, cross-modal, and unimodality)\n- [ ] Integrate ImageBind model to embed images, text, and audio as a native embedder\n- [ ] Implement a method to choose query algorithm: `query([vectors], search_algorithm="knn")`\n- [ ] Implement shapeless and polymorphic support\n- [ ] Explore the integration of database worker agents that manage the embedding, tokenization, and indexation (like a swarm)\n- [ ] Implement an endless context length embedding model\n- [ ] Enable running the ImageBind embedding model offline in a database repository\n- [ ] Allow users to choose modality in the upsert method\n- [ ] Deploy ImageBind as an API and increase context length\n\n## Get involved at Agora\n\nOcean is a rapidly developing project. We welcome PR contributors and ideas for how to improve the project.\n\n- [Join the conversation on Discord](https://discord.gg/sbYvXgqc)\n- [Review the roadmap and contribute your ideas](https://docs.tryocean.com/roadmap)\n- [Grab an issue and open a PR](https://github.com/ocean-core/ocean/issues)\n\n## License\n\n[Apache 2.0](./LICENSE)\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
