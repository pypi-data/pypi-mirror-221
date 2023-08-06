"""Snowflake testing suite. Can be run against live Snowflake environment if SNOWFLAKE_ACCOUNT and AUTH environment variables are defined."""
# pylint: disable=unused-import, unused-argument, redefined-outer-name, protected-access
import os
import snowflake.connector as sc
from snowcross.aws import resolve_parameters
from snowcross.snowflake import (
    connection,
    cursor,
    execute_statement,
    execute_query,
    connection_args,
)
from tests.fixtures.aws import (
    fixture_ssm_params_snowflake,
    fixture_ssm_client,
    aws_credentials,
)
from tests.fixtures.snowflake import (
    fixture_snowflake_credentials,
    fixture_snowflake_credentials_private_link,
    fixture_snowflake_credentials_ssm,
    fixture_snowflake_connector,
    fixture_snowflake_cursor,
)


def test_connection_args():
    test_password = "test_password"
    conn_args = connection_args(password=test_password)
    assert conn_args["password"] == test_password


def test_connection(monkeypatch, fixture_snowflake_credentials, fixture_snowflake_connector):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        private_key_path=os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"),
        private_key_passphrase=os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"),
    ) as conn:
        assert type(conn) == sc.SnowflakeConnection


def test_connection_account_privatelink(
    monkeypatch, fixture_snowflake_credentials_private_link, fixture_snowflake_connector
):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        privatelink=False,
    ) as conn:
        assert ".privatelink" not in conn.account


def test_connection_account_not_privatelink(
    monkeypatch, fixture_snowflake_credentials_private_link, fixture_snowflake_connector
):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        privatelink=True,
    ) as conn:
        assert ".privatelink" in conn.account


def test_cursor(
    monkeypatch,
    fixture_snowflake_credentials,
    fixture_snowflake_connector,
    fixture_snowflake_cursor,
):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        private_key_path=os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"),
        private_key_passphrase=os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"),
    ) as conn:
        with cursor(conn) as cur:
            assert type(cur) == sc.DictCursor


def test_execute_statement(
    monkeypatch,
    fixture_snowflake_credentials,
    fixture_snowflake_connector,
    fixture_snowflake_cursor,
):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        private_key_path=os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"),
        private_key_passphrase=os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"),
    ) as conn:
        execute_statement(conn=conn, sql="select 1;")


def test_execute_query(
    monkeypatch,
    fixture_snowflake_credentials,
    fixture_snowflake_connector,
    fixture_snowflake_cursor,
):
    with connection(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USERNAME"],
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        private_key_path=os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"),
        private_key_passphrase=os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"),
    ) as conn:
        res = execute_query(conn=conn, sql="select 1;")

    assert len(res) == 1
    assert res[0]["1"] == 1
