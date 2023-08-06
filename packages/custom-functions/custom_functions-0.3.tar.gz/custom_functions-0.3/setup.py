from setuptools import setup

setup(
    name="Median_housing_value_Prediction",
    version="0.3",
    description="Median housing value prediction",
    author="TA-Davish",
    author_email="davish.balamurug@tigeranalytics.com",
    packages=["src"],
    install_requires=["numpy", "pandas", "sklearn", "scipy", "six", "argparse"],
)
