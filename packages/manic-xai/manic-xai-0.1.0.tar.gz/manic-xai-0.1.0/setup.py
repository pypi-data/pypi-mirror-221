from setuptools import setup, find_packages

setup(
    name='manic-xai',
    version='0.1.0',
    description='Genetic Algorithm for Generating Metacounterfactual Explanations',
    author='Craig Pirie',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.2',
        'scikit-learn>=0.24.2'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
