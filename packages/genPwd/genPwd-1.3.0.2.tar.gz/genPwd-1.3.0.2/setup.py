import os

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def find_data_files():
    data_files = []
    for dirpath, dirnames, filenames in os.walk('your_package_name/data'):
        for filename in filenames:
            if filename.endswith('.csv'):
                data_files.append(os.path.join(dirpath, filename))
    return data_files

setup(
    name="genPwd",
    version="1.3.0.2",
    author="Kanchan",
    author_email="kanchanbora321@gmail.com",
    description="This is a sample Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/GenPwd",
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
        # If your project requires any additional files, specify them here.
        # For example, if you need to include the CSV files in your package,
        # you can specify them like this:
        #"GenPwd": ["genPwd/*.csv"],
        'genPwd' : find_data_files(),
    },
    entry_points={
        "console_scripts": [
            "generate_password = GenPwd.generate_password:main",
            # Add any other entry points if needed
        ],
    },
)

