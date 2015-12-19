#!/usr/bin/python

"""
Classes representing LAMAs.
"""

import unittest
import database
import practices
import datetime

def nowString():
    now=datetime.datetime.now()
    return "{} {} {}".format(now.day, now.month, now.year)
    

class Team(object):
    def __init__(self, team_name, department_name):
        self.name = team_name
        self.department = department_name


class Lama(object):
    def __init__(self, team, results, date_reported=None):
        self.team = team
        if date_reported is not None:
            self.date_reported = date_reported
        else:
            self.date_reported = nowString()
        self.standups = results['standups']
        self.retrospectives = results['retrospectives']
        self.backlog_management = results['backlog_management']
        self.product_ownership = results['product_ownership']
        self.iteration_management = results['iteration_management']
        self.track_and_visualise_progress = results['track_and_visualise_progress']
        self.building_quality_in = results['building_quality_in']
        self.adaptive_planning = results['adaptive_planning']

    def to_html(self):
        html="""
        <div class="lama">
          <span class="title">Team name: {}</span>
          <span class="title">Dept name: {}</span>
          <span class="title">Date: {}</span>
          <table class="lama_table">
            <tr><th>Practice</th><th>Maturity</th></tr>
            <tr><td>Standups</td><td>{}</td></tr>
            <tr><td>Retrospectives</td><td>{}</td></tr>
            <tr><td>Backlog Management</td><td>{}</td></tr>
            <tr><td>Product Ownership</td><td>{}</td></tr>
            <tr><td>Iteration Management</td><td>{}</td></tr>
            <tr><td>Track and Visualise Progress</td><td>{}</td></tr>
            <tr><td>Building Quality In</td><td>{}</td></tr>
            <tr><td>Adaptive_Planning</td><td>{}</td></tr>
          </table>
        </div>""".format(self.team.name,
                         self.team.department,
                         self.date_reported,
                         self.standups,
                         self.retrospectives,
                         self.backlog_management,
                         self.product_ownership,
                         self.iteration_management,
                         self.track_and_visualise_progress,
                         self.building_quality_in,
                         self.adaptive_planning)
        return html

    def write(self):
        sql = """
        insert into lama (
          team_name,
          department_name,
          date_reported,
          standups,
          retrospectives,
          backlog_management,
          product_ownership,
          iteration_management,
          track_and_visualise_progress,
          building_quality_in,
          adaptive_planning,date_reported)
          values (?,?,?,?,?,?,?,?,?,?,?,?);"""
        database.execute(sql,
                         (self.team.name,
                          self.team.department,
                          nowString(),
                          self.standups,
                          self.retrospectives,
                          self.backlog_management,
                          self.product_ownership,
                          self.iteration_management,
                          self.track_and_visualise_progress,
                          self.building_quality_in,
                          self.adaptive_planning,
                          nowString()))
        

    @classmethod
    def findById(cls, lamaID):
        """Load a single LAMA from the database"""
        sql = """select 
        team_name,
        department_name,
        standups,
        retrospectives,
        backlog_management,
        product_ownership,
        iteration_management,
        track_and_visualise_progress,
        building_quality_in,
        adaptive_planning,
        date_reported
        from lama
        where id=?"""

        cursor = database.getCursor()
        print sql
        print lamaID, type(lamaID)
        cursor.execute(sql, (str(lamaID),))
        record = cursor.fetchone()
        results={}
        results['standups']=record[2]
        results['retrospectives']=record[3]
        results['backlog_management']=record[4]
        results['product_ownership']=record[5]
        results['iteration_management']=record[6]
        results['track_and_visualise_progress']=record[7]
        results['building_quality_in']=record[8]
        results['adaptive_planning']=record[9]

        team = Team(record[0], record[1])
        lama = Lama(team, results, record[10])

        cursor.close()
        return lama



###############
#### Tests ####
###############
class TestTeams(unittest.TestCase):
    def testInit(self):
        team = Team("A", "B")
        self.assertEqual(team.name, "A")
        self.assertEqual(team.department, "B")

if __name__ == "__main__":
    unittest.main()
