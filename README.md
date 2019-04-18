# [dsp-api-testing](https://git.vm.snqu.com/snqu-network/sndo/automated-testing) api自动化测试工具

------
使用[Python](https://www.python.org)组合工具[Reuqests](https://github.com/requests/requests)实现对api自动化测试。使用 Requests 作为底层框架，[Pytest](https://docs.pytest.org/en/latest/) 作为测试管理工具，[Allure](http://allure.qatools.ru) 作为报告输出工具。
目录结构如下：

>  api-testing<br>
>   |-parameters<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-tsa.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-wx.py<br>
>   |<br>
>   |-report<br>
>   |<br>
>   |-tests<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-test_tsa.py<br>
>   |&nbsp;&nbsp;&nbsp;&nbsp;|-test_wx.py<br>
>   |<br>
>   -conftest.py<br>
>   -Pipfile<br>
>   -Pipfile.lock<br>
>   -README.md<br>
>   -requirements.txt<br>
>   -runner.py<br>
>   -utils.py<br>

## [api-testing](https://git.vm.snqu.com/snqu-network/sndo/automated-testing) 结构文件说明
### parameters
存放参数化数据文件
* test_tsa.py
广点通业务参数化数据文件，通过添加不通的参数化配置信息，以达到扩充测试场景的目的
* test_wx.py
微信业务参数化数据文件，通过添加不通的参数化配置信息，以达到扩充测试场景的目的
### report
存放测试结果以及测试报告，其中测试结果由**Pytest**执行用例后生成，测试报告由**Allure**在执行完成后配置Pytest的结果生成，可通过网页进行查看<br>
测试结果文件：****.json<br>
测试报告入口：/html/index.html
### tests
存放测试文件，测试文件需要以**test_xxxx**开头
* test_tsa.py
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
pymongo==3.7.2<br>
#### 依赖安装
pip install -r requirements.txt
#### 插件
allure==2.8.1
#### 插件安装
brew install allure （MacOS）
scoop install allure (Windows)

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

## 注意
1.忽略接口：<br>
tsa:
    debug/auth
    adcreative_previews<br>
    promoted_objects<br>
    pages(需正式服，且落地页审核通过)<br>
目前遗漏：（未有mongo数据保存）<br>
wx:
    custom_audiences(有用例，但mongo无数据结构)<br>
    
2.返回值错误：<br>
{'code': 10000, 'message': 'We are unable to process your request at this time. Please retry your request. If you encounter this error repeatedly, please contact our dedicated supporting team.'} 测试服常见，腾讯方面原因，无法解决<br>

## TODO
减少测试用例中断言出现次数