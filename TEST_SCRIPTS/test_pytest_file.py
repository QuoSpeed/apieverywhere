import pytest
import unittest


from BIN.ApiFunction import ApiFunction


class test_pytest(unittest.TestCase,ApiFunction):

    def setUp(self):
        pass

    def test_1_student_unknown_api(self):
        api=self.call_specific_api("student_unknown")
        print (api)
        return api

    def test_2_User2_api(self):
        api = self.call_specific_api("User2")
        print(api)
        return api
