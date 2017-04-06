#### 主要测试蓝图在使用过程中：关于蓝图名的一些问题
##### 问题描述：
当我在html里通过url_for('xxx.function')，这个xxx不知道是谁！比如有个代码片段如下：

``` python
bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/')
def user():
    return render_template('user.html')
```
如上代码段，xxx不确定是bp还是user，于是我们涉及一个demoz-project：buleprint-url_for来验证一下
#### 验证过程：
验证过程很简单，就是在index.html中分别通过url_for('bp.user')和url_for('user.user')
来验证是否能跳转到user.html

#### 详细描述见[http://www.cnblogs.com/codeblock/p/flask-blueprint-urlfor.html](http://www.cnblogs.com/codeblock/p/flask-blueprint-urlfor.html)