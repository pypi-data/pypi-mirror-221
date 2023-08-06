from setuptools import setup, find_packages


def get_readme():
    with open("README.md", "r") as file:
        return file.read()


setup(
  name='aioskd',
  version='0.0.5',
  author='Artem Sydorenko',
  author_email='kradworkmail@gmail.com',
  description='Asynchronous Background Task Schedule',
  long_description=get_readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['click==8.1.3'],
  classifiers=[
    'Programming Language :: Python :: 3.11'
  ],
  entry_points='''
        [console_scripts]
        skd=aioskd.cli:skd
  ''',
  keywords='async scheduling background-tasks asynchronous-programming scheduler-library python task-scheduler background-processing concurrency asyncio timed-tasks library python3 interval-tasks task-scheduling asynchronous-background-tasks background-scheduler background-jobs background-execution task-execution scheduling-tasks async-jobs async-tasks job-scheduler task-runner task-manager background-processing-library async-processing async-execution background-work async-worker async-scheduler python-library python-package background-job-queue job-queue python-developers python-projects python-tools python-modules python-development python-programming python-coding python-library-package python-async python-scheduling python-tasks python-asyncio asyncio-library asyncio-tasks asyncio-scheduler concurrent-tasks concurrent-processing concurrent-jobs concurrent-programming concurrent-execution',
  python_requires='>=3.11'
)