import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gammarer.aws-rds-database-running-scheduler",
    "version": "0.3.12",
    "description": "AWS RDS Database Running Scheduler",
    "license": "Apache-2.0",
    "url": "https://github.com/yicr/aws-rds-database-running-scheduler.git",
    "long_description_content_type": "text/markdown",
    "author": "yicr<yicr@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/yicr/aws-rds-database-running-scheduler.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gammarer.aws_rds_database_running_scheduler",
        "gammarer.aws_rds_database_running_scheduler._jsii"
    ],
    "package_data": {
        "gammarer.aws_rds_database_running_scheduler._jsii": [
            "aws-rds-database-running-scheduler@0.3.12.jsii.tgz"
        ],
        "gammarer.aws_rds_database_running_scheduler": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.60.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.85.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
