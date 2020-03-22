from pyecharts.charts import Liquid
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType
import random

liquid=Liquid()
liquid.add("Liquid",[0.7,0.6,0.5])

liquid.set_global_opts(
    title_opts=opts.TitleOpts(title="Geo-基本示例"),

)
liquid.render()