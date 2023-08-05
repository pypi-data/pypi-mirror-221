from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="cow_api",
    version="0.1.1",
    url="https://github.com/falkolav/cow_api",
    author="Falko L",
    author_email="falkolavitt@gmail.com",
    description="Cow API using FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "faker",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10",
    ],
)
