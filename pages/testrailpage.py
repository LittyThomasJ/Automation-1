import os
import testrail
from section_id import section_id
from dotenv import load_dotenv
# import redis
import json
from sqlitedict import SqliteDict
load_dotenv()


class TestRailPage:
    def __init__(self):
        # self.driver = driver
        self.client = testrail.APIClient(os.environ.get('WCFEF_TESTRAIL'))

        # Get and set the TestRail User and Password
        self.client.user = os.environ.get('WCFEF_TESTRAIL_USERNAME')
        self.client.password = os.environ.get('WCFEF_TESTRAIL_PASSWORD')

    def close_testrail_test_run(self, run_id):
        """ Close the current test run"""

        parameter1 = 'close_run/{}'.format(run_id)
        self.client.send_post(parameter1, {"id": run_id})

    def create_testrail_test_run(self, project_id, name):
        """ For creating test run in testrail by using project_id  and we also passes run_name """
        create_test_run = self.client.send_post('add_run/{}'.format(project_id), {"name": name, "include_all": True})
        run_id_created = create_test_run['id']
        return run_id_created

    def get_section_data(self, section_id):
        """ We get the section data by entering section id"""

        parameter = 'get_cases/13&section_id={}'.format(section_id)
        get_section_data = self.client.send_get(parameter)
        return get_section_data['cases']

    def pass_testrail(self, run_id, test_id, comment):
        """ pass the testrail """
        parameter1 = 'add_result_for_case/{}/{}'.format(run_id, test_id)
        result = self.client.send_post(
            parameter1,
            {'status_id': 1, 'comment': comment}
        )
        return result

    def fail_testrail(self, run_id, test_id, comment):
        """ Pass testrail API that the test run failed"""
        parameter1 = 'add_result_for_case/{}/{}'.format(run_id, test_id)
        result = self.client.send_post(
            parameter1,
            {'status_id': 5, 'comment': comment}
        )
        return result

    def add_result_for_all(self, run_id):
        """ Add results for all in one function call """
        #########################################
        # r = redis.Redis(host='localhost', port=6379, db=1)
        # result_val = json.loads(r.get("Results"))

        db = SqliteDict("CFE.db", tablename="cfe", autocommit=True)
        flag = False
        for key, item in db.items():
            if "Results" in key:
            	flag = True
            	break
        if flag:
            result_val = json.loads(db["Results"])
            # print(result_val)
            if bool(result_val):
                parameter1 = 'add_results_for_cases/{}'.format(run_id)
                result = self.client.send_post(
                    parameter1,
                    {"results": result_val }
                )
            # print(result)
        return result
