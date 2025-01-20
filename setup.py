from setuptools import setup, find_packages

setup(
    name="pdf2png",
    version="0.1.0",
    description="A quick script to convert PDFs to PNGs",
    author="Varun Aditya",
    url="https://github.com/varunaditya-plus/pdf2png",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["pdf2png"],
    install_requires=[
        "pdf2image",
    ],
    entry_points={
        "console_scripts": [
            "pdf2png=app:main",
        ]
    },
    python_requires=">=3.12",
)
