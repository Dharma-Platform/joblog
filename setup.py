from distutils.core import setup

setup(
    name="joblog",
    version="1.1.0",
    description="Standardized logging for batch jobs and others.",
    long_description="""The Joblog library provides a simple logging system.
    It’s ideal for batch jobs but can also be used for longer running systems.
    * Log format compatible with [Google Logging Library](https://github.com/google/glog).
    * Log files are automatically written to a directory tree arranged by date with unique names.
    * Available for several programming languages.
    * Status lines logged automatically at start and exit.""",
    author="James Bursa",
    author_email="james@zamez.org",
    url="https://github.com/jamesbursa/joblog",
    py_modules=["joblog",],
    license="MIT",
)
