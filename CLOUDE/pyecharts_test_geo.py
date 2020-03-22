from pyecharts.charts import Geo
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType
import random

geo=Geo()
geo.add_schema(maptype="湖北")
geo.add(
    "geo",
    [list(z) for z in zip(Faker.provinces,Faker.values())],
)

geo.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
)

geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="Geo-基本示例"),

)
geo.render()