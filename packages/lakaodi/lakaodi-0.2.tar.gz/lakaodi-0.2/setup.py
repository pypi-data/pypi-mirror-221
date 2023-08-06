from setuptools import setup, find_packages

setup(
    name='lakaodi',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot',
    ],
    entry_points={
        'console_scripts': [
            'lakaodi-post-install = post_install:send_notification'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
