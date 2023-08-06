import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def find_data_files():
    data_files = []
    base_dir = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, 'genpwd', 'data')
    for dirpath, dirnames, filenames in os.walk(data_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                relative_path = os.path.relpath(os.path.join(dirpath, filename), base_dir)
                data_files.append(relative_path)
    return data_files

setup(
    name="genPwd",
    version="1.3.0.3",
    author="Kanchan",
    author_email="kanchanbora321@gmail.com",
    description="This is a sample Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kanchann/GenPwd",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # List any dependencies your project requires here
    ],
    package_data={
        'genpwd': find_data_files(),
    },
    entry_points={
        "console_scripts": [
            "generate_password = genpwd.generate_password:main",
            # Add any other entry points if needed
        ],
    },
)


