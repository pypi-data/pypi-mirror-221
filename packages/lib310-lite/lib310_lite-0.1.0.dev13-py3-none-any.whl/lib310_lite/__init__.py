import os

from .bigquery.client import Client as BigQueryClient
from .laser.laser import Laser


def set_gcloud_key_path(path: str):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path


__all__ = ['BigQueryClient', 'set_gcloud_key_path', 'Laser']
