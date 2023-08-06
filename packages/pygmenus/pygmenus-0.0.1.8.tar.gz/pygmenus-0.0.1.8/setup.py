from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pygmenus',
    version='0.0.1.8', #Major_update.Minor_update.Patch.Hotfix
    packages=find_packages(),
    description='A simple menu system for Pygame.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='@JoshuaParsonsCreativity',
    author_email='your.email@example.com',
    keywords=['pygame', 'menu'],
    classifiers=[],
)
