from setuptools import setup, find_packages

setup(
    name = "otgCrypto",
    
    version = "0.0.5",
    
    author = "Tahsin Ahmed",

    description = "OTG cryptography is architectured by Tahsin Ahmed. The expansion of OTG is One Time Gamble.",

    long_description = open("README.txt").read(),
    
    keywords = ["cryptography", "encryption", "decryption", "otg", "otg cryptography", "one time gamble", "one time gamble cryptography"],
    
    url = "",
    
    install_requires = [""],
    
    packages = find_packages(),

    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Natural Language :: English"
    ]
)