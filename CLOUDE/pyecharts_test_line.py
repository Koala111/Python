from pyecharts.charts import Line
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType
import random

line=Line()
line.add_xaxis(Faker.choose())
line.add_yaxis('商家A',Faker.values(),is_smooth=True)
line.add_yaxis('商家B',Faker.values())

line.set_global_opts(title_opts=opts.TitleOpts(
    title="Bar-基本示例",
    subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)), #旋转角度
    )
    
    
line.render()