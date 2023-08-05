#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/7 11:43
@Author   : ji hao ran
@File     : data_class.py
@Project  : StreamlitAntdComponents
@Software : PyCharm
"""
from dataclasses import dataclass
from typing import List, Literal

# global field type
Label = Literal['title', 'upper']
Align = Literal['start', 'center', 'end']
Align2 = Literal['right', 'center', 'left']
Direction = Literal["horizontal", "vertical"]
Size = Literal["large", "middle", "small"]
Msg = Literal['success', 'info', 'warning', 'error']
Position = Literal["top", "right", "bottom", "left"]


@dataclass
class BsIcon:
    name: str


@dataclass
class Item:
    label: str = ''  # label
    icon: str = None  # boostrap icon,https://icons.getbootstrap.com/
    disabled: bool = False  # disabled item


@dataclass
class NestedItem(Item):
    children: List = None  # item children


@dataclass
class ButtonsItem(Item):
    href: str = None  # link address


@dataclass
class SegmentedItem(Item):
    pass


@dataclass
class TabsItem(Item):
    pass


@dataclass
class TreeItem(NestedItem):
    pass


@dataclass
class CasItem(NestedItem):
    pass


@dataclass
class MenuItem(NestedItem):
    href: str = None  # item link address
    type: Literal['group', 'divider'] = None  # item type
    dashed: bool = False  # divider line style,available when type=='divider'
