from pyecharts.charts import Bar3D
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType
import random

data=[(i,j,random.randint(0,12)) for i in range(24) for j in range(24)]

bar3d=Bar3D()
bar3d.add(
    "",
    data,
    xaxis3d_opts=opts.Axis3DOpts(Faker.clock,type_="category"),
    yaxis3d_opts=opts.Axis3DOpts(Faker.week_en,type_="category"),
    zaxis3d_opts=opts.Axis3DOpts(type_="value"),
)

bar3d.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=20),
    title_opts=opts.TitleOpts(title="Bar3D-基本示例"),

)
bar3d.render()