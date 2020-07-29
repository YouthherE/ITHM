import time

from config import PUB_ARTICAL_TITLE
from page.mis.aduit_page import AduitProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, is_exists_element
import  pytest

# 1.定义测试类
@pytest.mark.run(order=102)
class TestAduit:
    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        # 创建的业务方法所在类的对象
        self.home_proxy = HomeProxy()
        self.aduit_proxy = AduitProxy()

    # 3.定义测试方法:文案的测试步骤-----业务层中的业务方法
    def test_aduit_aritcal(self):
        # 定义测试数据
        ari_title = PUB_ARTICAL_TITLE
        # 执行测试步骤
        self.home_proxy.to_aduit_page()
        self.aduit_proxy.test_aduit_ari(ari_title)
        # 断言
        assert is_exists_element(self.driver, PUB_ARTICAL_TITLE)

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()
