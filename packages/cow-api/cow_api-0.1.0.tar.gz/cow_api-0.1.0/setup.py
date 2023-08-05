from setuptools import setup, find_packages

setup(
    name="cow_api",
    version="0.1.0",
    url="https://github.com/falkolav/cow_api",
    author="Falko Lavitt",
    author_email="falkolavitt@gmail.com",
    description="Cow API using FastAPI",
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
