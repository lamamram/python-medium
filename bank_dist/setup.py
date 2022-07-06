import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # nom lié au pip install
    name="bank_mlamam_0722",
    version="0.0.1",
    author="matthieu LAMAMRA",
    author_email="author@example.com",
    description="bank account management classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    # informations sur les platforme
    # pour fixer une platforme dans le nom d'archive: 
    # ajouter  l'option --plat-name=... dans la commande
    platforms=["win-amd64", "Linux", "OSX"],
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)