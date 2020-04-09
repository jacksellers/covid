import os
import shutil
import urllib
import pandas as pd
import django
import glob
import dateutil.parser
import sys

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from github import Github

from data.models import Report, Update
from data.keys import GITHUB_PASSWORD


def update():
    started_at = datetime.now()
    """
    g = Github('jackwsellers', GITHUB_PASSWORD)
    repo = g.get_repo('CSSEGISandData/COVID-19')
    reports = repo.get_contents(
        'csse_covid_19_data/csse_covid_19_daily_reports', 'master'
    )
    """
    files_dir = '{}/data/files'.format(os.getcwd())
    db_path = '{}/db.sqlite3'.format(os.getcwd())
    print(os.getcwd())
    print(files_dir)
    print(db_path)
    """
    try:
        shutil.rmtree(files_dir)
    except FileNotFoundError:
        pass

    os.mkdir(files_dir)

    for report in reports:
        url = report.download_url
        if url[-4:] == '.csv':
            urllib.request.urlretrieve(
                url, '{}/{}'.format(files_dir, url[-14:])
            )
            print(url[-14:])
    """
    files = glob.glob(os.path.join(files_dir, '*.csv'))

    for file_name in files:
        csv_data = pd.read_csv(file_name)
        csv_data = csv_data.fillna('')
        csv_data = csv_data.values.tolist()
        for row in csv_data:
            print(
                file_name[-14:][:-4], ',', row[0], ',', row[1], ',',
                row[2], ',', row[3], ',', row[4], ',', row[5]
            )
            try:
                last_update = dateutil.parser.parse(row[2])
                city = ''
                state = row[0]
                region = row[1]
                if row[3]:
                    confirmed = int(row[3])
                else:
                    confirmed = 0
                if row[4]:
                    deaths = int(row[4])
                else:
                    deaths = 0
                if row[5]:
                    recovered = int(row[5])
                else:
                    recovered = 0
            except ParserError:
                last_update = dateutil.parser.parse(row[4])
                city = row[1]
                state = row[2]
                region = row[3]
                if row[7]:
                    confirmed = int(row[7])
                else:
                    confirmed = 0
                if row[8]:
                    deaths = int(row[8])
                else:
                    deaths = 0
                if row[9]:
                    recovered = int(row[9])
                else:
                    recovered = 0
            report_needed = True
            try:
                old_report = Report.objects.get(
                    file_name=file_name[-14:][:-4],
                    city=city,
                    state=state,
                    region=region
                )
                if confirmed > old_report.confirmed:
                    old_report.delete()
                else:
                    report_needed = False
            except ObjectDoesNotExist:
                pass
            """
            if report_needed:
                new_report = Report.objects.create(
                    file_name=file_name[-14:][:-4],
                    city=city,
                    state=state,
                    region=region,
                    last_update=last_update,
                    confirmed=confirmed,
                    deaths=deaths,
                    recovered=recovered
                )
                new_report.save()
            """
    """
    ended_at = datetime.now()
    elapsed_time = ended_at - started_at
    update = Update.objects.create(
        started_at=started_at,
        ended_at=ended_at,
        elapsed_time=elapsed_time
    )
    update.save()
    """

update()