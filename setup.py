import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine-Quality-Prediction"
AUTHOR_USER_NAME = "sj020"
SRC_REPO = "wine_quality_prediction"
AUTHOR_EMAIL = "sidhantjainoff@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Wine Quality Prediction",
    long_description=long_description,
    # long_description_context="text/markdown",/
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)