from setuptools import setup, find_packages

setup(
    name='google-drive-manager',
    version='1.0.4',
    author="Guillaume LECOSSOIS",
    author_email="<guillaume.lecossois@diabeloop.fr>",
    description='Un gestionnaire de Google Drive',
    long_description_content_type="text/markdown",
    long_description="""`google-drive-manager` est une librairie conçue pour interagir avec Google Drive en Python. Avec son API simple, vous pouvez gérer les données de différents fichiers et dossiers dans le Google Drive de Diabeloop. 

La liste des méthodes:

- `get_service`
- `connect`
- `getSpreadSheetInfoByID`
- `listSheets`
- `getSheetByName`
- `getAllValuesFromSheet`
- `getPosDataInCol`
- `getRowDataFromSheet`
- `getRangeDataFromSheet`
- `getColDataFromSheet`
- `getRangeValueFromSheet`
- `setColData`
- `setRangeData`
- `getFileByID`""",
    packages=find_packages(),
    install_requires=[
        "google-api-python-client==2.64.0",
        "google-auth-oauthlib==0.5.0"
    ],
    keywords=['python', 'google', 'drive'],
    python_requires='>=3.8'
)