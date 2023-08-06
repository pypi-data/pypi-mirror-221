from setuptools import setup, find_packages

LICENSE = '''MIT License

Copyright (c) 2023 MYR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

md = '''# ShanHeUniversity

## **使用方法**

### **使用流程总览**

1.申请密钥(apply)

2.新建记录(CreateNewAPI)

3.循环聊天(ChatAPI)

---

### **申请密钥**

#### **准备工作**
1.Python3.*

2.`pip install shanheuniversity`

#### **示例代码**

```python
from ShanHeuniversity import api

api.apply(email='demo@shu.edu')

```

#### **参数总览**

| 参数名 | 参数类型 | 是否必填 | 默认值 | 示例 |
| --- | --- | --- | --- | --- |
| email | String | 是 | 无 | sb@xxx.com |

---

### **新建记录**

#### **准备工作**
1.Python3.*

2.`pip install shanheuniversity`

#### **示例代码**

```python
from ShanHeuniversity import api
import sys
import os

function = lambda data: sys.stdout.write(str(data))

api._api_key = os.getenv('MOBAI_API_KEY')
function(
    api.CreateNewAPI(model='MobAI')
)

```

#### **参数总览**

| 参数名 | 参数类型 | 是否必填 | 默认值 | 示例 |
| --- | --- | --- | --- | --- |
| api_key | String | 是 | 无 | sk-demo |
| model | String | 是 | 无 | 天马行空 |

---

### **循环聊天**

#### **准备工作**
1.Python3.*

2.`pip install shanheuniversity`

#### **示例代码**

```python
import sys
import os
from ShanHeuniversity import api

function = lambda data: sys.stdout.write(
    'MobAI:' + data.data.reply + '\n\n'
    if data.state == 'success'
    else 'ERROR:' + data.data.error + '\n\n'
)
ask = input

api._api_key = os.getenv('MOBAI_API_KEY')
while True:
    function(
        api.ChatAPI(
            _id='id',
            password='password',
            question=ask('User:')
        )
    )

```

#### **参数总览**

| 参数名 | 参数类型 | 是否必填 | 默认值 | 示例 |
| --- | --- | --- | --- | --- |
| api_key | String | 是 | 无 | sk-demo |
| _id | String | 是 | 无 | 0000-0000-0000-0000 |
| password | String | 是 | 无 | password-1234 |
| question | String | 是 | 无 | Hello! |


### 可参考示例

> 以下代码可直接运行，但不建议，因为这只是一个最基本的示例。

```python
import sys
from ShanHeuniversity import api

ask = input
function = lambda data: sys.stdout.write(
    'MobAI:' + str(data.get('data').get('reply')) + '\n\n'
    if data.get('state') == 'success'
    else 'ERROR:' + data.get('data').get('error') + '\n\n'
)

api.apply(email=ask('Mail:'))

api._api_key = ask('Key:')

ai = api.CreateNewAPI(model=ask('Model:'))

while True:
    function(
        api.ChatAPI(
            _id=ai.data.id,
            password=ai.data.password,
            question=ask('User:')
        )
    )

```
'''

setup(
    name='ShanHeuniversity',
    version='0.1.0',
    packages=find_packages(),
    url='https://shu.university/',
    license=LICENSE,
    author='MoYeRanQianZhi',
    author_email='moyeranqianzhi@gmail.com',
    description='This is a module for MobAI.API.',
    long_description=md,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6.0',
    requires=[
        'requests'
    ]
)
