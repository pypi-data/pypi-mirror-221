from setuptools import setup, find_packages

setup(
    name='google-drive-manager',
    version='1.0.2',
    author="Guillaume LECOSSOIS",
    author_email="<guillaume.lecossois@diabeloop.fr>",
    description='Un gestionnaire de Google Drive',
    packages=find_packages(),
    install_requires=[
        "google-api-python-client==2.64.0",
        "google-auth-oauthlib==0.5.0"
    ],
    keywords=['python', 'google', 'drive'],
    python_requires='>=3.8'
)