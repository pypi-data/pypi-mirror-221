from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        # Install nltk punkt
        import nltk
        nltk.download('punkt')
        install.run(self)


with open('README.md', "r") as f:
    long_description = f.read()

print(find_packages(
    exclude=["examples", "tests"],
))


setup(
    name='interactivenlp',
    version='0.2.4',
    description='Interactive NLP',
    long_description=long_description,
    author="Chunxu Yang",
    author_email="chunxuyang@ucla.edu",
    # include_package_data=True,
    packages=["interactivenlp"],
    package_dir={
        "interactivenlp": "interactivenlp"
    },
    package_data={
        "interactivenlp": ["interactivenlp/templates/*"
                           "interactivenlp/static/*"
                           ]
    },
    install_requires=[
        'flask',
        'flask-cors',
        'newspaper3k',
        'nltk',
        'feedparser',
        'pydantic',
    ],
    license='MIT',
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
