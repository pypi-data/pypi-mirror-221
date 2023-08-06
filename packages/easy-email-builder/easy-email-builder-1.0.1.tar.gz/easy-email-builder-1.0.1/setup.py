from setuptools import setup, find_packages

with open("./requirements.txt") as f:
    requirements = f.read().split("\n")

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='easy-email-builder',
    version='1.0.1',
    description='Simple interface for sending emails with the builder design pattern with different services.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ryan Schreiber',
    author_email='ryanschreiber86@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    keywords="email emails builder smtp gmail ses aws",
    project_urls={
    'Documentation': 'https://github.com/ryan-schreiber/email-builder/',
    'Source': 'https://github.com/ryan-schreiber/email-builder/',
    'Tracker': 'https://github.com/ryan-schreiber/email-builder/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0')
