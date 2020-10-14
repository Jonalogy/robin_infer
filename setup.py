from setuptools import setup

setup(
  name="robin_infer",
  version="1.0.0",
  entry_points={
    'console_scripts': [
      'robin=src.robin:infer'
    ]
  },
  python_requires='~=3.7'
)