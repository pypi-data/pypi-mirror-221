# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_botmailnotice']

package_data = \
{'': ['*']}

install_requires = \
['aiosmtplib>=2.0.0,<3.0.0', 'nonebot2>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-botmailnotice',
    'version': '0.0.1',
    'description': '基于nonebot2bot断连时的Mail通知插件',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-BotMailNotice\n\n_✨ bot断连时的Mail通知插件 ✨_\n\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/ZM25XC/BotMailNotice.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-BotMailNotice">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-BotMailNotice.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n\n</div>\n\n\n## 介绍\n\n- 可以在bot断开与nonebot2的连接时向指定邮箱发送邮件通知，用来通知是否掉线\n  \n\n##  安装及更新\n\n<details>\n<summary>第一种方式(不推荐)</summary>\n\n- 使用`git clone https://github.com/ZM25XC/BotMailNotice.git`指令克隆本仓库或下载压缩包文件\n\n</details>\n\n<details>\n<summary>第二种方式(二选一)</summary>\n\n- 使用`pip install nonebot-plugin-BotMailNotice`来进行安装,使用`pip install nonebot-plugin-BotMailNotice -U`进行更新\n- 使用`nb plugin install nonebot-plugin-BotMailNotice`来进行安装,使用`nb plugin install nonebot-plugin-BotMailNotice -U`进行更新\n\n</details>\n\n\n## 导入插件\n\n<details>\n<summary>使用第一种方式安装看此方法</summary>\n\n- 将`nonebot_plugin_BotMailNotice`放在nb的`plugins`目录下，运行nb机器人即可\n\n- 文件结构如下\n\n    ```py\n    📦 AweSome-Bot\n    ├── 📂 awesome_bot\n    │   └── 📂 plugins\n    |       └── 📂 nonebot_plugin_BotMailNotice\n    |           └── 📜 __init__.py\n    ├── 📜 .env.prod\n    ├── 📜 .gitignore\n    ├── 📜 pyproject.toml\n    └── 📜 README.md\n    ```\n\n    \n\n</details>\n\n<details>\n<summary>使用第二种方式安装看此方法</summary>\n\n- 在`pyproject.toml`里的`[tool.nonebot]`中添加`plugins = ["TeenStudy"]`\n\n</details>\n\n\n\n##  配置\n运行插件前，需要在 nonebot2 项目的`.env.prod`文件中添加下表中配置项\n\n| 配置项 | 必填 | 值类型 | 默认值 | 说明 |\n|:------:|:----:|:---:|:---:|:--:|\n| username | 是 | str | ""  | 邮箱账号 |\n| password | 是 | str | ""  | 邮箱密码或授权码 |\n| hostname | 是 | str | ""  | 邮箱服务器地址 |\n| port | 是 | int | 465  | 邮箱端口号，ssl模式时为465 |\n\n## 示例配置\n  \n```env\nmail_notice=\'{\n"username":"xxx@qq.com",\n"password":"qflgxxxxxx",\n"hostname":"smtp.qq.com",\n"port":587\n}\'\n```',
    'author': 'ZM25XC',
    'author_email': 'xingling25@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZM25XC/BotMailNotice',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
