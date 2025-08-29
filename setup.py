import setuptools

setuptools.setup(
    name="streamlit-bokeh-events",
    version="0.1.4",
    author="Ashish Shukla and Christoph Naumann and Guilherme Zagatti",
    description="A custom streamlit component to return js event values from bokeh plots to streamlit",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    install_requires=[
        "bokeh>=2.4.3,<3",
        "streamlit >= 1.23.0",
    ],
)
