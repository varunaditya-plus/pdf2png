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
    install_requires=[
        "pdf2image",  # Ensures pdf2image is installed as a dependency
    ],
    entry_points={
        "console_scripts": [
            "pdf2png=app:main",  # Entry point for the script
        ]
    },
    python_requires=">=3.12",
)