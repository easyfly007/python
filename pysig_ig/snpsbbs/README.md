### 如何使用
> * 点击页面download zip 下载并解压到你的自己的目录
> * 确保你在自己的电脑上安装了django，没有的话安装一个
> * 进入第一层mysite目录，运行python manager.py runserver
> * 访问 http://localhost:8000， 开始访问论坛


------
相比于我们上一次的展示，目前的版本多了以下功能：
> * 提供不同的板块界面
> * 每个版块有一名版主
> * 版主在他的板块界面会有一个版面管理链接
> * 在这个版面管理链接里面，版主可以
> * 删除帖子
> * 设置对于用户的发帖子权限，禁止用户在该版面下发帖，或者将该被禁止的用户回复发帖功能
> * 版主的设置需要在admin下由管理员设置 http://localhost:8000/admin

如果你在运行的时候碰到了 comments 模块找不到的问题，你可以暂时注释掉comments模块，方法如下：
> * 在第二层mysite目录的setting.py文件内注释掉 comments相关内容
> * 在第二层mysite目录下的urls.py文件内注释掉comments相关内容
> * 在bbspro目录下的views.py文件中注释掉comments相关内容


如有问题，请联系 yfhuang@synopsys.com


