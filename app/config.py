"""
    Configuration
    ______________
    define all configuration used on provider
"""
import os

LOGGING = {"TIMEOUT": 15}

FORWARD_CONFIG = {
    "BNI_OPG": os.getenv("BNI_OPG_FORWARD_URL") or "https://apidev.bni.co.id:8066",
    "BNI_RDL": os.getenv("BNI_RDL_FORWARD_URL") or "https://apidev.bni.co.id:8066",
}

CALLBACK = {"URLS": os.getenv("CALLBACK_URLS") or "http://127.0.0.1:5001/callback/"}

BNI_ECOLLECTION = {
    "BASE_URL": os.getenv("BNI_VA_URL") or "https://apibeta.bni-ecollection.com/",
    "CREDIT_SECRET_KEY": os.getenv("BNI_VA_CREDIT_SECRET_KEY")
    or "0281c0c18992b97ae79efb2ac99ef529",
    "CREDIT_CLIENT_ID": os.getenv("BNI_VA_CREDIT_CLIENT_ID") or "99096",
    "VA_PREFIX": os.getenv("BNI_VA_PREFIX") or "988",
    "VA_LENGTH": 16,
    "UPDATE": "updatebilling",
    "INQUIRY": "inquirybilling",
}

# BNI RDL  CONFIG
BNI_RDL = {
    "CLIENT_NAME": os.getenv("BNI_RDL_CLIENT_NAME") or "client-name",
    "COMPANY": os.getenv("BNI_RDL_COMPANY") or "client-name",
    "SECRET_API_KEY": os.getenv("BNI_RDL_SECRET_API_KEY") or "secret-api-key"
}
