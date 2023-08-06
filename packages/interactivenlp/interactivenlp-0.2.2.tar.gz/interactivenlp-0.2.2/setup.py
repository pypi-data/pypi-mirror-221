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

setup(
    name='interactivenlp',
    version='0.2.2',
    description='Interactive NLP',
    long_description=long_description,
    author="Chunxu Yang",
    author_email="chunxuyang@ucla.edu",
    install_requires=[
        'flask',
        'flask-cors',
        'newspaper3k',
        'nltk',
        'feedparser',
        'pydantic',
    ],
    license='MIT',
    packages=find_packages(
        exclude=["examples", "tests"]
    ),
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
