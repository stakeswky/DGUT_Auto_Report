# 东莞理工疫情自动打卡助手

### 使用方法
设置好Secrets即可。设置方法[点击这里](https://github.com/Bertramoon/Auto_Attendance/blob/main/README.md#22-%E8%AE%BE%E7%BD%AEsecrets)。有多个账号的话，以","分隔开，如设置USERNAME为"2018001,2018002"，PASSWORD为"123456,7891011"。

另，有一个经纬度参数**LOCATIONS**
当你不设置该参数时，打卡的定位默认为东莞理工学院松山湖校区，适合在校时直接使用无需设置。
当你不在松山湖校区时需要设置该参数，设置格式为"-L [[<第i个账号>,<经度>,<维度>],[……]]"，如"-L [[1,112.321328,36.213527],[2,114.324132,40.233232]]"（注意只要-L和数据间有空格，其余地方无空格）的意思是为第一个账号设置经度为112.321328 纬度为36.213527，为第二个账号设置经度为114.324132 纬度为40.233232，若没有指定的话，默认经纬度为(113.87651,22.90701) 
