def multiply_add_up_entries(expense_report, add_up_number, n_entries=2):
    if n_entries == 2:
        for expense in expense_report:
            for expense_2 in expense_report:
                if expense + expense_2 == add_up_number:
                    return expense * expense_2
    elif n_entries == 3:
        for expense in expense_report:
            for expense_2 in expense_report:
                if expense + expense_2 <= add_up_number:
                    for expense_3 in expense_report:
                        if expense + expense_2 + expense_3 == add_up_number:
                            return expense * expense_2 * expense_3
