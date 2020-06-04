from django.core.management.base import BaseCommand
import json
from member.models import *
import dateutil.parser

dummy_data = '''{
	"ok": true,
	"members": [{
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
} '''

class Command(BaseCommand):
    help = 'addd some dummy data'

    def handle(self, *args, **kwargs):

        try:
            json_dummy_data = json.loads(dummy_data)

            for member in json_dummy_data['members']:
                user = User()
                user.real_name = member['real_name']
                user.tz = member['tz']
                user.save()

                for activity in member['activity_periods']:
                    activity_period = ActivityPeriod()
                    activity_period.user = user
                    activity_period.start_time = dateutil.parser.parse(activity['start_time'])
                    activity_period.end_time = dateutil.parser.parse(activity['end_time'])
                    activity_period.save()
            message = "successfully added dummy data to database table"
            self.stdout.write(self.style.SUCCESS(message))
        except Exception as e:
            message = "unable to populate dummy data in database table because {}".format(str(e)) 
            self.stdout.write(self.style.ERROR(message))


        
