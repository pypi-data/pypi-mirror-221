from pymongo import MongoClient
# from Precipitation_Forecast_ import weather_forecast
from Precipitation_Forecast import weather_forecast
from datetime import datetime
import geopandas as gpd
import pandas as pd


'''
   'region'：所在国家的经纬度范围。Region = [leftlon, rightlon, lowerlat, upperlat]
'''

# 加载全国州地图
statemaps = [r"D:\天邦\33地图信息\argentina\Argentina_GeoJSON-master\Provincia\provincia.json",  # 阿根廷
            r"D:\天邦\33地图信息\china\China_GeoJSON-master\china_province.json",  # 中国
            r'D:\pythonProject2\pythonProject\weather_01_download_drop\data\usastates.geojson',  # 美国
            r"D:\天邦\33地图信息\brazil\brazil-states-master\br_states.geojson"  # 巴西
            ]

# 各县地图
countymaps = [r"D:\天邦\33地图信息\argentina\Argentina_GeoJSON-master\arg_departamentos.json",  # 阿根廷
              r"D:\天邦\33地图信息\china\China_GeoJSON-master\china_cities.json",  # 中国
              r"D:\天邦\33地图信息\usa\usa-geojson-master\usa-geojson-master\data\usa_counties.json",  # 美国
              r"D:\天邦\33地图信息\brazil\brazil-states-master\br_cities.json"  # 巴西
              ]  # 加载各州地图

# 一、阿根廷
def get_argentina():
    # 处理国家的作物数据
    # 创建MongoDB客户端
    client = MongoClient()
    # 选择数据库
    db = client["argentina"]
    # 选择集合：
    collection = db["argfiledcrops"]

    # 加载各县地图
    countymap = r"D:\天邦\33地图信息\argentina\Argentina_GeoJSON-master\arg_departamentos.json"
    country_gpd = gpd.read_file(countymap)
    country_gpd = country_gpd.to_crs('EPSG:4326') # 将几何数据转换为相同的CRS

    argentina = {
        'country': "argentina",
        'china_name': '阿根廷',
        # 'region': [-80, -50, -20, -50],
        'region': [-180, 180, 90, -90],
        'central_longitude': -65,
        'satategeo': [r"D:\天邦\33地图信息\argentina\Argentina_GeoJSON-master\Provincia\provincia.json"],
        'countygeo':country_gpd,#已经读取好的县市文件
        # 'figsize': (9, 10),
        'figsize': (45, 50),  # 图片尺寸
        'dpi': 120,  # 图片分辨率
        'crops': {'Maíz': '玉米', 'Soja total': '所有大豆'}, #, 'Soja total': '所有大豆', 'Soja 1ra': '一季大豆', 'Soja 2da': '二季大豆'
        'collections': {'Maíz': collection, 'Soja total': collection}, #, 'Soja 1ra': collection, 'Soja 2da': collection
        'county_crops': {}#获得各县市的作物产量数据
    }
    for crop in argentina.get('crops'):
        # print(crop)
        county_crop = countymap_cropvalues(argentina, crop)
        argentina['county_crops'][crop] = [county_crop]

    return argentina

# 二、巴西
def get_brazil():
    # 处理国家的作物数据
    # 创建MongoDB客户端
    client = MongoClient()
    # 选择数据库
    db = client["brazil"]
    # 选择集合：
    # col_milho = db["pam_milho"]
    col_temp = db["pam_lavouras_temporárias"]

    # 加载各县地图
    countymap = r"D:\天邦\33地图信息\brazil\brazil-states-master\br_cities.json"
    country_gpd = gpd.read_file(countymap)
    country_gpd = country_gpd.to_crs('EPSG:4326') # 将几何数据转换为相同的CRS


    brazil = {
        'country': "brazil",
        'china_name': '巴西',
        # 'region': [-80, -50, -20, -50],
        'region': [-180, 180, 90, -90],
        'central_longitude': -65,
        'satategeo': [r"D:\天邦\33地图信息\brazil\brazil-states-master\br_states.geojson"],
        'countygeo':country_gpd,#已经读取好的县市文件
        # 'figsize': (9, 10),
        'figsize': (45, 50),  # 图片尺寸
        'dpi': 120,  # 图片分辨率
        'crops': {'Milho (em grão)':'所有玉米',  'Soja (em grão)': '大豆', 'Cana-de-açúcar': '甘蔗'},# ,'Milho (em grão) - 2ª safra': '二季玉米','Milho (em grão) - 1ª safra': '一季玉米'
        'collections': {'Milho (em grão)': col_temp,  'Soja (em grão)': col_temp, 'Cana-de-açúcar': col_temp}, # 'milho':col_milho'Milho (em grão) - 2ª safra': col_temp,'Milho (em grão) - 1ª safra': col_temp
        'county_crops': {}#获得各县市的作物产量数据
    }
    for crop in brazil.get('crops'):
        # print(crop)
        county_crop = countymap_cropvalues(brazil, crop)
        brazil['county_crops'][crop] = [county_crop]

    return brazil

# 三、中国
def get_china():
    # 处理国家的作物数据
    # 创建MongoDB客户端
    client = MongoClient()
    # 选择数据库
    db = client["china"]
    # 选择集合：
    collection = db["crop_area_production"]

    # 加载各县地图
    countymap = r"D:\天邦\33地图信息\china\China_GeoJSON-master\china_cities.json"
    country_gpd = gpd.read_file(countymap)
    country_gpd = country_gpd.to_crs('EPSG:4326') # 将几何数据转换为相同的CRS


    china = {
        'country': "CNA",
        'china_name': '中国',
        # 'region': [73, 135, 10, 55], #中国
        'region': [-180, 180, 90, -90],
        'central_longitude': -65,
        'satategeo': [r"D:\天邦\33地图信息\china\China_GeoJSON-master\china_province.json"],
        'countygeo':country_gpd,#已经读取好的县市文件
        # 'figsize': (9, 10),
        'figsize': (45, 50),  # 图片尺寸
        'dpi': 120,  # 图片分辨率
        'crops': {'玉米': '玉米', '大豆': '大豆', '甘蔗': '甘蔗'}, #, '小麦': '小麦', '棉花': '棉花'
        'collections': {'玉米': collection, '大豆': collection, '甘蔗': collection}, #'棉花': collection,
        'county_crops': {}#获得各县市的作物产量数据
    }
    for crop in china.get('crops'):
        # print(crop)
        county_crop = countymap_cropvalues(china, crop)
        china['county_crops'][crop] = [county_crop]

    return china

# 四、美国
def get_USA():
    # 处理国家的作物数据
    # 创建MongoDB客户端
    client = MongoClient()
    # 选择数据库
    db = client["usa"]
    # 选择集合：
    collection = db["usafiledcrops"]

    # 加载各县地图
    countymap = r"D:\天邦\33地图信息\usa\usa-geojson-master\usa-geojson-master\data\usa_counties.json"
    country_gpd = gpd.read_file(countymap)
    country_gpd = country_gpd.to_crs('EPSG:4326') # 将几何数据转换为相同的CRS


    USA = {
        'country': "USA",
        'china_name': '美国',
        # 'region': [-70, -130, 25, 50],#美国
        'region': [-180, 180, 90, -90],
        'central_longitude': -65,
        'satategeo': [r"D:\天邦\33地图信息\usa\usa-geojson-master\usa-geojson-master\data\states.json"],
        'countygeo':country_gpd,#已经读取好的县市文件
        # 'figsize': (9, 10),
        'figsize': (45, 50),  # 图片尺寸
        'dpi': 120,  # 图片分辨率
        'crops': {
              "CORN": '玉米', "SOYBEANS": '大豆',
            # "SORGHUM": '高粱',
                  # "COTTON": '棉花',
                  # "WHEAT, SPRING, (EXCL DURUM)": '春小麦（不含杜兰麦）', "WHEAT, SPRING, DURUM": '春小麦，杜兰麦',
                  # "WHEAT, WINTER": '冬小麦'
            },
        'collections': {'CORN': collection, 'SOYBEANS': collection,
                        # 'SORGHUM': collection, 'WHEAT, SPRING, (EXCL DURUM)': collection,
                        # 'WHEAT, SPRING, DURUM': collection, 'WHEAT, WINTER': collection
                        },
        'county_crops': {} #获得各县市的作物产量数据crop:merge
    }
    for crop in USA.get('crops'):
        # print(crop)
        county_crop = countymap_cropvalues(USA, crop)
        USA['county_crops'][crop] = [county_crop]
    return USA

def get_main_counties():
    # 获得各国数据
    argentina = get_argentina()
    print('阿根廷数据读取完毕')
    brazil = get_brazil()
    print('巴西数据读取完毕')
    china = get_china()
    print('中国数据读取完毕')
    usa = get_USA()
    print('美国数据读取完毕')

    main_counties = {
        'country': "main_counties",
        'china_name': '主产国',
        'counties': {'argentina':argentina,'brazil': brazil,'china': china, 'usa': usa},  #
        # 'region': [-70, -130, 25, 50],#美国
        'region': [-180, 180, 90, -90],
        'central_longitude': -65,
        'satategeo': statemaps,
        'countygeo':countymaps,
        # 'figsize': (9, 10),
        'figsize': (45, 50),  # 图片尺寸
        'dpi': 120,  # 图片分辨率
        'county_crops': {}, #crop:[merge]
        'crops':{
            "大豆": {
                'argentina': 'Soja total',#{'Soja 1ra': '一季大豆', 'Soja 2da': '二季大豆'},
                'brazil': 'Soja (em grão)',#{'Soja (em grão)': '大豆'},
                'china':'大豆',# {'大豆':'大豆'},
                'usa': 'SOYBEANS'#{'SOYBEANS':'大豆'},
            },
            "玉米": {
                'argentina':'Maíz',#{'Maíz': '玉米'},
                'brazil': 'Milho (em grão)',#{'Milho (em grão) - 2ª safra': '二季玉米', 'Milho (em grão) - 1ª safra': '一季玉米'},
                'china': '玉米',#{'玉米': '玉米'},
                'usa':'CORN' ,#{'CORN': '玉米'},
            },
            # "小麦": {
            #     # 'argentina': '小麦',
            #     # 'brazil': '小麦',
            #     'china': {'小麦': '小麦'},
            #     'usa': {'WHEAT, SPRING, (EXCL DURUM)': '春小麦', 'WHEAT, SPRING, DURUM': '春小麦', 'WHEAT, WINTER': '冬小麦'},
            # },
            # "高粱": {
            #     'usa':'SORGHUM',
            # },
            "甘蔗": {
                'china': '甘蔗',#{'甘蔗': '甘蔗'},
                'brazil': 'Cana-de-açúcar',#{'Cana-de-açúcar': '甘蔗'},
                # 'india': '甘蔗',
                # 'thailand':'甘蔗',
            },
            # "棉花": {
            #     'china': '棉花',
            #     'brazil': '棉花',
            #     'usa': 'COTTON',
            # },
            # "花生": {
            #     'china': '花生',
            # },
        }
    }

    for crop in main_counties['crops']:
        # 获得某种作物的主产国县和作物结合数据
        # crops  = [main_counties['counties'][country]['county_crops'][main_counties['crops'][crop][country]] for country in main_counties['crops'][crop]]
        main_counties['county_crops'][crop] =[]
        for country in main_counties['crops'][crop]:
            # 将国家的县作物数据遍历出来，存入county_crops
            for cr_df in main_counties['counties'][country]['county_crops'][main_counties['crops'][crop][country]]:
                main_counties['county_crops'][crop].append(cr_df)

        # print(f'crops的值是：{crops}')
        # merged_df = pd.concat(crops)
        # print(f'merged_df的值是：{merged_df}')
        # merged_df.to_excel(f'{crop}.xlsx', index=False)
        # print(main_counties)


    return main_counties


def countymap_cropvalues(country, crop):
    # 加载各县地图
    country_gpd = country.get('countygeo')
    # 省和市组成一列，以防有相同的市。，省市大写
    country_gpd['state_country'] = country_gpd['state'].str.normalize('NFD').str.lower() + '_' + country_gpd['name'].str.normalize('NFD').str.lower()  # 新增一行省和市（县）的组合

    country_gpd = country_gpd[['state_country', 'geometry']]
    # # 存入excel
    # country_gpd.to_excel(f'country_gpd.xlsx', index=False)

    # 列出最近3年
    match_1 = {"commodity_desc": crop,"statisticcat_desc":"PRODUCTION"}
    if len(crop.split(',', 1)) >1:
        match_1["commodity_desc"] = crop.split(',', 1)[0].strip()
        match_1["class_desc"] = crop.split(',', 1)[-1].strip()

    # print(match_1)
    pipeline = [
        {"$match":match_1 },  # 筛选包含特定字符串的数据{"$regex": crop}
        {"$group": {"_id": "$year"}},  # 对另一列数据进行分组
        {"$sort": {"_id": -1}},  # 对分组后的数据进行降序排序
        # {"$project": {"_id": 0, "year": 1, "commodity_desc": 1}}
    ]

    collection = country.get('collections')[crop]
    years = [year.get("_id") for year in list(collection.aggregate(pipeline))[:3]]
    # print(country_gpd)
    print(years)
    # 最近3年各县市的平均产量
    match_ = {
            "county_name": {"$exists": True,'$nin': [float('nan'), None,''] }, #"$ne": ''
            "Value": {"$exists": True, "$ne": ''},
            "year": {"$in": years},  # 列值与列表中的值匹配
            "commodity_desc": crop,  # 列值与字符串匹配
            # "class_desc": crop.split(',', 1)[-1],  # 列值与字符串匹配
            "statisticcat_desc": "PRODUCTION",
        }
    if len(crop.split(',', 1)) >1:
        match_["commodity_desc"] = crop.split(',', 1)[0].strip()
        match_["class_desc"] = crop.split(',', 1)[-1].strip()

    # print(match_)

    values = collection.aggregate([
        {"$match": match_},
        {"$addFields": {
            "state_country": {"$concat": [{'$toUpper': "$state_name"}, "_", {'$toUpper':"$county_name"}]}  # 新增省和市（县）的组合，省市大写
        }},
        {"$group": {
            "_id": {
                "state_country": "$state_country",
                # "commodity_desc": "$field2",
                # "year": "$reference_period_desc"
            },
            "Value": {"$avg": {
                '$toDouble': {
                    '$replaceAll': {
                        'input': {'$toString':'$Value'},
                        'find': ',',
                        'replacement': ''
                    }
                }
            }}  # 最近3年某县的平均值

            # "Value": {"$avg": { "$toDouble": "$Value" }}  # 最近3年某县的平均值
            # "Value": {"$avg": "$Value"}  # 最近3年某县的平均值
        }},
        {"$project": {
            "state_country": "$_id.state_country",
            "Value": 1,
            "_id": 0
        }}
    ])
    crop_mean_values = pd.DataFrame(list(values))
    # 所有字母小写
    crop_mean_values['state_country'] = crop_mean_values['state_country'].str.normalize('NFD').str.lower()

    # # 存入excel
    # crop_mean_values.to_excel(f'crop_mean_values.xlsx', index=False)
    # print(crop_mean_values)
    # 将地图数据与作物数据合并,并降序排列
    merge = country_gpd.merge(crop_mean_values, on='state_country', how='right').sort_values(by='Value',
                                                                                             ascending=False)
    merge = merge[merge["Value"] > 10000] #只保留产量大于10000吨的县市

    # print(merge)
    # # 将数据存储到Excel表格
    # merge.to_excel(f'{crop}.xlsx', index=False)
    return merge

def mian_pro(paymoney):

    start_time = datetime.now()
    print(f'预报图片开始制作时间:{start_time}')
    forecast_result = weather_forecast(paymoney) #paymoney='nofree'会有付款信息，paymoney='free'没有付款信息
    # country = get_argentina()
    # country = get_brazil()
    # country = get_china()
    # country = get_USA()
    # print(country)
    country = get_main_counties()
    forecast_result.crop_draw(country)

    stop_time = datetime.now()
    during_time = (stop_time - start_time).seconds / 60
    print(f'本次预报图片花费时间：{during_time}分钟')

if __name__ == '__main__':
    start_time = datetime.now()
    #
    # # # 利用apscheduler模块实现定时发送，运行dodraw()主函数
    # # # # 设置时域
    # # scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # # # 时间设置，每年的10月，每天的8-11,2-4点半，
    # # # scheduler.add_job(send_message, 'cron', month='10', hour='8-11,2-4', minute='30')
    # # scheduler.add_job(dodraw, 'cron',['argentina','free'], hour='11', minute='46')
    # # # 定时语言
    # # try:
    # #     scheduler.start()
    # # except (KeyboardInterrupt, SystemExit):
    # #     pass
    mian_pro('free')


