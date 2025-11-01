from server_config import api_base_path

#api base path
base_path=api_base_path


#api end-points
TEST_END_POINT = f"{base_path}/test"
DUMMY_END_POINT = f"{base_path}/dummy"
USER_END_POINT =f"{base_path}/user"
INVENTORY_END_POINT =f"{base_path}/inventory"

#auth
USER_REGISTER_END_POINT = f"{base_path}/auth/register"
USER_LOGIN_END_POINT = f"{base_path}/auth/login"