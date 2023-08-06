from pathlib import Path

TEST_AWS_REGION = "us-east-1"
TEST_AWS_ACCOUNT_ID = "123456789012"
TEST_BUCKET_NAME = "test-bucket"
TEST_ECR_REPO_NAME = "test-repo"
TEST_FILE_NAME = "s3testfile"
TEST_FILE_PATH = Path(f"tests/files/{TEST_FILE_NAME}.json")
TEST_IMAGE_TAG = "0.0.1"
TEST_SSM_PARAM_SNOWFLAKE_ACCOUNT = {
    "name": "tests/snowflake/account",
    "type": "String",
    "value": "test_account",
}
TEST_SSM_PARAM_SNOWFLAKE_PASSWORD = {
    "name": "tests/snowflake/password",
    "type": "SecureString",
    "value": "test_password",
}
TEST_SSM_PARAM_SNOWFLAKE_USERNAME = {
    "name": "tests/snowflake/username",
    "type": "String",
    "value": "test_user",
}
TMP_PATH = Path("tests/tmp_dir")
