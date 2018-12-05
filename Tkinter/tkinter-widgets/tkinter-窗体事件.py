#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-窗体事件.py
# @Time    : 2018/10/28  13:51
# @Software: PyCharm
# @DESC    : 窗体事件,在网上看到的,视频没讲,目前不知道怎么用

"""
<Configure> 改变大小或位置
<Visibility> 当组件变为可视状态时触发
<Unmap> 当组件由显示状态变为隐藏状态时触发
<Map> 当组件由隐藏状态变为显示状态时触发
<Expose> 当组件从原本被其他组件遮盖的状态中暴漏出来时触发
<FocusIn> 组件获得焦点时触发
<FocusOut> 组件失去焦点时触发
<Circulate> 当窗体由于系统协议要求在堆栈中置顶或压底时触发
<Colormap> 当窗体的颜色或外貌改变时触发，Tk中忽略此细则
<Property> 当窗体的属性被删除或改变时触发，属于TK的核心
<Destroy> 当组件被销毁时触发
<Activate> 与组件选项中的state项有关，表示组件由不可用变为可用时触发
<Deactivate> 与组件选项中的state项有关，表示组件由可用变为不可用时候触发
"""