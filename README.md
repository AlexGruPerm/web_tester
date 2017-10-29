# web_tester
Python application for test web

Purpose of this application is providing complex test web sites, special web reports (tables,grids).
Test developer needs provide:
 url, cookies, header, run params and test criteria.

Each test is a Class that inherits TestProject, and has name WTestX (where X is number).
WTestX has next attributes:
 cookies (requests.cookies.RequestsCookieJar),
 header (class 'dict')
 url_main
 url_report (can be None, if you don't want test internal report)
 Test property:
  1. Download time
  2. Download size (bytes)
  3. Array of users's property (columns count, rows count, sum of column or row, ets.)

When user write test class WTestX next he needs just add it into TestRunner method and start test
(TestRunner.start)

