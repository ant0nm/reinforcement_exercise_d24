our_rows = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def seat_user(rows):
    for row_index, row in enumerate(rows):
        for seat_index, seat in enumerate(row):
            if seat is None:
                print("Row {} seat {} is free. Do you want to sit there? (y/n)".format(row_index+1, seat_index+1))
                user_choice = input()
                if user_choice.lower() == 'y':
                    print("What is your name?")
                    user_name = input()
                    rows[row_index][seat_index] = user_name
    return rows

new_rows = seat_user(our_rows)
print(new_rows)
