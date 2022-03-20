import os
from utils_function import read_date, read_and_update_counter, send_email, keep_reports
#
report_folder_name = f"{read_date()}_{read_and_update_counter()}"

# For running testCases
command = f"pytest -s --alluredir=report_allure/{report_folder_name} --html=report_html/report_{report_folder_name}.html --self-contained-html testcase"
# command = f"pytest -s --alluredir=report_allure/{report_folder_name} --html=report_html/report_{report_folder_name}.html --self-contained-html testcase --ignore=testcase/provider_management --ignore=testcase/scribeManagement --ignore=testcase/site_management  --ignore=testcase/super_admin_management"
os.system(command)

# # Send email
# sender = 'asif.augmedix@gmail.com'
# # password = 'asdfqwer#12'
# # receivers = 'asif.rouf@augmedix.com, rouf.asifur@gmail.com'
# # send_email(sender, password, receivers)
#
# Number of allure & html reports to keep
# number = 2
# keep_reports(number, "report_allure", "report_html")
#
# # For generating report
command = f"allure serve report_allure/{report_folder_name}"
os.system(command)
