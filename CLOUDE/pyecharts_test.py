#pyecharts 可视化
#https://www.echartsjs.com/zh/index.html 
# http://pyecharts.org/#/zh-cn 学习网站
from pyecharts.faker import Faker #虚构的数据
from pyecharts import options as opts #配置
from pyecharts.charts import Bar #导入bar图
from pyecharts.globals import ThemeType

bar=Bar(
    init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width="1920px",
    height="1080px"),
    ) #主题配色
  
 
 
  
bar.add_xaxis(Faker.choose())
bar.add_yaxis('商家A',Faker.values(),stack='stack1')
bar.add_yaxis('商家B',Faker.values(),stack='stack2')
# bar.add_xaxis(['衬衫','毛衣','领带','裤子','风衣','高跟鞋','袜子']) #x轴标签
# bar.add_yaxis("商家A",[92,134,141,96,54,59,117]) #y轴标签 list数据
#bar.reversal_axis() #x轴与y轴交换  
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),#不显示数字
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max",name="最大值"),
            opts.MarkPointItem(type_="min",name="最小值"),
            
        ]
    ),
    markline_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="average",name="平均值"),    
        ]
    ),
) 
bar.set_global_opts(title_opts=opts.TitleOpts(
    title="Bar-基本示例",
    subtitle="我是副标题"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)), #旋转角度
    datazoom_opts=[opts.DataZoomOpts()],
    )   
    
bar.add_xaxis(Faker.days_attrs)
bar.add_yaxis("商家A",Faker.days_values)
bar.render()