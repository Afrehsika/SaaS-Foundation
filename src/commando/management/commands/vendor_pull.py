import helpers

from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings


STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
}

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        print("Pulling vendor static files...")
        complted_urls = []
        for filename, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / filename
            dl_success = helpers.download_to_local(url,out_path)
            if dl_success:
                complted_urls.append(url)
                print(f"Downloaded {filename} from {url} to {out_path}")
            else:
                print(f"Failed to download {filename} from {url}")
        if set(complted_urls) == set(VENDOR_STATICFILES.values()):
            print("All vendor static files downloaded successfully.")
        else:
            print("Some vendor static files failed to download. Please check the logs.")
