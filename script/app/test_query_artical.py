import time
from page.app.home_page import HomeProxy
from utils import DriverUtils, is_exists_element_by_attr


# 1.定义测试类
class TestQueryArtical:
    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.home_proxy = HomeProxy()

    # 3.定义测试方法
    def test_query_artical(self):
        # 定义测试数据
        channel_name = "前端"
        # 调用测试方法
        self.home_proxy.test_query_artical_by_clname(channel_name)
        # 断言
        assert is_exists_element_by_attr(self.driver, "text", "猜你喜欢")

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_app_driver()
