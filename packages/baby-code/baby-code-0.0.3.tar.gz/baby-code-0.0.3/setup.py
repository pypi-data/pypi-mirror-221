from setuptools import setup, find_packages

setup(
    name='baby-code',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'langchain',
        'llama-cpp-python',
        'flask_cors',
    ],
    entry_points={
        'console_scripts': [
            'baby-code = baby_code.engine.run_llm.:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
