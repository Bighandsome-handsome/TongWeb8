# 原创TongWeb的license动态更新

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121598643

---

自TongWeb7.0.4.5版本起，license更新可以不用重启验证。
通过commandstool.bat update-license命令可以动态更新license。
1. 放要替换的license.dat放在license_update目录下。
2. 执行commandstool.bat update-license命令：
commandstool.bat update-license
Please enter the admin user name>cli
Please enter the admin password>cli456!.COM
************************
consumer_name=aaa
project_name=aaaaaa
license_type=trail
create_date=2021-03-17
end_date=2021-12-17
TW_Product_Name=TongWeb
TW_Version_Number=7.0
TW_Edition=Enterprise
TW_CPU_COUNT=
************************
Command update-license executed successfully.
3. 若license不合法，则更新失败。
commandstool.bat update-license
Please enter the admin user name>cli
Please enter the admin password>cli456!.COM
************************
java.io.IOException: License is not for this edition of product, License type is : Light
************************
CLI137 Command update-license failed.