import traceback
import json
from asset_tracking_pepsico.dto.PostgresSchema import PostgresSchemaDto
import pandas as pd
from datetime import datetime


class AssetTrackingIngest:
    def __init__(self) -> None:
        self.stop_list = [',', '[', ']', '(', ')', '\n', ' ', '"']
        self.no_route_no_transition_event_list = ['UserCheckedoutOfServiceAppointment', 'AppLaunchedEvent', 'UserStartedShiftEvent']
        self.route_no_transition_event_list = ['MemoryWarningEvent', 'UserEnteredAGeofence']

    def convert_datetime(self, time_str):
        try:
            datetime_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            date = datetime_obj.date()
            return date
        except:
            traceback.print_exc()

    def create_dataframe(self, json_list):
        try:
            df = pd.DataFrame.from_records(json_list)
            df['Properties'] = df['Properties'].replace('', '{}').apply(json.loads)
            print("DATAFRAME COLUMNS == \n", df.columns, '\n', '-'*150)
            return df
        except:
            traceback.print_exc()

    def extract_json(self, data):
        try:
            st = 1
            ind = []
            json_list = []
            for ix, i in enumerate(data):
                if ix == 0 or i in self.stop_list:
                    continue
                if i == '{':
                    ind.append(i)
                elif i == '}' and len(ind) > 0:
                    ind.pop(-1)
                if len(ind) == 0:
                    end = ix
                    sub_str = data[st:end + 1]
                    sub = json.loads(sub_str)
                    json_list.append(sub)
                    st = end + 2
            return json_list
        except:
            traceback.print_exc()

    def extract_properties(self, properties):
        try:
            # print("properties === ", properties)
            emp_det = properties['Employee']
            loc_info = properties['UserLocationCoordinates']
            object_id, emp_name = emp_det[:emp_det.find(',')], emp_det[emp_det.find(',')+1:]
            lat, long, acc, _ = loc_info.split(',')
            lat, long, acc = float(lat.strip()), float(long.strip()), float(acc.strip())
            event_desc = properties['Description']
            try:
                loc_desc = properties['LocationDescription'].replace("'", "")
            except KeyError:
                loc_desc = None
            try:
                loc_id = properties['LocationId']
            except KeyError:
                loc_id = None
            try:
                transition = properties['Transition']
            except KeyError:
                transition = None
            try:
                route = properties['Route']
            except KeyError:
                route = None
            version = properties['Version']
            return object_id, emp_name, lat, long, acc, event_desc, transition, route, version, loc_desc, loc_id
        except KeyError:
            traceback.print_exc()

    def filter_properties(self, properties_dict):
        try:
            for key in properties_dict:
                item = properties_dict[key]
                item = item.replace("'", "").replace(":", "").replace(",", "")
                properties_dict[key] = item
        except:
            traceback.print_exc()
        return properties_dict

    def create_schema_list(self, df, object_type, data_source, schema_version):
        try:
            schema_list = []
            for idx, item in df.iterrows():
                if item['EventName'] == 'CrashDiagnostics' or item['EventName'] == '':
                    continue
                object_id, emp_name, lat, long, acc, event_desc, transition, route, version, loc_desc, loc_id = \
                    None, None, None, None, None, None, None, None, None, None, None
                if len(item['Properties']) != 0:
                    object_id, emp_name, lat, long, acc, event_desc, transition, route, version, loc_desc, loc_id = \
                        self.extract_properties(item['Properties'])

                times = item['Timestamp']
                event = item['EventName']

                properties_dict = {
                    'Employee_Name': emp_name,
                    'AppNamespace': item['AppNamespace'],
                    'AppVersion': item['AppVersion'],
                    'OsVersion': item['OsVersion'],
                    'Transition': transition,
                    'Version': version,
                    'EventId': item['EventId'],
                    'Description': event_desc
                }

                properties_dict = self.filter_properties(properties_dict)

                schema = PostgresSchemaDto(schema_version=schema_version, object_id=object_id, object_type=object_type, event_type=event,
                                           location_hint=loc_desc, location_id=loc_id, object_latitude=lat, object_longitude=long,
                                           created_ts=times, lat_long_acc=acc, datasource=data_source,
                                           properties_dict=str(properties_dict), routeid=route)
                schema_list.append(schema)
            return schema_list
        except:
            traceback.print_exc()
