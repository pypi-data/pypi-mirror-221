# coding: UTF-8
import sys
bstack11l_opy_ = sys.version_info [0] == 2
bstack1l1l_opy_ = 2048
bstack1lll_opy_ = 7
def bstack1l_opy_ (bstack1_opy_):
    global bstack1l1_opy_
    stringNr = ord (bstack1_opy_ [-1])
    bstack111_opy_ = bstack1_opy_ [:-1]
    bstack1ll_opy_ = stringNr % len (bstack111_opy_)
    bstack1ll1_opy_ = bstack111_opy_ [:bstack1ll_opy_] + bstack111_opy_ [bstack1ll_opy_:]
    if bstack11l_opy_:
        bstack11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l_opy_ - (bstackl_opy_ + stringNr) % bstack1lll_opy_) for bstackl_opy_, char in enumerate (bstack1ll1_opy_)])
    else:
        bstack11_opy_ = str () .join ([chr (ord (char) - bstack1l1l_opy_ - (bstackl_opy_ + stringNr) % bstack1lll_opy_) for bstackl_opy_, char in enumerate (bstack1ll1_opy_)])
    return eval (bstack11_opy_)
import atexit
import os
import signal
import sys
import time
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
from multiprocessing import Pool
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
bstack11111l11_opy_ = {
	bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧࠁ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡴࠪࠂ"),
  bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪࠃ"): bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡬ࡧࡼࠫࠄ"),
  bstack1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬࠅ"): bstack1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧࠆ"),
  bstack1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫࠇ"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬࠈ"),
  bstack1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫࠉ"): bstack1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࠨࠊ"),
  bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫࠋ"): bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࠨࠌ"),
  bstack1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࠍ"): bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩࠎ"),
  bstack1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫࠏ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪࠫࠐ"),
  bstack1l_opy_ (u"ࠧࡤࡱࡱࡷࡴࡲࡥࡍࡱࡪࡷࠬࠑ"): bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡷࡴࡲࡥࠨࠒ"),
  bstack1l_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࠧࠓ"): bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࠧࠔ"),
  bstack1l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨࠕ"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡐࡴ࡭ࡳࠨࠖ"),
  bstack1l_opy_ (u"࠭ࡶࡪࡦࡨࡳࠬࠗ"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡶࡪࡦࡨࡳࠬ࠘"),
  bstack1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧ࠙"): bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡏࡳ࡬ࡹࠧࠚ"),
  bstack1l_opy_ (u"ࠪࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪࠛ"): bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡲࡥ࡮ࡧࡷࡶࡾࡒ࡯ࡨࡵࠪࠜ"),
  bstack1l_opy_ (u"ࠬ࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪࠝ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡭ࡥࡰࡎࡲࡧࡦࡺࡩࡰࡰࠪࠞ"),
  bstack1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩࠟ"): bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵ࡫ࡰࡩࡿࡵ࡮ࡦࠩࠠ"),
  bstack1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࠡ"): bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬࠢ"),
  bstack1l_opy_ (u"ࠫࡲࡧࡳ࡬ࡅࡲࡱࡲࡧ࡮ࡥࡵࠪࠣ"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡲࡧࡳ࡬ࡅࡲࡱࡲࡧ࡮ࡥࡵࠪࠤ"),
  bstack1l_opy_ (u"࠭ࡩࡥ࡮ࡨࡘ࡮ࡳࡥࡰࡷࡷࠫࠥ"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡩࡥ࡮ࡨࡘ࡮ࡳࡥࡰࡷࡷࠫࠦ"),
  bstack1l_opy_ (u"ࠨ࡯ࡤࡷࡰࡈࡡࡴ࡫ࡦࡅࡺࡺࡨࠨࠧ"): bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡯ࡤࡷࡰࡈࡡࡴ࡫ࡦࡅࡺࡺࡨࠨࠨ"),
  bstack1l_opy_ (u"ࠪࡷࡪࡴࡤࡌࡧࡼࡷࠬࠩ"): bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡷࡪࡴࡤࡌࡧࡼࡷࠬࠪ"),
  bstack1l_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡥ࡮ࡺࠧࠫ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡵࡵࡱ࡚ࡥ࡮ࡺࠧࠬ"),
  bstack1l_opy_ (u"ࠧࡩࡱࡶࡸࡸ࠭࠭"): bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡩࡱࡶࡸࡸ࠭࠮"),
  bstack1l_opy_ (u"ࠩࡥࡪࡨࡧࡣࡩࡧࠪ࠯"): bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡪࡨࡧࡣࡩࡧࠪ࠰"),
  bstack1l_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸࠬ࠱"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸࠬ࠲"),
  bstack1l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡃࡰࡴࡶࡖࡪࡹࡴࡳ࡫ࡦࡸ࡮ࡵ࡮ࡴࠩ࠳"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡪࡵࡤࡦࡱ࡫ࡃࡰࡴࡶࡖࡪࡹࡴࡳ࡫ࡦࡸ࡮ࡵ࡮ࡴࠩ࠴"),
  bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ࠵"): bstack1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࠶"),
  bstack1l_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧ࠷"): bstack1l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡡࡰࡳࡧ࡯࡬ࡦࠩ࠸"),
  bstack1l_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ࠹"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡰࡱ࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࠺"),
  bstack1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡎࡦࡶࡺࡳࡷࡱࠧ࠻"): bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡷࡶࡸࡴࡳࡎࡦࡶࡺࡳࡷࡱࠧ࠼"),
  bstack1l_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡓࡶࡴ࡬ࡩ࡭ࡧࠪ࠽"): bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡱࡩࡹࡽ࡯ࡳ࡭ࡓࡶࡴ࡬ࡩ࡭ࡧࠪ࠾"),
  bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪ࠿"): bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭ࡀ"),
  bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨࡁ"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨࡂ"),
  bstack1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨࡃ"): bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡲࡹࡷࡩࡥࠨࡄ"),
  bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࡅ"): bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࡆ"),
  bstack1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧࡇ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧࡈ"),
}
bstack1l1llll11_opy_ = [
  bstack1l_opy_ (u"ࠧࡰࡵࠪࡉ"),
  bstack1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫࡊ"),
  bstack1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࡋ"),
  bstack1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨࡌ"),
  bstack1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨࡍ"),
  bstack1l_opy_ (u"ࠬࡸࡥࡢ࡮ࡐࡳࡧ࡯࡬ࡦࠩࡎ"),
  bstack1l_opy_ (u"࠭ࡡࡱࡲ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࡏ"),
]
bstack1l111ll11_opy_ = {
  bstack1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩࡐ"): [bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩࡑ"), bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡎࡂࡏࡈࠫࡒ")],
  bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ࡓ"): bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧࡔ"),
  bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨࡕ"): bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠩࡖ"),
  bstack1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬࡗ"): bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊ࠭ࡘ"),
  bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࡙ࠫ"): bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࡚ࠬ"),
  bstack1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰ࡛ࠫ"): bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡇࡒࡂࡎࡏࡉࡑ࡙࡟ࡑࡇࡕࡣࡕࡒࡁࡕࡈࡒࡖࡒ࠭࡜"),
  bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ࡝"): bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࠬ࡞"),
  bstack1l_opy_ (u"ࠨࡴࡨࡶࡺࡴࡔࡦࡵࡷࡷࠬ࡟"): bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ࡠ"),
  bstack1l_opy_ (u"ࠪࡥࡵࡶࠧࡡ"): [bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖ࡟ࡊࡆࠪࡢ"), bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡖࡐࠨࡣ")],
  bstack1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨࡤ"): bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞ࡥࡄࡆࡄࡘࡋࠬࡥ"),
  bstack1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬࡦ"): bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬࡧ")
}
bstack11111l_opy_ = {
  bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࡨ"): [bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ࡩ"), bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࡪ")],
  bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ࡫"): [bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡥ࡫ࡦࡻࠪ࡬"), bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ࡭")],
  bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ࡮"): bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ࡯"),
  bstack1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩࡰ"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩࡱ"),
  bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࡲ"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࡳ"),
  bstack1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨࡴ"): [bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡳࡴࠬࡵ"), bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩࡶ")],
  bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࡷ"): bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪࡸ"),
  bstack1l_opy_ (u"࠭ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪࡹ"): bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡲࡦࡴࡸࡲ࡙࡫ࡳࡵࡵࠪࡺ"),
  bstack1l_opy_ (u"ࠨࡣࡳࡴࠬࡻ"): bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴࠬࡼ"),
  bstack1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࡽ"): bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࡾ"),
  bstack1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩࡿ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩࢀ")
}
bstack1ll11111l_opy_ = {
  bstack1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࢁ"): bstack1l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬࢂ"),
  bstack1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࢃ"): [bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬࢄ"), bstack1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠧࢅ")],
  bstack1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪࢆ"): bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫࢇ"),
  bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ࢈"): bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨࢉ"),
  bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧࢊ"): [bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫࢋ"), bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪࢌ")],
  bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࢍ"): bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨࢎ"),
  bstack1l_opy_ (u"ࠧࡳࡧࡤࡰࡒࡵࡢࡪ࡮ࡨࠫ࢏"): bstack1l_opy_ (u"ࠨࡴࡨࡥࡱࡥ࡭ࡰࡤ࡬ࡰࡪ࠭࢐"),
  bstack1l_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ࢑"): [bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡴࡵ࡯ࡵ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠪ࢒"), bstack1l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࢓")],
  bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡎࡴࡳࡦࡥࡸࡶࡪࡉࡥࡳࡶࡶࠫ࢔"): [bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹࡹࠧ࢕"), bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡓࡴ࡮ࡆࡩࡷࡺࠧ࢖")]
}
bstack1ll111l11_opy_ = [
  bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࠧࢗ"),
  bstack1l_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬ࢘"),
  bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺ࢙ࠩ"),
  bstack1l_opy_ (u"ࠫࡸ࡫ࡴࡘ࡫ࡱࡨࡴࡽࡒࡦࡥࡷ࢚ࠫ"),
  bstack1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡲࡹࡹࡹ࢛ࠧ"),
  bstack1l_opy_ (u"࠭ࡳࡵࡴ࡬ࡧࡹࡌࡩ࡭ࡧࡌࡲࡹ࡫ࡲࡢࡥࡷࡥࡧ࡯࡬ࡪࡶࡼࠫ࢜"),
  bstack1l_opy_ (u"ࠧࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡓࡶࡴࡳࡰࡵࡄࡨ࡬ࡦࡼࡩࡰࡴࠪ࢝"),
  bstack1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭࢞"),
  bstack1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ࢟"),
  bstack1l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫࢠ"),
  bstack1l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪࢡ"),
  bstack1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ࢢ"),
]
bstack1lll1llll_opy_ = [
  bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪࢣ"),
  bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢤ"),
  bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢥ"),
  bstack1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩࢦ"),
  bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࢧ"),
  bstack1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ࢨ"),
  bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨࢩ"),
  bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪࢪ"),
  bstack1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪࢫ"),
  bstack1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢬ")
]
bstack111ll_opy_ = [
  bstack1l_opy_ (u"ࠩࡸࡴࡱࡵࡡࡥࡏࡨࡨ࡮ࡧࠧࢭ"),
  bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࢮ"),
  bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧࢯ"),
  bstack1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪࢰ"),
  bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࡔࡷ࡯࡯ࡳ࡫ࡷࡽࠬࢱ"),
  bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪࢲ"),
  bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡔࡢࡩࠪࢳ"),
  bstack1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧࢴ"),
  bstack1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬࢵ"),
  bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩࢶ"),
  bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ࢷ"),
  bstack1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬࢸ"),
  bstack1l_opy_ (u"ࠧࡰࡵࠪࢹ"),
  bstack1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫࢺ"),
  bstack1l_opy_ (u"ࠩ࡫ࡳࡸࡺࡳࠨࢻ"),
  bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯ࡘࡣ࡬ࡸࠬࢼ"),
  bstack1l_opy_ (u"ࠫࡷ࡫ࡧࡪࡱࡱࠫࢽ"),
  bstack1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡽࡳࡳ࡫ࠧࢾ"),
  bstack1l_opy_ (u"࠭࡭ࡢࡥ࡫࡭ࡳ࡫ࠧࢿ"),
  bstack1l_opy_ (u"ࠧࡳࡧࡶࡳࡱࡻࡴࡪࡱࡱࠫࣀ"),
  bstack1l_opy_ (u"ࠨ࡫ࡧࡰࡪ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ࣁ"),
  bstack1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡑࡵ࡭ࡪࡴࡴࡢࡶ࡬ࡳࡳ࠭ࣂ"),
  bstack1l_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࠩࣃ"),
  bstack1l_opy_ (u"ࠫࡳࡵࡐࡢࡩࡨࡐࡴࡧࡤࡕ࡫ࡰࡩࡴࡻࡴࠨࣄ"),
  bstack1l_opy_ (u"ࠬࡨࡦࡤࡣࡦ࡬ࡪ࠭ࣅ"),
  bstack1l_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬࣆ"),
  bstack1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫࣇ"),
  bstack1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡧࡱࡨࡐ࡫ࡹࡴࠩࣈ"),
  bstack1l_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭ࣉ"),
  bstack1l_opy_ (u"ࠪࡲࡴࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠧ࣊"),
  bstack1l_opy_ (u"ࠫࡨ࡮ࡥࡤ࡭ࡘࡖࡑ࠭࣋"),
  bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ࣌"),
  bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹࡉ࡯ࡰ࡭࡬ࡩࡸ࠭࣍"),
  bstack1l_opy_ (u"ࠧࡤࡣࡳࡸࡺࡸࡥࡄࡴࡤࡷ࡭࠭࣎"),
  bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩ࣏ࠬ"),
  bstack1l_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡘࡨࡶࡸ࡯࡯࡯࣐ࠩ"),
  bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡖࡦࡴࡶ࡭ࡴࡴ࣑ࠧ"),
  bstack1l_opy_ (u"ࠫࡳࡵࡂ࡭ࡣࡱ࡯ࡕࡵ࡬࡭࡫ࡱ࡫࣒ࠬ"),
  bstack1l_opy_ (u"ࠬࡳࡡࡴ࡭ࡖࡩࡳࡪࡋࡦࡻࡶ࣓ࠫ"),
  bstack1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡒ࡯ࡨࡵࠪࣔ"),
  bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡉࡥࠩࣕ"),
  bstack1l_opy_ (u"ࠨࡦࡨࡨ࡮ࡩࡡࡵࡧࡧࡈࡪࡼࡩࡤࡧࠪࣖ"),
  bstack1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡒࡤࡶࡦࡳࡳࠨࣗ"),
  bstack1l_opy_ (u"ࠪࡴ࡭ࡵ࡮ࡦࡐࡸࡱࡧ࡫ࡲࠨࣘ"),
  bstack1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࠩࣙ"),
  bstack1l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࡒࡴࡹ࡯࡯࡯ࡵࠪࣚ"),
  bstack1l_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫࣛ"),
  bstack1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧࣜ"),
  bstack1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡍࡱࡪࡷࠬࣝ"),
  bstack1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡄ࡬ࡳࡲ࡫ࡴࡳ࡫ࡦࠫࣞ"),
  bstack1l_opy_ (u"ࠪࡺ࡮ࡪࡥࡰࡘ࠵ࠫࣟ"),
  bstack1l_opy_ (u"ࠫࡲ࡯ࡤࡔࡧࡶࡷ࡮ࡵ࡮ࡊࡰࡶࡸࡦࡲ࡬ࡂࡲࡳࡷࠬ࣠"),
  bstack1l_opy_ (u"ࠬ࡫ࡳࡱࡴࡨࡷࡸࡵࡓࡦࡴࡹࡩࡷ࠭࣡"),
  bstack1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡍࡱࡪࡷࠬ࣢"),
  bstack1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡅࡧࡴࣣࠬ"),
  bstack1l_opy_ (u"ࠨࡶࡨࡰࡪࡳࡥࡵࡴࡼࡐࡴ࡭ࡳࠨࣤ"),
  bstack1l_opy_ (u"ࠩࡶࡽࡳࡩࡔࡪ࡯ࡨ࡛࡮ࡺࡨࡏࡖࡓࠫࣥ"),
  bstack1l_opy_ (u"ࠪ࡫ࡪࡵࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨࣦ"),
  bstack1l_opy_ (u"ࠫ࡬ࡶࡳࡍࡱࡦࡥࡹ࡯࡯࡯ࠩࣧ"),
  bstack1l_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡖࡲࡰࡨ࡬ࡰࡪ࠭ࣨ"),
  bstack1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰࣩ࠭"),
  bstack1l_opy_ (u"ࠧࡧࡱࡵࡧࡪࡉࡨࡢࡰࡪࡩࡏࡧࡲࠨ࣪"),
  bstack1l_opy_ (u"ࠨࡺࡰࡷࡏࡧࡲࠨ࣫"),
  bstack1l_opy_ (u"ࠩࡻࡱࡽࡐࡡࡳࠩ࣬"),
  bstack1l_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴ࣭ࠩ"),
  bstack1l_opy_ (u"ࠫࡲࡧࡳ࡬ࡄࡤࡷ࡮ࡩࡁࡶࡶ࡫࣮ࠫ"),
  bstack1l_opy_ (u"ࠬࡽࡳࡍࡱࡦࡥࡱ࡙ࡵࡱࡲࡲࡶࡹ࣯࠭"),
  bstack1l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡃࡰࡴࡶࡖࡪࡹࡴࡳ࡫ࡦࡸ࡮ࡵ࡮ࡴࣰࠩ"),
  bstack1l_opy_ (u"ࠧࡢࡲࡳ࡚ࡪࡸࡳࡪࡱࡱࣱࠫ"),
  bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡊࡰࡶࡩࡨࡻࡲࡦࡅࡨࡶࡹࡹࣲࠧ"),
  bstack1l_opy_ (u"ࠩࡵࡩࡸ࡯ࡧ࡯ࡃࡳࡴࠬࣳ"),
  bstack1l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳࡹࠧࣴ"),
  bstack1l_opy_ (u"ࠫࡨࡧ࡮ࡢࡴࡼࠫࣵ"),
  bstack1l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽࣶ࠭"),
  bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ࣷ"),
  bstack1l_opy_ (u"ࠧࡪࡧࠪࣸ"),
  bstack1l_opy_ (u"ࠨࡧࡧ࡫ࡪࣹ࠭"),
  bstack1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࣺࠩ"),
  bstack1l_opy_ (u"ࠪࡵࡺ࡫ࡵࡦࠩࣻ"),
  bstack1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ࣼ"),
  bstack1l_opy_ (u"ࠬࡧࡰࡱࡕࡷࡳࡷ࡫ࡃࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳ࠭ࣽ"),
  bstack1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡉࡡ࡮ࡧࡵࡥࡎࡳࡡࡨࡧࡌࡲ࡯࡫ࡣࡵ࡫ࡲࡲࠬࣾ"),
  bstack1l_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡊࡾࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪࣿ"),
  bstack1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡏ࡮ࡤ࡮ࡸࡨࡪࡎ࡯ࡴࡶࡶࠫऀ"),
  bstack1l_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡃࡳࡴࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ँ"),
  bstack1l_opy_ (u"ࠪࡶࡪࡹࡥࡳࡸࡨࡈࡪࡼࡩࡤࡧࠪं"),
  bstack1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫः"),
  bstack1l_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾࡹࠧऄ"),
  bstack1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡖࡡࡴࡵࡦࡳࡩ࡫ࠧअ"),
  bstack1l_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡉࡰࡵࡇࡩࡻ࡯ࡣࡦࡕࡨࡸࡹ࡯࡮ࡨࡵࠪआ"),
  bstack1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡷࡧ࡭ࡴࡏ࡮࡫ࡧࡦࡸ࡮ࡵ࡮ࠨइ"),
  bstack1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡃࡳࡴࡱ࡫ࡐࡢࡻࠪई"),
  bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫउ"),
  bstack1l_opy_ (u"ࠫࡼࡪࡩࡰࡕࡨࡶࡻ࡯ࡣࡦࠩऊ"),
  bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧऋ"),
  bstack1l_opy_ (u"࠭ࡰࡳࡧࡹࡩࡳࡺࡃࡳࡱࡶࡷࡘ࡯ࡴࡦࡖࡵࡥࡨࡱࡩ࡯ࡩࠪऌ"),
  bstack1l_opy_ (u"ࠧࡩ࡫ࡪ࡬ࡈࡵ࡮ࡵࡴࡤࡷࡹ࠭ऍ"),
  bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡑࡴࡨࡪࡪࡸࡥ࡯ࡥࡨࡷࠬऎ"),
  bstack1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡕ࡬ࡱࠬए"),
  bstack1l_opy_ (u"ࠪࡷ࡮ࡳࡏࡱࡶ࡬ࡳࡳࡹࠧऐ"),
  bstack1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡸࡨࡍࡔ࡙ࡁࡱࡲࡖࡩࡹࡺࡩ࡯ࡩࡶࡐࡴࡩࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠩऑ"),
  bstack1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧऒ"),
  bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨओ"),
  bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩऔ"),
  bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧक"),
  bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫख"),
  bstack1l_opy_ (u"ࠪࡴࡦ࡭ࡥࡍࡱࡤࡨࡘࡺࡲࡢࡶࡨ࡫ࡾ࠭ग"),
  bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪघ"),
  bstack1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡲࡹࡹࡹࠧङ"),
  bstack1l_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩच")
]
bstack11l1l1l1_opy_ = {
  bstack1l_opy_ (u"ࠧࡷࠩछ"): bstack1l_opy_ (u"ࠨࡸࠪज"),
  bstack1l_opy_ (u"ࠩࡩࠫझ"): bstack1l_opy_ (u"ࠪࡪࠬञ"),
  bstack1l_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪट"): bstack1l_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࠫठ"),
  bstack1l_opy_ (u"࠭࡯࡯࡮ࡼࡥࡺࡺ࡯࡮ࡣࡷࡩࠬड"): bstack1l_opy_ (u"ࠧࡰࡰ࡯ࡽࡆࡻࡴࡰ࡯ࡤࡸࡪ࠭ढ"),
  bstack1l_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬण"): bstack1l_opy_ (u"ࠩࡩࡳࡷࡩࡥ࡭ࡱࡦࡥࡱ࠭त"),
  bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡪࡲࡷࡹ࠭थ"): bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧद"),
  bstack1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡴࡴࡸࡴࠨध"): bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩन"),
  bstack1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡻࡳࡦࡴࠪऩ"): bstack1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫप"),
  bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬफ"): bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ब"),
  bstack1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬभ"): bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡊࡲࡷࡹ࠭म"),
  bstack1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧय"): bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡴࡸࡴࠨर"),
  bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩऱ"): bstack1l_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡕࡴࡧࡵࠫल"),
  bstack1l_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡶࡵࡨࡶࠬळ"): bstack1l_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡗࡶࡩࡷ࠭ऴ"),
  bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭व"): bstack1l_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼࡔࡦࡹࡳࠨश"),
  bstack1l_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩष"): bstack1l_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡖࡡࡴࡵࠪस"),
  bstack1l_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ह"): bstack1l_opy_ (u"ࠪࡦ࡮ࡴࡡࡳࡻࡳࡥࡹ࡮ࠧऺ"),
  bstack1l_opy_ (u"ࠫࡵࡧࡣࡧ࡫࡯ࡩࠬऻ"): bstack1l_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ़"),
  bstack1l_opy_ (u"࠭ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨऽ"): bstack1l_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪा"),
  bstack1l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫि"): bstack1l_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬी"),
  bstack1l_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫु"): bstack1l_opy_ (u"ࠫࡱࡵࡧࡧ࡫࡯ࡩࠬू"),
  bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧृ"): bstack1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨॄ"),
}
bstack11llll_opy_ = bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡹࡧ࠳࡭ࡻࡢࠨॅ")
bstack11ll1llll_opy_ = bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡪࡸࡦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠫॆ")
bstack11l1l1ll_opy_ = bstack1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲࡬ࡺࡨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡲࡪࡾࡴࡠࡪࡸࡦࡸ࠭े")
bstack1l1l1l11l_opy_ = {
  bstack1l_opy_ (u"ࠪࡧࡷ࡯ࡴࡪࡥࡤࡰࠬै"): 50,
  bstack1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪॉ"): 40,
  bstack1l_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ॊ"): 30,
  bstack1l_opy_ (u"࠭ࡩ࡯ࡨࡲࠫो"): 20,
  bstack1l_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ौ"): 10
}
bstack11ll111l_opy_ = bstack1l1l1l11l_opy_[bstack1l_opy_ (u"ࠨ࡫ࡱࡪࡴ्࠭")]
bstack11ll111l1_opy_ = bstack1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨॎ")
bstack11lll1l1l_opy_ = bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࠨॏ")
bstack11l1ll1ll_opy_ = bstack1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪॐ")
bstack1lll111ll_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫ॑")
bstack1l11ll1l_opy_ = [bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋ॒ࠧ"), bstack1l_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ॓")]
bstack1l11l11l1_opy_ = [bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ॔"), bstack1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫॕ")]
bstack11l1ll11_opy_ = [
  bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡎࡢ࡯ࡨࠫॖ"),
  bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ॗ"),
  bstack1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩक़"),
  bstack1l_opy_ (u"࠭࡮ࡦࡹࡆࡳࡲࡳࡡ࡯ࡦࡗ࡭ࡲ࡫࡯ࡶࡶࠪख़"),
  bstack1l_opy_ (u"ࠧࡢࡲࡳࠫग़"),
  bstack1l_opy_ (u"ࠨࡷࡧ࡭ࡩ࠭ज़"),
  bstack1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫड़"),
  bstack1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡧࠪढ़"),
  bstack1l_opy_ (u"ࠫࡴࡸࡩࡦࡰࡷࡥࡹ࡯࡯࡯ࠩफ़"),
  bstack1l_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡩࡧࡼࡩࡦࡹࠪय़"),
  bstack1l_opy_ (u"࠭࡮ࡰࡔࡨࡷࡪࡺࠧॠ"), bstack1l_opy_ (u"ࠧࡧࡷ࡯ࡰࡗ࡫ࡳࡦࡶࠪॡ"),
  bstack1l_opy_ (u"ࠨࡥ࡯ࡩࡦࡸࡓࡺࡵࡷࡩࡲࡌࡩ࡭ࡧࡶࠫॢ"),
  bstack1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡕ࡫ࡰ࡭ࡳ࡭ࡳࠨॣ"),
  bstack1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡓࡩࡷ࡬࡯ࡳ࡯ࡤࡲࡨ࡫ࡌࡰࡩࡪ࡭ࡳ࡭ࠧ।"),
  bstack1l_opy_ (u"ࠫࡴࡺࡨࡦࡴࡄࡴࡵࡹࠧ॥"),
  bstack1l_opy_ (u"ࠬࡶࡲࡪࡰࡷࡔࡦ࡭ࡥࡔࡱࡸࡶࡨ࡫ࡏ࡯ࡈ࡬ࡲࡩࡌࡡࡪ࡮ࡸࡶࡪ࠭०"),
  bstack1l_opy_ (u"࠭ࡡࡱࡲࡄࡧࡹ࡯ࡶࡪࡶࡼࠫ१"), bstack1l_opy_ (u"ࠧࡢࡲࡳࡔࡦࡩ࡫ࡢࡩࡨࠫ२"), bstack1l_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡃࡦࡸ࡮ࡼࡩࡵࡻࠪ३"), bstack1l_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡓࡥࡨࡱࡡࡨࡧࠪ४"), bstack1l_opy_ (u"ࠪࡥࡵࡶࡗࡢ࡫ࡷࡈࡺࡸࡡࡵ࡫ࡲࡲࠬ५"),
  bstack1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩ६"),
  bstack1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡪࡹࡴࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠩ७"),
  bstack1l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࠨ८"), bstack1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡄࡱࡹࡩࡷࡧࡧࡦࡇࡱࡨࡎࡴࡴࡦࡰࡷࠫ९"),
  bstack1l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡆࡨࡺ࡮ࡩࡥࡓࡧࡤࡨࡾ࡚ࡩ࡮ࡧࡲࡹࡹ࠭॰"),
  bstack1l_opy_ (u"ࠩࡤࡨࡧࡖ࡯ࡳࡶࠪॱ"),
  bstack1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡈࡪࡼࡩࡤࡧࡖࡳࡨࡱࡥࡵࠩॲ"),
  bstack1l_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰ࡙࡯࡭ࡦࡱࡸࡸࠬॳ"),
  bstack1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡏ࡮ࡴࡶࡤࡰࡱࡖࡡࡵࡪࠪॴ"),
  bstack1l_opy_ (u"࠭ࡡࡷࡦࠪॵ"), bstack1l_opy_ (u"ࠧࡢࡸࡧࡐࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪॶ"), bstack1l_opy_ (u"ࠨࡣࡹࡨࡗ࡫ࡡࡥࡻࡗ࡭ࡲ࡫࡯ࡶࡶࠪॷ"), bstack1l_opy_ (u"ࠩࡤࡺࡩࡇࡲࡨࡵࠪॸ"),
  bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡋࡦࡻࡶࡸࡴࡸࡥࠨॹ"), bstack1l_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡵࡪࠪॺ"), bstack1l_opy_ (u"ࠬࡱࡥࡺࡵࡷࡳࡷ࡫ࡐࡢࡵࡶࡻࡴࡸࡤࠨॻ"),
  bstack1l_opy_ (u"࠭࡫ࡦࡻࡄࡰ࡮ࡧࡳࠨॼ"), bstack1l_opy_ (u"ࠧ࡬ࡧࡼࡔࡦࡹࡳࡸࡱࡵࡨࠬॽ"),
  bstack1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡅࡹࡧࡦࡹࡹࡧࡢ࡭ࡧࠪॾ"), bstack1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡂࡴࡪࡷࠬॿ"), bstack1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࡉ࡯ࡲࠨঀ"), bstack1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡆ࡬ࡷࡵ࡭ࡦࡏࡤࡴࡵ࡯࡮ࡨࡈ࡬ࡰࡪ࠭ঁ"), bstack1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵ࡙ࡸ࡫ࡓࡺࡵࡷࡩࡲࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩং"),
  bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࠩঃ"), bstack1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡖ࡯ࡳࡶࡶࠫ঄"),
  bstack1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡄࡪࡵࡤࡦࡱ࡫ࡂࡶ࡫࡯ࡨࡈ࡮ࡥࡤ࡭ࠪঅ"),
  bstack1l_opy_ (u"ࠩࡤࡹࡹࡵࡗࡦࡤࡹ࡭ࡪࡽࡔࡪ࡯ࡨࡳࡺࡺࠧআ"),
  bstack1l_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡄࡧࡹ࡯࡯࡯ࠩই"), bstack1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡇࡦࡺࡥࡨࡱࡵࡽࠬঈ"), bstack1l_opy_ (u"ࠬ࡯࡮ࡵࡧࡱࡸࡋࡲࡡࡨࡵࠪউ"), bstack1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࡊࡰࡷࡩࡳࡺࡁࡳࡩࡸࡱࡪࡴࡴࡴࠩঊ"),
  bstack1l_opy_ (u"ࠧࡥࡱࡱࡸࡘࡺ࡯ࡱࡃࡳࡴࡔࡴࡒࡦࡵࡨࡸࠬঋ"),
  bstack1l_opy_ (u"ࠨࡷࡱ࡭ࡨࡵࡤࡦࡍࡨࡽࡧࡵࡡࡳࡦࠪঌ"), bstack1l_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡌࡧࡼࡦࡴࡧࡲࡥࠩ঍"),
  bstack1l_opy_ (u"ࠪࡲࡴ࡙ࡩࡨࡰࠪ঎"),
  bstack1l_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨ࡙ࡳ࡯࡭ࡱࡱࡵࡸࡦࡴࡴࡗ࡫ࡨࡻࡸ࠭এ"),
  bstack1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇ࡮ࡥࡴࡲ࡭ࡩ࡝ࡡࡵࡥ࡫ࡩࡷࡹࠧঐ"),
  bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭঑"),
  bstack1l_opy_ (u"ࠧࡳࡧࡦࡶࡪࡧࡴࡦࡅ࡫ࡶࡴࡳࡥࡅࡴ࡬ࡺࡪࡸࡓࡦࡵࡶ࡭ࡴࡴࡳࠨ঒"),
  bstack1l_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡘࡧࡥࡗࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧও"),
  bstack1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡖࡡࡵࡪࠪঔ"),
  bstack1l_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡗࡵ࡫ࡥࡥࠩক"),
  bstack1l_opy_ (u"ࠫ࡬ࡶࡳࡆࡰࡤࡦࡱ࡫ࡤࠨখ"),
  bstack1l_opy_ (u"ࠬ࡯ࡳࡉࡧࡤࡨࡱ࡫ࡳࡴࠩগ"),
  bstack1l_opy_ (u"࠭ࡡࡥࡤࡈࡼࡪࡩࡔࡪ࡯ࡨࡳࡺࡺࠧঘ"),
  bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ঙ"),
  bstack1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡊࡥࡷ࡫ࡦࡩࡎࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠬচ"),
  bstack1l_opy_ (u"ࠩࡤࡹࡹࡵࡇࡳࡣࡱࡸࡕ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠩছ"),
  bstack1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡒࡦࡺࡵࡳࡣ࡯ࡓࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨজ"),
  bstack1l_opy_ (u"ࠫࡸࡿࡳࡵࡧࡰࡔࡴࡸࡴࠨঝ"),
  bstack1l_opy_ (u"ࠬࡸࡥ࡮ࡱࡷࡩࡆࡪࡢࡉࡱࡶࡸࠬঞ"),
  bstack1l_opy_ (u"࠭ࡳ࡬࡫ࡳ࡙ࡳࡲ࡯ࡤ࡭ࠪট"), bstack1l_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡔࡺࡲࡨࠫঠ"), bstack1l_opy_ (u"ࠨࡷࡱࡰࡴࡩ࡫ࡌࡧࡼࠫড"),
  bstack1l_opy_ (u"ࠩࡤࡹࡹࡵࡌࡢࡷࡱࡧ࡭࠭ঢ"),
  bstack1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡍࡱࡪࡧࡦࡺࡃࡢࡲࡷࡹࡷ࡫ࠧণ"),
  bstack1l_opy_ (u"ࠫࡺࡴࡩ࡯ࡵࡷࡥࡱࡲࡏࡵࡪࡨࡶࡕࡧࡣ࡬ࡣࡪࡩࡸ࠭ত"),
  bstack1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪ࡝ࡩ࡯ࡦࡲࡻࡆࡴࡩ࡮ࡣࡷ࡭ࡴࡴࠧথ"),
  bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨ࡙ࡵ࡯࡭ࡵ࡙ࡩࡷࡹࡩࡰࡰࠪদ"),
  bstack1l_opy_ (u"ࠧࡦࡰࡩࡳࡷࡩࡥࡂࡲࡳࡍࡳࡹࡴࡢ࡮࡯ࠫধ"),
  bstack1l_opy_ (u"ࠨࡧࡱࡷࡺࡸࡥࡘࡧࡥࡺ࡮࡫ࡷࡴࡊࡤࡺࡪࡖࡡࡨࡧࡶࠫন"), bstack1l_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࡇࡩࡻࡺ࡯ࡰ࡮ࡶࡔࡴࡸࡴࠨ঩"), bstack1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧ࡚ࡩࡧࡼࡩࡦࡹࡇࡩࡹࡧࡩ࡭ࡵࡆࡳࡱࡲࡥࡤࡶ࡬ࡳࡳ࠭প"),
  bstack1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡵࡶࡳࡄࡣࡦ࡬ࡪࡒࡩ࡮࡫ࡷࠫফ"),
  bstack1l_opy_ (u"ࠬࡩࡡ࡭ࡧࡱࡨࡦࡸࡆࡰࡴࡰࡥࡹ࠭ব"),
  bstack1l_opy_ (u"࠭ࡢࡶࡰࡧࡰࡪࡏࡤࠨভ"),
  bstack1l_opy_ (u"ࠧ࡭ࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧম"),
  bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡉࡳࡧࡢ࡭ࡧࡧࠫয"), bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࡗࡪࡸࡶࡪࡥࡨࡷࡆࡻࡴࡩࡱࡵ࡭ࡿ࡫ࡤࠨর"),
  bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯ࡂࡥࡦࡩࡵࡺࡁ࡭ࡧࡵࡸࡸ࠭঱"), bstack1l_opy_ (u"ࠫࡦࡻࡴࡰࡆ࡬ࡷࡲ࡯ࡳࡴࡃ࡯ࡩࡷࡺࡳࠨল"),
  bstack1l_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩࡎࡴࡳࡵࡴࡸࡱࡪࡴࡴࡴࡎ࡬ࡦࠬ঳"),
  bstack1l_opy_ (u"࠭࡮ࡢࡶ࡬ࡺࡪ࡝ࡥࡣࡖࡤࡴࠬ঴"),
  bstack1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡉ࡯࡫ࡷ࡭ࡦࡲࡕࡳ࡮ࠪ঵"), bstack1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡂ࡮࡯ࡳࡼࡖ࡯ࡱࡷࡳࡷࠬশ"), bstack1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡋࡪࡲࡴࡸࡥࡇࡴࡤࡹࡩ࡝ࡡࡳࡰ࡬ࡲ࡬࠭ষ"), bstack1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡒࡴࡪࡴࡌࡪࡰ࡮ࡷࡎࡴࡂࡢࡥ࡮࡫ࡷࡵࡵ࡯ࡦࠪস"),
  bstack1l_opy_ (u"ࠫࡰ࡫ࡥࡱࡍࡨࡽࡈ࡮ࡡࡪࡰࡶࠫহ"),
  bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯࡭ࡿࡧࡢ࡭ࡧࡖࡸࡷ࡯࡮ࡨࡵࡇ࡭ࡷ࠭঺"),
  bstack1l_opy_ (u"࠭ࡰࡳࡱࡦࡩࡸࡹࡁࡳࡩࡸࡱࡪࡴࡴࡴࠩ঻"),
  bstack1l_opy_ (u"ࠧࡪࡰࡷࡩࡷࡑࡥࡺࡆࡨࡰࡦࡿ়ࠧ"),
  bstack1l_opy_ (u"ࠨࡵ࡫ࡳࡼࡏࡏࡔࡎࡲ࡫ࠬঽ"),
  bstack1l_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡖࡸࡷࡧࡴࡦࡩࡼࠫা"),
  bstack1l_opy_ (u"ࠪࡻࡪࡨ࡫ࡪࡶࡕࡩࡸࡶ࡯࡯ࡵࡨࡘ࡮ࡳࡥࡰࡷࡷࠫি"), bstack1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡘࡣ࡬ࡸ࡙࡯࡭ࡦࡱࡸࡸࠬী"),
  bstack1l_opy_ (u"ࠬࡸࡥ࡮ࡱࡷࡩࡉ࡫ࡢࡶࡩࡓࡶࡴࡾࡹࠨু"),
  bstack1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡇࡳࡺࡰࡦࡉࡽ࡫ࡣࡶࡶࡨࡊࡷࡵ࡭ࡉࡶࡷࡴࡸ࠭ূ"),
  bstack1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡑࡵࡧࡄࡣࡳࡸࡺࡸࡥࠨৃ"),
  bstack1l_opy_ (u"ࠨࡹࡨࡦࡰ࡯ࡴࡅࡧࡥࡹ࡬ࡖࡲࡰࡺࡼࡔࡴࡸࡴࠨৄ"),
  bstack1l_opy_ (u"ࠩࡩࡹࡱࡲࡃࡰࡰࡷࡩࡽࡺࡌࡪࡵࡷࠫ৅"),
  bstack1l_opy_ (u"ࠪࡻࡦ࡯ࡴࡇࡱࡵࡅࡵࡶࡓࡤࡴ࡬ࡴࡹ࠭৆"),
  bstack1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࡈࡵ࡮࡯ࡧࡦࡸࡗ࡫ࡴࡳ࡫ࡨࡷࠬে"),
  bstack1l_opy_ (u"ࠬࡧࡰࡱࡐࡤࡱࡪ࠭ৈ"),
  bstack1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡓࡍࡅࡨࡶࡹ࠭৉"),
  bstack1l_opy_ (u"ࠧࡵࡣࡳ࡛࡮ࡺࡨࡔࡪࡲࡶࡹࡖࡲࡦࡵࡶࡈࡺࡸࡡࡵ࡫ࡲࡲࠬ৊"),
  bstack1l_opy_ (u"ࠨࡵࡦࡥࡱ࡫ࡆࡢࡥࡷࡳࡷ࠭ো"),
  bstack1l_opy_ (u"ࠩࡺࡨࡦࡒ࡯ࡤࡣ࡯ࡔࡴࡸࡴࠨৌ"),
  bstack1l_opy_ (u"ࠪࡷ࡭ࡵࡷ࡙ࡥࡲࡨࡪࡒ࡯ࡨ্ࠩ"),
  bstack1l_opy_ (u"ࠫ࡮ࡵࡳࡊࡰࡶࡸࡦࡲ࡬ࡑࡣࡸࡷࡪ࠭ৎ"),
  bstack1l_opy_ (u"ࠬࡾࡣࡰࡦࡨࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠧ৏"),
  bstack1l_opy_ (u"࠭࡫ࡦࡻࡦ࡬ࡦ࡯࡮ࡑࡣࡶࡷࡼࡵࡲࡥࠩ৐"),
  bstack1l_opy_ (u"ࠧࡶࡵࡨࡔࡷ࡫ࡢࡶ࡫࡯ࡸ࡜ࡊࡁࠨ৑"),
  bstack1l_opy_ (u"ࠨࡲࡵࡩࡻ࡫࡮ࡵ࡙ࡇࡅࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠩ৒"),
  bstack1l_opy_ (u"ࠩࡺࡩࡧࡊࡲࡪࡸࡨࡶࡆ࡭ࡥ࡯ࡶࡘࡶࡱ࠭৓"),
  bstack1l_opy_ (u"ࠪ࡯ࡪࡿࡣࡩࡣ࡬ࡲࡕࡧࡴࡩࠩ৔"),
  bstack1l_opy_ (u"ࠫࡺࡹࡥࡏࡧࡺ࡛ࡉࡇࠧ৕"),
  bstack1l_opy_ (u"ࠬࡽࡤࡢࡎࡤࡹࡳࡩࡨࡕ࡫ࡰࡩࡴࡻࡴࠨ৖"), bstack1l_opy_ (u"࠭ࡷࡥࡣࡆࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ৗ"),
  bstack1l_opy_ (u"ࠧࡹࡥࡲࡨࡪࡕࡲࡨࡋࡧࠫ৘"), bstack1l_opy_ (u"ࠨࡺࡦࡳࡩ࡫ࡓࡪࡩࡱ࡭ࡳ࡭ࡉࡥࠩ৙"),
  bstack1l_opy_ (u"ࠩࡸࡴࡩࡧࡴࡦࡦ࡚ࡈࡆࡈࡵ࡯ࡦ࡯ࡩࡎࡪࠧ৚"),
  bstack1l_opy_ (u"ࠪࡶࡪࡹࡥࡵࡑࡱࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡲࡵࡑࡱࡰࡾ࠭৛"),
  bstack1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨ࡙࡯࡭ࡦࡱࡸࡸࡸ࠭ড়"),
  bstack1l_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷ࡯ࡥࡴࠩঢ়"), bstack1l_opy_ (u"࠭ࡷࡥࡣࡖࡸࡦࡸࡴࡶࡲࡕࡩࡹࡸࡹࡊࡰࡷࡩࡷࡼࡡ࡭ࠩ৞"),
  bstack1l_opy_ (u"ࠧࡤࡱࡱࡲࡪࡩࡴࡉࡣࡵࡨࡼࡧࡲࡦࡍࡨࡽࡧࡵࡡࡳࡦࠪয়"),
  bstack1l_opy_ (u"ࠨ࡯ࡤࡼ࡙ࡿࡰࡪࡰࡪࡊࡷ࡫ࡱࡶࡧࡱࡧࡾ࠭ৠ"),
  bstack1l_opy_ (u"ࠩࡶ࡭ࡲࡶ࡬ࡦࡋࡶ࡚࡮ࡹࡩࡣ࡮ࡨࡇ࡭࡫ࡣ࡬ࠩৡ"),
  bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡃࡢࡴࡷ࡬ࡦ࡭ࡥࡔࡵ࡯ࠫৢ"),
  bstack1l_opy_ (u"ࠫࡸ࡮࡯ࡶ࡮ࡧ࡙ࡸ࡫ࡓࡪࡰࡪࡰࡪࡺ࡯࡯ࡖࡨࡷࡹࡓࡡ࡯ࡣࡪࡩࡷ࠭ৣ"),
  bstack1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡍ࡜ࡊࡐࠨ৤"),
  bstack1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻ࡙ࡵࡵࡤࡪࡌࡨࡊࡴࡲࡰ࡮࡯ࠫ৥"),
  bstack1l_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࡈࡪࡦࡧࡩࡳࡇࡰࡪࡒࡲࡰ࡮ࡩࡹࡆࡴࡵࡳࡷ࠭০"),
  bstack1l_opy_ (u"ࠨ࡯ࡲࡧࡰࡒ࡯ࡤࡣࡷ࡭ࡴࡴࡁࡱࡲࠪ১"),
  bstack1l_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈࡲࡶࡲࡧࡴࠨ২"), bstack1l_opy_ (u"ࠪࡰࡴ࡭ࡣࡢࡶࡉ࡭ࡱࡺࡥࡳࡕࡳࡩࡨࡹࠧ৩"),
  bstack1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡇࡩࡱࡧࡹࡂࡦࡥࠫ৪")
]
bstack1l11llll_opy_ = bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡺࡶ࡬ࡰࡣࡧࠫ৫")
bstack11ll1l1l_opy_ = [bstack1l_opy_ (u"࠭࠮ࡢࡲ࡮ࠫ৬"), bstack1l_opy_ (u"ࠧ࠯ࡣࡤࡦࠬ৭"), bstack1l_opy_ (u"ࠨ࠰࡬ࡴࡦ࠭৮")]
bstack1ll1l1l1l_opy_ = [bstack1l_opy_ (u"ࠩ࡬ࡨࠬ৯"), bstack1l_opy_ (u"ࠪࡴࡦࡺࡨࠨৰ"), bstack1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧৱ"), bstack1l_opy_ (u"ࠬࡹࡨࡢࡴࡨࡥࡧࡲࡥࡠ࡫ࡧࠫ৲")]
bstack1111_opy_ = {
  bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭৳"): bstack1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ৴"),
  bstack1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩ৵"): bstack1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ৶"),
  bstack1l_opy_ (u"ࠪࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ৷"): bstack1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬ৸"),
  bstack1l_opy_ (u"ࠬ࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ৹"): bstack1l_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ৺"),
  bstack1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡏࡱࡶ࡬ࡳࡳࡹࠧ৻"): bstack1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩৼ")
}
bstack11ll1l_opy_ = [
  bstack1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ৽"),
  bstack1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨ৾"),
  bstack1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬ৿"),
  bstack1l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ਀"),
  bstack1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧਁ"),
]
bstack11l11ll1_opy_ = bstack1lll1llll_opy_ + bstack111ll_opy_ + bstack11l1ll11_opy_
bstack1l11lll11_opy_ = [
  bstack1l_opy_ (u"ࠧ࡟࡮ࡲࡧࡦࡲࡨࡰࡵࡷࠨࠬਂ"),
  bstack1l_opy_ (u"ࠨࡠࡥࡷ࠲ࡲ࡯ࡤࡣ࡯࠲ࡨࡵ࡭ࠥࠩਃ"),
  bstack1l_opy_ (u"ࠩࡡ࠵࠷࠽࠮ࠨ਄"),
  bstack1l_opy_ (u"ࠪࡢ࠶࠶࠮ࠨਅ"),
  bstack1l_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠴࡟࠻࠳࠹࡞࠰ࠪਆ"),
  bstack1l_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠶ࡠ࠶࠭࠺࡟࠱ࠫਇ"),
  bstack1l_opy_ (u"࠭࡞࠲࠹࠵࠲࠸ࡡ࠰࠮࠳ࡠ࠲ࠬਈ"),
  bstack1l_opy_ (u"ࠧ࡟࠳࠼࠶࠳࠷࠶࠹࠰ࠪਉ")
]
bstack1l1llll1l_opy_ = bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁࠬਊ")
bstack11l11l_opy_ = bstack1l_opy_ (u"ࠩࡶࡨࡰ࠵ࡶ࠲࠱ࡨࡺࡪࡴࡴࠨ਋")
bstack111111l1_opy_ = [ bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ਌") ]
bstack111ll1ll_opy_ = [ bstack1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪ਍") ]
bstack1lll111l_opy_ = [ bstack1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ਎") ]
bstack11llll1_opy_ = bstack1l_opy_ (u"࠭ࡓࡅࡍࡖࡩࡹࡻࡰࠨਏ")
bstack111l11l1_opy_ = bstack1l_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡂࡶࡷࡩࡲࡶࡴࡦࡦࠪਐ")
bstack1l1111ll_opy_ = bstack1l_opy_ (u"ࠨࡕࡇࡏ࡙࡫ࡳࡵࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠬ਑")
bstack11l111ll_opy_ = bstack1l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࠨ਒")
bstack1ll111l1l_opy_ = [
  bstack1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡇࡃࡌࡐࡊࡊࠧਓ"),
  bstack1l_opy_ (u"ࠫࡊࡘࡒࡠࡖࡌࡑࡊࡊ࡟ࡐࡗࡗࠫਔ"),
  bstack1l_opy_ (u"ࠬࡋࡒࡓࡡࡅࡐࡔࡉࡋࡆࡆࡢࡆ࡞ࡥࡃࡍࡋࡈࡒ࡙࠭ਕ"),
  bstack1l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡊ࡚ࡗࡐࡔࡎࡣࡈࡎࡁࡏࡉࡈࡈࠬਖ"),
  bstack1l_opy_ (u"ࠧࡆࡔࡕࡣࡘࡕࡃࡌࡇࡗࡣࡓࡕࡔࡠࡅࡒࡒࡓࡋࡃࡕࡇࡇࠫਗ"),
  bstack1l_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡆࡐࡔ࡙ࡅࡅࠩਘ"),
  bstack1l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊ࡙ࡅࡕࠩਙ"),
  bstack1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡗࡋࡆࡖࡕࡈࡈࠬਚ"),
  bstack1l_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡇࡂࡐࡔࡗࡉࡉ࠭ਛ"),
  bstack1l_opy_ (u"ࠬࡋࡒࡓࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ਜ"),
  bstack1l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧਝ"),
  bstack1l_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤࡏࡎࡗࡃࡏࡍࡉ࠭ਞ"),
  bstack1l_opy_ (u"ࠨࡇࡕࡖࡤࡇࡄࡅࡔࡈࡗࡘࡥࡕࡏࡔࡈࡅࡈࡎࡁࡃࡎࡈࠫਟ"),
  bstack1l_opy_ (u"ࠩࡈࡖࡗࡥࡔࡖࡐࡑࡉࡑࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪਠ"),
  bstack1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣ࡙ࡏࡍࡆࡆࡢࡓ࡚࡚ࠧਡ"),
  bstack1l_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡋࡇࡉࡍࡇࡇࠫਢ"),
  bstack1l_opy_ (u"ࠬࡋࡒࡓࡡࡖࡓࡈࡑࡓࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡎࡏࡔࡖࡢ࡙ࡓࡘࡅࡂࡅࡋࡅࡇࡒࡅࠨਣ"),
  bstack1l_opy_ (u"࠭ࡅࡓࡔࡢࡔࡗࡕࡘ࡚ࡡࡆࡓࡓࡔࡅࡄࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ਤ"),
  bstack1l_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡑࡓ࡙ࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࠨਥ"),
  bstack1l_opy_ (u"ࠨࡇࡕࡖࡤࡔࡁࡎࡇࡢࡖࡊ࡙ࡏࡍࡗࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧਦ"),
  bstack1l_opy_ (u"ࠩࡈࡖࡗࡥࡍࡂࡐࡇࡅ࡙ࡕࡒ࡚ࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠࡈࡄࡍࡑࡋࡄࠨਧ"),
]
bstack1l11l11ll_opy_ = bstack1l_opy_ (u"ࠪ࠲࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡦࡸࡴࡪࡨࡤࡧࡹࡹ࠯ࠨਨ")
def bstack1l1l1l_opy_():
  global CONFIG
  headers = {
        bstack1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ਩"): bstack1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨਪ"),
      }
  proxies = bstack1l1l11ll1_opy_(CONFIG, bstack11l1l1ll_opy_)
  try:
    response = requests.get(bstack11l1l1ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack111ll1l_opy_ = response.json()[bstack1l_opy_ (u"࠭ࡨࡶࡤࡶࠫਫ")]
      logger.debug(bstack1lll1ll1l_opy_.format(response.json()))
      return bstack111ll1l_opy_
    else:
      logger.debug(bstack11l1ll1l1_opy_.format(bstack1l_opy_ (u"ࠢࡓࡧࡶࡴࡴࡴࡳࡦࠢࡍࡗࡔࡔࠠࡱࡣࡵࡷࡪࠦࡥࡳࡴࡲࡶࠥࠨਬ")))
  except Exception as e:
    logger.debug(bstack11l1ll1l1_opy_.format(e))
def bstack1l11lll_opy_(hub_url):
  global CONFIG
  url = bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥਭ")+  hub_url + bstack1l_opy_ (u"ࠤ࠲ࡧ࡭࡫ࡣ࡬ࠤਮ")
  headers = {
        bstack1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਯ"): bstack1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਰ"),
      }
  proxies = bstack1l1l11ll1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l111ll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1l11l1_opy_.format(hub_url, e))
def bstack111l1111_opy_():
  try:
    global bstack1l1lllll_opy_
    bstack111ll1l_opy_ = bstack1l1l1l_opy_()
    bstack1l111l_opy_ = []
    results = []
    for bstack1lllll111_opy_ in bstack111ll1l_opy_:
      bstack1l111l_opy_.append(bstack11llll11_opy_(target=bstack1l11lll_opy_,args=(bstack1lllll111_opy_,)))
    for t in bstack1l111l_opy_:
      t.start()
    for t in bstack1l111l_opy_:
      results.append(t.join())
    bstack11lllll1_opy_ = {}
    for item in results:
      hub_url = item[bstack1l_opy_ (u"ࠬ࡮ࡵࡣࡡࡸࡶࡱ࠭਱")]
      latency = item[bstack1l_opy_ (u"࠭࡬ࡢࡶࡨࡲࡨࡿࠧਲ")]
      bstack11lllll1_opy_[hub_url] = latency
    bstack11111l1l_opy_ = min(bstack11lllll1_opy_, key= lambda x: bstack11lllll1_opy_[x])
    bstack1l1lllll_opy_ = bstack11111l1l_opy_
    logger.debug(bstack11llllll1_opy_.format(bstack11111l1l_opy_))
  except Exception as e:
    logger.debug(bstack1111ll1l_opy_.format(e))
bstack1l11l1l11_opy_ = bstack1l_opy_ (u"ࠧࡔࡧࡷࡸ࡮ࡴࡧࠡࡷࡳࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠽ࠤࢀࢃࠧਲ਼")
bstack1l111lll1_opy_ = bstack1l_opy_ (u"ࠨࡅࡲࡱࡵࡲࡥࡵࡧࡧࠤࡸ࡫ࡴࡶࡲࠤࠫ਴")
bstack1l111l11_opy_ = bstack1l_opy_ (u"ࠩࡓࡥࡷࡹࡥࡥࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫਵ")
bstack1ll1l1ll_opy_ = bstack1l_opy_ (u"ࠪࡗࡦࡴࡩࡵ࡫ࡽࡩࡩࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨਸ਼")
bstack11l1l11ll_opy_ = bstack1l_opy_ (u"࡚ࠫࡹࡩ࡯ࡩࠣ࡬ࡺࡨࠠࡶࡴ࡯࠾ࠥࢁࡽࠨ਷")
bstack111ll11_opy_ = bstack1l_opy_ (u"࡙ࠬࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࡾࢁࠬਸ")
bstack11lll1l11_opy_ = bstack1l_opy_ (u"࠭ࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡ࡫ࡱࡸࡪࡸࡲࡶࡲࡷ࠰ࠥ࡫ࡸࡪࡶ࡬ࡲ࡬࠭ਹ")
bstack1ll1lll_opy_ = bstack1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡵࡨࡰࡪࡴࡩࡶ࡯ࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࡤࠬ਺")
bstack1l1l1l11_opy_ = bstack1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡤࡲࡩࠦࡰࡺࡶࡨࡷࡹ࠳ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡲࡤࡧࡰࡧࡧࡦࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶࠣࡴࡾࡺࡥࡴࡶ࠰ࡷࡪࡲࡥ࡯࡫ࡸࡱࡥ࠭਻")
bstack11111l1_opy_ = bstack1l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵ࠮ࠣࡴࡦࡨ࡯ࡵࠢࡤࡲࡩࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࡭࡫ࡥࡶࡦࡸࡹࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡸࡴࠦࡲࡶࡰࠣࡶࡴࡨ࡯ࡵࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࡵࡧࡲࡢ࡮࡯ࡩࡱ࠴ࠠࡡࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡲࡰࡤࡲࡸ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡲࡤࡦࡴࡺࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡵࡨࡰࡪࡴࡩࡶ࡯࡯࡭ࡧࡸࡡࡳࡻࡣ਼ࠫ")
bstack1l11111_opy_ = bstack1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡦࡪ࡮ࡡࡷࡧࡣࠫ਽")
bstack11l111ll1_opy_ = bstack1l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡧࡰࡱ࡫ࡸࡱ࠲ࡩ࡬ࡪࡧࡱࡸࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶ࠲ࠥࡦࡰࡪࡲࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡆࡶࡰࡪࡷࡰ࠱ࡕࡿࡴࡩࡱࡱ࠱ࡈࡲࡩࡦࡰࡷࡤࠬਾ")
bstack1lll111l1_opy_ = bstack1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡦࠧਿ")
bstack1lll1l11l_opy_ = bstack1l_opy_ (u"࠭ࡃࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡩ࡭ࡳࡪࠠࡦ࡫ࡷ࡬ࡪࡸࠠࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡲࡶࠥࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳ࠯ࠢࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡹࡧ࡬࡭ࠢࡷ࡬ࡪࠦࡲࡦ࡮ࡨࡺࡦࡴࡴࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡹࡸ࡯࡮ࡨࠢࡳ࡭ࡵࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷ࠳࠭ੀ")
bstack1lll11l1l_opy_ = bstack1l_opy_ (u"ࠧࡉࡣࡱࡨࡱ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡱࡵࡳࡦࠩੁ")
bstack1llllll1_opy_ = bstack1l_opy_ (u"ࠨࡃ࡯ࡰࠥࡪ࡯࡯ࡧࠤࠫੂ")
bstack111l11_opy_ = bstack1l_opy_ (u"ࠩࡆࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࠡࡣࡷࠤࡦࡴࡹࠡࡲࡤࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡴ࡬ࠠࠣࡽࢀࠦ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡥ࡯ࡹࡩ࡫ࠠࡢࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰ࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠢࡩ࡭ࡱ࡫ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࡹ࠮ࠨ੃")
bstack1ll11ll1l_opy_ = bstack1l_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡶࡪࡪࡥ࡯ࡶ࡬ࡥࡱࡹࠠ࡯ࡱࡷࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡢࡦࡧࠤࡹ࡮ࡥ࡮ࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࠦࡡࡴࠢࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧࠦࡡ࡯ࡦࠣࠦࡦࡩࡣࡦࡵࡶࡏࡪࡿࠢࠡࡱࡵࠤࡸ࡫ࡴࠡࡶ࡫ࡩࡲࠦࡡࡴࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࡵ࠽ࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨࠠࡢࡰࡧࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠣࠩ੄")
bstack1l1111111_opy_ = bstack1l_opy_ (u"ࠫࡒࡧ࡬ࡧࡱࡵࡱࡪࡪࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠿ࠨࡻࡾࠤࠪ੅")
bstack1l1ll1l11_opy_ = bstack1l_opy_ (u"ࠬࡋ࡮ࡤࡱࡸࡲࡹ࡫ࡲࡦࡦࠣࡩࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡸࡴࠥ࠳ࠠࡼࡿࠪ੆")
bstack1l111l1_opy_ = bstack1l_opy_ (u"࠭ࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱ࠭ੇ")
bstack11ll1_opy_ = bstack1l_opy_ (u"ࠧࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠧੈ")
bstack1111lll1_opy_ = bstack1l_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱࠦࡩࡴࠢࡱࡳࡼࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠡࠨ੉")
bstack111ll1_opy_ = bstack1l_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࠤࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡐࡴࡩࡡ࡭࠼ࠣࡿࢂ࠭੊")
bstack11l111l1l_opy_ = bstack1l_opy_ (u"ࠪࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡼ࡯ࡴࡩࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࢀࢃࠧੋ")
bstack1l1ll_opy_ = bstack1l_opy_ (u"࡚ࠫࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠬੌ")
bstack111l_opy_ = bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀ੍ࠫ")
bstack1l11l1ll_opy_ = bstack1l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࠠࡢࡰࠣࡥࡵࡶࡲࡰࡲࡵ࡭ࡦࡺࡥࠡࡈ࡚ࠤ࠭ࡸ࡯ࡣࡱࡷ࠳ࡵࡧࡢࡰࡶࠬࠤ࡮ࡴࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠱ࠦࡳ࡬࡫ࡳࠤࡹ࡮ࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤࡰ࡫ࡹࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡮࡬ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡵ࡬ࡱࡵࡲࡥࠡࡲࡼࡸ࡭ࡵ࡮ࠡࡵࡦࡶ࡮ࡶࡴࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡤࡲࡾࠦࡆࡘ࠰ࠪ੎")
bstack1l111lll_opy_ = bstack1l_opy_ (u"ࠧࡔࡧࡷࡸ࡮ࡴࡧࠡࡪࡷࡸࡵࡖࡲࡰࡺࡼ࠳࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡤࡷࡵࡶࡪࡴࡴ࡭ࡻࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡰࡨࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࠮ࡻࡾࠫ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡺࡶࡧࡳࡣࡧࡩࠥࡺ࡯ࠡࡕࡨࡰࡪࡴࡩࡶ࡯ࡁࡁ࠹࠴࠰࠯࠲ࠣࡳࡷࠦࡲࡦࡨࡨࡶࠥࡺ࡯ࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡱ࡫࡮ࡪࡷࡰ࠳ࡷࡻ࡮࠮ࡶࡨࡷࡹࡹ࠭ࡣࡧ࡫࡭ࡳࡪ࠭ࡱࡴࡲࡼࡾࠩࡰࡺࡶ࡫ࡳࡳࠦࡦࡰࡴࠣࡥࠥࡽ࡯ࡳ࡭ࡤࡶࡴࡻ࡮ࡥ࠰ࠪ੏")
bstack11l1l1lll_opy_ = bstack1l_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴࠮ࠨ੐")
bstack11ll1ll1_opy_ = bstack1l_opy_ (u"ࠩࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡹ࡮ࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠧࠧੑ")
bstack11l1lll_opy_ = bstack1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫࡯࡬ࡦ࠰ࠣࡿࢂ࠭੒")
bstack1ll11llll_opy_ = bstack1l_opy_ (u"ࠫࡊࡾࡰࡦࡥࡷࡩࡩࠦࡡࡵࠢ࡯ࡩࡦࡹࡴࠡ࠳ࠣ࡭ࡳࡶࡵࡵ࠮ࠣࡶࡪࡩࡥࡪࡸࡨࡨࠥ࠶ࠧ੓")
bstack1111ll11_opy_ = bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡩࡻࡲࡪࡰࡪࠤࡆࡶࡰࠡࡷࡳࡰࡴࡧࡤ࠯ࠢࡾࢁࠬ੔")
bstack11l11_opy_ = bstack1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡱࡵࡡࡥࠢࡄࡴࡵ࠴ࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡻࡾ࠰ࠪ੕")
bstack11lllll_opy_ = bstack1l_opy_ (u"ࠧࡌࡧࡼࡷࠥࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࠮ࡧࡻ࡭ࡸࡺࠠࡢࡵࠣࡥࡵࡶࠠࡷࡣ࡯ࡹࡪࡹࠬࠡࡷࡶࡩࠥࡧ࡮ࡺࠢࡲࡲࡪࠦࡰࡳࡱࡳࡩࡷࡺࡹࠡࡨࡵࡳࡲࠦࡻࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡶࡡࡵࡪ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡩࡵࡴࡶࡲࡱࡤ࡯ࡤ࠽ࡵࡷࡶ࡮ࡴࡧ࠿࠮ࠣࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀࢀ࠰ࠥࡵ࡮࡭ࡻࠣࠦࡵࡧࡴࡩࠤࠣࡥࡳࡪࠠࠣࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠦࠥࡩࡡ࡯ࠢࡦࡳ࠲࡫ࡸࡪࡵࡷࠤࡹࡵࡧࡦࡶ࡫ࡩࡷ࠴ࠧ੖")
bstack1llll11_opy_ = bstack1l_opy_ (u"ࠨ࡝ࡌࡲࡻࡧ࡬ࡪࡦࠣࡥࡵࡶࠠࡱࡴࡲࡴࡪࡸࡴࡺ࡟ࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠣࡥࡷ࡫ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੗")
bstack1ll1l1l1_opy_ = bstack1l_opy_ (u"ࠩ࡞ࡍࡳࡼࡡ࡭࡫ࡧࠤࡦࡶࡰࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࡠࠤࡘࡻࡰࡱࡱࡵࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࡹࠠࡰࡨࠣࡥࡵࡶࠠࡢࡴࡨࠤࡴ࡬ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੘")
bstack1l1lll1ll_opy_ = bstack1l_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡦࡶࡰࠡ࡫ࡧࠤࢀࢃࠠࡧࡱࡵࠤ࡭ࡧࡳࡩࠢ࠽ࠤࢀࢃ࠮ࠨਖ਼")
bstack111llllll_opy_ = bstack1l_opy_ (u"ࠫࡆࡶࡰࠡࡗࡳࡰࡴࡧࡤࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠣࡍࡉࠦ࠺ࠡࡽࢀࠫਗ਼")
bstack11l111l1_opy_ = bstack1l_opy_ (u"࡛ࠬࡳࡪࡰࡪࠤࡆࡶࡰࠡ࠼ࠣࡿࢂ࠴ࠧਜ਼")
bstack1l111l11l_opy_ = bstack1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲࠦࡩࡴࠢࡱࡳࡹࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡳࡷࠦࡶࡢࡰ࡬ࡰࡱࡧࠠࡱࡻࡷ࡬ࡴࡴࠠࡵࡧࡶࡸࡸ࠲ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡰࡢࡴࡤࡰࡱ࡫࡬ࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠥࡃࠠ࠲ࠩੜ")
bstack11llll1l_opy_ = bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡀࠠࡼࡿࠪ੝")
bstack1lllll11_opy_ = bstack1l_opy_ (u"ࠨࡅࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡨࡲ࡯ࡴࡧࠣࡦࡷࡵࡷࡴࡧࡵ࠾ࠥࢁࡽࠨਫ਼")
bstack1ll1ll11_opy_ = bstack1l_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥ࡭ࡥࡵࠢࡵࡩࡦࡹ࡯࡯ࠢࡩࡳࡷࠦࡢࡦࡪࡤࡺࡪࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥ࠯ࠢࡾࢁࠬ੟")
bstack11l11ll_opy_ = bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡤࡴ࡮ࠦࡣࡢ࡮࡯࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ੠")
bstack111llll11_opy_ = bstack1l_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡪࡲࡻࠥࡨࡵࡪ࡮ࡧࠤ࡚ࡘࡌ࠭ࠢࡤࡷࠥࡨࡵࡪ࡮ࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡷࡶࡩࡩ࠴ࠧ੡")
bstack1111l1_opy_ = bstack1l_opy_ (u"࡙ࠬࡥࡳࡸࡨࡶࠥࡹࡩࡥࡧࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠮ࡻࡾࠫࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡦࡳࡥࠡࡣࡶࠤࡨࡲࡩࡦࡰࡷࠤࡸ࡯ࡤࡦࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩ࠭ࢁࡽࠪࠩ੢")
bstack1l1lll_opy_ = bstack1l_opy_ (u"࠭ࡖࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡳࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠻ࠢࡾࢁࠬ੣")
bstack1llll1ll_opy_ = bstack1l_opy_ (u"ࠧࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡥࡨࡩࡥࡴࡵࠣࡥࠥࡶࡲࡪࡸࡤࡸࡪࠦࡤࡰ࡯ࡤ࡭ࡳࡀࠠࡼࡿࠣ࠲࡙ࠥࡥࡵࠢࡷ࡬ࡪࠦࡦࡰ࡮࡯ࡳࡼ࡯࡮ࡨࠢࡦࡳࡳ࡬ࡩࡨࠢ࡬ࡲࠥࡿ࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠾ࠥࡢ࡮࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥࡢ࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰ࠿ࠦࡴࡳࡷࡨࠤࡡࡴ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠫ੤")
bstack1l1llll_opy_ = bstack1l_opy_ (u"ࠨࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣ࡫ࡪࡺ࡟࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࡤ࡫ࡲࡳࡱࡵࠤ࠿ࠦࡻࡾࠩ੥")
bstack1ll1l1ll1_opy_ = bstack1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫࡮ࡥࡡࡤࡱࡵࡲࡩࡵࡷࡧࡩࡤ࡫ࡶࡦࡰࡷࠤ࡫ࡵࡲࠡࡕࡇࡏࡘ࡫ࡴࡶࡲࠣࡿࢂࠨ੦")
bstack1l1ll11_opy_ = bstack1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥ࡯ࡦࡢࡥࡲࡶ࡬ࡪࡶࡸࡨࡪࡥࡥࡷࡧࡱࡸࠥ࡬࡯ࡳࠢࡖࡈࡐ࡚ࡥࡴࡶࡄࡸࡹ࡫࡭ࡱࡶࡨࡨࠥࢁࡽࠣ੧")
bstack11ll1l1l1_opy_ = bstack1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡰࡧࡣࡦࡳࡰ࡭࡫ࡷࡹࡩ࡫࡟ࡦࡸࡨࡲࡹࠦࡦࡰࡴࠣࡗࡉࡑࡔࡦࡵࡷࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠠࡼࡿࠥ੨")
bstack11llllll_opy_ = bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡵࡩࡤࡸࡥࡲࡷࡨࡷࡹࠦࡻࡾࠤ੩")
bstack1ll111ll_opy_ = bstack1l_opy_ (u"ࠨࡐࡐࡕࡗࠤࡊࡼࡥ࡯ࡶࠣࡿࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡ࠼ࠣࡿࢂࠨ੪")
bstack1lll1111_opy_ = bstack1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦࡰࡳࡱࡻࡽࠥࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫ੫")
bstack1lll1ll1l_opy_ = bstack1l_opy_ (u"ࠨࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡ࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠥࢁࡽࠨ੬")
bstack11l1ll1l1_opy_ = bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥ࠵࡮ࡦࡺࡷࡣ࡭ࡻࡢࡴ࠼ࠣࡿࢂ࠭੭")
bstack11llllll1_opy_ = bstack1l_opy_ (u"ࠪࡒࡪࡧࡲࡦࡵࡷࠤ࡭ࡻࡢࠡࡣ࡯ࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡹ࠺ࠡࡽࢀࠫ੮")
bstack1111ll1l_opy_ = bstack1l_opy_ (u"ࠫࡊࡘࡒࡐࡔࠣࡍࡓࠦࡁࡍࡎࡒࡇࡆ࡚ࡅࠡࡊࡘࡆࠥࢁࡽࠨ੯")
bstack1l111ll1_opy_ = bstack1l_opy_ (u"ࠬࡒࡡࡵࡧࡱࡧࡾࠦ࡯ࡧࠢ࡫ࡹࡧࡀࠠࡼࡿࠣ࡭ࡸࡀࠠࡼࡿࠪੰ")
bstack1l1l11l1_opy_ = bstack1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢ࡯ࡥࡹ࡫࡮ࡤࡻࠣࡪࡴࡸࠠࡼࡿࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੱ")
bstack1ll1lll11_opy_ = bstack1l_opy_ (u"ࠧࡉࡷࡥࠤࡺࡸ࡬ࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢࡲࡴࡹ࡯࡭ࡢ࡮ࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੲ")
bstack1l1l1ll11_opy_ = bstack1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡴࡶࡴࡪ࡯ࡤࡰࠥ࡮ࡵࡣࠢࡸࡶࡱࡀࠠࡼࡿࠪੳ")
bstack11l111l11_opy_ = bstack1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡰ࡮ࡹࡴࡴ࠼ࠣࡿࢂ࠭ੴ")
bstack1l111l111_opy_ = bstack1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴ࠼ࠣࡿࢂ࠭ੵ")
bstack11ll11_opy_ = bstack1l_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡰࡢࡥࠣࡪ࡮ࡲࡥࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠩ੶")
bstack11l1lll1_opy_ = bstack1l_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬ੷")
bstack11l1l1l_opy_ = bstack1l_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬ੸")
from ._version import __version__
bstack1l1l1lll_opy_ = None
CONFIG = {}
bstack11llll1ll_opy_ = {}
bstack11ll111_opy_ = {}
bstack11l1l1111_opy_ = None
bstack1111l_opy_ = None
bstack111lll1l_opy_ = None
bstack1ll1111l1_opy_ = -1
bstack1l11l1l1l_opy_ = bstack11ll111l_opy_
bstack1l1111_opy_ = 1
bstack11ll1l111_opy_ = False
bstack1llll1111_opy_ = False
bstack1l1l1111l_opy_ = bstack1l_opy_ (u"ࠧࠨ੹")
bstack1l11ll1l1_opy_ = bstack1l_opy_ (u"ࠨࠩ੺")
bstack11l11l11l_opy_ = False
bstack1ll11l1ll_opy_ = True
bstack1ll1ll111_opy_ = bstack1l_opy_ (u"ࠩࠪ੻")
bstack1l11l111_opy_ = []
bstack1l1lllll_opy_ = bstack1l_opy_ (u"ࠪࠫ੼")
bstack1ll11l1_opy_ = False
bstack1l1ll11ll_opy_ = None
bstack1l1lll1_opy_ = -1
bstack11ll11l11_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭੽")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ੾"), bstack1l_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫ੿"))
bstack11l11l1ll_opy_ = []
bstack111llll1l_opy_ = False
bstack1l1ll1l1_opy_ = None
bstack1l1ll1ll1_opy_ = None
bstack1ll11l1l_opy_ = None
bstack11l11l1l_opy_ = None
bstack1ll1l11l1_opy_ = None
bstack1llllllll_opy_ = None
bstack1111l1l_opy_ = None
bstack1l1l1l1ll_opy_ = None
bstack1lll1l1ll_opy_ = None
bstack1l111_opy_ = None
bstack1111l11l_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack1l1lll1l1_opy_ = None
bstack1lll1l1l1_opy_ = None
bstack1l1l1l1l1_opy_ = None
bstack11l11ll11_opy_ = bstack1l_opy_ (u"ࠢࠣ઀")
class bstack11llll11_opy_(threading.Thread):
  def run(self):
    self.exc = None
    try:
      self.ret = self._target(*self._args, **self._kwargs)
    except Exception as e:
      self.exc = e
  def join(self, timeout=None):
    super(bstack11llll11_opy_, self).join(timeout)
    if self.exc:
      raise self.exc
    return self.ret
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l11l1l1l_opy_,
                    format=bstack1l_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ઁ"),
                    datefmt=bstack1l_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫં"))
def bstack11lll111l_opy_():
  global CONFIG
  global bstack1l11l1l1l_opy_
  if bstack1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬઃ") in CONFIG:
    bstack1l11l1l1l_opy_ = bstack1l1l1l11l_opy_[CONFIG[bstack1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭઄")]]
    logging.getLogger().setLevel(bstack1l11l1l1l_opy_)
def bstack1l1l11l_opy_():
  global CONFIG
  global bstack111llll1l_opy_
  bstack1l111ll1l_opy_ = bstack11l1ll_opy_(CONFIG)
  if(bstack1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઅ") in bstack1l111ll1l_opy_ and str(bstack1l111ll1l_opy_[bstack1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ")]).lower() == bstack1l_opy_ (u"ࠧࡵࡴࡸࡩࠬઇ")):
    bstack111llll1l_opy_ = True
def bstack1ll1llll_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1l11111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1llll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧઈ") == args[i].lower() or bstack1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥઉ") == args[i].lower():
      path = args[i+1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll1ll111_opy_
      bstack1ll1ll111_opy_ += bstack1l_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨઊ") + path
      return path
  return None
def bstack1l1llll1_opy_():
  bstack11l1ll111_opy_ = bstack1llll_opy_()
  if bstack11l1ll111_opy_ and os.path.exists(os.path.abspath(bstack11l1ll111_opy_)):
    fileName = bstack11l1ll111_opy_
  if bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨઋ") in os.environ and os.path.exists(os.path.abspath(os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩઌ")])) and not bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨઍ") in locals():
    fileName = os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ઎")]
  if bstack1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪએ") in locals():
    bstack1l11lll1_opy_ = os.path.abspath(fileName)
  else:
    bstack1l11lll1_opy_ = bstack1l_opy_ (u"ࠩࠪઐ")
  bstack111l1l_opy_ = os.getcwd()
  bstack1ll111111_opy_ = bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ઑ")
  bstack11l1111l1_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨ઒")
  while (not os.path.exists(bstack1l11lll1_opy_)) and bstack111l1l_opy_ != bstack1l_opy_ (u"ࠧࠨઓ"):
    bstack1l11lll1_opy_ = os.path.join(bstack111l1l_opy_, bstack1ll111111_opy_)
    if not os.path.exists(bstack1l11lll1_opy_):
      bstack1l11lll1_opy_ = os.path.join(bstack111l1l_opy_, bstack11l1111l1_opy_)
    if bstack111l1l_opy_ != os.path.dirname(bstack111l1l_opy_):
      bstack111l1l_opy_ = os.path.dirname(bstack111l1l_opy_)
    else:
      bstack111l1l_opy_ = bstack1l_opy_ (u"ࠨࠢઔ")
  if not os.path.exists(bstack1l11lll1_opy_):
    bstack1l1ll111l_opy_(
      bstack111l11_opy_.format(os.getcwd()))
  with open(bstack1l11lll1_opy_, bstack1l_opy_ (u"ࠧࡳࠩક")) as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      bstack1l1ll111l_opy_(bstack1l1111111_opy_.format(str(exc)))
def bstack1lll111_opy_(config):
  bstack1lll11_opy_ = bstack1l111111l_opy_(config)
  for option in list(bstack1lll11_opy_):
    if option.lower() in bstack11l1l1l1_opy_ and option != bstack11l1l1l1_opy_[option.lower()]:
      bstack1lll11_opy_[bstack11l1l1l1_opy_[option.lower()]] = bstack1lll11_opy_[option]
      del bstack1lll11_opy_[option]
  return config
def bstack1l11ll11l_opy_():
  global bstack11ll111_opy_
  for key, bstack1l11ll11_opy_ in bstack1l111ll11_opy_.items():
    if isinstance(bstack1l11ll11_opy_, list):
      for var in bstack1l11ll11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11ll111_opy_[key] = os.environ[var]
          break
    elif bstack1l11ll11_opy_ in os.environ and os.environ[bstack1l11ll11_opy_] and str(os.environ[bstack1l11ll11_opy_]).strip():
      bstack11ll111_opy_[key] = os.environ[bstack1l11ll11_opy_]
  if bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪખ") in os.environ:
    bstack11ll111_opy_[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")] = {}
    bstack11ll111_opy_[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")][bstack1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઙ")] = os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧચ")]
def bstack111111ll_opy_():
  global bstack11llll1ll_opy_
  global bstack1ll1ll111_opy_
  for idx, val in enumerate(sys.argv):
    if idx<len(sys.argv) and bstack1l_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩછ").lower() == val.lower():
      bstack11llll1ll_opy_[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")] = {}
      bstack11llll1ll_opy_[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")][bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ")] = sys.argv[idx+1]
      del sys.argv[idx:idx+2]
      break
  for key, bstack11111ll_opy_ in bstack11111l_opy_.items():
    if isinstance(bstack11111ll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack11111ll_opy_:
          if idx<len(sys.argv) and bstack1l_opy_ (u"ࠪ࠱࠲࠭ટ") + var.lower() == val.lower() and not key in bstack11llll1ll_opy_:
            bstack11llll1ll_opy_[key] = sys.argv[idx+1]
            bstack1ll1ll111_opy_ += bstack1l_opy_ (u"ࠫࠥ࠳࠭ࠨઠ") + var + bstack1l_opy_ (u"ࠬࠦࠧડ") + sys.argv[idx+1]
            del sys.argv[idx:idx+2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx<len(sys.argv) and bstack1l_opy_ (u"࠭࠭࠮ࠩઢ") + bstack11111ll_opy_.lower() == val.lower() and not key in bstack11llll1ll_opy_:
          bstack11llll1ll_opy_[key] = sys.argv[idx+1]
          bstack1ll1ll111_opy_ += bstack1l_opy_ (u"ࠧࠡ࠯࠰ࠫણ") + bstack11111ll_opy_ + bstack1l_opy_ (u"ࠨࠢࠪત") + sys.argv[idx+1]
          del sys.argv[idx:idx+2]
def bstack11ll1ll1l_opy_(config):
  bstack11l1111ll_opy_ = config.keys()
  for bstack1l11l1111_opy_, bstack1ll1l1111_opy_ in bstack11111l11_opy_.items():
    if bstack1ll1l1111_opy_ in bstack11l1111ll_opy_:
      config[bstack1l11l1111_opy_] = config[bstack1ll1l1111_opy_]
      del config[bstack1ll1l1111_opy_]
  for bstack1l11l1111_opy_, bstack1ll1l1111_opy_ in bstack1ll11111l_opy_.items():
    if isinstance(bstack1ll1l1111_opy_, list):
      for bstack1l1l111ll_opy_ in bstack1ll1l1111_opy_:
        if bstack1l1l111ll_opy_ in bstack11l1111ll_opy_:
          config[bstack1l11l1111_opy_] = config[bstack1l1l111ll_opy_]
          del config[bstack1l1l111ll_opy_]
          break
    elif bstack1ll1l1111_opy_ in bstack11l1111ll_opy_:
        config[bstack1l11l1111_opy_] = config[bstack1ll1l1111_opy_]
        del config[bstack1ll1l1111_opy_]
  for bstack1l1l111ll_opy_ in list(config):
    for bstack1l11_opy_ in bstack11l11ll1_opy_:
      if bstack1l1l111ll_opy_.lower() == bstack1l11_opy_.lower() and bstack1l1l111ll_opy_ != bstack1l11_opy_:
        config[bstack1l11_opy_] = config[bstack1l1l111ll_opy_]
        del config[bstack1l1l111ll_opy_]
  bstack1l11l_opy_ = []
  if bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ") in config:
    bstack1l11l_opy_ = config[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭દ")]
  for platform in bstack1l11l_opy_:
    for bstack1l1l111ll_opy_ in list(platform):
      for bstack1l11_opy_ in bstack11l11ll1_opy_:
        if bstack1l1l111ll_opy_.lower() == bstack1l11_opy_.lower() and bstack1l1l111ll_opy_ != bstack1l11_opy_:
          platform[bstack1l11_opy_] = platform[bstack1l1l111ll_opy_]
          del platform[bstack1l1l111ll_opy_]
  for bstack1l11l1111_opy_, bstack1ll1l1111_opy_ in bstack1ll11111l_opy_.items():
    for platform in bstack1l11l_opy_:
      if isinstance(bstack1ll1l1111_opy_, list):
        for bstack1l1l111ll_opy_ in bstack1ll1l1111_opy_:
          if bstack1l1l111ll_opy_ in platform:
            platform[bstack1l11l1111_opy_] = platform[bstack1l1l111ll_opy_]
            del platform[bstack1l1l111ll_opy_]
            break
      elif bstack1ll1l1111_opy_ in platform:
        platform[bstack1l11l1111_opy_] = platform[bstack1ll1l1111_opy_]
        del platform[bstack1ll1l1111_opy_]
  for bstack1ll11ll11_opy_ in bstack1111_opy_:
    if bstack1ll11ll11_opy_ in config:
      if not bstack1111_opy_[bstack1ll11ll11_opy_] in config:
        config[bstack1111_opy_[bstack1ll11ll11_opy_]] = {}
      config[bstack1111_opy_[bstack1ll11ll11_opy_]].update(config[bstack1ll11ll11_opy_])
      del config[bstack1ll11ll11_opy_]
  for platform in bstack1l11l_opy_:
    for bstack1ll11ll11_opy_ in bstack1111_opy_:
      if bstack1ll11ll11_opy_ in list(platform):
        if not bstack1111_opy_[bstack1ll11ll11_opy_] in platform:
          platform[bstack1111_opy_[bstack1ll11ll11_opy_]] = {}
        platform[bstack1111_opy_[bstack1ll11ll11_opy_]].update(platform[bstack1ll11ll11_opy_])
        del platform[bstack1ll11ll11_opy_]
  config = bstack1lll111_opy_(config)
  return config
def bstack1l11lll1l_opy_(config):
  global bstack1l11ll1l1_opy_
  if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨધ") in config and str(config[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩન")]).lower() != bstack1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ઩"):
    if not bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ") in config:
      config[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬફ")] = {}
    if not bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ") in config[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ")]:
      bstack1ll1llll1_opy_ = datetime.datetime.now()
      bstack11l1llll1_opy_ = bstack1ll1llll1_opy_.strftime(bstack1l_opy_ (u"ࠫࠪࡪ࡟ࠦࡤࡢࠩࡍࠫࡍࠨમ"))
      hostname = socket.gethostname()
      bstack1lll1ll11_opy_ = bstack1l_opy_ (u"ࠬ࠭ય").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l_opy_ (u"࠭ࡻࡾࡡࡾࢁࡤࢁࡽࠨર").format(bstack11l1llll1_opy_, hostname, bstack1lll1ll11_opy_)
      config[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઱")][bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")] = identifier
    bstack1l11ll1l1_opy_ = config[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")][bstack1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]
  return config
def bstack11111lll_opy_():
  if (
    isinstance(os.getenv(bstack1l_opy_ (u"ࠫࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠩવ")), str) and len(os.getenv(bstack1l_opy_ (u"ࠬࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠪશ"))) > 0
  ) or (
    isinstance(os.getenv(bstack1l_opy_ (u"࠭ࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠬષ")), str) and len(os.getenv(bstack1l_opy_ (u"ࠧࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊ࠭સ"))) > 0
  ):
    return os.getenv(bstack1l_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧહ"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠩࡆࡍࠬ઺"))).lower() == bstack1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ઻") and str(os.getenv(bstack1l_opy_ (u"ࠫࡈࡏࡒࡄࡎࡈࡇࡎ઼࠭"))).lower() == bstack1l_opy_ (u"ࠬࡺࡲࡶࡧࠪઽ"):
    return os.getenv(bstack1l_opy_ (u"࠭ࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠩા"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠧࡄࡋࠪિ"))).lower() == bstack1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ી") and str(os.getenv(bstack1l_opy_ (u"ࠩࡗࡖࡆ࡜ࡉࡔࠩુ"))).lower() == bstack1l_opy_ (u"ࠪࡸࡷࡻࡥࠨૂ"):
    return os.getenv(bstack1l_opy_ (u"࡙ࠫࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠪૃ"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠬࡉࡉࠨૄ"))).lower() == bstack1l_opy_ (u"࠭ࡴࡳࡷࡨࠫૅ") and str(os.getenv(bstack1l_opy_ (u"ࠧࡄࡋࡢࡒࡆࡓࡅࠨ૆"))).lower() == bstack1l_opy_ (u"ࠨࡥࡲࡨࡪࡹࡨࡪࡲࠪે"):
    return 0 # bstack1l11l11l_opy_ bstack1lll11ll1_opy_ not set build number env
  if os.getenv(bstack1l_opy_ (u"ࠩࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠬૈ")) and os.getenv(bstack1l_opy_ (u"ࠪࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙࠭ૉ")):
    return os.getenv(bstack1l_opy_ (u"ࠫࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭૊"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠬࡉࡉࠨો"))).lower() == bstack1l_opy_ (u"࠭ࡴࡳࡷࡨࠫૌ") and str(os.getenv(bstack1l_opy_ (u"ࠧࡅࡔࡒࡒࡊ્࠭"))).lower() == bstack1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭૎"):
    return os.getenv(bstack1l_opy_ (u"ࠩࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠧ૏"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠪࡇࡎ࠭ૐ"))).lower() == bstack1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ૑") and str(os.getenv(bstack1l_opy_ (u"࡙ࠬࡅࡎࡃࡓࡌࡔࡘࡅࠨ૒"))).lower() == bstack1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ૓"):
    return os.getenv(bstack1l_opy_ (u"ࠧࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠪ૔"), 0)
  if str(os.getenv(bstack1l_opy_ (u"ࠨࡅࡌࠫ૕"))).lower() == bstack1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૖") and str(os.getenv(bstack1l_opy_ (u"ࠪࡋࡎ࡚ࡌࡂࡄࡢࡇࡎ࠭૗"))).lower() == bstack1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ૘"):
    return os.getenv(bstack1l_opy_ (u"ࠬࡉࡉࡠࡌࡒࡆࡤࡏࡄࠨ૙"), 0)
  if str(os.getenv(bstack1l_opy_ (u"࠭ࡃࡊࠩ૚"))).lower() == bstack1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ૛") and str(os.getenv(bstack1l_opy_ (u"ࠨࡄࡘࡍࡑࡊࡋࡊࡖࡈࠫ૜"))).lower() == bstack1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ૝"):
    return os.getenv(bstack1l_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠬ૞"), 0)
  if str(os.getenv(bstack1l_opy_ (u"࡙ࠫࡌ࡟ࡃࡗࡌࡐࡉ࠭૟"))).lower() == bstack1l_opy_ (u"ࠬࡺࡲࡶࡧࠪૠ"):
    return os.getenv(bstack1l_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭ૡ"), 0)
  return -1
def bstack1ll1ll1_opy_(bstack1lll1l11_opy_):
  global CONFIG
  if not bstack1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩૢ") in CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૣ")]:
    return
  CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤")] = CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૥")].replace(
    bstack1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૦"),
    str(bstack1lll1l11_opy_)
  )
def bstack1l11ll_opy_():
  global CONFIG
  if not bstack1l_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ૧") in CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૨")]:
    return
  bstack1ll1llll1_opy_ = datetime.datetime.now()
  bstack11l1llll1_opy_ = bstack1ll1llll1_opy_.strftime(bstack1l_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬ૩"))
  CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૪")] = CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૫")].replace(
    bstack1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ૬"),
    bstack11l1llll1_opy_
  )
def bstack1l11l1l1_opy_():
  global CONFIG
  if bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૭") in CONFIG and not bool(CONFIG[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૮")]):
    del CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૯")]
    return
  if not bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૰") in CONFIG:
    CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૱")] = bstack1l_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ૲")
  if bstack1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ૳") in CONFIG[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૴")]:
    bstack1l11ll_opy_()
    os.environ[bstack1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ૵")] = CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૶")]
  if not bstack1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૷") in CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૸")]:
    return
  bstack1lll1l11_opy_ = bstack1l_opy_ (u"ࠩࠪૹ")
  bstack11l11lll1_opy_ = bstack11111lll_opy_()
  if bstack11l11lll1_opy_ != -1:
    bstack1lll1l11_opy_ = bstack1l_opy_ (u"ࠪࡇࡎࠦࠧૺ") + str(bstack11l11lll1_opy_)
  if bstack1lll1l11_opy_ == bstack1l_opy_ (u"ࠫࠬૻ"):
    bstack11lllllll_opy_ = bstack11ll11l_opy_(CONFIG[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨૼ")])
    if bstack11lllllll_opy_ != -1:
      bstack1lll1l11_opy_ = str(bstack11lllllll_opy_)
  if bstack1lll1l11_opy_:
    bstack1ll1ll1_opy_(bstack1lll1l11_opy_)
    os.environ[bstack1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ૽")] = CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૾")]
def bstack11llll1l1_opy_(bstack1ll1l1l11_opy_, bstack1lllll_opy_, path):
  bstack1111lll_opy_ = {
    bstack1l_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૿"): bstack1lllll_opy_
  }
  if os.path.exists(path):
    bstack11l1l1_opy_ = json.load(open(path, bstack1l_opy_ (u"ࠩࡵࡦࠬ଀")))
  else:
    bstack11l1l1_opy_ = {}
  bstack11l1l1_opy_[bstack1ll1l1l11_opy_] = bstack1111lll_opy_
  with open(path, bstack1l_opy_ (u"ࠥࡻ࠰ࠨଁ")) as outfile:
    json.dump(bstack11l1l1_opy_, outfile)
def bstack11ll11l_opy_(bstack1ll1l1l11_opy_):
  bstack1ll1l1l11_opy_ = str(bstack1ll1l1l11_opy_)
  bstack111l1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭ଂ")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬଃ"))
  try:
    if not os.path.exists(bstack111l1l1l_opy_):
      os.makedirs(bstack111l1l1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l_opy_ (u"࠭ࡾࠨ଄")), bstack1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧଅ"), bstack1l_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪଆ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l_opy_ (u"ࠩࡺࠫଇ")):
        pass
      with open(file_path, bstack1l_opy_ (u"ࠥࡻ࠰ࠨଈ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l_opy_ (u"ࠫࡷ࠭ଉ")) as bstack1ll111l_opy_:
      bstack11lllll1l_opy_ = json.load(bstack1ll111l_opy_)
    if bstack1ll1l1l11_opy_ in bstack11lllll1l_opy_:
      bstack11l1l1ll1_opy_ = bstack11lllll1l_opy_[bstack1ll1l1l11_opy_][bstack1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩଊ")]
      bstack1ll1ll11l_opy_ = int(bstack11l1l1ll1_opy_) + 1
      bstack11llll1l1_opy_(bstack1ll1l1l11_opy_, bstack1ll1ll11l_opy_, file_path)
      return bstack1ll1ll11l_opy_
    else:
      bstack11llll1l1_opy_(bstack1ll1l1l11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11llll1l_opy_.format(str(e)))
    return -1
def bstack1l1l1lll1_opy_(config):
  if not config[bstack1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨଋ")] or not config[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪଌ")]:
    return True
  else:
    return False
def bstack11l1lll11_opy_(config):
  if bstack1l_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ଍") in config:
    del(config[bstack1l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ଎")])
    return False
  if bstack1l1l11111_opy_() < version.parse(bstack1l_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩଏ")):
    return False
  if bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪଐ")):
    return True
  if bstack1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ଑") in config and config[bstack1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭଒")] == False:
    return False
  else:
    return True
def bstack11l1l111l_opy_(config, index = 0):
  global bstack11l11l11l_opy_
  bstack11111111_opy_ = {}
  caps = bstack1lll1llll_opy_ + bstack1ll111l11_opy_
  if bstack11l11l11l_opy_:
    caps += bstack11l1ll11_opy_
  for key in config:
    if key in caps + [bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଓ")]:
      continue
    bstack11111111_opy_[key] = config[key]
  if bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଔ") in config:
    for bstack1l11l1l_opy_ in config[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬକ")][index]:
      if bstack1l11l1l_opy_ in caps + [bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଖ"), bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଗ")]:
        continue
      bstack11111111_opy_[bstack1l11l1l_opy_] = config[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଘ")][index][bstack1l11l1l_opy_]
  bstack11111111_opy_[bstack1l_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨଙ")] = socket.gethostname()
  if bstack1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨଚ") in bstack11111111_opy_:
    del(bstack11111111_opy_[bstack1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩଛ")])
  return bstack11111111_opy_
def bstack11l11ll1l_opy_(config):
  global bstack11l11l11l_opy_
  bstack1l1ll1111_opy_ = {}
  caps = bstack1ll111l11_opy_
  if bstack11l11l11l_opy_:
    caps+= bstack11l1ll11_opy_
  for key in caps:
    if key in config:
      bstack1l1ll1111_opy_[key] = config[key]
  return bstack1l1ll1111_opy_
def bstack111llll1_opy_(bstack11111111_opy_, bstack1l1ll1111_opy_):
  bstack1l1ll1lll_opy_ = {}
  for key in bstack11111111_opy_.keys():
    if key in bstack11111l11_opy_:
      bstack1l1ll1lll_opy_[bstack11111l11_opy_[key]] = bstack11111111_opy_[key]
    else:
      bstack1l1ll1lll_opy_[key] = bstack11111111_opy_[key]
  for key in bstack1l1ll1111_opy_:
    if key in bstack11111l11_opy_:
      bstack1l1ll1lll_opy_[bstack11111l11_opy_[key]] = bstack1l1ll1111_opy_[key]
    else:
      bstack1l1ll1lll_opy_[key] = bstack1l1ll1111_opy_[key]
  return bstack1l1ll1lll_opy_
def bstack11l1l11_opy_(config, index = 0):
  global bstack11l11l11l_opy_
  caps = {}
  bstack1l1ll1111_opy_ = bstack11l11ll1l_opy_(config)
  bstack1llll11l1_opy_ = bstack1ll111l11_opy_
  bstack1llll11l1_opy_ += bstack11ll1l_opy_
  if bstack11l11l11l_opy_:
    bstack1llll11l1_opy_ += bstack11l1ll11_opy_
  if bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ") in config:
    if bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଝ") in config[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଞ")][index]:
      caps[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଟ")] = config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଠ")][index][bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଡ")]
    if bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଢ") in config[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଣ")][index]:
      caps[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫତ")] = str(config[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଥ")][index][bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଦ")])
    bstack11l1111_opy_ = {}
    for bstack1l1l111l1_opy_ in bstack1llll11l1_opy_:
      if bstack1l1l111l1_opy_ in config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଧ")][index]:
        if bstack1l1l111l1_opy_ == bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩନ"):
          bstack11l1111_opy_[bstack1l1l111l1_opy_] = str(config[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଩")][index][bstack1l1l111l1_opy_] * 1.0)
        else:
          bstack11l1111_opy_[bstack1l1l111l1_opy_] = config[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬପ")][index][bstack1l1l111l1_opy_]
        del(config[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଫ")][index][bstack1l1l111l1_opy_])
    bstack1l1ll1111_opy_ = update(bstack1l1ll1111_opy_, bstack11l1111_opy_)
  bstack11111111_opy_ = bstack11l1l111l_opy_(config, index)
  for bstack1l1l111ll_opy_ in bstack1ll111l11_opy_ + [bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩବ"), bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଭ")]:
    if bstack1l1l111ll_opy_ in bstack11111111_opy_:
      bstack1l1ll1111_opy_[bstack1l1l111ll_opy_] = bstack11111111_opy_[bstack1l1l111ll_opy_]
      del(bstack11111111_opy_[bstack1l1l111ll_opy_])
  if bstack11l1lll11_opy_(config):
    bstack11111111_opy_[bstack1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ମ")] = True
    caps.update(bstack1l1ll1111_opy_)
    caps[bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଯ")] = bstack11111111_opy_
  else:
    bstack11111111_opy_[bstack1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨର")] = False
    caps.update(bstack111llll1_opy_(bstack11111111_opy_, bstack1l1ll1111_opy_))
    if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଱") in caps:
      caps[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଲ")] = caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଳ")]
      del(caps[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଴")])
    if bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଵ") in caps:
      caps[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩଶ")] = caps[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଷ")]
      del(caps[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪସ")])
  return caps
def bstack111lll_opy_():
  global bstack1l1lllll_opy_
  if bstack1l1l11111_opy_() <= version.parse(bstack1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪହ")):
    if bstack1l1lllll_opy_ != bstack1l_opy_ (u"ࠫࠬ଺"):
      return bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ଻") + bstack1l1lllll_opy_ + bstack1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤ଼ࠥ")
    return bstack11ll1llll_opy_
  if  bstack1l1lllll_opy_ != bstack1l_opy_ (u"ࠧࠨଽ"):
    return bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥା") + bstack1l1lllll_opy_ + bstack1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥି")
  return bstack11llll_opy_
def bstack1lll1lll_opy_(options):
  return hasattr(options, bstack1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫୀ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1ll1l1lll_opy_(options, bstack1llll1l11_opy_):
  for bstack1l1l111_opy_ in bstack1llll1l11_opy_:
    if bstack1l1l111_opy_ in [bstack1l_opy_ (u"ࠫࡦࡸࡧࡴࠩୁ"), bstack1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩୂ")]:
      next
    if bstack1l1l111_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1l111_opy_]= update(options._experimental_options[bstack1l1l111_opy_], bstack1llll1l11_opy_[bstack1l1l111_opy_])
    else:
      options.add_experimental_option(bstack1l1l111_opy_, bstack1llll1l11_opy_[bstack1l1l111_opy_])
  if bstack1l_opy_ (u"࠭ࡡࡳࡩࡶࠫୃ") in bstack1llll1l11_opy_:
    for arg in bstack1llll1l11_opy_[bstack1l_opy_ (u"ࠧࡢࡴࡪࡷࠬୄ")]:
      options.add_argument(arg)
    del(bstack1llll1l11_opy_[bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୅")])
  if bstack1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭୆") in bstack1llll1l11_opy_:
    for ext in bstack1llll1l11_opy_[bstack1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧେ")]:
      options.add_extension(ext)
    del(bstack1llll1l11_opy_[bstack1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨୈ")])
def bstack1lllll1l1_opy_(options, bstack1llll1l_opy_):
  if bstack1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ୉") in bstack1llll1l_opy_:
    for bstack1ll1ll1ll_opy_ in bstack1llll1l_opy_[bstack1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ୊")]:
      if bstack1ll1ll1ll_opy_ in options._preferences:
        options._preferences[bstack1ll1ll1ll_opy_] = update(options._preferences[bstack1ll1ll1ll_opy_], bstack1llll1l_opy_[bstack1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ୋ")][bstack1ll1ll1ll_opy_])
      else:
        options.set_preference(bstack1ll1ll1ll_opy_, bstack1llll1l_opy_[bstack1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧୌ")][bstack1ll1ll1ll_opy_])
  if bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡹ୍ࠧ") in bstack1llll1l_opy_:
    for arg in bstack1llll1l_opy_[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ୎")]:
      options.add_argument(arg)
def bstack11lll1l_opy_(options, bstack111111l_opy_):
  if bstack1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬ୏") in bstack111111l_opy_:
    options.use_webview(bool(bstack111111l_opy_[bstack1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭୐")]))
  bstack1ll1l1lll_opy_(options, bstack111111l_opy_)
def bstack11ll_opy_(options, bstack11l1l_opy_):
  for bstack1ll1l_opy_ in bstack11l1l_opy_:
    if bstack1ll1l_opy_ in [bstack1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ୑"), bstack1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ୒")]:
      next
    options.set_capability(bstack1ll1l_opy_, bstack11l1l_opy_[bstack1ll1l_opy_])
  if bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୓") in bstack11l1l_opy_:
    for arg in bstack11l1l_opy_[bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ୔")]:
      options.add_argument(arg)
  if bstack1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧ୕") in bstack11l1l_opy_:
    options.use_technology_preview(bool(bstack11l1l_opy_[bstack1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨୖ")]))
def bstack1ll1lll1l_opy_(options, bstack11l11l1l1_opy_):
  for bstack1l1l11lll_opy_ in bstack11l11l1l1_opy_:
    if bstack1l1l11lll_opy_ in [bstack1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩୗ"), bstack1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ୘")]:
      next
    options._options[bstack1l1l11lll_opy_] = bstack11l11l1l1_opy_[bstack1l1l11lll_opy_]
  if bstack1l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୙") in bstack11l11l1l1_opy_:
    for bstack11ll1l11_opy_ in bstack11l11l1l1_opy_[bstack1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୚")]:
      options.add_additional_option(
          bstack11ll1l11_opy_, bstack11l11l1l1_opy_[bstack1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୛")][bstack11ll1l11_opy_])
  if bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଡ଼") in bstack11l11l1l1_opy_:
    for arg in bstack11l11l1l1_opy_[bstack1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଢ଼")]:
      options.add_argument(arg)
def bstack1lll1ll_opy_(options, caps):
  if not hasattr(options, bstack1l_opy_ (u"ࠬࡑࡅ࡚ࠩ୞")):
    return
  if options.KEY == bstack1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫୟ") and options.KEY in caps:
    bstack1ll1l1lll_opy_(options, caps[bstack1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬୠ")])
  elif options.KEY == bstack1l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ୡ") and options.KEY in caps:
    bstack1lllll1l1_opy_(options, caps[bstack1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧୢ")])
  elif options.KEY == bstack1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫୣ") and options.KEY in caps:
    bstack11ll_opy_(options, caps[bstack1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ୤")])
  elif options.KEY == bstack1l_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୥") and options.KEY in caps:
    bstack11lll1l_opy_(options, caps[bstack1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୦")])
  elif options.KEY == bstack1l_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୧") and options.KEY in caps:
    bstack1ll1lll1l_opy_(options, caps[bstack1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୨")])
def bstack1lll11111_opy_(caps):
  global bstack11l11l11l_opy_
  if bstack11l11l11l_opy_:
    if bstack1ll1llll_opy_() < version.parse(bstack1l_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨ୩")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ୪")
    if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୫") in caps:
      browser = caps[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୬")]
    elif bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ୭") in caps:
      browser = caps[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ୮")]
    browser = str(browser).lower()
    if browser == bstack1l_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨ୯") or browser == bstack1l_opy_ (u"ࠩ࡬ࡴࡦࡪࠧ୰"):
      browser = bstack1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪୱ")
    if browser == bstack1l_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬ୲"):
      browser = bstack1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୳")
    if browser not in [bstack1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୴"), bstack1l_opy_ (u"ࠧࡦࡦࡪࡩࠬ୵"), bstack1l_opy_ (u"ࠨ࡫ࡨࠫ୶"), bstack1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୷"), bstack1l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫ୸")]:
      return None
    try:
      package = bstack1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭୹").format(browser)
      name = bstack1l_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭୺")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lll1lll_opy_(options):
        return None
      for bstack1l1l111ll_opy_ in caps.keys():
        options.set_capability(bstack1l1l111ll_opy_, caps[bstack1l1l111ll_opy_])
      bstack1lll1ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1llll11ll_opy_(options, bstack1l111ll_opy_):
  if not bstack1lll1lll_opy_(options):
    return
  for bstack1l1l111ll_opy_ in bstack1l111ll_opy_.keys():
    if bstack1l1l111ll_opy_ in bstack11ll1l_opy_:
      next
    if bstack1l1l111ll_opy_ in options._caps and type(options._caps[bstack1l1l111ll_opy_]) in [dict, list]:
      options._caps[bstack1l1l111ll_opy_] = update(options._caps[bstack1l1l111ll_opy_], bstack1l111ll_opy_[bstack1l1l111ll_opy_])
    else:
      options.set_capability(bstack1l1l111ll_opy_, bstack1l111ll_opy_[bstack1l1l111ll_opy_])
  bstack1lll1ll_opy_(options, bstack1l111ll_opy_)
  if bstack1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬ୻") in options._caps:
    if options._caps[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୼")] and options._caps[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୽")].lower() != bstack1l_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ୾"):
      del options._caps[bstack1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩ୿")]
def bstack1111111l_opy_(proxy_config):
  if bstack1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ஀") in proxy_config:
    proxy_config[bstack1l_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧ஁")] = proxy_config[bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪஂ")]
    del(proxy_config[bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫஃ")])
  if bstack1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ஄") in proxy_config and proxy_config[bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬஅ")].lower() != bstack1l_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪஆ"):
    proxy_config[bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧஇ")] = bstack1l_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬஈ")
  if bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫஉ") in proxy_config:
    proxy_config[bstack1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪஊ")] = bstack1l_opy_ (u"ࠨࡲࡤࡧࠬ஋")
  return proxy_config
def bstack11l1ll1_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ஌") in config:
    return proxy
  config[bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ஍")] = bstack1111111l_opy_(config[bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪஎ")])
  if proxy == None:
    proxy = Proxy(config[bstack1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫஏ")])
  return proxy
def bstack1l111llll_opy_(self):
  global CONFIG
  global bstack1lll1l1ll_opy_
  try:
    proxy = bstack11lll1l1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l_opy_ (u"࠭࠮ࡱࡣࡦࠫஐ")):
        proxies = bstack11111_opy_(proxy, bstack111lll_opy_())
        if len(proxies) > 0:
          protocol, bstack1lllll1l_opy_ = proxies.popitem()
          if bstack1l_opy_ (u"ࠢ࠻࠱࠲ࠦ஑") in bstack1lllll1l_opy_:
            return bstack1lllll1l_opy_
          else:
            return bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤஒ") + bstack1lllll1l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨஓ").format(str(e)))
  return bstack1lll1l1ll_opy_(self)
def bstack11ll1ll_opy_():
  global CONFIG
  return bstack1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ஔ") in CONFIG or bstack1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨக") in CONFIG
def bstack11lll1l1_opy_(config):
  if not bstack11ll1ll_opy_():
    return
  if config.get(bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ஖")):
    return config.get(bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ஗"))
  if config.get(bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ஘")):
    return config.get(bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬங"))
def bstack1l11lllll_opy_(url):
  try:
      result = urlparse(url)
      return all([result.scheme, result.netloc])
  except:
      return False
def bstack11lll11l1_opy_(bstack1l11l1ll1_opy_, bstack11ll11l1l_opy_):
  from pypac import get_pac
  from pypac import PACSession
  from pypac.parser import PACFile
  import socket
  if os.path.isfile(bstack1l11l1ll1_opy_):
    with open(bstack1l11l1ll1_opy_) as f:
      pac = PACFile(f.read())
  elif bstack1l11lllll_opy_(bstack1l11l1ll1_opy_):
    pac = get_pac(url=bstack1l11l1ll1_opy_)
  else:
    raise Exception(bstack1l_opy_ (u"ࠩࡓࡥࡨࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠩச").format(bstack1l11l1ll1_opy_))
  session = PACSession(pac)
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((bstack1l_opy_ (u"ࠥ࠼࠳࠾࠮࠹࠰࠻ࠦ஛"), 80))
    bstack1ll1lll1_opy_ = s.getsockname()[0]
    s.close()
  except:
    bstack1ll1lll1_opy_ = bstack1l_opy_ (u"ࠫ࠵࠴࠰࠯࠲࠱࠴ࠬஜ")
  proxy_url = session.get_pac().find_proxy_for_url(bstack11ll11l1l_opy_, bstack1ll1lll1_opy_)
  return proxy_url
def bstack11111_opy_(bstack1l11l1ll1_opy_, bstack11ll11l1l_opy_):
  proxies = {}
  global bstack11l111111_opy_
  if bstack1l_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨ஝") in globals():
    return bstack11l111111_opy_
  try:
    proxy = bstack11lll11l1_opy_(bstack1l11l1ll1_opy_,bstack11ll11l1l_opy_)
    if bstack1l_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨஞ") in proxy:
      proxies = {}
    elif bstack1l_opy_ (u"ࠢࡉࡖࡗࡔࠧட") in proxy or bstack1l_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢ஠") in proxy or bstack1l_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣ஡") in proxy:
      bstack1l11ll111_opy_ = proxy.split(bstack1l_opy_ (u"ࠥࠤࠧ஢"))
      if bstack1l_opy_ (u"ࠦ࠿࠵࠯ࠣண") in bstack1l_opy_ (u"ࠧࠨத").join(bstack1l11ll111_opy_[1:]):
        proxies = {
          bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ஥"): bstack1l_opy_ (u"ࠢࠣ஦").join(bstack1l11ll111_opy_[1:])
        }
      else:
        proxies = {
          bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧ஧") : str(bstack1l11ll111_opy_[0]).lower()+ bstack1l_opy_ (u"ࠤ࠽࠳࠴ࠨந") + bstack1l_opy_ (u"ࠥࠦன").join(bstack1l11ll111_opy_[1:])
        }
    elif bstack1l_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥப") in proxy:
      bstack1l11ll111_opy_ = proxy.split(bstack1l_opy_ (u"ࠧࠦࠢ஫"))
      if bstack1l_opy_ (u"ࠨ࠺࠰࠱ࠥ஬") in bstack1l_opy_ (u"ࠢࠣ஭").join(bstack1l11ll111_opy_[1:]):
        proxies = {
          bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧம"): bstack1l_opy_ (u"ࠤࠥய").join(bstack1l11ll111_opy_[1:])
        }
      else:
        proxies = {
          bstack1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩர"): bstack1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧற") + bstack1l_opy_ (u"ࠧࠨல").join(bstack1l11ll111_opy_[1:])
        }
    else:
      proxies = {
        bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬள"): proxy
      }
  except Exception as e:
    logger.error(bstack11ll11_opy_.format(bstack1l11l1ll1_opy_, str(e)))
  bstack11l111111_opy_ = proxies
  return proxies
def bstack1l1l11ll1_opy_(config, bstack11ll11l1l_opy_):
  proxy = bstack11lll1l1_opy_(config)
  proxies = {}
  if config.get(bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪழ")) or config.get(bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬவ")):
    if proxy.endswith(bstack1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧஶ")):
      proxies = bstack11111_opy_(proxy,bstack11ll11l1l_opy_)
    else:
      proxies = {
        bstack1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩஷ"): proxy
      }
  return proxies
def bstack1ll1ll1l_opy_():
  return bstack11ll1ll_opy_() and bstack1l1l11111_opy_() >= version.parse(bstack11l111ll_opy_)
def bstack1l111111l_opy_(config):
  bstack1lll11_opy_ = {}
  if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஸ") in config:
    bstack1lll11_opy_ =  config[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩஹ")]
  if bstack1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ஺") in config:
    bstack1lll11_opy_ = config[bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭஻")]
  proxy = bstack11lll1l1_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭஼")) and os.path.isfile(proxy):
      bstack1lll11_opy_[bstack1l_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ஽")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨா")):
        proxies = bstack1l1l11ll1_opy_(config, bstack111lll_opy_())
        if len(proxies) > 0:
          protocol, bstack1lllll1l_opy_ = proxies.popitem()
          if bstack1l_opy_ (u"ࠦ࠿࠵࠯ࠣி") in bstack1lllll1l_opy_:
            parsed_url = urlparse(bstack1lllll1l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l_opy_ (u"ࠧࡀ࠯࠰ࠤீ") + bstack1lllll1l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1lll11_opy_[bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩு")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1lll11_opy_[bstack1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪூ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1lll11_opy_[bstack1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫ௃")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1lll11_opy_[bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬ௄")] = str(parsed_url.password)
  return bstack1lll11_opy_
def bstack11l1ll_opy_(config):
  if bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ௅") in config:
    return config[bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩெ")]
  return {}
def bstack11ll1l1_opy_(caps):
  global bstack1l11ll1l1_opy_
  if bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ே") in caps:
    caps[bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧை")][bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭௉")] = True
    if bstack1l11ll1l1_opy_:
      caps[bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩொ")][bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫோ")] = bstack1l11ll1l1_opy_
  else:
    caps[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨௌ")] = True
    if bstack1l11ll1l1_opy_:
      caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ்ࠬ")] = bstack1l11ll1l1_opy_
def bstack11111ll1_opy_():
  global CONFIG
  if bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ௎") in CONFIG and CONFIG[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ௏")]:
    bstack1lll11_opy_ = bstack1l111111l_opy_(CONFIG)
    bstack1l1111l1_opy_(CONFIG[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪௐ")], bstack1lll11_opy_)
def bstack1l1111l1_opy_(key, bstack1lll11_opy_):
  global bstack1l1l1lll_opy_
  logger.info(bstack1l111l1_opy_)
  try:
    bstack1l1l1lll_opy_ = Local()
    bstack1lllll1_opy_ = {bstack1l_opy_ (u"ࠨ࡭ࡨࡽࠬ௑"): key}
    bstack1lllll1_opy_.update(bstack1lll11_opy_)
    logger.debug(bstack11l111l1l_opy_.format(str(bstack1lllll1_opy_)))
    bstack1l1l1lll_opy_.start(**bstack1lllll1_opy_)
    if bstack1l1l1lll_opy_.isRunning():
      logger.info(bstack1111lll1_opy_)
  except Exception as e:
    bstack1l1ll111l_opy_(bstack111ll1_opy_.format(str(e)))
def bstack1ll1111ll_opy_():
  global bstack1l1l1lll_opy_
  if bstack1l1l1lll_opy_.isRunning():
    logger.info(bstack11ll1_opy_)
    bstack1l1l1lll_opy_.stop()
  bstack1l1l1lll_opy_ = None
def bstack1ll1111l_opy_(bstack1l1l1_opy_=[]):
  global CONFIG
  bstack11lll1111_opy_ = []
  bstack11l1_opy_ = [bstack1l_opy_ (u"ࠩࡲࡷࠬ௒"), bstack1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭௓"), bstack1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ௔"), bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ௕"), bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ௖"), bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨௗ")]
  try:
    for err in bstack1l1l1_opy_:
      bstack11l1l11l1_opy_ = {}
      for k in bstack11l1_opy_:
        val = CONFIG[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௘")][int(err[bstack1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ௙")])].get(k)
        if val:
          bstack11l1l11l1_opy_[k] = val
      bstack11l1l11l1_opy_[bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ௚")] = {
        err[bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ௛")]: err[bstack1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ௜")]
      }
      bstack11lll1111_opy_.append(bstack11l1l11l1_opy_)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ௝") +str(e))
  finally:
    return bstack11lll1111_opy_
def bstack11l11lll_opy_():
  global bstack11l11ll11_opy_
  global bstack1l11l111_opy_
  global bstack11l11l1ll_opy_
  if bstack11l11ll11_opy_:
    logger.warning(bstack1llll1ll_opy_.format(str(bstack11l11ll11_opy_)))
  logger.info(bstack1lll11l1l_opy_)
  global bstack1l1l1lll_opy_
  if bstack1l1l1lll_opy_:
    bstack1ll1111ll_opy_()
  try:
    for driver in bstack1l11l111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1llllll1_opy_)
  bstack1llll1_opy_()
  if len(bstack11l11l1ll_opy_) > 0:
    message = bstack1ll1111l_opy_(bstack11l11l1ll_opy_)
    bstack1llll1_opy_(message)
  else:
    bstack1llll1_opy_()
def bstack111l1ll1_opy_(self, *args):
  logger.error(bstack11lll1l11_opy_)
  bstack11l11lll_opy_()
  sys.exit(1)
def bstack1l1ll111l_opy_(err):
  logger.critical(bstack1l1ll1l11_opy_.format(str(err)))
  bstack1llll1_opy_(bstack1l1ll1l11_opy_.format(str(err)))
  atexit.unregister(bstack11l11lll_opy_)
  sys.exit(1)
def bstack1l1l1l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1llll1_opy_(message)
  atexit.unregister(bstack11l11lll_opy_)
  sys.exit(1)
def bstack11lllll11_opy_():
  global CONFIG
  global bstack11llll1ll_opy_
  global bstack11ll111_opy_
  global bstack1ll11l1ll_opy_
  CONFIG = bstack1l1llll1_opy_()
  bstack1l11ll11l_opy_()
  bstack111111ll_opy_()
  CONFIG = bstack11ll1ll1l_opy_(CONFIG)
  update(CONFIG, bstack11ll111_opy_)
  update(CONFIG, bstack11llll1ll_opy_)
  CONFIG = bstack1l11lll1l_opy_(CONFIG)
  if bstack1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ௞") in CONFIG and str(CONFIG[bstack1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ௟")]).lower() == bstack1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ௠"):
    bstack1ll11l1ll_opy_ = False
  if (bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") in CONFIG and bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௢") in bstack11llll1ll_opy_) or (bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in CONFIG and bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") not in bstack11ll111_opy_):
    if os.getenv(bstack1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௥")):
      CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௦")] = os.getenv(bstack1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭௧"))
    else:
      bstack1l11l1l1_opy_()
  elif (bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") not in CONFIG and bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௩") in CONFIG) or (bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௪") in bstack11ll111_opy_ and bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௫") not in bstack11llll1ll_opy_):
    del(CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௬")])
  if bstack1l1l1lll1_opy_(CONFIG):
    bstack1l1ll111l_opy_(bstack1ll11ll1l_opy_)
  bstack1l1l1111_opy_()
  bstack11lll11_opy_()
  if bstack11l11l11l_opy_:
    CONFIG[bstack1l_opy_ (u"ࠨࡣࡳࡴࠬ௭")] = bstack111111_opy_(CONFIG)
    logger.info(bstack11l111l1_opy_.format(CONFIG[bstack1l_opy_ (u"ࠩࡤࡴࡵ࠭௮")]))
def bstack11lll11_opy_():
  global CONFIG
  global bstack11l11l11l_opy_
  if bstack1l_opy_ (u"ࠪࡥࡵࡶࠧ௯") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack11l111ll1_opy_)
    bstack11l11l11l_opy_ = True
def bstack111111_opy_(config):
  bstack1l11l1_opy_ = bstack1l_opy_ (u"ࠫࠬ௰")
  app = config[bstack1l_opy_ (u"ࠬࡧࡰࡱࠩ௱")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11ll1l1l_opy_:
      if os.path.exists(app):
        bstack1l11l1_opy_ = bstack1lllllll_opy_(config, app)
      elif bstack1l1l1l1_opy_(app):
        bstack1l11l1_opy_ = app
      else:
        bstack1l1ll111l_opy_(bstack11l11_opy_.format(app))
    else:
      if bstack1l1l1l1_opy_(app):
        bstack1l11l1_opy_ = app
      elif os.path.exists(app):
        bstack1l11l1_opy_ = bstack1lllllll_opy_(app)
      else:
        bstack1l1ll111l_opy_(bstack1ll1l1l1_opy_)
  else:
    if len(app) > 2:
      bstack1l1ll111l_opy_(bstack11lllll_opy_)
    elif len(app) == 2:
      if bstack1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௲") in app and bstack1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௳") in app:
        if os.path.exists(app[bstack1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௴")]):
          bstack1l11l1_opy_ = bstack1lllllll_opy_(config, app[bstack1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௵")], app[bstack1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௶")])
        else:
          bstack1l1ll111l_opy_(bstack11l11_opy_.format(app))
      else:
        bstack1l1ll111l_opy_(bstack11lllll_opy_)
    else:
      for key in app:
        if key in bstack1ll1l1l1l_opy_:
          if key == bstack1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௷"):
            if os.path.exists(app[key]):
              bstack1l11l1_opy_ = bstack1lllllll_opy_(config, app[key])
            else:
              bstack1l1ll111l_opy_(bstack11l11_opy_.format(app))
          else:
            bstack1l11l1_opy_ = app[key]
        else:
          bstack1l1ll111l_opy_(bstack1llll11_opy_)
  return bstack1l11l1_opy_
def bstack1l1l1l1_opy_(bstack1l11l1_opy_):
  import re
  bstack1lll1111l_opy_ = re.compile(bstack1l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௸"))
  bstack11l11111_opy_ = re.compile(bstack1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௹"))
  if bstack1l_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭௺") in bstack1l11l1_opy_ or re.fullmatch(bstack1lll1111l_opy_, bstack1l11l1_opy_) or re.fullmatch(bstack11l11111_opy_, bstack1l11l1_opy_):
    return True
  else:
    return False
def bstack1lllllll_opy_(config, path, bstack1ll11l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l_opy_ (u"ࠨࡴࡥࠫ௻")).read()).hexdigest()
  bstack1ll111ll1_opy_ = bstack1l1ll1_opy_(md5_hash)
  bstack1l11l1_opy_ = None
  if bstack1ll111ll1_opy_:
    logger.info(bstack1l1lll1ll_opy_.format(bstack1ll111ll1_opy_, md5_hash))
    return bstack1ll111ll1_opy_
  bstack1llll1l1_opy_ = MultipartEncoder(
    fields={
        bstack1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ௼"): (os.path.basename(path), open(os.path.abspath(path), bstack1l_opy_ (u"ࠪࡶࡧ࠭௽")), bstack1l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨ௾")),
        bstack1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௿"): bstack1ll11l_opy_
    }
  )
  response = requests.post(bstack1l11llll_opy_, data=bstack1llll1l1_opy_,
                         headers={bstack1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬఀ"): bstack1llll1l1_opy_.content_type}, auth=(config[bstack1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఁ")], config[bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫం")]))
  try:
    res = json.loads(response.text)
    bstack1l11l1_opy_ = res[bstack1l_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪః")]
    logger.info(bstack111llllll_opy_.format(bstack1l11l1_opy_))
    bstack1l1111l1l_opy_(md5_hash, bstack1l11l1_opy_)
  except ValueError as err:
    bstack1l1ll111l_opy_(bstack1111ll11_opy_.format(str(err)))
  return bstack1l11l1_opy_
def bstack1l1l1111_opy_():
  global CONFIG
  global bstack1l1111_opy_
  bstack11ll11ll1_opy_ = 0
  bstack1ll1l11l_opy_ = 1
  if bstack1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఄ") in CONFIG:
    bstack1ll1l11l_opy_ = CONFIG[bstack1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఅ")]
  if bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG:
    bstack11ll11ll1_opy_ = len(CONFIG[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")])
  bstack1l1111_opy_ = int(bstack1ll1l11l_opy_) * int(bstack11ll11ll1_opy_)
def bstack1l1ll1_opy_(md5_hash):
  bstack11ll1lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠧࡿࠩఈ")), bstack1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨఉ"), bstack1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪఊ"))
  if os.path.exists(bstack11ll1lll_opy_):
    bstack11l1ll1l_opy_ = json.load(open(bstack11ll1lll_opy_,bstack1l_opy_ (u"ࠪࡶࡧ࠭ఋ")))
    if md5_hash in bstack11l1ll1l_opy_:
      bstack11l1l1l11_opy_ = bstack11l1ll1l_opy_[md5_hash]
      bstack1lll11ll_opy_ = datetime.datetime.now()
      bstack1lll11l1_opy_ = datetime.datetime.strptime(bstack11l1l1l11_opy_[bstack1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఌ")], bstack1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ఍"))
      if (bstack1lll11ll_opy_ - bstack1lll11l1_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack11l1l1l11_opy_[bstack1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఎ")]):
        return None
      return bstack11l1l1l11_opy_[bstack1l_opy_ (u"ࠧࡪࡦࠪఏ")]
  else:
    return None
def bstack1l1111l1l_opy_(md5_hash, bstack1l11l1_opy_):
  bstack111l1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠨࢀࠪఐ")), bstack1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఑"))
  if not os.path.exists(bstack111l1l1l_opy_):
    os.makedirs(bstack111l1l1l_opy_)
  bstack11ll1lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠪࢂࠬఒ")), bstack1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఓ"), bstack1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఔ"))
  bstack1ll1l111_opy_ = {
    bstack1l_opy_ (u"࠭ࡩࡥࠩక"): bstack1l11l1_opy_,
    bstack1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఖ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬగ")),
    bstack1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఘ"): str(__version__)
  }
  if os.path.exists(bstack11ll1lll_opy_):
    bstack11l1ll1l_opy_ = json.load(open(bstack11ll1lll_opy_,bstack1l_opy_ (u"ࠪࡶࡧ࠭ఙ")))
  else:
    bstack11l1ll1l_opy_ = {}
  bstack11l1ll1l_opy_[md5_hash] = bstack1ll1l111_opy_
  with open(bstack11ll1lll_opy_, bstack1l_opy_ (u"ࠦࡼ࠱ࠢచ")) as outfile:
    json.dump(bstack11l1ll1l_opy_, outfile)
def bstack1l1l1l111_opy_(self):
  return
def bstack1l11l111l_opy_(self):
  return
def bstack1lll11lll_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1ll11lll_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack11l1l1111_opy_
  global bstack1ll1111l1_opy_
  global bstack111lll1l_opy_
  global bstack11ll1l111_opy_
  global bstack1llll1111_opy_
  global bstack1l1l1111l_opy_
  global bstack1l1ll1l1_opy_
  global bstack1l11l111_opy_
  global bstack1l1lll1_opy_
  CONFIG[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧఛ")] = str(bstack1l1l1111l_opy_) + str(__version__)
  command_executor = bstack111lll_opy_()
  logger.debug(bstack11l1l11ll_opy_.format(command_executor))
  proxy = bstack11l1ll1_opy_(CONFIG, proxy)
  bstack1l11111ll_opy_ = 0 if bstack1ll1111l1_opy_ < 0 else bstack1ll1111l1_opy_
  if bstack11ll1l111_opy_ is True:
    bstack1l11111ll_opy_ = int(multiprocessing.current_process().name)
  if bstack1llll1111_opy_ is True:
    bstack1l11111ll_opy_ = int(threading.current_thread().name)
  bstack1l111ll_opy_ = bstack11l1l11_opy_(CONFIG, bstack1l11111ll_opy_)
  logger.debug(bstack1l111l11_opy_.format(str(bstack1l111ll_opy_)))
  if bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪజ") in CONFIG and CONFIG[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫఝ")]:
    bstack11ll1l1_opy_(bstack1l111ll_opy_)
  if desired_capabilities:
    bstack1llll1ll1_opy_ = bstack11ll1ll1l_opy_(desired_capabilities)
    bstack1llll1ll1_opy_[bstack1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨఞ")] = bstack11l1lll11_opy_(CONFIG)
    bstack111ll111_opy_ = bstack11l1l11_opy_(bstack1llll1ll1_opy_)
    if bstack111ll111_opy_:
      bstack1l111ll_opy_ = update(bstack111ll111_opy_, bstack1l111ll_opy_)
    desired_capabilities = None
  if options:
    bstack1llll11ll_opy_(options, bstack1l111ll_opy_)
  if not options:
    options = bstack1lll11111_opy_(bstack1l111ll_opy_)
  if proxy and bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩట")):
    options.proxy(proxy)
  if options and bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩఠ")):
    desired_capabilities = None
  if (
      not options and not desired_capabilities
  ) or (
      bstack1l1l11111_opy_() < version.parse(bstack1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪడ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l111ll_opy_)
  logger.info(bstack1l111lll1_opy_)
  if bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬఢ")):
    bstack1l1ll1l1_opy_(self, command_executor=command_executor,
          options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬణ")):
    bstack1l1ll1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧత")):
    bstack1l1ll1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l1ll1l1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  try:
    bstack111lllll1_opy_ = bstack1l_opy_ (u"ࠨࠩథ")
    if bstack1l1l11111_opy_() >= version.parse(bstack1l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪద")):
      bstack111lllll1_opy_ = self.caps.get(bstack1l_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥధ"))
    else:
      bstack111lllll1_opy_ = self.capabilities.get(bstack1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦన"))
    if bstack111lllll1_opy_:
      if bstack1l1l11111_opy_() <= version.parse(bstack1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ఩")):
        self.command_executor._url = bstack1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢప") + bstack1l1lllll_opy_ + bstack1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦఫ")
      else:
        self.command_executor._url = bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥబ") + bstack111lllll1_opy_ + bstack1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥభ")
      logger.debug(bstack1ll1lll11_opy_.format(bstack111lllll1_opy_))
    else:
      logger.debug(bstack1l1l1ll11_opy_.format(bstack1l_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦమ")))
  except Exception as e:
    logger.debug(bstack1l1l1ll11_opy_.format(e))
  if bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪయ") in bstack1l1l1111l_opy_:
    bstack1l1l11ll_opy_(bstack1ll1111l1_opy_, bstack1l1lll1_opy_)
  bstack11l1l1111_opy_ = self.session_id
  bstack1l11l111_opy_.append(self)
  if bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨర") in CONFIG and bstack1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫఱ") in CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪల")][bstack1l11111ll_opy_]:
    bstack111lll1l_opy_ = CONFIG[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫళ")][bstack1l11111ll_opy_][bstack1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧఴ")]
  logger.debug(bstack111ll11_opy_.format(bstack11l1l1111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1llll111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll11l1_opy_
      if(bstack1l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧవ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭శ")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬష"), bstack1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨస")), bstack1l_opy_ (u"ࠧࡸࠩహ")) as fp:
          fp.write(bstack1l_opy_ (u"ࠣࠤ఺"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ఻")))):
          with open(args[1], bstack1l_opy_ (u"ࠪࡶ఼ࠬ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪఽ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11l1lll1_opy_)
            lines.insert(1, bstack11l1l1l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢా")), bstack1l_opy_ (u"࠭ࡷࠨి")) as bstack11ll1l1ll_opy_:
              bstack11ll1l1ll_opy_.writelines(lines)
        CONFIG[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩీ")] = str(bstack1l1l1111l_opy_) + str(__version__)
        bstack1l11111ll_opy_ = 0 if bstack1ll1111l1_opy_ < 0 else bstack1ll1111l1_opy_
        if bstack11ll1l111_opy_ is True:
          bstack1l11111ll_opy_ = int(threading.current_thread().getName())
        CONFIG[bstack1l_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣు")] = False
        CONFIG[bstack1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣూ")] = True
        bstack1l111ll_opy_ = bstack11l1l11_opy_(CONFIG, bstack1l11111ll_opy_)
        logger.debug(bstack1l111l11_opy_.format(str(bstack1l111ll_opy_)))
        if CONFIG[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧృ")]:
          bstack11ll1l1_opy_(bstack1l111ll_opy_)
        if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౄ") in CONFIG and bstack1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ౅") in CONFIG[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩె")][bstack1l11111ll_opy_]:
          bstack111lll1l_opy_ = CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪే")][bstack1l11111ll_opy_][bstack1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ై")]
        args.append(os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫ౉")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪొ"), bstack1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ో")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l111ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢౌ"))
      bstack1ll11l1_opy_ = True
      return bstack1l1l1ll1_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l11l1_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack11l1l1111_opy_
    global bstack1ll1111l1_opy_
    global bstack111lll1l_opy_
    global bstack11ll1l111_opy_
    global bstack1l1l1111l_opy_
    global bstack1l1ll1l1_opy_
    CONFIG[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ్")] = str(bstack1l1l1111l_opy_) + str(__version__)
    bstack1l11111ll_opy_ = 0 if bstack1ll1111l1_opy_ < 0 else bstack1ll1111l1_opy_
    if bstack11ll1l111_opy_ is True:
      bstack1l11111ll_opy_ = int(threading.current_thread().getName())
    CONFIG[bstack1l_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ౎")] = True
    bstack1l111ll_opy_ = bstack11l1l11_opy_(CONFIG, bstack1l11111ll_opy_)
    logger.debug(bstack1l111l11_opy_.format(str(bstack1l111ll_opy_)))
    if CONFIG[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ౏")]:
      bstack11ll1l1_opy_(bstack1l111ll_opy_)
    if bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౐") in CONFIG and bstack1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ౑") in CONFIG[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ౒")][bstack1l11111ll_opy_]:
      bstack111lll1l_opy_ = CONFIG[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౓")][bstack1l11111ll_opy_][bstack1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ౔")]
    import urllib
    import json
    bstack1l1lll11_opy_ = bstack1l_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ౕࠩ") + urllib.parse.quote(json.dumps(bstack1l111ll_opy_))
    browser = self.connect(bstack1l1lll11_opy_)
    return browser
except Exception as e:
    pass
def bstack1l1lllll1_opy_():
    global bstack1ll11l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11l11l1_opy_
        bstack1ll11l1_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1llll111_opy_
      bstack1ll11l1_opy_ = True
    except Exception as e:
      pass
def bstack111l111_opy_(context, bstack1lll1l_opy_):
  try:
    context.page.evaluate(bstack1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤౖ"), bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭౗")+ json.dumps(bstack1lll1l_opy_) + bstack1l_opy_ (u"ࠥࢁࢂࠨౘ"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤౙ"), e)
def bstack11lll11l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨౚ"), bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ౛") + json.dumps(message) + bstack1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪ౜") + json.dumps(level) + bstack1l_opy_ (u"ࠨࡿࢀࠫౝ"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧ౞"), e)
def bstack1111l1l1_opy_(context, status, message = bstack1l_opy_ (u"ࠥࠦ౟")):
  try:
    if(status == bstack1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦౠ")):
      context.page.evaluate(bstack1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨౡ"), bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡸࡥࡢࡵࡲࡲࠧࡀࠧౢ") + json.dumps(bstack1l_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡࠤౣ") + str(message)) + bstack1l_opy_ (u"ࠨ࠮ࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠬ౤") + json.dumps(status) + bstack1l_opy_ (u"ࠤࢀࢁࠧ౥"))
    else:
      context.page.evaluate(bstack1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ౦"), bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡷࡹࡧࡴࡶࡵࠥ࠾ࠬ౧") + json.dumps(status) + bstack1l_opy_ (u"ࠧࢃࡽࠣ౨"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡼࡿࠥ౩"), e)
def bstack1l1l11l1l_opy_(self, url):
  global bstack1111l11l_opy_
  try:
    bstack111l1l11_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1llll_opy_.format(str(err)))
  try:
    bstack1111l11l_opy_(self, url)
  except Exception as e:
    try:
      bstack1ll1lllll_opy_ = str(e)
      if any(err_msg in bstack1ll1lllll_opy_ for err_msg in bstack1ll111l1l_opy_):
        bstack111l1l11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1llll_opy_.format(str(err)))
    raise e
def bstack1lll1l111_opy_(self):
  global bstack1l1ll11ll_opy_
  bstack1l1ll11ll_opy_ = self
  return
def bstack111l1_opy_(self, test):
  global CONFIG
  global bstack1l1ll11ll_opy_
  global bstack11l1l1111_opy_
  global bstack1111l_opy_
  global bstack111lll1l_opy_
  global bstack1l1ll1ll1_opy_
  global bstack1ll11l1l_opy_
  global bstack1l11l111_opy_
  try:
    if not bstack11l1l1111_opy_:
      with open(os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠧࡿࠩ౪")), bstack1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ౫"), bstack1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ౬"))) as f:
        bstack1lll1l1_opy_ = json.loads(bstack1l_opy_ (u"ࠥࡿࠧ౭") + f.read().strip() + bstack1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭౮") + bstack1l_opy_ (u"ࠧࢃࠢ౯"))
        bstack11l1l1111_opy_ = bstack1lll1l1_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l11l111_opy_:
    for driver in bstack1l11l111_opy_:
      if bstack11l1l1111_opy_ == driver.session_id:
        if test:
          bstack11l1lll1l_opy_ = str(test.data)
        if not bstack111llll1l_opy_ and bstack11l1lll1l_opy_:
          bstack1ll11l11l_opy_ = {
            bstack1l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭౰"): bstack1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ౱"),
            bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ౲"): {
              bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ౳"): bstack11l1lll1l_opy_
            }
          }
          bstack1ll1ll_opy_ = bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ౴").format(json.dumps(bstack1ll11l11l_opy_))
          driver.execute_script(bstack1ll1ll_opy_)
        if bstack1111l_opy_:
          bstack1l111l1ll_opy_ = {
            bstack1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ౵"): bstack1l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ౶"),
            bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ౷"): {
              bstack1l_opy_ (u"ࠧࡥࡣࡷࡥࠬ౸"): bstack11l1lll1l_opy_ + bstack1l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ౹"),
              bstack1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ౺"): bstack1l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ౻")
            }
          }
          bstack1ll11l11l_opy_ = {
            bstack1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ౼"): bstack1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ౽"),
            bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ౾"): {
              bstack1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ౿"): bstack1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨಀ")
            }
          }
          if bstack1111l_opy_.status == bstack1l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧಁ"):
            bstack1llll11l_opy_ = bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨಂ").format(json.dumps(bstack1l111l1ll_opy_))
            driver.execute_script(bstack1llll11l_opy_)
            bstack1ll1ll_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩಃ").format(json.dumps(bstack1ll11l11l_opy_))
            driver.execute_script(bstack1ll1ll_opy_)
          elif bstack1111l_opy_.status == bstack1l_opy_ (u"ࠬࡌࡁࡊࡎࠪ಄"):
            reason = bstack1l_opy_ (u"ࠨࠢಅ")
            bstack1l1ll1ll_opy_ = bstack11l1lll1l_opy_ + bstack1l_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨಆ")
            if bstack1111l_opy_.message:
              reason = str(bstack1111l_opy_.message)
              bstack1l1ll1ll_opy_ = bstack1l1ll1ll_opy_ + bstack1l_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨಇ") + reason
            bstack1l111l1ll_opy_[bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬಈ")] = {
              bstack1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩಉ"): bstack1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪಊ"),
              bstack1l_opy_ (u"ࠬࡪࡡࡵࡣࠪಋ"): bstack1l1ll1ll_opy_
            }
            bstack1ll11l11l_opy_[bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩಌ")] = {
              bstack1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ಍"): bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨಎ"),
              bstack1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩಏ"): reason
            }
            bstack1llll11l_opy_ = bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨಐ").format(json.dumps(bstack1l111l1ll_opy_))
            driver.execute_script(bstack1llll11l_opy_)
            bstack1ll1ll_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ಑").format(json.dumps(bstack1ll11l11l_opy_))
            driver.execute_script(bstack1ll1ll_opy_)
  elif bstack11l1l1111_opy_:
    try:
      data = {}
      bstack11l1lll1l_opy_ = None
      if test:
        bstack11l1lll1l_opy_ = str(test.data)
      if not bstack111llll1l_opy_ and bstack11l1lll1l_opy_:
        data[bstack1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪಒ")] = bstack11l1lll1l_opy_
      if bstack1111l_opy_:
        if bstack1111l_opy_.status == bstack1l_opy_ (u"࠭ࡐࡂࡕࡖࠫಓ"):
          data[bstack1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧಔ")] = bstack1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨಕ")
        elif bstack1111l_opy_.status == bstack1l_opy_ (u"ࠩࡉࡅࡎࡒࠧಖ"):
          data[bstack1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪಗ")] = bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫಘ")
          if bstack1111l_opy_.message:
            data[bstack1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬಙ")] = str(bstack1111l_opy_.message)
      user = CONFIG[bstack1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨಚ")]
      key = CONFIG[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪಛ")]
      url = bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭ಜ").format(user, key, bstack11l1l1111_opy_)
      headers = {
        bstack1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨಝ"): bstack1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ಞ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack111l_opy_.format(str(e)))
  if bstack1l1ll11ll_opy_:
    bstack1ll11l1l_opy_(bstack1l1ll11ll_opy_)
  bstack1l1ll1ll1_opy_(self, test)
def bstack1lll1lll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l11l1l_opy_
  bstack11l11l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1111l_opy_
  bstack1111l_opy_ = self._test
def bstack11lll11ll_opy_():
  global bstack11ll11l11_opy_
  try:
    if os.path.exists(bstack11ll11l11_opy_):
      os.remove(bstack11ll11l11_opy_)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧಟ") + str(e))
def bstack1ll111lll_opy_():
  global bstack11ll11l11_opy_
  bstack11l1l1_opy_ = {}
  try:
    if not os.path.isfile(bstack11ll11l11_opy_):
      with open(bstack11ll11l11_opy_, bstack1l_opy_ (u"ࠬࡽࠧಠ")):
        pass
      with open(bstack11ll11l11_opy_, bstack1l_opy_ (u"ࠨࡷࠬࠤಡ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack11ll11l11_opy_):
      bstack11l1l1_opy_ = json.load(open(bstack11ll11l11_opy_, bstack1l_opy_ (u"ࠧࡳࡤࠪಢ")))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪಣ") + str(e))
  finally:
    return bstack11l1l1_opy_
def bstack1l1l11ll_opy_(platform_index, item_index):
  global bstack11ll11l11_opy_
  try:
    bstack11l1l1_opy_ = bstack1ll111lll_opy_()
    bstack11l1l1_opy_[item_index] = platform_index
    with open(bstack11ll11l11_opy_, bstack1l_opy_ (u"ࠤࡺ࠯ࠧತ")) as outfile:
      json.dump(bstack11l1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨಥ") + str(e))
def bstack111l1lll_opy_(bstack1l1l11_opy_):
  global CONFIG
  bstack11ll1111l_opy_ = bstack1l_opy_ (u"ࠫࠬದ")
  if not bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಧ") in CONFIG:
    logger.info(bstack1l_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪನ"))
  try:
    platform = CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ಩")][bstack1l1l11_opy_]
    if bstack1l_opy_ (u"ࠨࡱࡶࠫಪ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠩࡲࡷࠬಫ")]) + bstack1l_opy_ (u"ࠪ࠰ࠥ࠭ಬ")
    if bstack1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧಭ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨಮ")]) + bstack1l_opy_ (u"࠭ࠬࠡࠩಯ")
    if bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫರ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬಱ")]) + bstack1l_opy_ (u"ࠩ࠯ࠤࠬಲ")
    if bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬಳ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭಴")]) + bstack1l_opy_ (u"ࠬ࠲ࠠࠨವ")
    if bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫಶ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬಷ")]) + bstack1l_opy_ (u"ࠨ࠮ࠣࠫಸ")
    if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪಹ") in platform:
      bstack11ll1111l_opy_ += str(platform[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ಺")]) + bstack1l_opy_ (u"ࠫ࠱ࠦࠧ಻")
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲ಼ࠬ") + str(e))
  finally:
    if bstack11ll1111l_opy_[len(bstack11ll1111l_opy_) - 2:] == bstack1l_opy_ (u"࠭ࠬࠡࠩಽ"):
      bstack11ll1111l_opy_ = bstack11ll1111l_opy_[:-2]
    return bstack11ll1111l_opy_
def bstack1ll111l1_opy_(path, bstack11ll1111l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack111l1l1_opy_ = ET.parse(path)
    bstack1ll1l11_opy_ = bstack111l1l1_opy_.getroot()
    bstack11l111lll_opy_ = None
    for suite in bstack1ll1l11_opy_.iter(bstack1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ಾ")):
      if bstack1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨಿ") in suite.attrib:
        suite.attrib[bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧೀ")] += bstack1l_opy_ (u"ࠪࠤࠬು") + bstack11ll1111l_opy_
        bstack11l111lll_opy_ = suite
    bstack111ll11l_opy_ = None
    for robot in bstack1ll1l11_opy_.iter(bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪೂ")):
      bstack111ll11l_opy_ = robot
    bstack1llllll_opy_ = len(bstack111ll11l_opy_.findall(bstack1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫೃ")))
    if bstack1llllll_opy_ == 1:
      bstack111ll11l_opy_.remove(bstack111ll11l_opy_.findall(bstack1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬೄ"))[0])
      bstack1ll11l111_opy_ = ET.Element(bstack1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭೅"), attrib={bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ೆ"):bstack1l_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩೇ"), bstack1l_opy_ (u"ࠪ࡭ࡩ࠭ೈ"):bstack1l_opy_ (u"ࠫࡸ࠶ࠧ೉")})
      bstack111ll11l_opy_.insert(1, bstack1ll11l111_opy_)
      bstack1l11l1lll_opy_ = None
      for suite in bstack111ll11l_opy_.iter(bstack1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫೊ")):
        bstack1l11l1lll_opy_ = suite
      bstack1l11l1lll_opy_.append(bstack11l111lll_opy_)
      bstack111lll11_opy_ = None
      for status in bstack11l111lll_opy_.iter(bstack1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ೋ")):
        bstack111lll11_opy_ = status
      bstack1l11l1lll_opy_.append(bstack111lll11_opy_)
    bstack111l1l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬೌ") + str(e))
def bstack1111111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1l1l1l1_opy_
  global CONFIG
  if bstack1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬್ࠧ") in options:
    del options[bstack1l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ೎")]
  bstack1111lll_opy_ = bstack1ll111lll_opy_()
  for bstack11l111_opy_ in bstack1111lll_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪ೏"), str(bstack11l111_opy_), bstack1l_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨ೐"))
    bstack1ll111l1_opy_(path, bstack111l1lll_opy_(bstack1111lll_opy_[bstack11l111_opy_]))
  bstack11lll11ll_opy_()
  return bstack1l1l1l1l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11lll1ll_opy_(self, ff_profile_dir):
  global bstack1ll1l11l1_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1l11l1_opy_(self, ff_profile_dir)
def bstack11ll11l1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l11ll1l1_opy_
  bstack1lll1l1l_opy_ = []
  if bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೑") in CONFIG:
    bstack1lll1l1l_opy_ = CONFIG[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೒")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣ೓")],
      pabot_args[bstack1l_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤ೔")],
      argfile,
      pabot_args.get(bstack1l_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢೕ")),
      pabot_args[bstack1l_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨೖ")],
      platform[0],
      bstack1l11ll1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦ೗")] or [(bstack1l_opy_ (u"ࠧࠨ೘"), None)]
    for platform in enumerate(bstack1lll1l1l_opy_)
  ]
def bstack111lll1ll_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0,bstack1ll11l1l1_opy_=bstack1l_opy_ (u"࠭ࠧ೙")):
  global bstack1111l1l_opy_
  self.platform_index = platform_index
  self.bstack1lllll11l_opy_ = bstack1ll11l1l1_opy_
  bstack1111l1l_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack111l11ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1l1l1ll_opy_
  global bstack1ll1ll111_opy_
  if not bstack1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ೚") in item.options:
    item.options[bstack1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ೛")] = []
  for v in item.options[bstack1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ೜")]:
    if bstack1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩೝ") in v:
      item.options[bstack1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ೞ")].remove(v)
    if bstack1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ೟") in v:
      item.options[bstack1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨೠ")].remove(v)
  item.options[bstack1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩೡ")].insert(0, bstack1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪೢ").format(item.platform_index))
  item.options[bstack1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫೣ")].insert(0, bstack1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪ೤").format(item.bstack1lllll11l_opy_))
  if bstack1ll1ll111_opy_:
    item.options[bstack1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭೥")].insert(0, bstack1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ೦").format(bstack1ll1ll111_opy_))
  return bstack1l1l1l1ll_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack11l1111l_opy_(command, item_index):
  global bstack1ll1ll111_opy_
  if bstack1ll1ll111_opy_:
    command[0] = command[0].replace(bstack1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ೧"), bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫ೨") + str(item_index) + bstack1ll1ll111_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ೩"), bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭೪") + str(item_index), 1)
def bstack11ll11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1llllllll_opy_
  bstack11l1111l_opy_(command, item_index)
  return bstack1llllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1ll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1llllllll_opy_
  bstack11l1111l_opy_(command, item_index)
  return bstack1llllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1l11l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1llllllll_opy_
  bstack11l1111l_opy_(command, item_index)
  return bstack1llllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1ll1ll1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack11lll1ll1_opy_
  bstack11lll1_opy_ = bstack11lll1ll1_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1l_opy_ (u"ࠪࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡥࡡࡳࡴࠪ೫")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l_opy_ (u"ࠫࡪࡾࡣࡠࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࡣࡦࡸࡲࠨ೬")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11lll1_opy_
def bstack1l1111l11_opy_(self, name, context, *args):
  global bstack11l1l1l1l_opy_
  if name in [bstack1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭೭"), bstack1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ೮")]:
    bstack11l1l1l1l_opy_(self, name, context, *args)
  if name == bstack1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ೯"):
    try:
      if(not bstack111llll1l_opy_):
        bstack1lll1l_opy_ = str(self.feature.name)
        bstack111l111_opy_(context, bstack1lll1l_opy_)
        context.browser.execute_script(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭೰") + json.dumps(bstack1lll1l_opy_) + bstack1l_opy_ (u"ࠩࢀࢁࠬೱ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪೲ").format(str(e)))
  if name == bstack1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ೳ"):
    try:
      if not hasattr(self, bstack1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ೴")):
        self.driver_before_scenario = True
      if(not bstack111llll1l_opy_):
        bstack1l1ll11l_opy_ = args[0].name
        bstack1l1111l_opy_ = bstack1lll1l_opy_ = str(self.feature.name)
        bstack1lll1l_opy_ = bstack1l1111l_opy_ + bstack1l_opy_ (u"࠭ࠠ࠮ࠢࠪ೵") + bstack1l1ll11l_opy_
        if self.driver_before_scenario:
          bstack111l111_opy_(context, bstack1lll1l_opy_)
          context.browser.execute_script(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬ೶") + json.dumps(bstack1lll1l_opy_) + bstack1l_opy_ (u"ࠨࡿࢀࠫ೷"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪ೸").format(str(e)))
  if name == bstack1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ೹"):
    try:
      bstack11l11111l_opy_ = args[0].status.name
      if str(bstack11l11111l_opy_).lower() == bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ೺"):
        bstack1lll11l_opy_ = bstack1l_opy_ (u"ࠬ࠭೻")
        bstack1l1111lll_opy_ = bstack1l_opy_ (u"࠭ࠧ೼")
        bstack1l11111l_opy_ = bstack1l_opy_ (u"ࠧࠨ೽")
        try:
          import traceback
          bstack1lll11l_opy_ = self.exception.__class__.__name__
          bstack11ll1l11l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1l1111lll_opy_ = bstack1l_opy_ (u"ࠨࠢࠪ೾").join(bstack11ll1l11l_opy_)
          bstack1l11111l_opy_ = bstack11ll1l11l_opy_[-1]
        except Exception as e:
          logger.debug(bstack1ll1ll11_opy_.format(str(e)))
        bstack1lll11l_opy_ += bstack1l11111l_opy_
        bstack11lll11l_opy_(context, json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ೿") + str(bstack1l1111lll_opy_)), bstack1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤഀ"))
        if self.driver_before_scenario:
          bstack1111l1l1_opy_(context, bstack1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦഁ"), bstack1lll11l_opy_)
        context.browser.execute_script(bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪം") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧഃ") + str(bstack1l1111lll_opy_)) + bstack1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧഄ"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡩࡥ࡮ࡲࡥࡥࠤ࠯ࠤࠧࡸࡥࡢࡵࡲࡲࠧࡀࠠࠨഅ") + json.dumps(bstack1l_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨആ") + str(bstack1lll11l_opy_)) + bstack1l_opy_ (u"ࠪࢁࢂ࠭ഇ"))
      else:
        bstack11lll11l_opy_(context, bstack1l_opy_ (u"ࠦࡕࡧࡳࡴࡧࡧࠥࠧഈ"), bstack1l_opy_ (u"ࠧ࡯࡮ࡧࡱࠥഉ"))
        if self.driver_before_scenario:
          bstack1111l1l1_opy_(context, bstack1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨഊ"))
        context.browser.execute_script(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬഋ") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧഌ")) + bstack1l_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ഍"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦࡵࡧࡳࡴࡧࡧࠦࢂࢃࠧഎ"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ഏ").format(str(e)))
  if name == bstack1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬഐ"):
    try:
      if context.failed is True:
        bstack11l111l_opy_ = []
        bstack1111l1ll_opy_ = []
        bstack1ll11_opy_ = []
        bstack1l1lll1l_opy_ = bstack1l_opy_ (u"࠭ࠧ഑")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11l111l_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack11ll1l11l_opy_ = traceback.format_tb(exc_tb)
            bstack11l1l111_opy_ = bstack1l_opy_ (u"ࠧࠡࠩഒ").join(bstack11ll1l11l_opy_)
            bstack1111l1ll_opy_.append(bstack11l1l111_opy_)
            bstack1ll11_opy_.append(bstack11ll1l11l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll1ll11_opy_.format(str(e)))
        bstack1lll11l_opy_ = bstack1l_opy_ (u"ࠨࠩഓ")
        for i in range(len(bstack11l111l_opy_)):
          bstack1lll11l_opy_ += bstack11l111l_opy_[i] + bstack1ll11_opy_[i] + bstack1l_opy_ (u"ࠩ࡟ࡲࠬഔ")
        bstack1l1lll1l_opy_ = bstack1l_opy_ (u"ࠪࠤࠬക").join(bstack1111l1ll_opy_)
        if not self.driver_before_scenario:
          bstack11lll11l_opy_(context, bstack1l1lll1l_opy_, bstack1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥഖ"))
          bstack1111l1l1_opy_(context, bstack1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧഗ"), bstack1lll11l_opy_)
          context.browser.execute_script(bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫഘ") + json.dumps(bstack1l1lll1l_opy_) + bstack1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧങ"))
          context.browser.execute_script(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡩࡥ࡮ࡲࡥࡥࠤ࠯ࠤࠧࡸࡥࡢࡵࡲࡲࠧࡀࠠࠨച") + json.dumps(bstack1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢഛ") + str(bstack1lll11l_opy_)) + bstack1l_opy_ (u"ࠪࢁࢂ࠭ജ"))
      else:
        if not self.driver_before_scenario:
          bstack11lll11l_opy_(context, bstack1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢഝ") + str(self.feature.name) + bstack1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢഞ"), bstack1l_opy_ (u"ࠨࡩ࡯ࡨࡲࠦട"))
          bstack1111l1l1_opy_(context, bstack1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢഠ"))
          context.browser.execute_script(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ഡ") + json.dumps(bstack1l_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧഢ") + str(self.feature.name) + bstack1l_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧണ")) + bstack1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪത"))
          context.browser.execute_script(bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡰࡢࡵࡶࡩࡩࠨࡽࡾࠩഥ"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨദ").format(str(e)))
  if name in [bstack1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧധ"), bstack1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩന")]:
    bstack11l1l1l1l_opy_(self, name, context, *args)
    if (name == bstack1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪഩ") and self.driver_before_scenario) or (name == bstack1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪപ") and not self.driver_before_scenario):
      try:
        context.browser.quit()
      except Exception:
        pass
def bstack1l1ll111_opy_(config, startdir):
  return bstack1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤഫ").format(bstack1l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦബ"))
class Notset:
  def __repr__(self):
    return bstack1l_opy_ (u"ࠨ࠼ࡏࡑࡗࡗࡊ࡚࠾ࠣഭ")
notset = Notset()
def bstack1111ll1_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1lll1l1_opy_
  if str(name).lower() == bstack1l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧമ"):
    return bstack1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢയ")
  else:
    return bstack1l1lll1l1_opy_(self, name, default, skip)
def bstack11l11l11_opy_(item, when):
  global bstack1lll1l1l1_opy_
  try:
    bstack1lll1l1l1_opy_(item, when)
  except Exception as e:
    pass
def bstack1lllllll1_opy_():
  return
def bstack1llll1l1l_opy_(framework_name):
  global bstack1l1l1111l_opy_
  global bstack1ll11l1_opy_
  bstack1l1l1111l_opy_ = framework_name
  logger.info(bstack1l11l1l11_opy_.format(bstack1l1l1111l_opy_.split(bstack1l_opy_ (u"ࠩ࠰ࠫര"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    Service.start = bstack1l1l1l111_opy_
    Service.stop = bstack1l11l111l_opy_
    webdriver.Remote.__init__ = bstack1ll11lll_opy_
    webdriver.Remote.get = bstack1l1l11l1l_opy_
    WebDriver.close = bstack1lll11lll_opy_
    bstack1ll11l1_opy_ = True
  except Exception as e:
    pass
  bstack1l1lllll1_opy_()
  if not bstack1ll11l1_opy_:
    bstack1l1l1l1l_opy_(bstack1l_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧറ"), bstack1lll1l11l_opy_)
  if bstack1ll1ll1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l111llll_opy_
    except Exception as e:
      logger.error(bstack1lll1111_opy_.format(str(e)))
  if (bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪല") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11lll1ll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1lll1l111_opy_
      except Exception as e:
        logger.warn(bstack11111l1_opy_ + str(e))
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack11111l1_opy_)
    Output.end_test = bstack111l1_opy_
    TestStatus.__init__ = bstack1lll1lll1_opy_
    QueueItem.__init__ = bstack111lll1ll_opy_
    pabot._create_items = bstack11ll11l1_opy_
    try:
      from pabot import __version__ as bstack1ll1l1_opy_
      if version.parse(bstack1ll1l1_opy_) >= version.parse(bstack1l_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬള")):
        pabot._run = bstack1l11l11_opy_
      elif version.parse(bstack1ll1l1_opy_) >= version.parse(bstack1l_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭ഴ")):
        pabot._run = bstack1ll1111_opy_
      else:
        pabot._run = bstack11ll11111_opy_
    except Exception as e:
      pabot._run = bstack11ll11111_opy_
    pabot._create_command_for_execution = bstack111l11ll_opy_
    pabot._report_results = bstack1111111_opy_
  if bstack1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧവ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack1l11111_opy_)
    Runner.run_hook = bstack1l1111l11_opy_
    Step.run = bstack1ll1ll1l1_opy_
  if bstack1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨശ") in str(framework_name).lower():
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      from _pytest import runner
      pytest_selenium.pytest_report_header = bstack1l1ll111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1lllllll1_opy_
      Config.getoption = bstack1111ll1_opy_
      runner._update_current_test_var = bstack11l11l11_opy_
    except Exception as e:
      pass
def bstack111l1ll_opy_():
  global CONFIG
  if bstack1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩഷ") in CONFIG and int(CONFIG[bstack1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪസ")]) > 1:
    logger.warn(bstack1l111l11l_opy_)
def bstack1llll1lll_opy_(arg):
  arg.append(bstack1l_opy_ (u"ࠦ࠲࠳ࡣࡢࡲࡷࡹࡷ࡫࠽ࡴࡻࡶࠦഹ"))
  arg.append(bstack1l_opy_ (u"ࠧ࠳ࡗࠣഺ"))
  arg.append(bstack1l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤ഻"))
  global CONFIG
  bstack1llll1l1l_opy_(bstack1lll111ll_opy_)
  os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨ഼")] = CONFIG[bstack1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪഽ")]
  os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬാ")] = CONFIG[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ി")]
  from _pytest.config import main as bstack1l1lll11l_opy_
  bstack1l1lll11l_opy_(arg)
def bstack111llll_opy_(arg):
  bstack1llll1l1l_opy_(bstack11l1ll1ll_opy_)
  from behave.__main__ import main as bstack1lllll1ll_opy_
  bstack1lllll1ll_opy_(arg)
def bstack1llll111l_opy_():
  logger.info(bstack11l1l1lll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪീ"), help=bstack1l_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡣࡰࡰࡩ࡭࡬࠭ു"))
  parser.add_argument(bstack1l_opy_ (u"࠭࠭ࡶࠩൂ"), bstack1l_opy_ (u"ࠧ࠮࠯ࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫൃ"), help=bstack1l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧൄ"))
  parser.add_argument(bstack1l_opy_ (u"ࠩ࠰࡯ࠬ൅"), bstack1l_opy_ (u"ࠪ࠱࠲ࡱࡥࡺࠩെ"), help=bstack1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠬേ"))
  parser.add_argument(bstack1l_opy_ (u"ࠬ࠳ࡦࠨൈ"), bstack1l_opy_ (u"࠭࠭࠮ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ൉"), help=bstack1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ൊ"))
  bstack1l1ll1l_opy_ = parser.parse_args()
  try:
    bstack1l1l111l_opy_ = bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡨࡧࡱࡩࡷ࡯ࡣ࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬോ")
    if bstack1l1ll1l_opy_.framework and bstack1l1ll1l_opy_.framework not in (bstack1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩൌ"), bstack1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶്ࠫ")):
      bstack1l1l111l_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪൎ")
    bstack11ll1111_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1l111l_opy_)
    bstack1l11llll1_opy_ = open(bstack11ll1111_opy_, bstack1l_opy_ (u"ࠬࡸࠧ൏"))
    bstack1ll11lll1_opy_ = bstack1l11llll1_opy_.read()
    bstack1l11llll1_opy_.close()
    if bstack1l1ll1l_opy_.username:
      bstack1ll11lll1_opy_ = bstack1ll11lll1_opy_.replace(bstack1l_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭൐"), bstack1l1ll1l_opy_.username)
    if bstack1l1ll1l_opy_.key:
      bstack1ll11lll1_opy_ = bstack1ll11lll1_opy_.replace(bstack1l_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ൑"), bstack1l1ll1l_opy_.key)
    if bstack1l1ll1l_opy_.framework:
      bstack1ll11lll1_opy_ = bstack1ll11lll1_opy_.replace(bstack1l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ൒"), bstack1l1ll1l_opy_.framework)
    file_name = bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ൓")
    file_path = os.path.abspath(file_name)
    bstack11llll11l_opy_ = open(file_path, bstack1l_opy_ (u"ࠪࡻࠬൔ"))
    bstack11llll11l_opy_.write(bstack1ll11lll1_opy_)
    bstack11llll11l_opy_.close()
    logger.info(bstack11ll1ll1_opy_)
    try:
      os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ൕ")] = bstack1l1ll1l_opy_.framework if bstack1l1ll1l_opy_.framework != None else bstack1l_opy_ (u"ࠧࠨൖ")
      config = yaml.safe_load(bstack1ll11lll1_opy_)
      config[bstack1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ൗ")] = bstack1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠭ࡴࡧࡷࡹࡵ࠭൘")
      bstack1l11111l1_opy_(bstack11llll1_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1l1ll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11l1lll_opy_.format(str(e)))
def bstack1l11111l1_opy_(bstack11lll_opy_, config, bstack11l1llll_opy_ = {}):
  global bstack1ll11l1ll_opy_
  if not config:
    return
  bstack1ll1l11ll_opy_ = bstack1lll111l_opy_ if not bstack1ll11l1ll_opy_ else ( bstack111ll1ll_opy_ if bstack1l_opy_ (u"ࠨࡣࡳࡴࠬ൙") in config else bstack111111l1_opy_ )
  data = {
    bstack1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ൚"): config[bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ൛")],
    bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ൜"): config[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ൝")],
    bstack1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ൞"): bstack11lll_opy_,
    bstack1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪൟ"): {
      bstack1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ൠ"): str(config[bstack1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩൡ")]) if bstack1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪൢ") in config else bstack1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧൣ"),
      bstack1l_opy_ (u"ࠬࡸࡥࡧࡧࡵࡶࡪࡸࠧ൤"): bstack1111ll_opy_(os.getenv(bstack1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠣ൥"), bstack1l_opy_ (u"ࠢࠣ൦"))),
      bstack1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ൧"): bstack1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ൨"),
      bstack1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫ൩"): bstack1ll1l11ll_opy_,
      bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ൪"): config[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ൫")]if config[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ൬")] else bstack1l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ൭"),
      bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ൮"): str(config[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ൯")]) if bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ൰") in config else bstack1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ൱"),
      bstack1l_opy_ (u"ࠬࡵࡳࠨ൲"): sys.platform,
      bstack1l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ൳"): socket.gethostname()
    }
  }
  update(data[bstack1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ൴")], bstack11l1llll_opy_)
  try:
    response = bstack1l111111_opy_(bstack1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭൵"), bstack11l11l_opy_, data, config)
    if response:
      logger.debug(bstack1ll111ll_opy_.format(bstack11lll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11llllll_opy_.format(str(e)))
def bstack1l111111_opy_(type, url, data, config):
  bstack1l1l1ll_opy_ = bstack1l1llll1l_opy_.format(url)
  proxies = bstack1l1l11ll1_opy_(config, bstack1l1l1ll_opy_)
  if type == bstack1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ൶"):
    response = requests.post(bstack1l1l1ll_opy_, json=data,
                    headers={bstack1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ൷"): bstack1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ൸")}, auth=(config[bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ൹")], config[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩൺ")]), proxies=proxies)
  return response
def bstack1111ll_opy_(framework):
  return bstack1l_opy_ (u"ࠢࡼࡿ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦൻ").format(str(framework), __version__) if framework else bstack1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤർ").format(__version__)
def bstack1111llll_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack11lllll11_opy_()
    logger.debug(bstack1ll1l1ll_opy_.format(str(CONFIG)))
    bstack11lll111l_opy_()
    bstack1l1l11l_opy_()
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨൽ") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11lll111_opy_
  atexit.register(bstack11l11lll_opy_)
  signal.signal(signal.SIGINT, bstack111l1ll1_opy_)
  signal.signal(signal.SIGTERM, bstack111l1ll1_opy_)
def bstack11lll111_opy_(exctype, value, traceback):
  global bstack1l11l111_opy_
  try:
    for driver in bstack1l11l111_opy_:
      driver.execute_script(
        bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡶࡸࡦࡺࡵࡴࠤ࠽ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱ࠦࠢࡳࡧࡤࡷࡴࡴࠢ࠻ࠢࠪൾ") + json.dumps(bstack1l_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢൿ") + str(value)) + bstack1l_opy_ (u"ࠬࢃࡽࠨ඀"))
  except Exception:
    pass
  bstack1llll1_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1llll1_opy_(message = bstack1l_opy_ (u"࠭ࠧඁ")):
  global CONFIG
  try:
    if message:
      bstack11l1llll_opy_ = {
        bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ං"): str(message)
      }
      bstack1l11111l1_opy_(bstack1l1111ll_opy_, CONFIG, bstack11l1llll_opy_)
    else:
      bstack1l11111l1_opy_(bstack1l1111ll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11ll1l1l1_opy_.format(str(e)))
def bstack111l111l_opy_(bstack11ll11lll_opy_, size):
  bstack11l1ll11l_opy_ = []
  while len(bstack11ll11lll_opy_) > size:
    bstack1ll11ll1_opy_ = bstack11ll11lll_opy_[:size]
    bstack11l1ll11l_opy_.append(bstack1ll11ll1_opy_)
    bstack11ll11lll_opy_   = bstack11ll11lll_opy_[size:]
  bstack11l1ll11l_opy_.append(bstack11ll11lll_opy_)
  return bstack11l1ll11l_opy_
def run_on_browserstack(bstack11lll1lll_opy_=None, bstack111lllll_opy_=None):
  global CONFIG
  global bstack1l1lllll_opy_
  bstack111lll1_opy_ = bstack1l_opy_ (u"ࠨࠩඃ")
  if bstack11lll1lll_opy_:
    CONFIG = bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ඄")]
    bstack1l1lllll_opy_ = bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫඅ")]
    bstack111lll1_opy_ = bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫආ")
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll11llll_opy_)
    return
  if sys.argv[1] == bstack1l_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨඇ")  or sys.argv[1] == bstack1l_opy_ (u"࠭࠭ࡷࠩඈ"):
    logger.info(bstack1l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃࠧඉ").format(__version__))
    return
  if sys.argv[1] == bstack1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧඊ"):
    bstack1llll111l_opy_()
    return
  args = sys.argv
  bstack1111llll_opy_()
  global bstack1l1111_opy_
  global bstack11ll1l111_opy_
  global bstack1llll1111_opy_
  global bstack1ll1111l1_opy_
  global bstack1l11ll1l1_opy_
  global bstack1ll1ll111_opy_
  global bstack11l11l1ll_opy_
  if not bstack111lll1_opy_:
    if args[1] == bstack1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩඋ") or args[1] == bstack1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫඌ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫඍ")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඎ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬඏ")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ඐ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧඑ")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪඒ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫඓ")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫඔ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬඕ")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ඖ"):
      bstack111lll1_opy_ = bstack1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ඗")
      args = args[2:]
    else:
      if not bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ඘") in CONFIG or str(CONFIG[bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ඙")]).lower() in [bstack1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪක"), bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬඛ")]:
        bstack111lll1_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬග")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩඝ")]).lower() == bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ඞ"):
        bstack111lll1_opy_ = bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧඟ")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬච")]).lower() == bstack1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩඡ"):
        bstack111lll1_opy_ = bstack1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪජ")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨඣ")]).lower() == bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ඤ"):
        bstack111lll1_opy_ = bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧඥ")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫඦ")]).lower() == bstack1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩට"):
        bstack111lll1_opy_ = bstack1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪඨ")
        args = args[1:]
      else:
        os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ඩ")] = bstack111lll1_opy_
        bstack1l1ll111l_opy_(bstack1l11l1ll_opy_)
  global bstack1l1l1ll1_opy_
  if bstack11lll1lll_opy_:
    try:
      os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧඪ")] = bstack111lll1_opy_
      bstack1l11111l1_opy_(bstack111l11l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack11ll1l1l1_opy_.format(str(e)))
  global bstack1l1ll1l1_opy_
  global bstack1l1ll1ll1_opy_
  global bstack1ll11l1l_opy_
  global bstack11l11l1l_opy_
  global bstack1ll1l11l1_opy_
  global bstack1llllllll_opy_
  global bstack1111l1l_opy_
  global bstack1l1l1l1ll_opy_
  global bstack1l111_opy_
  global bstack11l1l1l1l_opy_
  global bstack11lll1ll1_opy_
  global bstack1111l11l_opy_
  global bstack1lll1l1ll_opy_
  global bstack1l1lll1l1_opy_
  global bstack1lll1l1l1_opy_
  global bstack1l1l1l1l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l1ll1l1_opy_ = webdriver.Remote.__init__
    bstack1l111_opy_ = WebDriver.close
    bstack1111l11l_opy_ = WebDriver.get
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l1l1ll1_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack11ll1ll_opy_():
    if bstack1l1l11111_opy_() < version.parse(bstack11l111ll_opy_):
      logger.error(bstack1l111lll_opy_.format(bstack1l1l11111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lll1l1ll_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1lll1111_opy_.format(str(e)))
  if bstack111lll1_opy_ != bstack1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ණ") or (bstack111lll1_opy_ == bstack1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧඬ") and not bstack11lll1lll_opy_):
    bstack111l1111_opy_()
  if (bstack111lll1_opy_ in [bstack1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧත"), bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨථ"), bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫද")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11lll1ll_opy_
        bstack1ll11l1l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11111l1_opy_ + str(e))
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack11111l1_opy_)
    if bstack111lll1_opy_ != bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬධ"):
      bstack11lll11ll_opy_()
    bstack1l1ll1ll1_opy_ = Output.end_test
    bstack11l11l1l_opy_ = TestStatus.__init__
    bstack1llllllll_opy_ = pabot._run
    bstack1111l1l_opy_ = QueueItem.__init__
    bstack1l1l1l1ll_opy_ = pabot._create_command_for_execution
    bstack1l1l1l1l1_opy_ = pabot._report_results
  if bstack111lll1_opy_ == bstack1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬන"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack1l11111_opy_)
    bstack11l1l1l1l_opy_ = Runner.run_hook
    bstack11lll1ll1_opy_ = Step.run
  if bstack111lll1_opy_ == bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭඲"):
    try:
      from _pytest.config import Config
      bstack1l1lll1l1_opy_ = Config.getoption
      from _pytest import runner
      bstack1lll1l1l1_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1l1l1l11_opy_)
  if bstack111lll1_opy_ == bstack1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧඳ"):
    bstack11ll1l111_opy_ = True
    if bstack11lll1lll_opy_:
      bstack1l11ll1l1_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬප"), {}).get(bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫඵ"))
      bstack1llll1l1l_opy_(bstack11ll111l1_opy_)
      sys.path.append(os.path.dirname(os.path.abspath(bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭බ")])))
      mod_globals = globals()
      mod_globals[bstack1l_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭භ")] = bstack1l_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧම")
      mod_globals[bstack1l_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨඹ")] = os.path.abspath(bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪය")])
      global bstack1l11l111_opy_
      try:
        exec(open(bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫර")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l_opy_ (u"ࠩࡆࡥࡺ࡭ࡨࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠩ඼").format(str(e)))
          for driver in bstack1l11l111_opy_:
            bstack111lllll_opy_.append({
              bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨල"): bstack11lll1lll_opy_[bstack1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ඾")],
              bstack1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ඿"): str(e),
              bstack1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬව"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࠮ࠣࠦࡷ࡫ࡡࡴࡱࡱࠦ࠿ࠦࠧශ") + json.dumps(bstack1l_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦෂ") + str(e)) + bstack1l_opy_ (u"ࠩࢀࢁࠬස"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l11l111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      bstack11111ll1_opy_()
      bstack111l1ll_opy_()
      if bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭හ") in CONFIG:
        bstack1ll1l1l_opy_ = {
          bstack1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧළ"): args[0],
          bstack1l_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬෆ"): CONFIG,
          bstack1l_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ෇"): bstack1l1lllll_opy_
        }
        bstack111ll1l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l111_opy_ = manager.list()
        for index, platform in enumerate(CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ෈")]):
          bstack1ll1l1l_opy_[bstack1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ෉")] = index
          bstack111ll1l1_opy_.append(multiprocessing.Process(name=str(index),
                                        target=run_on_browserstack, args=(bstack1ll1l1l_opy_, bstack1111l111_opy_)))
        for t in bstack111ll1l1_opy_:
          t.start()
        for t in bstack111ll1l1_opy_:
          t.join()
        bstack11l11l1ll_opy_ = list(bstack1111l111_opy_)
      else:
        bstack1llll1l1l_opy_(bstack11ll111l1_opy_)
        sys.path.append(os.path.dirname(os.path.abspath(args[0])))
        mod_globals = globals()
        mod_globals[bstack1l_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢ්ࠫ")] = bstack1l_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬ෋")
        mod_globals[bstack1l_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭෌")] = os.path.abspath(args[0])
        exec(open(args[0]).read(), mod_globals)
  elif bstack111lll1_opy_ == bstack1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ෍") or bstack111lll1_opy_ == bstack1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ෎"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack11111l1_opy_)
    bstack11111ll1_opy_()
    bstack1llll1l1l_opy_(bstack11lll1l1l_opy_)
    if bstack1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬා") in args:
      i = args.index(bstack1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ැ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1l1111_opy_))
    args.insert(0, str(bstack1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧෑ")))
    pabot.main(args)
  elif bstack111lll1_opy_ == bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫි"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack11111l1_opy_)
    for a in args:
      if bstack1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪී") in a:
        bstack1ll1111l1_opy_ = int(a.split(bstack1l_opy_ (u"ࠬࡀࠧු"))[1])
      if bstack1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ෕") in a:
        bstack1l11ll1l1_opy_ = str(a.split(bstack1l_opy_ (u"ࠧ࠻ࠩූ"))[1])
      if bstack1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨ෗") in a:
        bstack1ll1ll111_opy_ = str(a.split(bstack1l_opy_ (u"ࠩ࠽ࠫෘ"))[1])
    bstack11l1lllll_opy_ = None
    if bstack1l_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩෙ") in args:
      i = args.index(bstack1l_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪේ"))
      args.pop(i)
      bstack11l1lllll_opy_ = args.pop(i)
    if bstack11l1lllll_opy_ is not None:
      global bstack1l1lll1_opy_
      bstack1l1lll1_opy_ = bstack11l1lllll_opy_
    bstack1llll1l1l_opy_(bstack11lll1l1l_opy_)
    run_cli(args)
  elif bstack111lll1_opy_ == bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬෛ"):
    try:
      from _pytest.config import _prepareconfig
      from _pytest.config import Config
      from _pytest import runner
      import importlib
      bstack111l11l_opy_ = importlib.find_loader(bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨො"))
    except Exception as e:
      logger.warn(e, bstack1l1l1l11_opy_)
    bstack11111ll1_opy_()
    try:
      if bstack1l_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩෝ") in args:
        i = args.index(bstack1l_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪෞ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬෟ") in args:
        i = args.index(bstack1l_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭෠"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l_opy_ (u"ࠫ࠲ࡶࠧ෡") in args:
        i = args.index(bstack1l_opy_ (u"ࠬ࠳ࡰࠨ෢"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ෣") in args:
        i = args.index(bstack1l_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ෤"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l_opy_ (u"ࠨ࠯ࡱࠫ෥") in args:
        i = args.index(bstack1l_opy_ (u"ࠩ࠰ࡲࠬ෦"))
        args.pop(i+1)
        args.pop(i)
    except Exception as exc:
      logger.error(str(exc))
    config = _prepareconfig(args)
    bstack11ll1ll11_opy_ = config.args
    bstack1lll1ll1_opy_ = config.invocation_params.args
    bstack1lll1ll1_opy_ = list(bstack1lll1ll1_opy_)
    bstack1l1l1ll1l_opy_ = []
    for arg in bstack1lll1ll1_opy_:
      for spec in bstack11ll1ll11_opy_:
        if os.path.normpath(arg) != os.path.normpath(spec):
          bstack1l1l1ll1l_opy_.append(arg)
    import platform as pf
    if pf.system().lower() == bstack1l_opy_ (u"ࠪࡻ࡮ࡴࡤࡰࡹࡶࠫ෧"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11ll1ll11_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll1l111l_opy_)))
                    for bstack1ll1l111l_opy_ in bstack11ll1ll11_opy_]
    if (bstack111llll1l_opy_):
      bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ෨"))
      bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"࡚ࠬࡲࡶࡧࠪ෩"))
    bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"࠭࠭ࡱࠩ෪"))
    bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠬ෫"))
    bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪ෬"))
    bstack1l1l1ll1l_opy_.append(bstack1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ෭"))
    bstack1ll11111_opy_ = []
    for spec in bstack11ll1ll11_opy_:
      bstack1llllll1l_opy_ = []
      bstack1llllll1l_opy_.append(spec)
      bstack1llllll1l_opy_ += bstack1l1l1ll1l_opy_
      bstack1ll11111_opy_.append(bstack1llllll1l_opy_)
    bstack1llll1111_opy_ = True
    bstack11ll111ll_opy_ = 1
    if bstack1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ෮") in CONFIG:
      bstack11ll111ll_opy_ = CONFIG[bstack1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ෯")]
    bstack1111l11_opy_ = int(bstack11ll111ll_opy_)*int(len(CONFIG[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෰")]))
    execution_items = []
    for index, _ in enumerate(CONFIG[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෱")]):
      for bstack1llllll1l_opy_ in bstack1ll11111_opy_:
        item = {}
        item[bstack1l_opy_ (u"ࠧࡢࡴࡪࠫෲ")] = bstack1llllll1l_opy_
        item[bstack1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧෳ")] = index
        execution_items.append(item)
    bstack1ll111_opy_ = bstack111l111l_opy_(execution_items, bstack1111l11_opy_)
    for execution_item in bstack1ll111_opy_:
      bstack111ll1l1_opy_ = []
      for item in execution_item:
        bstack111ll1l1_opy_.append(bstack11llll11_opy_(name=str(item[bstack1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ෴")]),
                                            target=bstack1llll1lll_opy_,
                                            args=(item[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࠧ෵")],)))
      for t in bstack111ll1l1_opy_:
        t.start()
      for t in bstack111ll1l1_opy_:
        t.join()
  elif bstack111lll1_opy_ == bstack1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ෶"):
    try:
      from behave.__main__ import main as bstack1lllll1ll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1l1l1l_opy_(e, bstack1l11111_opy_)
    bstack11111ll1_opy_()
    bstack1llll1111_opy_ = True
    bstack11ll111ll_opy_ = 1
    if bstack1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ෷") in CONFIG:
      bstack11ll111ll_opy_ = CONFIG[bstack1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭෸")]
    bstack1111l11_opy_ = int(bstack11ll111ll_opy_)*int(len(CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ෹")]))
    config = Configuration(args)
    bstack11ll1ll11_opy_ = config.paths
    bstack11l11l111_opy_ = []
    for arg in args:
      if os.path.normpath(arg) not in bstack11ll1ll11_opy_:
        bstack11l11l111_opy_.append(arg)
    import platform as pf
    if pf.system().lower() == bstack1l_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩ෺"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11ll1ll11_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll1l111l_opy_)))
                    for bstack1ll1l111l_opy_ in bstack11ll1ll11_opy_]
    bstack1ll11111_opy_ = []
    for spec in bstack11ll1ll11_opy_:
      bstack1llllll1l_opy_ = []
      bstack1llllll1l_opy_ += bstack11l11l111_opy_
      bstack1llllll1l_opy_.append(spec)
      bstack1ll11111_opy_.append(bstack1llllll1l_opy_)
    execution_items = []
    for index, _ in enumerate(CONFIG[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ෻")]):
      for bstack1llllll1l_opy_ in bstack1ll11111_opy_:
        item = {}
        item[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࠧ෼")] = bstack1l_opy_ (u"ࠫࠥ࠭෽").join(bstack1llllll1l_opy_)
        item[bstack1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ෾")] = index
        execution_items.append(item)
    bstack1ll111_opy_ = bstack111l111l_opy_(execution_items, bstack1111l11_opy_)
    for execution_item in bstack1ll111_opy_:
      bstack111ll1l1_opy_ = []
      for item in execution_item:
        bstack111ll1l1_opy_.append(bstack11llll11_opy_(name=str(item[bstack1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ෿")]),
                                            target=bstack111llll_opy_,
                                            args=(item[bstack1l_opy_ (u"ࠧࡢࡴࡪࠫ฀")],)))
      for t in bstack111ll1l1_opy_:
        t.start()
      for t in bstack111ll1l1_opy_:
        t.join()
  else:
    bstack1l1ll111l_opy_(bstack1l11l1ll_opy_)
  if not bstack11lll1lll_opy_:
    bstack1l1lll111_opy_()
def bstack1l1lll111_opy_():
  [bstack11ll1lll1_opy_, bstack11llll111_opy_] = bstack1l1l1llll_opy_()
  if bstack11ll1lll1_opy_ is not None and bstack11111lll_opy_() != -1:
    sessions = bstack1l111l1l1_opy_(bstack11ll1lll1_opy_)
    bstack1l111l1l_opy_(sessions, bstack11llll111_opy_)
def bstack1l11ll1ll_opy_(bstack1ll11ll_opy_):
    if bstack1ll11ll_opy_:
        return bstack1ll11ll_opy_.capitalize()
    else:
        return bstack1ll11ll_opy_
def bstack1l1ll11l1_opy_(bstack1llllll11_opy_):
    if bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ก") in bstack1llllll11_opy_ and bstack1llllll11_opy_[bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧข")] != bstack1l_opy_ (u"ࠪࠫฃ"):
        return bstack1llllll11_opy_[bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩค")]
    else:
        bstack11l1lll1l_opy_ = bstack1l_opy_ (u"ࠧࠨฅ")
        if bstack1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ฆ") in bstack1llllll11_opy_ and bstack1llllll11_opy_[bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧง")] != None:
            bstack11l1lll1l_opy_ += bstack1llllll11_opy_[bstack1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨจ")] + bstack1l_opy_ (u"ࠤ࠯ࠤࠧฉ")
            if bstack1llllll11_opy_[bstack1l_opy_ (u"ࠪࡳࡸ࠭ช")] == bstack1l_opy_ (u"ࠦ࡮ࡵࡳࠣซ"):
                bstack11l1lll1l_opy_ += bstack1l_opy_ (u"ࠧ࡯ࡏࡔࠢࠥฌ")
            bstack11l1lll1l_opy_ += (bstack1llllll11_opy_[bstack1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪญ")] or bstack1l_opy_ (u"ࠧࠨฎ"))
            return bstack11l1lll1l_opy_
        else:
            bstack11l1lll1l_opy_ += bstack1l11ll1ll_opy_(bstack1llllll11_opy_[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩฏ")]) + bstack1l_opy_ (u"ࠤࠣࠦฐ") + (bstack1llllll11_opy_[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬฑ")] or bstack1l_opy_ (u"ࠫࠬฒ")) + bstack1l_opy_ (u"ࠧ࠲ࠠࠣณ")
            if bstack1llllll11_opy_[bstack1l_opy_ (u"࠭࡯ࡴࠩด")] == bstack1l_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣต"):
                bstack11l1lll1l_opy_ += bstack1l_opy_ (u"࡙ࠣ࡬ࡲࠥࠨถ")
            bstack11l1lll1l_opy_ += bstack1llllll11_opy_[bstack1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ท")] or bstack1l_opy_ (u"ࠪࠫธ")
            return bstack11l1lll1l_opy_
def bstack1l1111ll1_opy_(bstack1lll11l11_opy_):
    if bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠦࡩࡵ࡮ࡦࠤน"):
        return bstack1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨบ")
    elif bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨป"):
        return bstack1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪผ")
    elif bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣฝ"):
        return bstack1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩพ")
    elif bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤฟ"):
        return bstack1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ภ")
    elif bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨม"):
        return bstack1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫย")
    elif bstack1lll11l11_opy_ == bstack1l_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣร"):
        return bstack1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩฤ")
    else:
        return bstack1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭ล")+bstack1l11ll1ll_opy_(bstack1lll11l11_opy_)+bstack1l_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩฦ")
def bstack1l1ll1l1l_opy_(session):
    return bstack1l_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫว").format(session[bstack1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩศ")],bstack1l1ll11l1_opy_(session), bstack1l1111ll1_opy_(session[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬษ")]), bstack1l1111ll1_opy_(session[bstack1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧส")]), bstack1l11ll1ll_opy_(session[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩห")] or session[bstack1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩฬ")] or bstack1l_opy_ (u"ࠪࠫอ")) + bstack1l_opy_ (u"ࠦࠥࠨฮ") + (session[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧฯ")] or bstack1l_opy_ (u"࠭ࠧะ")), session[bstack1l_opy_ (u"ࠧࡰࡵࠪั")] + bstack1l_opy_ (u"ࠣࠢࠥา") + session[bstack1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ำ")], session[bstack1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬิ")] or bstack1l_opy_ (u"ࠫࠬี"), session[bstack1l_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩึ")] if session[bstack1l_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪื")] else bstack1l_opy_ (u"ࠧࠨุ"))
def bstack1l111l1l_opy_(sessions, bstack11llll111_opy_):
  try:
    bstack1l1llllll_opy_ = bstack1l_opy_ (u"ࠣࠤู")
    if not os.path.exists(bstack1l11l11ll_opy_):
      os.mkdir(bstack1l11l11ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲฺࠧ")), bstack1l_opy_ (u"ࠪࡶࠬ฻")) as f:
      bstack1l1llllll_opy_ = f.read()
    bstack1l1llllll_opy_ = bstack1l1llllll_opy_.replace(bstack1l_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨ฼"), str(len(sessions)))
    bstack1l1llllll_opy_ = bstack1l1llllll_opy_.replace(bstack1l_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬ฽"), bstack11llll111_opy_)
    bstack1l1llllll_opy_ = bstack1l1llllll_opy_.replace(bstack1l_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧ฾"), sessions[0].get(bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨࠫ฿")) if sessions[0] else bstack1l_opy_ (u"ࠨࠩเ"))
    with open(os.path.join(bstack1l11l11ll_opy_, bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭แ")), bstack1l_opy_ (u"ࠪࡻࠬโ")) as stream:
      stream.write(bstack1l1llllll_opy_.split(bstack1l_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨใ"))[0])
      for session in sessions:
        stream.write(bstack1l1ll1l1l_opy_(session))
      stream.write(bstack1l1llllll_opy_.split(bstack1l_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩไ"))[1])
    logger.info(bstack1l_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩๅ").format(bstack1l11l11ll_opy_));
  except Exception as e:
    logger.debug(bstack1l111l111_opy_.format(str(e)))
def bstack1l111l1l1_opy_(bstack11ll1lll1_opy_):
  global CONFIG
  try:
    host = bstack1l_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪๆ") if bstack1l_opy_ (u"ࠨࡣࡳࡴࠬ็") in CONFIG else bstack1l_opy_ (u"ࠩࡤࡴ࡮่࠭")
    user = CONFIG[bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ้ࠬ")]
    key = CONFIG[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ๊ࠧ")]
    bstack11l1l11l_opy_ = bstack1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨ๋ࠫ") if bstack1l_opy_ (u"࠭ࡡࡱࡲࠪ์") in CONFIG else bstack1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩํ")
    url = bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠯࡬ࡶࡳࡳ࠭๎").format(user, key, host, bstack11l1l11l_opy_, bstack11ll1lll1_opy_)
    headers = {
      bstack1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ๏"): bstack1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭๐"),
    }
    proxies = bstack1l1l11ll1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ๑")], response.json()))
  except Exception as e:
    logger.debug(bstack11l111l11_opy_.format(str(e)))
def bstack1l1l1llll_opy_():
  global CONFIG
  try:
    if bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ๒") in CONFIG:
      host = bstack1l_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩ๓") if bstack1l_opy_ (u"ࠧࡢࡲࡳࠫ๔") in CONFIG else bstack1l_opy_ (u"ࠨࡣࡳ࡭ࠬ๕")
      user = CONFIG[bstack1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ๖")]
      key = CONFIG[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭๗")]
      bstack11l1l11l_opy_ = bstack1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪ๘") if bstack1l_opy_ (u"ࠬࡧࡰࡱࠩ๙") in CONFIG else bstack1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ๚")
      url = bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧ๛").format(user, key, host, bstack11l1l11l_opy_)
      headers = {
        bstack1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ๜"): bstack1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ๝"),
      }
      if bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ๞") in CONFIG:
        params = {bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ๟"):CONFIG[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ๠")], bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ๡"):CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ๢")]}
      else:
        params = {bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭๣"):CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ๤")]}
      proxies = bstack1l1l11ll1_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack11l11llll_opy_ = response.json()[0][bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭๥")]
        if bstack11l11llll_opy_:
          bstack11llll111_opy_ = bstack11l11llll_opy_[bstack1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ๦")].split(bstack1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫ๧"))[0] + bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧ๨") + bstack11l11llll_opy_[bstack1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ๩")]
          logger.info(bstack1l1lll_opy_.format(bstack11llll111_opy_))
          bstack1l1l11l11_opy_ = CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ๪")]
          if bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ๫") in CONFIG:
            bstack1l1l11l11_opy_ += bstack1l_opy_ (u"ࠪࠤࠬ๬") + CONFIG[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭๭")]
          if bstack1l1l11l11_opy_!= bstack11l11llll_opy_[bstack1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ๮")]:
            logger.debug(bstack1111l1_opy_.format(bstack11l11llll_opy_[bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ๯")], bstack1l1l11l11_opy_))
          return [bstack11l11llll_opy_[bstack1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ๰")], bstack11llll111_opy_]
    else:
      logger.warn(bstack111llll11_opy_)
  except Exception as e:
    logger.debug(bstack11l11ll_opy_.format(str(e)))
  return [None, None]
def bstack111l1l11_opy_(url, bstack1lll1_opy_=False):
  global CONFIG
  global bstack11l11ll11_opy_
  if not bstack11l11ll11_opy_:
    hostname = bstack11ll11ll_opy_(url)
    is_private = bstack1l11ll1_opy_(hostname)
    if (bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ๱") in CONFIG and not CONFIG[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭๲")]) and (is_private or bstack1lll1_opy_):
      bstack11l11ll11_opy_ = hostname
def bstack11ll11ll_opy_(url):
  return urlparse(url).hostname
def bstack1l11ll1_opy_(hostname):
  for bstack1ll11l11_opy_ in bstack1l11lll11_opy_:
    regex = re.compile(bstack1ll11l11_opy_)
    if regex.match(hostname):
      return True
  return False