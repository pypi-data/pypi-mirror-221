# 本脚本绘制密西西比河地区的降水预报图
# 导入需要的包，缺什么就pip安装什么,主要依赖matplotlib、pygrib、cartopy三个包。
from locale import *
import matplotlib
import pandas as pd
from matplotlib.ticker import FuncFormatter
import xarray as xr  #需要安装spyder xarray eccodes cfgrib及其他所需依赖库
import matplotlib.pyplot as plt
import os
import geopandas as gpd  #需要安装的5个依赖包,然后pip install geopandas：shapely、pyproj、gdal、fiona https://www.lfd.uci.edu/~gohlke/pythonlibs/
import cartopy.crs as ccrs  #需要安装的四个依赖包：Cartopy必须要先安装GEOS、Shapely和 pyshp
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import numpy as np
from pylab import *
import matplotlib.colors as col
import matplotlib.cm as cm
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from apscheduler.schedulers.blocking import BlockingScheduler
# from _00_tools.Mycolormap import gen_perp_color
from Mycolormap import gen_perp_color
from PIL import Image
from urllib.request import urlretrieve
from datetime import datetime,timedelta
import imageio.v2 as imageio
import socket
from queue import Queue
from threading import Thread


class weather_forecast:
    # 初始化
    def __init__(self,paymoney):
        self.paymoney = paymoney
        pd.set_option('display.max_columns', None)
        pd.set_option('max_colwidth', 600)

        # 处理汉字
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        #设置Matplotlib的后端引擎为Qt5 Agg。它告诉Matplotlib在绘图时使用Qt5 Agg后端来处理图形的显示和交互
        matplotlib.use('qt5agg')

        # 设置地图投影
        self.proj = ccrs.PlateCarree()  # 图片的中心经度线，proj = ccrs.PlateCarree(central_longitude=180)


        # 一、1.首先删除历史APCP(累计降水）数据，
        hour_ = datetime.now().hour
        self.date_ = datetime.now().strftime('%Y%m%d')

        if 18 > hour_ >= 12:
            self.hour = 0
        elif 24 > hour_ >= 18:
            self.hour = 6
        elif 6 > hour_ >= 0:
            self.hour = 12
            self.date_ = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        else:
            self.hour = 18
            self.date_ = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        self.APCP_dir = fr'D:\pythonProject311\_04_Crops_Precipitation_forecast\data\apcp\time{self.hour:02d}'
        print(f'APCP_dir:{self.APCP_dir}')
        self.create_delete_dir(self.APCP_dir)  # 没有路径创建，有路径删除路径内文件
        # 2.然后重新下载历史APCP数据
        self.downloadAPCP(self.APCP_dir,self.hour, self.date_)  # 下载最新APCP(累计降水）数据


    # 二、重新下载历史APCP数据
    def downloadAPCP(self,APCP_dir,hour, date_):
        urls_queue = Queue()
        for n in range(6, 385, 6):
            url = fr'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t{hour:02d}z.pgrb2.0p25.f{n:03d}&var_APCP=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.{date_}%2F{hour:02d}%2Fatmos'
            APCP_filename = APCP_dir + fr'\gfs.t{hour:02d}z.pgrb2.0p25.f{n:03d}'
            urls_queue.put([url, APCP_filename])

        # 创建16个线程
        thread_pool = []
        for i in range(16):
            t = Thread(target=self.downloadAPCP_files, args=[urls_queue])
            thread_pool.append(t)
        for t in thread_pool:
            t.start()
        for t in thread_pool:
            t.join()

    def downloadAPCP_files(self,urls_queue):
        urls_num = urls_queue.qsize()
        while not urls_queue.empty():
            url, APCP_filename = urls_queue.get()
            try:
                urlretrieve(url, APCP_filename)
                print(f'{APCP_filename}已下载完毕')
            except socket.timeout:
                count = 1
                while count <= 5:
                    try:
                        urlretrieve(url, APCP_filename)
                        break
                    except socket.timeout:  # 利用socket模块，使得每次重新下载的时间变短，且避免陷入死循环，从而提高运行效率
                        err_info = f'{APCP_filename}文件重下载{count}次' if count == 1 else '{APCP_filename}文件重下载{count}次'
                        print(err_info)
                        count += 1
                if count > 5:
                    print(f"下载文件：{APCP_filename}失败!")

            # 进度条
            urls_num_lest = urls_queue.qsize()
            jindu = round((urls_num - urls_num_lest) / urls_num * 100)
            print(f'下载总完成进度:{jindu}%', jindu * '█',(100-jindu)*'\uF0A7', end='\r')  # , end='\r'

    # 判断路径是否存在，如果不存在创建，如果存在清空路径里面的文件
    def create_delete_dir(self,dir):
        # 判断路径是否存在
        IsExists = os.path.exists(dir)
        # 判断结果
        if not IsExists:
            # 如果不存在则创建目录
            os.makedirs(dir)
            print(dir + ' 创建成功')
        else:
            # 如果目录存在则不创建，并删除目录内文件
            print(f'删除文件夹:{dir}内的文件')
            self.del_files(dir)

    # 删除路径内的文件
    def del_files(self,path):
        '''
        删除下载的所有apcp文件，以防后期新下载的文件不能覆盖原文件；或者不能更新
        :return:
        '''

        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(fr"{root}\{file}")
                print(fr'{root}\{file}删除成功')
            if not files:
                print(f'空文件夹')



    def crop_draw(self,country):
        # 添加省地图
        self.satategeos =[]
        for map in country.get("satategeo"):
            satategeo = gpd.read_file(map).geometry
            self.satategeos.append(satategeo)


        # 获得天气数据
        os.chdir(self.APCP_dir)
        filenames = os.listdir()
        print(f'天气文件如下:{filenames}')

        for crop in country.get('crops'):
            # 二、删除历史天气图片
            image_dir = fr'D:\pythonProject311\_04_Crops_Precipitation_forecast\images\{country.get("country")}_Crops_Precipitation_forecast\{self.paymoney}\{crop}'  # 图片储存的目录地址
            days_image_dir = image_dir + r'\days'
            weeks_image_dir = image_dir + r'\weeks'

            self.create_delete_dir(days_image_dir)  # 判断路径是否存在，如果不存在创建，如果存在清空路径里面的文件
            self.create_delete_dir(weeks_image_dir)

            # 三、制作周度和日度图片
            # 三、1添加县市地图和作物数据
            # merge = self.countymap_cropvalues(country, crop)
            self.drawWeeksAndDays(filenames, self.APCP_dir, country, image_dir, crop)

            # 四、绘制周度和日度动图
            # createGif(country,crop,imagespath=weeks_image_dir, weeksOrDays='周度')
            self.createGif(country, crop, imagespath=days_image_dir, weeksOrDays='日度')

    # 三、制作周度/日度图片
    def drawWeeksAndDays(self, filenames, accpdir, country, image_dir, crop):
        try:
            # 1、绘制周度图片
            # for week in range(1,3):
            #     drawPre(filenames,accpdir=accpdir, country=country, weeksOrDays='weeks', weekOrDay=week, hours=168,image_dir=image_dir,crop=crop,paymoney=paymoney)
            #     print(f'未来第{week}周预报制作完毕')
            # 2、绘制日度图片
            for day in range(1, 17):
                self.drawPre(filenames, accpdir=accpdir, country=country, weeksOrDays='days', weekOrDay=day,
                             hours=24, image_dir=image_dir, crop=crop)
                print(f'未来第{day}日预报制作完毕')
        except Exception as e:
            print(e)

    def major_formatter(self,x, pos):
        if not str(x).endswith('.5'):
            x = str(int(x))
        else:
            x = x
        return f'{x}'

    # 读取天气数据，写入图片中
    def drawPre(self,filenames,accpdir, country, weeksOrDays, weekOrDay, hours, image_dir, crop):

        # fig = plt.gcf()
        # fig.set_size_inches(8, 12)

        # plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0) #tight_layout 也提供 pad, w_pad, h_pad 关键词参数设置 figure 边界和 子图间的间距。
        # plt.tight_layout()
        fig = plt.figure(figsize=country.get('figsize'), dpi=country.get('dpi'))  # 设置图片大小和分辨率
        ax = fig.subplots(1, 1, subplot_kw={'projection': self.proj})  # 设置图片所在坐标域大小和分辨率
        # plt.tight_layout()

        # 2、将天气数据绘入图中
        self.draw_wheather(crop,fig,ax,country,  weeksOrDays, weekOrDay, hours,filenames,accpdir)

        # 3、绘制地图基本结构
        self.draw_base_map(ax)



        # 4、2 将县地图和作物数据绘入图中
        self.draw_countymap_cropvalues( ax, country.get('county_crops').get(crop))
        # if country.get('country').upper() == 'ARG':
        #     self.add_ARG_mapAndcropValues(ax, country, crop)
        # if country.get('country').upper() == 'USA':
        #     add_USA_mapAndcropValues(ax, country, crop)
        # 添加图例
        plt.rcParams['legend.title_fontsize'] = 15 #12
        ax.legend(title="图例", loc='lower left', fontsize=15, ncol=1, shadow=True,
                  labels=['"+":网格线密度越高产量越高'])
        # fig.legend(title="图例", loc='lower left', fontsize=12,labels=['"+":Crop-growing Region'])
        # fig.legend(title=r"13611941980",loc=(0.1, 0.1), fontsize=12, ncol=1, shadow=True, )  # title=r"公众号：米手评谈",

        # 5、添加加微信好友和付款码图片
        print(f'添加加微信好友和付款码图片')
        self.add_paymoneyAndFriend_picture(plt, self.paymoney)

        # 6、保存图片
        print(f'开始保存图片')
        self.save_images(plt, weeksOrDays, weekOrDay, country, image_dir, crop)

    # 将天气数据绘入图中
    def draw_wheather(self,crop,fig,ax,country,  weeksOrDays, weekOrDay, hours,filenames,accpdir):
        # 1/读取未来降水数据
        # 读取文件，grib格式，全球的降水预报D:\pythonProject2\pythonProject\data\gfs.t00z.pgrb2.0p25.f168
        # 'filter_by_keys':这个数据分为hybrid、surface、isobaricInhPa
        rain = 0

        for filename in filenames:
            if ((not filename.endswith('.idx')) and (weekOrDay - 1) * hours < int(filename[-3:]) <= weekOrDay * hours):
                path = fr"{accpdir}\{filename}"
                data = xr.open_dataset(path, engine='cfgrib',
                                       backend_kwargs={'filter_by_keys': {'typeOfLevel': 'surface'}})
                # 读取变量
                # name= data[list(data.data_vars.variables.mapping.keys())[0]].name
                # rain = data[name].values  #可以用此方法
                rain_1 = data[list(data.data_vars.variables.mapping.keys())[0]]
                # 定义名称
                name = rain_1.GRIB_name
                units = rain_1.units
                time_ = data['time'].values

                # 获取经纬度
                lat = data['latitude']
                lon = data['longitude']
                rain += rain_1
        # else:
        #     return print('降水数据不足')
        # print(name+units)
        print(time_)

        # 这个国家的经纬度范围
        ax.set_extent(country.get('region'), crs=self.proj)
        # apcptime = pd.Timestamp(time_,tz='Asia/Shanghai')
        apcptime = pd.Timestamp(time_).tz_localize('UTC').tz_convert('Asia/Shanghai')
        year = str(apcptime.to_pydatetime().year)  # tz='Asia/Shanghai'，转为上海时间
        month = str(apcptime.to_pydatetime().month)
        day = str(apcptime.to_pydatetime().day)
        hour = str(apcptime.to_pydatetime().hour)

        # 图标题

        if weeksOrDays == 'weeks':
            # 计算当前时间往后{weekOrDay}天的日期
            btm = (apcptime + pd.Timedelta(days=(weekOrDay - 1) * 7)).strftime('%m')
            btd = (apcptime + pd.Timedelta(days=(weekOrDay - 1)) * 7).strftime('%d')
            btH = (apcptime + pd.Timedelta(days=(weekOrDay - 1)) * 7).strftime('%H')
            btw = (apcptime + pd.Timedelta(days=(weekOrDay - 1)) * 7).strftime('%w')
            stm = (apcptime + pd.Timedelta(days=weekOrDay * 7)).strftime('%m')
            std = (apcptime + pd.Timedelta(days=weekOrDay * 7)).strftime('%d')
            stH = (apcptime + pd.Timedelta(days=weekOrDay * 7)).strftime('%H')
            stw = (apcptime + pd.Timedelta(days=weekOrDay * 7)).strftime('%w')
            ax.set_title(f'{btm}月{btd}日{btH}时(星期{btw})-{stm}月{std}日{stH}时(星期{stw})', loc='left', fontsize=10)
            # ax.set_title(f'{country.get("china_name")}未来第{weekOrDay}周降水预报（mm）', loc='center', fontsize=10)
            # fig.legend(title=rf'{btm}月{btd}日{btH}时(星期{btw})-{stm}月{std}日{stH}时(星期{stw})', loc='upper left', fontsize=12, ncol=1,shadow=False)
            fig.legend(
                title=rf'{country.get("china_name")}{crop}主产区未来第{weekOrDay}周降水预报（mm）',
                loc='upper center', fontsize=22, ncol=1, shadow=False, frameon=False)
            # fig.legend(labels=rf'{country.get("china_name")}{country.get("crops").get(crop)}主产区未来第{weekOrDay}周降水预报（mm）', loc='upper center', fontsize=22, ncol=1,shadow=False,frameon=False)

        if weeksOrDays == 'days':
            # 计算当前时间往后{weekOrDay}天的日期
            btm = (apcptime + pd.Timedelta(days=(weekOrDay - 1))).strftime('%m')
            btd = (apcptime + pd.Timedelta(days=(weekOrDay - 1))).strftime('%d')
            btH = (apcptime + pd.Timedelta(days=(weekOrDay - 1))).strftime('%H')
            btw = (apcptime + pd.Timedelta(days=(weekOrDay - 1))).strftime('%w')
            stm = (apcptime + pd.Timedelta(days=weekOrDay)).strftime('%m')
            std = (apcptime + pd.Timedelta(days=weekOrDay)).strftime('%d')
            stH = (apcptime + pd.Timedelta(days=weekOrDay)).strftime('%H')
            stw = (apcptime + pd.Timedelta(days=weekOrDay)).strftime('%w')
            ax.set_title(f'{btm}月{btd}日{btH}时(星期{btw})-{stm}月{std}日{stH}时(星期{stw})', loc='left', fontsize=15)#, fontsize=10
            # fig.legend(
            #     title=rf'{country.get("china_name")}{crop}主产区未来第{weekOrDay}日降水预报（mm）',
            #     loc='upper center', fontsize=22, ncol=1, shadow=False, frameon=False)
            ax.set_title(rf'{country.get("china_name")}{crop}主产区未来第{weekOrDay}日降水预报（mm）', loc='center', fontsize=15) #, fontsize=10


        timetitle = f'北京时间{year[-2:]}{month.rjust(2, "0")}{day.rjust(2, "0")}{hour.rjust(2, "0")}时起报'
        print(timetitle)
        # fig.legend(title=rf'{country.get("china_name")}未来第{weekOrDay}日降水预报（mm）', loc='upper right', fontsize=12,shadow=False)
        ax.set_title(timetitle, loc='right', fontsize=15)#, fontsize=10

        # 绘入降水数据
        level1 = [i * 0.5 for i in range(6)]  # 生成6个序列
        level2 = [5, 7.5, 10, 13, 16, 20, 25, 30, 35]  # 生成9个序列
        level3 = [i for i in range(40, 101, 10)]  # 生成7个序列
        level4 = [i for i in range(125, 201, 25)]  # 生成4个序列
        levels = level1 + level2 + level3 + level4 + [250]  # 生成26个序列

        colors = gen_perp_color()
        # contours = plt.contourf(lon, lat, rain,levels=levels,extend='both',cmap='Accent',transform=ccrs.PlateCarree())
        contours = plt.contourf(lon, lat, rain, levels=levels, extend='both', colors=colors)
        formatter = FuncFormatter(self.major_formatter)  # colorbar数字改为字符
        cbar = fig.colorbar(contours, shrink=0.5, ticks=levels, format=formatter)  # ,location='left'
        cbar.set_label(name, fontsize=10)

    # 绘制地图基本结构:州界/湖泊/海洋/陆地/海岸线
    def draw_base_map(self, ax):
        # 添加省地图
        for satategeo in self.satategeos:
            ax.add_geometries(satategeo,self.proj, facecolor='none', linestyle=':', edgecolor='black',
                              linewidth=0.5,
                              zorder=1)  # linstyle:https://blog.csdn.net/fengdu78/article/details/104624007/
        ax.add_feature(cfeature.LAND.with_scale('10m'))  ####添加陆地######
        ax.add_feature(cfeature.LAKES.with_scale('10m'), zorder=1)
        ax.add_feature(cfeature.RIVERS.with_scale('10m'), lw=0.25, zorder=1,
                       color='red')  # lw=0.25，单位通常是点（points）。较大的值将产生更粗的边缘线，而较小的值将产生更细的边缘线。
        ax.add_feature(cfeature.COASTLINE.with_scale('10m'), lw=1, zorder=1)
        ax.add_feature(cfeature.BORDERS, linestyle='-', lw=0.7)  ####不推荐，我国丢失了藏南、台湾等领土############
        # ax.add_feature(cfeature.OCEAN.with_scale('10m'))  ######添加海洋########
        print('基本地图数据绘制完毕')

    def save_images(self,plt, weeksOrDays, weekOrDay, country, image_dir, crop):
        # 保存图片
        if weeksOrDays == 'days':
            save_image = fr'{image_dir}\{weeksOrDays}\{country.get("china_name")}{crop}第{weekOrDay}日降水预报.png'
        if weeksOrDays == 'weeks':
            save_image = fr'{image_dir}\{weeksOrDays}\{country.get("china_name")}{crop}第{weekOrDay}周降水预报.png'
        print(f'图片名称：{save_image}')
        print(f'plt对象为{plt}')
        # plt.show()
        plt.savefig(save_image)

    # 添加加微信好友和付款码图片
    def add_paymoneyAndFriend_picture(self,plt, paymoney):
        # 添加加微信好友图片
        plt.axes((0.85, 0.35, 0.15, 0.18))  # plt.axes((left, bottom, width, height),
        plt.axis('off')
        plt.imshow(
            Image.open(
                # 'D:\pythonProject2\pythonProject\weather_01_download_drop\data\paymoneyAndAddFriend\whfriend.bmp'
            'D:\pythonProject311\_04_Crops_Precipitation_forecast\images\paymoneyAndAddFriend\whfriend.png'
            ))

        # 添加付款码图片
        if paymoney != 'free':
            plt.axes((0.85, 0, 0.2, 0.3))
            plt.axis('off')
            plt.imshow(
                Image.open(
                    'D:\pythonProject2\pythonProject\weather_01_download_drop\data\paymoneyAndAddFriend\paymoney.bmp'))



    # 制作日度和周度动图
    def createGif(self,country, crop, imagespath, weeksOrDays):
        # 一、首先删除历史APCP(累计降水）数据
        imagesfiles = []
        for root, dirs, files in os.walk(imagespath):
            for file in files:
                imagefile = fr'{imagespath}\{file}'
                imagesfiles.append(imagefile)

        # img_paths = [ "img/1.jpg","img/2.jpg","img/3.jpg","img/4.jpg" ,"img/5.jpg","img/6.jpg", "img/7.jpg", "img/8.jpg",]
        gif_images = []
        for path in imagesfiles:
            gif_images.append(imageio.imread(path))
        imageio.mimsave(fr"{imagespath}\{country.get('china_name')}{crop}{weeksOrDays}降水预报.gif",
                        gif_images, fps=1)
        print(f'{weeksOrDays}.gif图制作完毕')


    def draw_countymap_cropvalues(self,ax,merges):
        for merge in merges:
            # 处理地图数据
            croplen = len(merge.index)
            try:
                merge1 = merge.sort_values(by='Value', ascending=False).iloc[:int(croplen / 10), :]
                # print(type(merge1))
                ax = merge1.plot(
                    ax=ax,
                    column='Value',
                    facecolor=None,
                    hatch="++++",
                    alpha=0,
                    # missing_kwds={ #数据缺失用missing_kwds参数
                    #     "color":None ,#"lightgrey"
                    #     'linestyle' : ':',
                    #     # "edgecolor": "red",
                    #     # "hatch": "///",
                    #     "label": "Missing values",
                    # },
                )
                merge2 = merge.sort_values(by='Value', ascending=False).iloc[int(croplen / 10):int(croplen / 5), :]
                ax = merge2.plot(
                    ax=ax,
                    column='Value',
                    facecolor=None,
                    hatch="+++",
                    alpha=0,
                )
                merge3 = merge.sort_values(by='Value', ascending=False).iloc[int(croplen / 5):int(croplen / 2), :]
                ax = merge3.plot(
                    ax=ax,
                    column='Value',
                    facecolor=None,
                    hatch="++",
                    alpha=0,
                    # label='Corn-growing Region',
                )
                merge4 = merge.sort_values(by='Value', ascending=False).iloc[int(croplen / 2):, :]
                ax = merge4.plot(
                    ax=ax,
                    column='Value',
                    facecolor=None,
                    hatch="+",
                    alpha=0
                )
            except Exception as e:
                print(e)





if __name__ == '__main__':
    start_time = datetime.now()

    # # 利用apscheduler模块实现定时发送，运行dodraw()主函数
    # # # 设置时域
    # scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # # 时间设置，每年的10月，每天的8-11,2-4点半，
    # # scheduler.add_job(send_message, 'cron', month='10', hour='8-11,2-4', minute='30')
    # scheduler.add_job(dodraw, 'cron',['argentina','free'], hour='11', minute='46')
    # # 定时语言
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     pass


    # dodraw('argentina',paymoney='free')#paymoney='nofree'会有付款信息，paymoney='free'没有付款信息
    # dodraw('usa', paymoney='free')  # paymoney='nofree'会有付款信息，paymoney='free'没有付款信息
    stop_time = datetime.now()
    during_time = (stop_time - start_time).seconds/60
    print(f'本次花费时间：{during_time}分钟')