import datetime
import os
from enum import Enum

from fastapi import FastAPI

from switcore.action.schemas import SwitRequest, PlatformTypes, UserInfo, UserPreferences, Context, UserAction, \
    UserActionType, View, Body
from switcore.ui.header import Header


def create_fastapi_app():
    os.environ["SWIT_CLIENT_ID"] = "test_client_id"
    os.environ["SWIT_CLIENT_SECRET"] = "test_client_secret"
    os.environ["APPS_ID"] = "test_apps_id"
    os.environ["DB_USERNAME"] = "test_db_username"
    os.environ["DB_PASSWORD"] = "test_db_password"
    os.environ["DB_NAME"] = "test_db_name"
    os.environ["ENV_OPERATION"] = "local"
    os.environ["BASE_URL"] = "test_base_url"
    os.environ["LOCALIZE_PROJECT_ID"] = "test_localize_project_id"
    os.environ["DB_HOST"] = "test_db_host"
    os.environ[
        "SCOPES"] = "imap:write+imap:read+user:read+message:write+channel:read+workspace:read+project:read+project:write+task:read+task:write"
    os.environ["BOT_REDIRECT_URL"] = "/auth/callback/bot"
    os.environ["USER_REDIRECT_URL"] = "/auth/callback/user"

    return FastAPI()


class ActionIdTypes(str, Enum):
    test_action_id01 = "test_action_id01"
    test_action_id02 = "test_action_id02"
    test_action_id03 = "test_action_id03"
    test_escape_action_id = "test_escape_action_id/escape"


class ViewIdTypes(str, Enum):
    right_panel = "right_panel"
    modal = "modal"


def create_swit_request(view_id: ViewIdTypes, action_id: str):
    return SwitRequest(
        platform=PlatformTypes.DESKTOP,
        time=datetime.datetime.now(),
        app_id="test_app_id",
        user_info=UserInfo(
            user_id="test_user_id",
            organization_id="test_organization_id"
        ),
        user_preferences=UserPreferences(
            language="ko",
            time_zone_offset="+0900",
            color_theme="light"
        ),
        context=Context(
            workspace_id="test_workspace_id",
            channel_id="test_channel_id"
        ),
        user_action=UserAction(
            type=UserActionType.view_actions_submit,
            id=action_id,
            slash_command="test_slash_command",
        ),
        current_view=View(
            view_id=view_id,
            state="state",
            header=Header(
                title="test_title",
            ),
            body=Body(),
        ))
