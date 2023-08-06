import allure

from service.app_t.asserts.points.asserts_points_points import AssertsPointsPoints
from service.app_t.apis.points import apis_points_points


class FunsPointsPoints(AssertsPointsPoints):
    @allure.step(title="查看积分明细- - 积分流水分页查询")
    def points_points_flowDetail(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/points/points/flowDetail
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_points.points_points_flowDetail(**_kwargs)

        self.assert_points_points_flowDetail(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



    @allure.step(title="积分统计-分页查询积分")
    def points_points_page(self, current=1, endTime="$None$", size=10, beforeTime="$None$", _assert=True,  **kwargs):
        """
            url=/points/points/page
                params: current :  :
                params: size :  :
                params: beforeTime :  :
                params: endTime :  :
                params: headers : 请求头
        """
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        beforeTime = self.get_list_choice(beforeTime, list_or_dict=None, key="beforeTime")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_points.points_points_page(**_kwargs)

        self.assert_points_points_page(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



    @allure.step(title="积分统计 - 导出")
    def points_points_download(self, current=1, endTime="$None$", size=10, beforeTime="$None$", _assert=True,  **kwargs):
        """
            url=/points/points/download
                params: current :  :
                params: size :  :
                params: endTime :  :
                params: beforeTime :  :
                params: headers : 请求头
        """
        endTime = self.get_list_choice(endTime, list_or_dict=None, key="endTime")
        beforeTime = self.get_list_choice(beforeTime, list_or_dict=None, key="beforeTime")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_points.points_points_download(**_kwargs)

        self.assert_points_points_download(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



    @allure.step(title="用户中心-兑换明细 - 分页查询")
    def points_points_convertDetail(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/points/points/convertDetail
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_points.points_points_convertDetail(**_kwargs)

        self.assert_points_points_convertDetail(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



