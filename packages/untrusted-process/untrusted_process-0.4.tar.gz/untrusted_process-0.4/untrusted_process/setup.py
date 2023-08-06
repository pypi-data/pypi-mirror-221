from setuptools import setup

setup(
    name='untrusted_process',
    version='0.4',
    packages=['untrusted_process'],
    install_requires=[
        'pandas',
        'matplotlib',

    ],
    python_requires='>=3.6',
    author='Ahsan Ali',
    author_email='misterj503@gmail.com',
    description='A package to analyze and visualize untrusted processes using osquery.',
    long_description='"Please refer to the README.md file for detailed information."',
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/untrusted_process',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
