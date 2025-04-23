from employatron.reporting import produce_employee_report, InMemoryReport
from employatron.employee import Employee

def tests_employee_inmemory_report():
    em = Employee('test','programmer', 34.5)
    report = produce_employee_report(em, report_type=InMemoryReport)
    report_contents = report.get_contents()

    correct_contents = {'name':'test',
                        'role':'programmer',
                        'hourly_rate':34}
    # Assert correct keys/field names
    assert set(correct_contents.keys()) == set(report_contents.keys())

    # Assert correct values
    for k in correct_contents.keys():
        assert report_contents[k] == correct_contents[k]