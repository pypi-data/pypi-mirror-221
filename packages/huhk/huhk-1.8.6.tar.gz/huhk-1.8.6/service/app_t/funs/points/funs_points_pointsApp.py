import allure

from service.app_t.asserts.points.asserts_points_pointsApp import AssertsPointsPointsapp
from service.app_t.apis.points import apis_points_pointsApp


class FunsPointsPointsapp(AssertsPointsPointsapp):
    @allure.step(title="APP-用户签到")
    def points_pointsApp_signIn(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/points/pointsApp/signIn
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_pointsApp.points_pointsApp_signIn(**_kwargs)

        self.assert_points_pointsApp_signIn(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



    @allure.step(title="APP - 查看我的积分")
    def points_pointsApp_myPoints(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/points/pointsApp/myPoints
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_pointsApp.points_pointsApp_myPoints(**_kwargs)

        self.assert_points_pointsApp_myPoints(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



    @allure.step(title="APP - 总积分查询")
    def points_pointsApp_myPointsTotal(self, userId="$None$", _assert=True,  **kwargs):
        """
            url=/points/pointsApp/myPointsTotal
                params: headers : 请求头
        """
        userId = self.get_list_choice(userId, list_or_dict=None, key="userId")

        _kwargs = self.get_kwargs(locals())
        self.res = apis_points_pointsApp.points_pointsApp_myPointsTotal(**_kwargs)

        self.assert_points_pointsApp_myPointsTotal(_assert, **_kwargs)
        self.set_output_value(_kwargs)
        self.set_value(_kwargs)



