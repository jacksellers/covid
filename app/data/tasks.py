from celery.decorators import periodic_task
from datetime import datetime, timedelta

from db_update.update import update


@periodic_task(run_every=timedelta(hours=8))
def every_8_hours():
    update()
    # Test this on a shorter timeframe (e.g. every 15 mins)