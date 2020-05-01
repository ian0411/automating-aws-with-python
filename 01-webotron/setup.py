from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Ian Hsu',
    author_email='ian0411@hotmail.com',
    description='Webotron 80 is a tool to deploy static website to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/ian0411/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
