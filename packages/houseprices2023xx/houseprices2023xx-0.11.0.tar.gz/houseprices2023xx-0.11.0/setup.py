from setuptools import setup, find_packages

setup(
    name='houseprices2023xx',
    version='0.11.0',
    author=['Abdul Rahman Fahad Deshmukh', 'Ben Dötsch', 'Mohamed Amr Mansouri', 'Uzair Majid'],
    author_email='deshmukh@uni-potsdam.de',
    description='Using Machine Learning to predict the SalePrice of properties',
    long_description="The aim of this project is to explore the train dataset by performing preprocessing operations, including data mining techniques like removing irrelevant data and updating missing values. Subsequently, we will apply various machine learning algorithms to the preprocessed dataset. The ultimate goal is to determine the best model for predicting property prices based on their features, including factors like location.",
    long_description_content_type='text/plain',
    url='https://gitup.uni-potsdam.de/mansouri1/house-prices',
    packages=find_packages(),
    install_requires=[
        'numpy',          
        'pandas',         
        'scikit-learn',
        'lightgbm',
        'seaborn',
        'matplotlib',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='house-prices machine-learning prediction',
)
