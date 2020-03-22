from pyecharts.charts import Pie
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType
import random

pie=Pie()
pie.add(
    "",
    [list(z) for z in zip(Faker.choose(),Faker.values())],
    radius=["40%","75%"],
    )
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

pie.set_global_opts(title_opts=opts.TitleOpts(
    title="Bar-基本示例",
    subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)), #旋转角度
    )
    
    
pie.render()