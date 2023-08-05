from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-plotly-plugin",
    version="0.1.3",
    description="MkDocs plugin to add plotly charts from plotly's json data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs plugin",
    url="https://github.com/haoda-li/mkdocs-plotly-plugin",
    author="Haoda Li",
    author_email="haoda_li@berkeley.edu",
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["mkdocs>=1.1", "pymdown-extensions>=9.2", "beautifulsoup4>=4.11.1", "flatten-dict>=0.4.2"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "mkdocs.plugins": ["plotly = mkdocs_plotly_plugin.plugin:PlotlyChartsPlugin"]
    },
)
