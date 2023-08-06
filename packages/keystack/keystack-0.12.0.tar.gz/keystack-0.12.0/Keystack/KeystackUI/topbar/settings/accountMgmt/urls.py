from django.urls import include, path, re_path
#from accounts import views as accountViews
#from accounts.views import ConfirmEmail, UserRegistryView, Login, Logout,ForgotPassword
#from topbar.accountMgmt.views import Login, Logout
from topbar.settings.accountMgmt.views import AccountMgmt

# , AddUser, DeleteUser, Login, Logout, GetUserAccountTableData, GetUserDetails, ModifyUserAccount, GetApiKey, GetPassword, RegenerateApiKey

urlpatterns = [
    #re_path('login', Login.as_view(), name='login'),

    # Note: login must go in KeystackUI/urls because we cannot have two patterns with '^$'
    #re_path('^$', Login.as_view(), name='login'),

    # path('addUser', AddUser.as_view(), name='addUser'),
    # path('deleteUser', DeleteUser.as_view(), name='deleteUser'),
    # path('getUserAccountTableData', GetUserAccountTableData.as_view(), name='getUserAccountTableData'),
    # path('getUserDetails', GetUserDetails.as_view(), name='getUserDetails'),
    # path('modifyUserAccount', ModifyUserAccount.as_view(), name='modifyUserAccount'),

    # path('getApiKey', GetApiKey.as_view(), name='getApiKey'),
    # path('getPassword', GetPassword.as_view(), name='getPassword'),
    # path('gregenerateApiKey', RegenerateApiKey.as_view(), name='regenerateApiKey'),
    re_path('^$', AccountMgmt.as_view(), name='accountMgmt'),
    #re_path(r'^forgotPassword$', ForgotPassword.as_view(), name='ForgotPassword'),
]

