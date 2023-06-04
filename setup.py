import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description=f.read()

__version__ = '0.0.0'

REPO_NAME = 'Chicken-Disease-Classification'
AUTHOR_USER_NAME = 'Shaktijain9'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'shaktijain9@gmail.com'
long_description = 'The Chicken Disease Classification model is an AI-based system that uses machine learning algorithms to identify and classify diseases affecting chickens. It analyzes images of chickens and provides predictions about the presence of specific diseases based on visual symptoms. The model aims to assist poultry farmers and veterinarians in quickly and accurately diagnosing diseases, enabling timely treatment and effective disease management strategies.'
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Small CNN Classifier",
    long_description=long_description,
    long_description_content="text/markdown" ,
    url='https://github.com/{AUTHOR_USER_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)