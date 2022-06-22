..
   Note: Items in this toctree form the top-level navigation. See `api.rst` for the `autosummary` directive, and for why `api.rst` isn't called directly.

.. toctree::
   :hidden:

   主页 <self>
   modules.rst
   GetFunctionSet.rst
   FunctionSuffix.rst
   WithRiskQuantLib.rst
   WithPycharm.rst

欢迎使用windget
===========================

windget是一个三方开发的万得python接口，它使得用户可以以更为方便的方式从万得获取数据。windget也集成于RiskQuantLib中。

使用windget的有效方法是使用windget的pycharm插件。使用pip安装了windget之后，您可以在pycharm的插件市场搜索并安装windget，此插件会为您提供实时的代码补全和中文字段提示。


为什么我应该使用windget?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

万得默认的python数据接口使用w.set, w.wss, w.wsd等函数向用户提供数据服务，但用户必须依赖万得的桌面终端中的代码生成器来寻找字段的名称，这非常不便。比如当用户需要下载某股票过去几年的每日涨跌时，需要先打开万得终端的代码生成器，找到涨跌对应的字段名为 **pct_chg** 而不是 **percentage_change**，然后再使用函数接口。当用户需要频繁获取字段时，这变得非常繁琐。

本库提供了通过名称直接检索函数的功能，使得用户不必使用代码生成器就可以快速找到想要的万得函数。在上面的例子中，只需要使用：
::

   from windget import *  
   getPctChg("000001.SZ","tradeDate=20200519")

本库将万得提供的所有字段都进行了重构，使得每个字段都有对应的函数，用户可以通过字段来获得函数。这样的函数集合被称为get函数族，其中的每个函数都以get开头，紧接字段的英文名称。当用户模糊输入英文名称时，诸如pycharm这样的IDE会自动补全其余的部分，大大加快用户的编码速度。

本库同时提供了可迭代对象的支持，任何的可迭代对象都可以作为证券代码的传入载体。同时，本库默认返回pandas.DataFrame，方便用户进行后续的数据处理。例如上面的例子中，可以使用列表传入多个证券：
::

   getPctChg(["000001.SZ","000004.SZ"],"tradeDate=20200519")

用户也可以通过中文来索引想要的万得函数，如果您是RiskQuantLib的用户，在工程项目的pycharm中同时按住Alt，Shift，以及F，可以打开文本搜索，在其中键入想要的字段的名称，就可以快速看到本库提供的所有相关函数的名称。

**注意：如果你安装了搜狗输入法，那么搜狗输入法会屏蔽Alt，Shift，以及F，搜狗将其定义为了其他功能，你需要先进入搜狗输入法的设置，快捷键，来关闭这一项。**

如果您不是RiskQuantLib的用户，您可以考虑使用pycharm插件仓库中名为windget的插件，此插件提供了自动的代码补全和中文提示，帮您快速索引万得函数。

你也可以访问 `RiskQuantLib文档 <https://riskquantlib-doc.readthedocs.io/zh_CN/latest/>`_ 来获取更多关于RiskQuantLib的信息。

谁应该使用windget?
^^^^^^^^^^^^^^^^^^^^^^^^^

windget被设计用于从万得数据接口中获取数据，如果您是金融从业人员，金融或经济系的学生或教职工，或者有意探索万得的python数据接口，那么您都可以使用windget。

**注意：windget封装了大部分的万得python接口，但依然不是全部。有部分函数可能无法在windget中找到，但这样的函数应该非常少。**

快速开始
^^^^^^^^^^^

使用pip命令安装windget库：
::

   pip install windget

如果您是pycharm的用户，您可以从pycharm的插件仓库中搜索并下载windget同名插件，此插件提供自动的代码补全，可以方便用户在pycharm中进行快速函数索引，而不必打开万得的代码生成器。打开pycharm插件仓库的方式为： **File-Settings-Plugins-Marketplace**

当安装好windget后，在python源代码中导入windget：
::

   from windget import *

然后当您输入任何以get开头的关键字时，pycharm插件会自动联想字段，帮您选择您可能需要的函数。您也可以记住自己的常用函数。
