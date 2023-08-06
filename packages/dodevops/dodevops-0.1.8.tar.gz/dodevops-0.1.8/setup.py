# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dodevops']
install_requires = \
['boto3>=1.26.143,<2.0.0',
 'botocore>=1.29.145,<2.0.0',
 'cryptography>=39.0.1,<40.0.0',
 'inquirer>=3.1.3,<4.0.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pydo>=0.1.4,<0.2.0',
 'python-dotenv>=0.21.1,<0.22.0']

entry_points = \
{'console_scripts': ['dodevops = dodevops:main']}

setup_kwargs = {
    'name': 'dodevops',
    'version': '0.1.8',
    'description': 'Devops tool for deploying and managing resources on DigitalOcean',
    'long_description': '# TLDR\n\nThis is a tool to take github repos for Django projects and put them on DigitalOcean App Spaces with managed database and DO Spaces S3 storage.\n\nYou will need:\n\n1) Poetry installed locally to run this tool\n2) DigitalOcean account https://www.digitalocean.com/?refcode=9ef6f738fd8a\n3) DigitalOcean API token: https://cloud.digitalocean.com/account/api/tokens\n4) DigitalOcean S3 keys: https://cloud.digitalocean.com/account/api/spaces\n5) Authorize DigitalOcean to pull your github repos: https://cloud.digitalocean.com/apps/github/install\n6) A DigitalOcean S3 bucket: https://cloud.digitalocean.com/spaces/new\n7) A DigitalOcean PostgreSQL database cluster: https://cloud.digitalocean.com/databases\n8) A database and user and connection pool configured on the database cluster\n9) Manually add the app as a trusted source on the database\n\nThere are plans to integrate items 6-9 into this tool, we just haven\'t gotten that far yet.\n\nTo run the tool:\n\n```shell\npoetry run start\n```\n\n# What is this\n\nThis is essentially an experiment/prototype that got a little too big and had some potential. So it\'s being turned into a project.\n\nproto.py is the original prototype.\n\nThis project uses inquirer to get user input. As far as I know it only works on linux and mac. \nWhen debugging in pycharm, you may need to set the run/debug settings to use the terminal emulation.\nYou can find a link with more info here: https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003383619-Pycharm-2019-termios-error-25-Inappropriate-ioctl-for-device-?page=1#community_comment_6589796593042 and here https://github.com/magmax/python-readchar/issues/11\n\n# Details\n\n## Generating DO API token\n\nIn order for this app to work it needs a valid DigitalOcean Personal Access Token. \nThe token is not required after this is run, so it is okay to recyle the token when finished. \nThe token can either be stored in a .env file, or it can be pasted into the app at run time. \n\n### To generating a new token\n\nGo here: https://cloud.digitalocean.com/account/api/tokens\n\nPick whatever name you want for the token, it doesn\'t matter. \nPick whatever token expiration you want depending on your personal paranoia level. \nWrite permissions are required. \n\nOnce the token is generated copy it and paste it somewhere safe like a password manager such as 1password. \nThe token won\'t be displayed again, so if you don\'t get it saved somewhere safe you\'ll have to regenerate it.\n\nProtect your token well. \nAnyone with access to your token has the ability to create and destroy things and incur you costs, so be careful with it. \nThis is opensource so that you can read the code if you want and verify how the token is used. \nStoring the token in the .env file is convenient but it is not the most secure, so if you feel paranoid don\'t do that or delete the token after. \n\nIf you want more info about DO tokens, see here: https://docs.digitalocean.com/reference/api/create-personal-access-token/\n\n## Generating DO Spaces Key\n\nA DO Spaces key is required for storing a media upload folder, as app platform doesn\'t have storage. \n\n### To generating an app spaces key \n\nGo here: https://cloud.digitalocean.com/account/api/spaces \n\nYou can use whatever name you want for the key, it doesn\'t matter. \nIt will display two values, a key ID and a longer access key, save both somewhere safe like a password manager. \nIt won\'t display the access key again, so if you don\'t save it you\'ll have to regenerate it. \n\nYou can put the values in an .env file, or enter it at runtime.\n\nProtect the token well.\n\nTo learn more about DO spaces keys, go here: https://docs.digitalocean.com/products/spaces/how-to/manage-access/#access-keys\n\n## Create a DO Spaces S3 bucket\n\nYou must create an S3 bucket on DO\'s web interface:\n\nhttps://cloud.digitalocean.com/spaces/new\n\n## Filling out .env file\n\nA .env file isn\'t required, but if you store values in it then it will save effort. \nBut if you feel storing values in the .env file isn\'t secure enough for your personal paranoia levels you can instead enter things at runtime.\n\nThe format of the env file is:\n\n```\nDIGITALOCEAN_TOKEN=dop_v1_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nAWS_ACCESS_KEY_ID=DOxxxxxxxxxxxxxxxxxxx\nAWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n# AWS_REGION=ams3\n# APP_NAME=example-rest-app\n# COMPONENT_NAME=example-rest\n# APP_PREFIX=example\nGH_REPO=xusernamex/xrepox\n# GH_BRANCH=main\n# DJANGO_ROOT_MODULE=example\n# DJANGO_USER_MODULE=core\n# SECRET_KEY_ENV_KEY=SECRET_KEY\n# SECRET_KEY=change_me\n# ALLOWED_HOSTS_ENV_KEY=ALLOWED_HOSTS\n# DEBUG=1\n# DOMAIN=rest.example.com\n# PARENT_DOMAIN=example.com\n# OIDC="\\"-----BEGIN RSA PRIVATE KEY-----\\\\n_xxx_\\\\n-----END RSA PRIVATE KEY-----\\\\n\\""\n```\n',
    'author': 'Abby Oakwright',
    'author_email': 'abby.oakwright@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Oakwright/dodevops',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
