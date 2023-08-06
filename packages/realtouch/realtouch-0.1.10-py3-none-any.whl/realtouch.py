import json
import time
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Union, Any
import base64
import numpy as np
import requests
from loguru import logger
import re
from pathlib import Path
import base64
import cv2


@dataclass
class ImgArea:
    start_x: float = 0
    end_x: float = 1
    start_y: float = 0
    end_y: float = 1


class ImgLocation(Enum):
    FULL = ImgArea(0, 1, 0, 1)
    LEFT = ImgArea(0, 0.5, 0, 1)
    RIGHT = ImgArea(0.5, 1, 0, 1)
    TOP = ImgArea(0, 1, 0, 0.5)
    BOTTOM = ImgArea(0, 1, 0.5, 1)
    MIDDLE = ImgArea(0, 1, 0.25, 0.75)
    HEAD = ImgArea(0, 1, 0, 0.25)
    HEADLINE = ImgArea(0, 1, 0, 0.1)
    TAIL = ImgArea(0, 1, 0.75, 1)
    FOOT = ImgArea(0, 1, 0.9, 1)


@dataclass
class TemplateLocation:
    points: list[Union[tuple[int, int], list[int]]]
    center: tuple[Union[int, float], Union[int, float]] = (-1, -1)
    found: bool = False
    size: int = 0


class TextAction(Enum):
    KEYCODE_NEXT = 'KEYCODE_NEXT'
    KEYCODE_PREVIOUS = 'KEYCODE_PREVIOUS'
    KEYCODE_DONE = 'KEYCODE_DONE'
    KEYCODE_SEARCH = 'KEYCODE_SEARCH'
    KEYCODE_SEND = 'KEYCODE_SEND'
    KEYCODE_GO = 'KEYCODE_GO'
    KEYCODE_DELETE = 'KEYCODE_DELETE'
    KEYCODE_DELETE_ALL = 'KEYCODE_DELETE_ALL'
    KEYCODE_MAIN_KEYBOARD = 'KEYCODE_MAIN_KEYBOARD'
    KEYCODE_CLOSE = 'KEYCODE_CLOSE'


@dataclass
class Photo:
    image: np.ndarray
    position: tuple[float, float]
    timestamp: float
    texts: list[list[list[float, float, float, float], str, float]]
    phone: int


def get_center(points: list):
    """
    get center of 4 points
    :param points:
    :return:
    """
    return np.mean(points, axis=0)


def location_serialize(location: Union[
    ImgLocation, list[ImgLocation],
    ImgArea, list[ImgArea]] = ImgLocation.FULL):
    try:
        if not isinstance(location, list) and not isinstance(location, tuple):
            location = [location]
        result = []
        for loc in location:
            if isinstance(loc, ImgLocation):
                result.append(loc.name)
            else:
                result.append(asdict(loc))
        return result
    except Exception as e:
        logger.exception(e)
        return location


class Robot:
    def __init__(self, ip: str):
        self.ip = ip
        self._phones: dict[int, Phone] = {}
        self.__load()

    def __load(self):
        """
        load phones from robot
        :return:
        """
        phones = self.call_api('phones/get')
        try:
            phones = phones.json()
            for phone in phones:
                pos = phone['position']
                self._phones[pos] = Phone(
                    pos,
                    self,
                    data=phone
                )
        except Exception as e:
            logger.exception(e)
            logger.debug(phones.content)

    def phone(self, position: int) -> 'Phone':
        return self._phones.get(position)

    @property
    def phones(self) -> dict[int, 'Phone']:
        return self._phones

    def call_func(self, position, path, **kwargs) -> Any:
        phone = self.phone(position)

        if 'location' in kwargs:
            kwargs['location'] = location_serialize(kwargs['location'])

        if phone:
            headers = {
                'PhonePosition': str(phone.position)
            }
        else:
            headers = {}
        result = requests.post(
            f'http://{self.ip}/api/{path}/',
            json=json.dumps(kwargs),
            headers=headers
        )
        try:
            return result.json()
        except Exception:
            try:
                return result.content.decode()
            except:
                return result.content

    def call_api(self, path, **kwargs):
        return requests.get(
            f'http://{self.ip}/api/{path}/',
            json=json.dumps(kwargs),
        )

    def home(self):
        """
        机器人回零复位
        :return:
        """
        return self.call_api('home-robot')


class ScreenInfo:
    def __init__(self, phone: 'Phone'):
        self.phone = phone
        self.model = None

    @property
    def phone_model(self):
        if not self.model:
            model = self.phone.robot.call_func(
                self.phone.position, 'screen/phone_model'
            )
            self.model = model
        return self.model

    def current_app(self):
        """
        当前APP
        :return:
        """
        key = 'screen/current_app'
        return self.phone.robot.call_func(self.phone.position, key)

    def is_front(self):
        """
        agent是否在前台
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/is_front')

    def launch_app(self, app=None):
        """
        启动app
        :param app:
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/launch_app', app=app)

    def to_front(self):
        """
        打开agent
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/to_front')

    def set_volume(self, value=20):
        """
        设置音量
        :param value: 0-100
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/set_volume', value=value)

    def set_brightness(self, value=20):
        """
        设置亮度
        :param value: 0-100
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/set_brightness', value=value)

    def uninstall(self, app):
        """
        卸载app
        :param app:
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/uninstall', app=app)

    def generate_password(self, app):
        """
        为指定app生成一个密码, UI界面可以直接输入
        :param app:
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/generate_password', app=app)

    def apps(self, update=False):
        """
        列出所有app
        :param update:
        :return:
        """
        key = 'screen/apps'
        return self.phone.robot.call_func(self.phone.position, key)

    def recent_apps(self):
        """
        列出最近app
        :return:
        """
        key = 'screen/recent_apps'
        return self.phone.robot.call_func(self.phone.position, key)

    def wait_app(self, app, timeout=120):
        """
        等待app启动成功
        :param app:
        :param timeout:
        :return:
        """
        key = 'screen/wait_app'
        self.phone.robot.call_func(self.phone.position, key, app=app, timeout=timeout)

    def read_sms(self):
        """
        读取最近短信. MIUI可以读取验证码短信 但是需要给agent授权
        :return:
        """
        key = 'screen/read_sms'
        return self.phone.robot.call_func(self.phone.position, key)

    def phone_info(self, update=True):
        """
        手机信息
        :return:
        """
        key = 'self/to-json'
        return self.phone.robot.call_func(self.phone.position, key, update=update)

    def copy_clipboard(self):
        info = self.phone_info()
        return info['clipboard']

    def get_phone_text(self, local_only=False):
        """
        获取手机屏幕上的文字
        格式: [[[start_x, start_y, end_x, end_y], 文字, 可信度]]
        :param local_only: 是否使用缓存
        :return:
        """
        key = 'screen/get_phone_text'
        return self.phone.robot.call_func(self.phone.position, key, local_only=local_only)

    def has_texts(self, texts: list[str, re.Pattern], prev=False, ignore_case=True,
                  location: Union[ImgLocation, list[ImgLocation], ImgArea, list[ImgArea]] = ImgLocation.FULL,
                  contain=True):
        """
        屏幕里是否有这些词
        :param texts: str或者regex
        :param prev: update前的text还是现在的
        :param ignore_case: 忽略大小写
        :param location: ImgLocation 或者 ImgArea, 可以多个组合
        :param contain: 包含还是完全匹配
        :return:
        """
        if not isinstance(texts, list):
            texts = [texts]
        return self.phone.robot.call_func(
            self.phone.position, 'screen/has_texts', texts=list(map(str, texts)),
            location=location,
            contain=contain,
            prev=prev,
            ignore_case=ignore_case
        )

    def has_any_texts(self, texts: list[str, re.Pattern], prev=False, ignore_case=True,
                      location: Union[ImgLocation, list[ImgLocation], ImgArea, list[ImgArea]] = ImgLocation.FULL,
                      contain=True, k=1):
        """
        屏幕里是否至少有这些词中的一部分
        :param texts: str或者regex
        :param prev: update前的text还是现在的
        :param ignore_case: 忽略大小写
        :param location: ImgLocation 或者 ImgArea, 可以多个组合
        :param contain: 包含还是完全匹配
        :param k: 至少需要几个
        :return:
        """
        return self.phone.robot.call_func(
            self.phone.position, 'screen/has_any_texts',
            texts=list(map(str, texts)),
            location=location,
            contain=contain,
            prev=prev,
            ignore_case=ignore_case,
            k=k,
        )

    def count_texts(self, texts: Union[list[str, re.Pattern], Union[str, re.Pattern]], prev=False, ignore_case=True,
                    location: Union[ImgLocation, list[ImgLocation], ImgArea, list[ImgArea]] = ImgLocation.FULL,
                    contain=True):
        """
        文字计数
        :param texts: str或者regex
        :param prev: update前的text还是现在的
        :param ignore_case: 忽略大小写
        :param location: ImgLocation 或者 ImgArea, 可以多个组合 多个区域不重叠回返回0
        :param contain: 包含还是完全匹配
        :return:
        """
        if not isinstance(texts, list):
            texts = [texts]
        return self.phone.robot.call_func(
            self.phone.position, 'screen/count_texts',
            texts=list(map(str, texts)),
            location=location,
            contain=contain,
            prev=prev,
            ignore_case=ignore_case
        )

    def filter_texts(self, texts: Union[list[str, re.Pattern], Union[str, re.Pattern]], prev=False, ignore_case=True,
                     location: Union[ImgLocation, list[ImgLocation], ImgArea, list[ImgArea]] = ImgLocation.FULL,
                     contain=True, texts_list=None):
        """
        文字过滤, 只保留所给区域的文字
        多个区域不重叠回返回空列表

        :param texts: str或者regex
        :param prev: update前的text还是现在的
        :param ignore_case: 忽略大小写
        :param location: ImgLocation 或者 ImgArea, 可以多个组合 多个区域不重叠回返回空列表
        :param contain: 包含还是完全匹配
        :param texts_list: 传入已经获取的文字列表
        :return:
        """
        if not isinstance(texts, list):
            texts = [texts]
        return self.phone.robot.call_func(
            self.phone.position, 'screen/filter_texts',
            texts=list(map(str, texts)),
            location=location,
            contain=contain,
            prev=prev,
            ignore_case=ignore_case,
            texts_list=json.dumps(texts_list)
        )

    def update(self, text=True):
        """
        更新屏幕图像和文字
        :param text: 是否更新文字
        :return:
        """
        key = 'screen/update'
        return self.phone.robot.call_func(self.phone.position, key, text=text)

    def home(self):
        """
        机器人回零复位
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/home')

    @property
    def image_raw(self):
        """
        当前屏幕图片的bytes
        :return:
        """
        return self.phone.robot.call_func(self.phone.position, 'screen/image_raw')

    def app_stick(self, app_str: str):
        """
        UI中置顶或者取消置顶app
        :param app_str: app package name
        :return:
        """
        return self.phone.robot.call_func(
            self.phone.position, 'screen/app_stick', app_str=app_str)

    def enter_text(self, text: Union[TextAction, str]):
        """
        输入文字
        :param text: 文字或者TextAction
        :return:
        """
        if isinstance(text, TextAction):
            text = text.name
        return self.phone.robot.call_func(self.phone.position,
                                          'screen/enter_text', text=text
                                          )

    def get_chinese(self, k=8, prev=False, start: int = None):
        """
        :param k: 总计对比多少组词
        :param prev: call update前的文字
        :param start: 竖屏默认值是3, 忽略前三个词， 因为时间一直在变
        :return:
        """
        return self.phone.robot.call_func(
            self.phone.position,
            'screen/get_chinese', k=k, prev=prev, start=start
        )

    def chinese_changed(self, update=True, k=8, start: int = None):
        """
        对比call update 前后是否中文有改变
        :param update: 是否先update再对比, 如果已经call了update这里可以用False
        :param k: 总计对比多少组词
        :param start: 竖屏默认值是3, 忽略前三个词， 因为时间一直在变
        :return:
        """
        return self.phone.robot.call_func(
            self.phone.position,
            'screen/chinese_changed', update=update, k=k, start=start
        )

    def clear_folder(self, folder: str = "DCIM"):
        """
        清空指定文件夹 默认清空DCIM
        :param folder: default DCIM
        :return:
        """
        return self.phone.robot.call_func(
            self.phone.position,
            'screen/clear_folder', folder=folder
        )

    def clear_midea(self):
        for folder in ['DCIM', 'Pictures']:
            self.clear_folder(folder)

    def locate_image(
            self, template: Union[Path, bytes],
            image: Union[Path, bytes] = None,
            location: Union[ImgLocation, list[ImgLocation], ImgArea, list[ImgArea]] = ImgLocation.FULL,
            threshold=0.8
    ) -> list[TemplateLocation]:
        """
        图查图. 仅作为实验用途. 如果效果不完美, 可以自行使用其它库去实现.

        :param template: 被查找的模版路径或者bytes
        :param image: 默认查找当前手机画面, 也可以提供被查图的路径或bytes
        :param location: 只查找指定位置
        :param threshold: 特征点集合阈值 , 0-∞, 越小越严格, 越大越宽松
        :return:
        """

        def read_img(path):
            if not path:
                return path
            if isinstance(path, bytes):
                content = path
            else:
                with open(path, 'rb') as fin:
                    content = fin.read()
            return base64.b64encode(content).decode()

        template_content = read_img(template)
        img_content = read_img(image)

        res = self.phone.robot.call_func(
            self.phone.position,
            'screen/locate-image',
            template=template_content,
            image=img_content,
            location=location,
            threshold=threshold,
        )
        result = []
        for loc in res:
            result.append(TemplateLocation(**loc))
        return result

    def show_keyboard(self):
        """
        显示输入法键盘
        可以自行调用 enter_text(TextAction) 去实现其它功能
        :return:
        """
        return self.enter_text(TextAction.KEYCODE_MAIN_KEYBOARD)

    def hide_keyboard(self):
        """
        隐藏输入法键盘
        :return:
        """
        return self.enter_text(TextAction.KEYCODE_CLOSE)

    def waited_update(self, before=2, after=2):
        time.sleep(before)
        self.update()
        time.sleep(after)

    def is_input_on(self):
        return self.phone.robot.call_func(self.phone.position, 'screen/is_input_on')


class Phone:
    def __init__(
            self,
            position: int,
            robot: Robot,
            data: dict
    ):
        self.position = position
        self.robot = robot
        self.data = data
        self.screen = ScreenInfo(self)

    @property
    def image(self):
        """
        当前屏幕图片的bytes
        :return:
        """
        return self.robot.call_api(f'{self.position}.jpeg').content

    @property
    def calibrated(self) -> bool:
        """
        是否已经校准
        :return:
        """
        return self.robot.call_func(self.position, 'self/is-calibrated')

    def upload(self, file, name=None):
        """
        上传文件到手机
        :param file: 文件路径
        :param name: 自定义文件名, 需要包含扩展名!!
        :return:
        """
        with open(file, 'rb') as f:
            files = {'file': f if not name else (name, f)}
            url = f'http://{self.robot.ip}/api/upload/{self.position}/'
            res = requests.post(
                url, files=files,
                timeout=(1000, 1000)
            )
            logger.debug(res)

    def _page_changed(self, current_page: callable = None, next_page: callable = None,
                      **kwargs):
        if not callable(current_page) and not callable(next_page):
            return True
        self.screen.waited_update()
        if callable(current_page):
            current = current_page()
            if not current:
                return True
        if callable(next_page):
            next_ = next_page()
            if next_:
                return True

    def _checked_call(self, func: callable, current_page: callable,
                      next_page: callable, retry=3):
        for _ in range(retry):
            func()
            if self._page_changed(current_page, next_page):
                return True
        return False

    def touch(self, x: Union[int, float] = None, y: Union[int, float] = None, z: Union[int, float] = None,
              speed: Union[int, float] = None, raw=False, lift=True, delay=0,
              current_page: callable = None,
              next_page: callable = None,
              retry: int = 3,
              repeat: int = 0,
              repeat_delay: int = 0,
              **kwargs):
        """
        点击某个坐标
        可以利用当前页以及下一页的检测函数判断是否已经成功点击. 如果current_page()返回False或者next_page()返回True,则退出
        :param x: (0-1) 百分比, > 1 实际像素
        :param y: (0-1) 百分比, > 1 实际像素
        :param z: z高度. 除非知道如何使用 否则不建议使用
        :param speed: 移动速度
        :param raw: 用mm尺寸. 除非知道如何使用 否则不建议使用
        :param lift: 是否抬起
        :param delay: 抬起延迟
        :param next_page: 检查是否已经切换到下个页面
        :param current_page: 检查是否已经离开到当前页面
        :param retry: 页面无变化重试次数
        :param repeat: 重复点击次数
        :param repeat_delay: 重复点击延迟
        :param kwargs:
        :return:
        """
        return self._checked_call(
            lambda: self.robot.call_func(self.position, 'self/touch', x=x, y=y, z=z, speed=speed, raw=raw, lift=lift,
                                         delay=delay, repeat=repeat, repeat_delay=repeat_delay, **kwargs),
            current_page=current_page, next_page=next_page, retry=retry,
        )

    def drag(self, x1: Union[int, float] = None, y1: Union[int, float] = None, x2: Union[int, float] = None,
             y2: Union[int, float] = None, speed=55000, lift=True, raw=False, precise=False, delay=0.1,
             current_page: callable = None,
             next_page: callable = None,
             retry: int = 3,
             ):
        """

        :param x1: 起始X (0-1) 百分比, > 1 实际像素
        :param y1: 起始Y (0-1) 百分比, > 1 实际像素
        :param x2: 结束X (0-1) 百分比, > 1 实际像素
        :param y2: 结束Y (0-1) 百分比, > 1 实际像素
        :param speed: 移动速度
        :param lift: 是否抬起
        :param raw: 用mm尺寸. 除非知道如何使用 否则不建议使用
        :param precise: 精确还是不精确. 不精确: 会模拟真实滑屏时的加速抬起
        :param delay: 抬起延迟
        :param next_page: 检查是否已经切换到下个页面
        :param current_page: 检查是否已经离开到当前页面
        :param retry: 页面无变化重试次数
        :return:
        """

        return self._checked_call(
            lambda: self.robot.call_func(
                self.position, 'self/drag', x1=x1, y1=y1, x2=x2, y2=y2, speed=speed, lift=lift,
                raw=raw, precise=precise, delay=delay
            ),
            current_page=current_page, next_page=next_page, retry=retry
        )

    def swipe_up(self):
        """
        模拟人手随机向上滑屏
        :return:
        """
        return self.robot.call_func(self.position, 'self/swipe-up')

    def swipe_down(self):
        """
        模拟人手随机向下滑屏
        :return:
        """
        return self.robot.call_func(self.position, 'self/swipe-down')

    def swipe_right(self):
        """
        模拟人手随机向右滑屏
        :return:
        """
        return self.robot.call_func(self.position, 'self/swipe-right')

    def hold(self, x, y, seconds: Union[int, float] = 2):
        """
        长按
        :param x: (0-1) 百分比, > 1 实际像素
        :param y: (0-1) 百分比, > 1 实际像素
        :param seconds: 延迟时间
        :return:
        """
        return self.robot.call_func(self.position, 'self/hold', x=x, y=y, seconds=seconds)

    def swipe_left(self):
        """
        模拟人手随机向左滑屏
        :return:
        """
        return self.robot.call_func(self.position, 'self/swipe-left')

    def enter_tasks(self, clear=False):
        """
        打开任务列表
        :param clear: 是否清除所有任务
        :return:
        """
        return self.robot.call_func(self.position, 'self/enter_tasks', clear=clear)

    def back(self):
        """
        机器人回零复位
        :return:
        """
        return self.robot.call_func(self.position, 'self/back')

    def calibrate(self):
        """
        校准单个手机
        :return:
        """
        return self.robot.call_func(self.position, 'self/calibrate')

    def take_picture(self, move=True, wait=1.5, offset_x=0.0, offset_y=0.0,
                     extract=False, force_wait=True):
        """
        用相机拍照
        :param move: 是否移动的对应的拍照点
        :param wait: 等待时间
        :param offset_x: x轴偏移, 用于微调拍照位置 范围: (-30, 30) 单位: mm
        :param offset_y: y轴偏移, 用于微调拍照位置 范围: (-30, 30) 单位: mm
        :param extract: 是否提取图片文字
        :param force_wait: 是否强制等待, 如果设置为True, 则会等待wait时间后再拍照, 否则监测到机器人到达指定位置后就会立即拍照(可能有虚像),
        :return:
        """
        result = self.robot.call_func(
            self.position, 'self/take_picture', move=move, wait=wait, offset_x=offset_x,
            offset_y=offset_y,
            extract=extract,
            force_wait=force_wait
        )
        if result and 'image' in result:
            # cv2 读取图片 from bytes
            image = cv2.imdecode(np.frombuffer(base64.b64decode(result['image']), np.uint8), cv2.IMREAD_COLOR)
            texts = []
            if extract:
                try:
                    texts = json.loads(result['texts'])
                except:
                    pass
            return Photo(
                image,
                result['pos'][:2],
                result['ts'],
                texts,
                phone=self.position
            )

    def touch_text(self, text: Union[str, re.Pattern],
                   index=0,
                   location: Union[
                       ImgLocation, list[ImgLocation],
                       ImgArea, list[ImgArea]] = ImgLocation.FULL,
                   contain=True,
                   offset: tuple[float, float] = (0.0, 0.0), jitter_x=True,
                   current_page: callable = None,
                   next_page: callable = None,
                   retry: int = 3,
                   repeat=0,
                   repeat_delay=0,
                   ):
        """
        点击屏幕里的文字
        :param text: 需要点击的文字或者regex
        :param index: 点击第几个匹配的文字 默认第一个
        :param location: ImgLocation 或者 ImgArea, 可以多个组合去匹配想要匹配的区域
        :param contain: 包含还是完全匹配
        :param offset: 偏移, 比如想点击文字左边的按钮可以用 (-0.05, 0) UI界面鼠标放在手机屏幕上可以看比例. 原点是左上角, 向下Y+, 向右x+
        :param jitter_x: 是否左右随机一点
        :param next_page: 检查是否已经切换到下个页面
        :param current_page: 检查是否已经离开到当前页面
        :param retry: 页面无变化重试次数
        :param repeat: 重复点击次数
        :param repeat_delay: 重复点击间隔
        :return:
        """
        return self._checked_call(
            lambda: self.robot.call_func(
                self.position,
                'self/touch_text',
                text=str(text),
                index=index,
                location=location,
                contain=contain,
                offset=list(offset),
                jitter_x=jitter_x,
                repeat=repeat, repeat_delay=repeat_delay
            ),
            current_page=current_page, next_page=next_page, retry=retry,
        )

    def move(self, x: Union[int, float] = None, y: Union[int, float] = None, z: Union[int, float] = None,
             speed: Union[int, float] = None, raw=False):
        """

        :param x: X (0-1) 百分比, > 1 实际像素
        :param y: Y (0-1) 百分比, > 1 实际像素
        :param speed: 移动速度
        :param raw: 用mm尺寸. 除非知道如何使用 否则不建议使用
        :return:
        """
        return self.robot.call_func(
            self.position, 'self/move', x=x, y=y, z=z, speed=speed, raw=raw,
        )

    def touch_photo(self, x, y, photo: Photo, speed=None, repeat=0, repeat_delay=0):
        """
        点击图片
        :param x: (0-1) 百分比, > 1 实际像素
        :param y: (0-1) 百分比, > 1 实际像素
        :param photo: 需要点击的照片
        :param speed: 移动速度
        :param repeat: 重复点击次数
        :param repeat_delay: 重复点击间隔
        :return:
        """
        return self.robot.call_func(
            self.position, 'self/touch_photo',
            x=x, y=y, pos=photo.position, taken_by=photo.phone, speed=speed,
            repeat=repeat, repeat_delay=repeat_delay
        )

    def touch_photo_text(self, text, photo: Photo, speed=None, location: Union[
        ImgLocation, list[ImgLocation],
        ImgArea, list[ImgArea]] = ImgLocation.FULL, repeat=0, repeat_delay=0, index=0):
        """
        点击图片上的文字
        :param text: 需要点击的文字
        :param photo: 需要点击的照片
        :param speed: 移动速度
        :param location:
        :param repeat: 重复点击次数
        :param repeat_delay: 重复点击间隔
        :param index: 第几个文字
        :return:
        """
        filtered_texts = self.screen.filter_texts(texts=text, location=location, contain=True,
                                                  texts_list=photo.texts)
        if filtered_texts and len(filtered_texts) > index:
            return self.touch_photo(*filtered_texts[index], photo=photo,
                                    speed=speed, repeat=repeat, repeat_delay=repeat_delay)
        return False

    def drag_photo(
            self, x1, y1, x2, y2, photo: Photo, speed=None, lift=True, delay=0.1, lift_delay=0
    ):
        """
        拖动图片
        :param photo:
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param photo:
        :param speed:
        :param lift:
        :param delay:
        :param lift_delay:
        :return:
        """
        return self.robot.call_func(
            self.position, 'self/drag_photo',
            x1=x1, y1=y1, x2=x2, y2=y2, pos=photo.position, taken_by=photo.phone, speed=speed,
            lift=lift, delay=delay, lift_delay=lift_delay
        )
