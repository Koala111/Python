from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import SymbolType


effectScatter=EffectScatter()
effectScatter.add_xaxis(Faker.choose())
effectScatter.add_yaxis(
    '商家A',
    Faker.values(),
    symbol=SymbolType.ARROW,
    )
    
effectScatter.set_global_opts(title_opts=opts.TitleOpts(
    title="Bar-基本示例",
    subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)), #旋转角度
    )
    
    
effectScatter.render()