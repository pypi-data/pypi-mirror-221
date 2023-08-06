from setuptools import setup, find_packages

setup(
    name='dbxslackmessage',
    version='0.1.1',
    description='A simple package to send custom messages to Slack via databricks notebooks.',
    author='Vaishali Khairnar',
    author_email='vkhairnar@ripple.com',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
