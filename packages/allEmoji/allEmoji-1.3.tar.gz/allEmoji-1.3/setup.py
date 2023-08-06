# Copyright (c) 2023 Nusab19 

import os
from setuptools import setup, find_packages

# Version
from emoji import __version__ as v


# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))




if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readme:
        big_description = readme.read()

else:
    big_description = "allEmoji - A Emoji Class for Python"





setup(name="allEmoji",
      version=v,
      description="Use Emojies as class attributes in Pthon",
      url="https://github.com/Nusab19/allEmoji",
      author="Nusab Taha",
      author_email="nusabtaha33@gmail.com",
      license="MIT",
      packages=find_packages(),
      download_url=f"https://github.com/Nusab19/allEmoji/releases/tag/allEmoji-{v}",
      keywords=["Emoji", "allEmoji", "pyEmoji"],
      long_description=big_description,
      long_description_content_type="text/markdown",
      
      package_data={"allEmoji": ["data/*.json"]},
      include_package_data=True,
      
      install_requires=[],
      python_requires = ">=3.6",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Education',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
)
