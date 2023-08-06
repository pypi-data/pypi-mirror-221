from distutils.core import setup
'''
使用twine工具将您的模块上传到PyPI的步骤如下： 
 1. 确保您已经注册了PyPI帐户。如果还没有，请访问https://pypi.org/并按照指示进行注册。 
 2. 在命令行中，安装twine工具。运行以下命令：
pip install twine
3. 在您的模块文件夹中，运行以下命令来构建您的模块：
python setup.py sdist bdist_wheel
这将生成一个dist文件夹，其中包含您的模块的构建文件。 
 4. 接下来，使用以下命令将构建文件上传到PyPI：
twine upload dist/*
twine工具将会提示您输入PyPI的用户名和密码。输入正确的凭据后，twine会将您的模块上传到PyPI。 
 5. 上传完成后，您的模块将在PyPI上可用。其他用户可以使用pip命令来安装您的模块：
pip install your_module_name
将"your_module_name"替换为您的模块在PyPI上的名称。 
 这些是使用twine工具将您的模块上传到PyPI的详细步骤。希望对您有所帮助！如果您有任何其他问题，请随时提问。
'''

setup(
    name="my_weather_forecast",                        # 包名
    version="1.0",                            # 版本号
    description="制作农作物主产区天气图片",              # 描述信息
    long_description="制作农作物主产区天气图片",  # 完整的描述信息
    author="Wang Zhao Qiang",                         # 作者
    author_email="349558455@qq.com",          # 作者邮箱
    # url="https://blog.csdn.net/KaiSarH",      # 主页
    py_modules=[							  # 希望分享模块列表
        "my_weather_forcast.get_countrys",
        "my_weather_forcast.Precipitation_Forecast"
    ]
)
