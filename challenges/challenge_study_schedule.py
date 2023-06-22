def study_schedule(permanence_period: list, target_time: int) -> int:
    if target_time is None:
        return None

    students = 0

    for period in permanence_period:
        period_index_zero = period[0]
        period_index_one = period[1]

        if (
            type(period_index_zero) != int
            or type(period_index_one) != int
            or period_index_zero < 0
            or period_index_one < 0
        ):
            return None

        if period_index_zero <= target_time <= period_index_one:
            students += 1

    return students


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 4
print(study_schedule(permanence_period, target_time))
