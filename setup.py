import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Mushrooms-Classification-With-MLflow"
AUTHOR_USER_NAME = "aman-srma"
USER_NAME = "AMAN SHARMA"
AUTHOR_EMAIL = "aman.srma.a7@gmail.com"


setuptools.setup(
    name=USER_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Mushroom Binary Classification",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)