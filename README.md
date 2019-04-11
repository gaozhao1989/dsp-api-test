# [api-testing](https://github.com/gaozhao1989/api-testing) api自动化测试工具

------
使用[Python](https://www.python.org)组合工具[Reuqests](https://github.com/requests/requests)实现对api自动化测试。使用 Requests 作为底层框架，[Pytest](https://docs.pytest.org/en/latest/) 作为测试管理工具，[Allure](http://allure.qatools.ru) 作为报告输出工具。
目录结构如下：

>  api-testing<br>
>   |-parameters<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-api_compare.py<br>
>   |<br>
>   |-report<br>
>   |<br>
>   |-tests<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-test_api_compare_date.py<br>
>   |<br>
>   -conftest.py<br>
>   -README.md<br>
>   -requirements.txt<br>
>   -runner.py<br>
>   -utils.py<br>

## [api-testing](https://github.com/gaozhao1989/api-testing) 结构文件说明
### parameters
存放参数化数据文件
### report
存放测试结果以及测试报告，其中测试结果由**Pytest**执行用例后生成，测试报告由**Allure**在执行完成后配置Pytest的结果生成，可通过网页进行查看<br>
测试结果文件：****.json<br>
测试报告入口：/html/index.html
### tests
存放测试文件，测试文件需要以**test_xxxx**开头
* test_api_compare_date.py
在测试类中，测试函数同样需要以**test_xxxx**开头。测试文件包含测试用例，可单独进行测试的运行与调试
###### conftest.py
**Pytest**的全局挂钩，实现测试setUp与tearDown
###### README.md
介绍文件
###### requirements.txt
当前工程所需依赖及版本
###### runner.py
批量执行测试入口文件（测试完成后将会自动生成网页版测试报告「该测试报告由[Allure](http://allure.qatools.ru)提供支持」）
###### utils.py
通用工具文件, 提供生成日志与获取文件路径

------

## 所需依赖、插件及安装方式
#### 依赖
pytest==4.1.0<br>
allure-pytest==2.5.4<br>
requests==2.21.0<br>
#### 依赖安装
pip install -r requirements.txt
#### 插件
allure==2.8.1
#### 插件安装
brew install allure

------

## 调试&运行
### 调试
通过**tests**目录下的单独**test_xxxx**运行测试，适用范围仅限于当前测试文件
### 运行
通过**runner.py**文件指定运行，运行指定测试目录默认为**tests**目录

------

## 查看测试结果
<span style="color:red">注意：直接打开*index.html*在某些浏览器中将显示结果为*404 not found*</span><br>
使用命令行工具：allure serve [path_of_report]<br>
可以直接启动allure服务并查看测试结果