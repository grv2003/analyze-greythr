from setuptools import setup, find_packages

setup(
    name="analyze-greythr",
    version="0.4.2",
    description="Meltano project file bundle of Matatika datasets for tap-greythr",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-greythr/*.yml",
            "orchestrate/tap-greythr/elt.sh"
        ]
    },
)
