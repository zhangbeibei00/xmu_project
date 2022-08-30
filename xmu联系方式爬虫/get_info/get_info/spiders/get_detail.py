# 解析网页信息,提取联系方式
import jieba.posseg as pseg
import re


# 输入文本字符,返回 元组

# 判断是否满足该模式
def check_string(re_exp, str):
    f = re.finditer(re_exp, str)
    for i in f:
        # print(i.group(1))
        if len(i.group(1)) < len(str):
            return False
        else:
            return True
        break
    return False


# 判断一个字符串是否是人名
def isname(single_word_string):
    if len(single_word_string) > 3 or len(single_word_string) < 2:
        return False
    pair_word_list = pseg.lcut(single_word_string)
    for eve_word, cixing in pair_word_list:
        if cixing == "nr":
            return True
    return False


def get_org_info(content):
    emailpat = r'([a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+)'
    phonepat = r'\b((0592-\d{7}|(13[0-9]|15[0|1|3|6|7|8|9]|18[8|9])\d{8})|\d{7})\b'

    str_list = re.split(r'[\s：:_|{}．、；, ]', content)
    your_list = [x.replace('\n', '') for x in str_list if x != '']
    # 寻找组织的名字
    # 一般在网页内容刚开头就是
    org_name = ''
    for i in range(0, len(your_list)):
        if "厦门大学"or "实验室" in your_list[i]:
            if len(your_list[i])>30:
                break
            org_name = your_list[i]
            break

    first_email_index = 0
    first_email = ''
    # 一般邮箱和电话都在一起
    for i in range(0, len(your_list)):
        # 该字符串满足邮箱的表达式
        # 邮箱的长度不可能十位以下
        if (len(your_list[i]) < 10):
            continue
        #     找到最后一个邮箱的index
        if check_string(emailpat, your_list[i]):
            first_email_index = i
            first_email = your_list[i]

    st = max(0, first_email_index - 20)
    end = min(len(your_list), first_email_index + 20)
    first_phone = ''
    address = ''
    for i in range(st, end):
        item = your_list[i]
        if len(item) > 15:
            continue
        if check_string(phonepat, item):
            first_phone = item
        if item == '地址' and i + 1 < len(your_list):
            address = your_list[i + 1]
        if '版权' in item:
            k = 0
            while k < 5 and i + k < len(your_list):
                k += 1
                if "厦门大学" in your_list[k]:
                    org_name = your_list[k]
                    break
    print(org_name,first_email,first_phone,address)
    return (org_name, first_email, first_phone, address)


def get_first_info(content):
    title_list = ['教授', '助理教授', '助教', '副教授', '工程师', '辅导员', '秘书', '财务', '主任', '实验师']
    emailpat = r'([a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+)'
    phonepat = r'\b((0592-\d{7}|(13[0-9]|15[0|1|3|6|7|8|9]|18[8|9])\d{8})|\d{7})\b'

    email = re.findall(emailpat, content)
    phone = re.findall(phonepat, content)
    str_list = re.split(r'[\s：:()_|{}．、；-]', content)

    your_list = [x.replace('\n', '') for x in str_list if x != '']
    # 判断是否满足邮箱和电话号码的正则匹配表达式
    # 判断是否满足人名的正则匹配表达式
    # print(your_list)

    first_email_index = 0
    first_email = ''
    for i in range(0, len(your_list)):
        # 该字符串满足邮箱的表达式
        # 邮箱的长度不可能十位以下
        if (len(your_list[i]) < 10):
            continue
        if check_string(emailpat, your_list[i]):
            first_email_index = i
            first_email = your_list[i]
            break

    # 根据页面的信息状况,名字和电话可能出现在前后20个字符串中
    # 在前后20的范围内寻找满足姓名和电话的字符串等个人信息的内容
    st = max(0, first_email_index - 20)
    end = min(len(your_list), first_email_index + 20)
    first_name = ''
    first_phone = ''
    first_title = ''
    name_flag = 0
    phone_flag = 0
    title_flag = 0
    for i in range(st, end):
        item = your_list[i]
        if len(item) > 25:
            continue
        if ~title_flag and item in title_list:
            first_title = item
            title_flag = 1
        if ~name_flag and isname(item):
            first_name = item
            name_flag = True
        if ~phone_flag and check_string(phonepat, item):
            first_phone = item
            phone_flag = True
        if phone_flag and name_flag and title_flag:
            break

    return (first_name, first_title, first_phone, first_email)


# 测试样例
if __name__ == "__main__":
    text = '''教授
            所在位置
                网站首页

                >
                师资队伍

                >
                专任教师

                >
                教授

                >
                正文















                陈黄鑫
                职称：教授
                职务：信息与计算数学系副系主任
                学历：博士
                电子邮件：0_chx@xmu.edu.cn
                联系电话：0592-2580621
					 2580621
                办 公 室：数学物理大楼R678









 教育经历：

1. 2002/09-2006/06，湖南大学，数学与应用数学专业，学士
2. 2006/09-2011/07，中国科学院数学与系统科学研究院，博士

 工作经历：

1.2020/08-至今，厦门大学，数学科学学院，教授
2.2014/08-2020/07，厦门大学，数学科学学院，副教授
3.2011/09-2014/07，厦门大学，数学科学学院，讲师
4.2013/02-2013/08，香港科技大学，访问学者
5.2015/05-2016/02，沙特阿卜杜拉国王科技大学，博士后


 研究方向：

自适应有限元方法、多重网格法、间断Galerkin方法、多孔介质流动输运问题，流体拓扑优化问题，高波数波动问题       


 授课情况：

《微积分》、《数值逼近》、《有限元方法及其应用》


 论文:

• Huangxin Chen, Haitao Leng, Dong Wang, Xiao-Ping Wang, An efficient threshold dynamics method for topology optimization for fluids, CSIAM Transactions on Applied Mathematics, accepted, 2021.
• Jisheng Kou, Huangxin Chen, Shuyu Sun, Xinhua Wang, A linear, decoupled and positivity-preserving numerical scheme for an epidemic model with advection and diffusion, Comm. Pure Appl. Anal., accepted, 2021.
• Haitao Leng, Dong Wang, Huangxin Chen, Xiao-Ping Wang, An iterative threshold- ing method for topology opti
mization for the Navier-Stokes flow, Conference of Recent Advances in Industrial and Applied Mathematics, accepted, 2021.
• Zhengkang He, Huangxin Chen, Jie Chen, Zhangxin Chen, Generalized multiscale approximation of mixed finite 
element methods with velocity elimination for Darcy flow in fractured porous media, Comput. Methods Appl. Mech. Engrg., 381 (2021), 113846.
• Haitao Leng, Huangxin Chen, Adaptive HDG methods for the Brinkman equations with application to optimal control, J. Sci. Comput. 87 (2021), Paper No. 46, 34 pp.
• Huangxin Chen, Jingzhi Li, Weifeng Qiu, Chao Wang, A mixed finite element scheme for quad-curl source and eigenvalue problems, Commun. Comput. Phys., 29 (2021), pp.1125–1151.
• Huangxin Chen, Shuyu Sun, A new physics-preserving IMPES scheme for incompressible and immiscible two-phase flow in heterogeneous porous media, J. Comput. Appl. Math., 381 (2021), 113035, 20 pp.
• Yihui Han, Huangxin Chen, Xiao-Ping Wang, Xiaoping Xie, EXtended HDG methods for second order elliptic interface problems, J. Sci. Comput. 84 (2020), no. 1, Paper No. 22, 29 pp.
• Huangxin Chen, Shuyu Sun, An expanded mixed finite element method for space fractional Darcy flow in porous media, Procedings of International Conference on Computational Science, 2020.
• Guangpu Zhu, Huangxin Chen, Aifen Li, Shuyu Sun, Jun Yao, A fully discrete energy stable scheme for a phase
-field moving contact line model with variable densities and viscosities, Applied Mathematical Modelling, 83 (2020), pp. 614–639.
• Huangxin Chen, Xiaolin Fan, Shuyu Sun, A fully mass-conservative iterative IMPEC method for multicomponent compressible flow in porous media, J. Comput. Appl. Math., 362 (2019), pp. 1–21.
• Huangxin Chen, Jisheng Kou, Shuyu Sun, Tao Zhang, Fully mass-conservative IMPES schemes for incompressible two-phase flow in porous media, Comput. Methods Appl. Mech. Engrg., 350 (2019), pp. 641–663.
• Guangpu Zhu, Huangxin Chen, Jun Yao, and Shuyu Sun, Efficient energy-stable schemes for the hydrodynamics coupled phase-field model, Applied Mathematical Modelling, 70 (2019), pp. 82–108.
• Huangxin Chen, Weifeng Qiu and Ke Shi, A priori and computable a posteriori error estimates for an HDG method for the coercive Maxwell equations, Comput. Methods Appl. Mech. Engrg., 333 (2018), pp. 287–310.
• Huangxin Chen, Shuyu Sun and Tao Zhang, Energy stability analysis of some fully discrete numerical schemes for incompressible Navier-Stokes equations on staggered grids, J. Sci. Comput., 75 (2018), pp. 427–456.      
• Huangxin Chen and Shuyu Sun, A residual-based a posteriori error estimator for single-phase Darcy flow in fractured porous media, Numer. Math., 136 (2017), pp. 805-839.
• Huangxin Chen, Weifeng Qiu, Ke Shi and Manuel Solano, A superconvergent HDG method for the Maxwell equations, J. Sci. Comput., 70 (2017), pp. 1010-1029.
• Huangxin Chen and Weifeng Qiu, A first order system least squares method for the Helmholtz equation, J. Comput. Appl. Math., 309 (2017), pp. 145–162.
• Peipei Lu, Huangxin Chen and Weifeng Qiu, An absolutely stable hp-HDG method for the time-harmonic Maxwell equations with high wave number, Math. Comp., 86 (2017), pp. 1553-1577.
• Huangxin Chen, Amgad Salama, and Shuyu Sun, Adaptive mixed finite element methods for Darcy flow in fractured porous media, Water Resour. Res., 52 (2016), pp. 7851–7868.
• Huangxin Chen and Shuyu Sun, A two-scale reduced model for Darcy flow in fractured porous media, Procedia Computer Science, 80 (2016), pp. 1324–1333.
• Huangxin Chen, Jingzhi Li and Weifeng Qiu, Robust a Posteriori Error Estimates for HDG method for Convection-Diffusion Equations, IMA J. Numer. Anal., 36 (2016), pp. 437–462.
• Huangxin Chen, Haijun Wu and Xuejun Xu, Multilevel preconditioner with stable coarse grid corrections for the Helmholtz equation, SIAM J. Sci. Comput., 37 (2015), pp. A221– A244.
• Huangxin Chen, Guosheng Fu, Jingzhi Li and Weifeng Qiu, First order least square method with weakly imposed
 boundary condition for convection dominated diffusion problems, Comput. Math. Appl., 68 (2014), pp. 1635–1652.
• Huangxin Chen, Peipei Lu and Xuejun Xu, A robust multilevel method for hybridizable discontinuous Galerkin method for the Helmholtz equation, J. Comp. Phys., 264 (2014), pp. 133–151.
• Huangxin Chen and Xiao-Ping Wang, A one-domain approach for modeling and simula- tion of free fluid over a porous medium, J. Comp. Phys., 259 (2014), pp. 650–671.
• Huangxin Chen, Peipei Lu and Xuejun Xu, A hybridizable discontinuous Galerkin method for the Helmholtz equation with high wave number, SIAM J. Numer. Anal., 51 (2013), pp. 2166–2188.
• Xuejun Xu, Huangxin Chen and R.H.W. Hoppe, Optimality of local multilevel methods for adaptive nonconforming P1 finite element methods, J. Comp. Math., 31 (2013), pp. 22–46.
• Huangxin Chen, R.H.W. Hoppe and Xuejun Xu, Uniform convergence of local multigrid methods for the time-harmonic Maxwell equation, ESAIM: M2AN, 47 (2013), pp. 125–147.
• Huangxin Chen, Xuejun Xu and Weiying Zheng, Local multilevel methods for second- order elliptic problems with highly discontinuous coefficients, J. Comp. Math., 30 (2012), pp. 223–248.
• Xuejun Xu, Huangxin Chen and R.H.W. Hoppe, Optimality of local multilevel methods on adaptively refined meshes for elliptic boundary value problems, J. Numer. Math., 18 (2010), pp. 59–90.
• Huangxin Chen and Xuejun Xu, Local multilevel methods for adaptive finite element methods for nonsymmetric and indefinite elliptic boundary value problems, SIAM J. Numer. Anal., 47 (2010), pp. 4492–4516.
• Huangxin Chen, Xuejun Xu and R.H.W. Hoppe, Convergence and quasi-optimality of adaptive nonconforming finite element methods for some nonsymmetric and indefinite problems, Numer. Math., 116 (2010), pp. 383–419.      

 主持项目：

• 国家自然科学基金优秀青年科学基金项目 (No. 11771363), 1/1/2022-31/12/2024, 主持.
• 国家自然科学基金面上项目 (No. 11771363), 1/1/2018-31/12/2021, 主持.
• 国家自然科学基金青年科学基金项目 (No. 11201394), 1/1/2013-31/12/2015, 主持.
• 厦门大学校长基金项目 (No. 20720180003), 1/1/2018-31/12/2020, 主持.
• 厦门大学校长基金项目 (No.20720150005), 1/1/2015-31/12/2017, 主持.
• 福建省自然科学基金青年科学基金项目 (No. 2013J05016), 1/1/2013-31/12/2015, 主持.

学生培养：
• 每年计划招收博士生1名，硕士生1-2名。有意者请将个人简历和成绩单（含本科、硕士阶段）发送至：chx@xmu.edu.cn   
• 在读硕士生：
张显鹏（2019），胡宇（2019）
• 在读博士生：
向亚红（2020），董飘飘（2021）
 地址：厦门大学数学科学学院 邮编：361005 电话：2580605 传真：2580608
 Copyright © 2020 厦门大学数学科学学院所有 管理员信箱：helpmath@xmu.edu.cn
 旧版网站




                    厦门大学数学科学学院微信公众号
                    扫一扫关注，获取最新信息
'''
    info = get_first_info(text)
    print(info)
