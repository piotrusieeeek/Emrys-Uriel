from setuptools import setup

setup(
    name='CLI',
    version='0.1.2',
    packages=['search'],
    entry_points={
        'console_scripts': [
            'search = search.__main__:main'
        ]
    }
)
