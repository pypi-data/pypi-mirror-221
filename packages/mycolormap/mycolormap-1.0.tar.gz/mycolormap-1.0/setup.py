from distutils.core import setup

setup(
    name="mycolormap",                        # 包名
    version="1.0",                            # 版本号
    description="为降水图片制作色表用",              # 描述信息
    long_description="为降水图片制作色表用",  # 完整的描述信息
    author="Wang Zhao Qiang",                         # 作者
    author_email="349558455@qq.com",          # 作者邮箱
    # url="https://blog.csdn.net/KaiSarH",      # 主页
    py_modules=[							  # 希望分享模块列表
        "Mycolormap"
    ]
)
