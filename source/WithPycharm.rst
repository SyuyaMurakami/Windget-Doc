与Pycharm配合使用
=======================

.. toctree::
   :maxdepth: 4

如果您不是RiskQuantLib的用户，但您使用pycharm，那么您可以考虑使用pycharm插件仓库中名为windget的插件，此插件提供了自动的代码补全和中文提示，帮您快速索引万得函数，而不必打开万得的代码生成器。打开pycharm插件仓库的方式为： **File-Settings-Plugins-Marketplace**

在安装pycharm插件时，您可能需要重新启动您的pycharm数次，确保windget插件已经处于激活状态时，windget插件才会生效。当您键入任何以get开头的词时，pycharm会用中文提示您可以获取的字段，并提示您可以选择补全的函数名称。

如果您的插件中对中文的显示是乱码，您应该考虑将pycharm的默认编码方式更改为utf-8，因为windget插件使用utf-8进行中文编码。