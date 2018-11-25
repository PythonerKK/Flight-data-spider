import urllib.request
import jsonpath
import json
import urllib.error
import csv
import threading
out = open('C:/4月12日查询5月3日.csv', 'a', newline='')
csv_writer = csv.writer(out, dialect='excel')

csv_writer.writerow(
    ['序号', '行程','日期','航班号', '航空公司', '出发机场', '到达机场',  '起飞时间', '到达时间', '飞行时长', '飞行里程', '执飞机型', '价格', '折扣', '餐食'])
def init():
    header=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    opener=urllib.request.build_opener()
    opener.addheaders=[header]
    urllib.request.install_opener(opener)
def getINFO(url='',start='',arrive=''):
    try:
        data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    except urllib.error.URLError as e:
        print("查询失败")
        return
    js=json.loads(data)
    info_list = jsonpath.jsonpath(js, '$..binfo')
    if (info_list == False):
        print('无航班记录\n')
        return

    aircode_list=jsonpath.jsonpath(js,'$..airCode')
    depairport_list=jsonpath.jsonpath(js,'$..depAirport')
    arrairport_list=jsonpath.jsonpath(js,'$..arrAirport')
    deptime_list=jsonpath.jsonpath(js,'$..depTime')
    arrtime_list=jsonpath.jsonpath(js,'$..arrTime')
    distance_list=jsonpath.jsonpath(js,'$..distance')
    time=jsonpath.jsonpath(js,'$..flightTime')
    fullname_list=jsonpath.jsonpath(js,'$..fullName')
    maincarrier_list=jsonpath.jsonpath(js,'$..mainCarrierFullName')

    mode_list=jsonpath.jsonpath(js,'$..planeFullType')
    price_list=jsonpath.jsonpath(js,'$..minPrice')
    discount_list=jsonpath.jsonpath(js,'$..discountStr')
    share_list=jsonpath.jsonpath(js,'$..codeShare')
    stops_list=jsonpath.jsonpath(js,'$..stops')
    mealDesc_list=jsonpath.jsonpath(js,'$..mealDesc')

    print('查询到'+str(len(info_list))+'条航班记录，已写入文件\n')

    for i in range(0,len(info_list)):
        if(share_list[i]==False):
            if(stops_list[i]==False):
                '''print('航班号：'+aircode_list[i]+' 航空公司：'+maincarrier_list[i]+' 出发机场：'+depairport_list[i]
                  +' 到达机场：'+arrairport_list[i]+' 起飞时间：'+deptime_list[i]+" 到达时间："+arrtime_list[i]
                  +' 飞行时长：'+time[i]+' 飞行里程：'+str(distance_list[i])+' 机型：'+mode_list[i]+' 价格：'+str(price_list[i])+' 折扣：'+discount_list[i]+' '+mealDesc_list[i]
                  )'''
                try:
                    csv_writer.writerow([str(i+1),start+'-'+arrive,date,aircode_list[i],maincarrier_list[i],start+depairport_list[i],arrive+arrairport_list[i],deptime_list[i],arrtime_list[i],
                                        time[i],str(distance_list[i])+'KM',mode_list[i],str(price_list[i]),discount_list[i],mealDesc_list[i]])
                except IndexError as i:
                    print("读写错误！")
                    return
                #csv_writer.writerow(['                                                                                                                     '])
            else:
                '''print('航班号：' + aircode_list[i] + ' 航空公司：' + maincarrier_list[i] + ' 出发机场：' + depairport_list[i]+' 经停机场：' + info_list[i]['stopAirports'][0]
                      + ' 到达机场：' + arrairport_list[i] +  '起飞时间：' + deptime_list[i] + " 到达时间：" + arrtime_list[i]
                      + ' 飞行时长：' + time[i] + ' 飞行里程：' + str(distance_list[i]) + ' 机型：' + mode_list[i] + ' 价格：' + str(
                    price_list[i]) + ' 折扣：' + discount_list[i]+' '+mealDesc_list[i]
                      )'''
                try:
                #csv_writer.writerow(['航班号', '航空公司', '出发机场','经停机场','到达机场', '起飞时间', '到达时间', '飞行时长', '飞行里程', '执飞机型', '价格', '折扣', '餐食'])
                    csv_writer.writerow(
                        [str(i+1),start+'-'+arrive,date,aircode_list[i], maincarrier_list[i], start+depairport_list[i]+'(经停'+info_list[i]['stopAirports'][0]+')', arrive+arrairport_list[i],deptime_list[i],
                        arrtime_list[i],
                        time[i], str(distance_list[i]) + 'KM', mode_list[i], str(price_list[i]), discount_list[i],
                        mealDesc_list[i]])
                except IndexError as i:
                    print("读写错误！")
                    return
                #csv_writer.writerow(['','','','经停：'+info_list[i]['stopAirports'][0]])
                #csv_writer.writerow([
                 #                       '                                                                                                                     '])


            pass
        else:
            if(stops_list[i]==False):
                '''print('航班号(共享)：' + aircode_list[i] + ' 航空公司：' + fullname_list[i] + ' 实际乘坐：'+info_list[i]['mainCarrier']+' 实际航空公司：'+maincarrier_list[i]+' 出发机场：' + depairport_list[i]
                  +  ' 到达机场：' + arrairport_list[i] + ' 起飞时间：' + deptime_list[i] + " 到达时间：" + arrtime_list[i]
                  + ' 飞行时长：' + time[i] +' 飞行里程：'+str(distance_list[i])+'KM'+ ' 机型：' + mode_list[i] + ' 价格：' + str(price_list[i]) + ' 折扣：' + discount_list[i]
                  )'''
                #csv_writer.writerow(
                    #['航班号', '航空公司', '实际乘坐','实际航空公司','出发机场', '到达机场', '起飞时间', '到达时间', '飞行时长', '飞行里程', '执飞机型', '价格', '折扣', '餐食'])
                try:
                    csv_writer.writerow(
                        [str(i+1),start+'-'+arrive,date,aircode_list[i]+'(共享) 实际乘坐'+info_list[i]['mainCarrier'], fullname_list[i]+'(实际承运'+maincarrier_list[i]+')',start+depairport_list[i], arrive+arrairport_list[i],deptime_list[i],
                        arrtime_list[i],
                        time[i], str(distance_list[i]) + 'KM', mode_list[i], str(price_list[i]), discount_list[i],
                        mealDesc_list[i]])
                except IndexError as i:
                    print("读写错误！")
                    return
                #csv_writer.writerow(['','实际乘坐'+info_list[i]['mainCarrier'],maincarrier_list[i]])

            else:
                '''print('航班号(共享)：' + aircode_list[i] + ' 航空公司：' + fullname_list[i] +' 实际乘坐：'+info_list[i]['mainCarrier']+' 实际航空公司：'+maincarrier_list[i]+ ' 出发机场：' + depairport_list[i]
                      + ' 经停机场：' + info_list[i]['stopAirports'][0] + ' 到达机场：' + arrairport_list[i] + ' 起飞时间：' +
                      deptime_list[i] + " 到达时间：" + arrtime_list[i]
                      + ' 飞行时长：' + time[i] + ' 飞行里程：' + str(distance_list[i]) + ' 机型：' + mode_list[i] + ' 价格：' + str(
                    price_list[i]) + ' 折扣：' + discount_list[i] + ' ' + mealDesc_list[i]
                      )'''
                #csv_writer.writerow(
                    #['航班号', '航空公司', '实际乘坐','实际航空公司','出发机场', '经停机场', '到达机场', '起飞时间', '到达时间', '飞行时长', '飞行里程', '执飞机型', '价格', '折扣', '餐食'])
                try:
                    csv_writer.writerow(
                        [str(i+1),start+'-'+arrive,date,aircode_list[i] + '(共享) 实际乘坐'+info_list[i]['mainCarrier'], fullname_list[i]+'(实际承运'+maincarrier_list[i]+')',
                        start+depairport_list[i]+'(经停'+info_list[i]['stopAirports'][0]+')', arrive+arrairport_list[i],deptime_list[i],
                        arrtime_list[i],
                        time[i], str(distance_list[i]) + 'KM', mode_list[i], str(price_list[i]), discount_list[i],
                        mealDesc_list[i]])
                except IndexError as e:
                    print("读写错误！")
                    return

            pass

def main(citylist,date):
    for start in citylist:
        start_code=urllib.request.quote(start)

        for arrive in citylist:
            if(start==arrive):
                continue;
            else:
                
                print('正在查询'+start+'飞往'+arrive+'的航班信息...')
                arrive_code=urllib.request.quote(arrive)
                url='https://flight.qunar.com/touch/api/domestic/wbdflightlist?departureCity='+start_code+'&arrivalCity='+arrive_code+'&departureDate='+date+'&ex_track=&sort=&isNewInterface=true'
                getINFO(url=url,start=start,arrive=arrive)

if __name__ == '__main__':

    date='2018-05-03'
    citylist=open('C:/city.txt','r')
    citylist=citylist.read()
    citylist=citylist.split('-')
    print(citylist)
    init()
    main(citylist,date)

    '''t1=threading.Thread(target=main,args=(citylist,date,),name='thread1')
    t2=threading.Thread(target=main,args=(citylist,date,),name='thread2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()'''


