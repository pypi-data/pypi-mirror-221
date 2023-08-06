import os
import contextlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from typing import Iterator, Optional
import snowflake.connector as sc


@contextlib.contextmanager
def connection(
    password: Optional[str] = None,
    private_key_path: Optional[str] = None,
    private_key_passphrase: Optional[str] = None,
    privatelink: Optional[bool] = False,
    **kwargs,
) -> Iterator[sc.SnowflakeConnection]:
    """Establish connection to Snowflake.

    Args:
        password (Optional[str], optional): Password (do not specify with private key). Defaults to None.
        private_key_path (Optional[str], optional): Path to private key file (do not specify with password). Defaults to None.
        private_key_passphrase (Optional[str], optional): Passcode to decrypt private key file, if encrypted (do not specify with password). Defaults to None.
        privatelink (Optional[bool], optional): PrivateLink enabled. Defaults to False.

    Yields:
        Iterator[sc.SnowflakeConnection]: Snowflake connection context.
    """
    conn_args = connection_args(
        password=password,
        private_key_path=private_key_path,
        private_key_passphrase=private_key_passphrase,
        **kwargs,
    )

    sc.paramstyle = "format"

    if not privatelink and conn_args["account"]:
        conn_args["account"] = conn_args["account"].replace(".privatelink", "")

    try:
        conn = sc.connect(
            **conn_args,
        )
        yield conn
    finally:
        conn.close()


@contextlib.contextmanager
def cursor(conn: sc.SnowflakeConnection) -> Iterator[sc.cursor.SnowflakeCursor]:
    """Initialize Snowflake dict cursor.

    Args:
        conn (sc.SnowflakeConnection): A Snowflake connection.

    Yields:
        Snowflake dictionary cursor generator.
    """
    try:
        dict_cursor = conn.cursor(sc.cursor.DictCursor)
        yield dict_cursor
    finally:
        dict_cursor.close()


def connection_args(
    password: Optional[str] = None,
    private_key_path: Optional[str] = None,
    private_key_passphrase: Optional[str] = None,
    **kwargs,
) -> dict:
    """Builds Snowflake connection arguments.

    Args:
        password (Optional[str], optional): Password (do not specify with private key). Defaults to None.
        private_key_path (Optional[str], optional): Path to private key file (do not specify with password). Defaults to None.
        private_key_passphrase (Optional[str], optional): Passcode to decrypt private key file, if encrypted (do not specify with password). Defaults to None.

    Returns:
        dict: Dictionary of all connection arguments with authentication ones resolved.
    """

    res = {**kwargs}

    if password:
        res["password"] = password
    elif private_key_path:
        with open(os.path.expanduser(private_key_path), "rb") as key:
            res["private_key"] = serialization.load_pem_private_key(
                data=key.read(),
                password=private_key_passphrase.encode() if private_key_passphrase else None,
                backend=default_backend(),
            ).private_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )

    return res


def execute_statement(conn: sc.SnowflakeConnection, sql: str, **kwargs):
    """Pass statement to Snowflake to execute.

    Args:
        conn (sc.SnowflakeConnection): A Snowflake connection.
        sql (str): The Snowflake SQL statement to execute.
    """
    with cursor(conn) as cur:
        cur.execute(sql, **kwargs)


def execute_query(conn: sc.SnowflakeConnection, sql: str, **kwargs) -> Optional[list]:
    """Pass SQL to Snowflake and return the result as a dictionary.

    Args:
        conn (sc.SnowflakeConnection): A Snowflake connection.
        sql: The Snowflake SQL to execute.
    Returns:
        A list of dictionaries representing the results of the query, or None if some error happened.
    """
    with cursor(conn) as cur:
        res = cur.execute(sql, **kwargs)
        if not res:
            return None
        return res.fetchall()
