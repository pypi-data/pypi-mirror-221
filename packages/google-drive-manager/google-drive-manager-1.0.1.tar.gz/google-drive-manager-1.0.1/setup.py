from setuptools import setup, find_packages

setup(
    name='google-drive-manager',
    version='1.0.1',
    description='Un gestionnaire pour Google Drive',
    packages=find_packages(),
    install_requires=[
        "google-api-python-client==2.64.0",
        "google-auth-oauthlib==0.5.0"
    ],
    python_requires='>=3.8'
)