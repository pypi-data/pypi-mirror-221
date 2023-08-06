import pandas as pd

LOCAL = "local"
DEV = "dev"
PROD = "prod"

FULL = "full"
INCREMENTAL = "incremental"

PREFECT_DMS = "prefect-dms"
PREFECT = "prefect"

SAVED_S3 = "saved-s3"
SAVED_REDSHIFT = "saved-redshift"

IAM_ROLE = "arn:aws:iam::977647303146:role/service-role/AmazonRedshift-CommandsAccessRole-20220714T104138"


def target_type_is_numeric(target_type):
    if (
        target_type == "int"
        or target_type == "bigint"
        or target_type == "numeric"
        or target_type == "float"
        or target_type == "double"
    ):
        return True
    else:
        return False


def convert_types(struct, df):
    for c in struct.columns:
        case_target_type = {
            "varchar": "str",
            "text": "str",
            "timestamp": "datetime64[ns]",
            "super": "str",
            "int": pd.Int64Dtype(),
            "bigint": pd.Int64Dtype(),
            "boolean": "bool",
        }

        if c["target_type"] in case_target_type.keys():
            df[c["source_name"]] = df[c["source_name"]].astype(
                case_target_type[c["target_type"]]
            )
            if case_target_type[c["target_type"]] == "str":
                df[c["source_name"]].replace("None", "", inplace=True)

    return df


def check_if_env_is_valid(env):
    if env not in [LOCAL, DEV, PROD]:
        raise ValueError("env must be 'local', 'dev' or 'prod'")


def check_if_option_is_valid(option):
    if option not in [FULL, INCREMENTAL, None]:
        raise ValueError("option must be 'full' or 'incremental'")
