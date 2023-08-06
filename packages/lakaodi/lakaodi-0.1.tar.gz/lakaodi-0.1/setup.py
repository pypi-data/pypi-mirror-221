import setuptools
from setuptools import setup, find_packages
import subprocess

# Ajoutez la commande personnalisée pour exécuter post_install.py après l'installation
class PostInstallCommand(setuptools.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(["python", "post_install.py"])

setup(
    name='lakaodi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Utilisez la commande personnalisée après l'installation
    cmdclass={
        'install': PostInstallCommand,
    }
)
