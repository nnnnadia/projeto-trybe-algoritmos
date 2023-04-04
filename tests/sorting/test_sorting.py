from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_sorted_by_max_salary = [
        {"max_salary": 20000, "min_salary": 15000},
        {"max_salary": 10000, "min_salary": 7000},
        {"max_salary": 4500, "min_salary": 3000},
        {"max_salary": 3000, "min_salary": 1000},
    ]

    jobs_sorted_by_min_salary = [
        {"max_salary": 3000, "min_salary": 1000},
        {"max_salary": 4500, "min_salary": 3000},
        {"max_salary": 10000, "min_salary": 7000},
        {"max_salary": 20000, "min_salary": 15000},
    ]

    jobsToSort = [
        {"max_salary": 3000, "min_salary": 1000},
        {"max_salary": 10000, "min_salary": 7000},
        {"max_salary": 20000, "min_salary": 15000},
        {"max_salary": 4500, "min_salary": 3000},
    ]

    sort_by(jobsToSort, "max_salary")
    assert jobsToSort == jobs_sorted_by_max_salary

    sort_by(jobsToSort, "min_salary")
    assert jobsToSort == jobs_sorted_by_min_salary
