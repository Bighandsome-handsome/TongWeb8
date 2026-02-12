# 原创TongWeb7.0动态密钥说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/148496600

---

为解决TongWeb密码硬编码问题，TongWeb7.0.4.9_M5及之后版本采用动态密钥，在使用过程或升级过程中可能会遇到密码加密异常问题。对其做一个说明：
在TongWeb单节点
情况下
，根节点和通过domain命令建的域，数据源用户名和密码、SSL证书密码、JCA适配器密码等的密钥是采用
动态密钥的。禁止不同TongWeb间的密码复制粘贴
。例如：
场景一：
A机 /opt/tongweb/conf/tongweb.xml  中的密码复制到   B机不同目录 /root/tongweb/conf/tongweb.xml
密码不可用
场景二：
A机 /opt/tongweb/conf/tongweb.xml  中的密码复制到  A机域下 /opt/tongweb/domains/node1/conf/tongweb.xml
密码不可用
TongDataGrid
组名也是根据TongWeb做为动态密钥的，
密码则根据组名做为动态密钥的
，组名不同，密码相同时生成的加密串不同。手工配置session复制时，步骤如下：
在控制台配置session管理器，如：组名tongdev, 密码tongtech
将tongweb.xml中生成的tdg-group-name="
_TSM_0oaTdXXU8MK/L/dJtwOsTQ==
" tdg-group-password="
_TSM_ADU772qVqjc33QGYPqdKpw==
" 复制到TDG的tongdatagrid.xml中。
<group>
     <name>tongdev</name>
     <password>_TSM_ADU772qVqjc33QGYPqdKpw==</password>
 </group>
若无法通过控制台配置密码，则可以通过命令生成密码串复制到tongweb.xml中。
数据源用户名和密码、SSL证书密码、JCA适配器密码、tdg-group-name则通过password命令生成加密串。
TDG的tdg-group-password则通过
commandstool generate-tdg-token --tongdatagrid_group_name=tongdev --tongdatagrid_group_password=tongtech  命令，将生成的加密串复制到tongweb.xml和tongdatagrid.xml中。
在采用TongWeb heimdall情况下，通过集中管理添加节点，新建集群和域，会在TongWeb conf\security目录下生成tsmtoken.txt文件动态密码，则相关域数据源用户名和密码、SSL证书密码、JCA适配器密码、tdg-group-name生成的加密串相同。 将该文件复制到其它TW域则得到相同加密串。
注意：TongWeb7.0.4.9_M5兼容旧密码，正常补丁升级后，在控制台保存密码，可以更新为新的加密方式。但注意更换TongWeb目录后要更新密码。