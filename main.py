from exercises import muscle_db


def show_main_menu():
    print("\n💪 MuscleTarget")
    print("1. Get workout recommendation")
    print("2. Exit")


def show_body_parts():
    print("\nSelect Body Part:")

    body_parts = list(muscle_db.keys())

    for i, part in enumerate(body_parts, start=1):
        print(f"{i}. {part}")

    return body_parts


def show_sub_parts(body_part):
    print(f"\nSelect Target Area for {body_part}:")

    sub_parts = list(muscle_db[body_part].keys())

    for i, sub in enumerate(sub_parts, start=1):
        print(f"{i}. {sub}")

    return sub_parts


def show_exercises(body, sub):
    print(f"\n🔥 Best Exercises for {body} → {sub}\n")

    exercises = muscle_db[body][sub]

    for i, ex in enumerate(exercises, start=1):
        print(f"{i}. {ex}")


def main():

    while True:
        show_main_menu()
        option = input("\nChoose option: ")

        if option == "1":

            # BODY PART
            body_parts = show_body_parts()
            body_choice = input("\nEnter choice: ")

            if not body_choice.isdigit() or int(body_choice) not in range(1, len(body_parts) + 1):
                print("❌ Invalid body part.")
                continue

            body = body_parts[int(body_choice) - 1]

            # SUB PART
            sub_parts = show_sub_parts(body)
            sub_choice = input("\nEnter choice: ")

            if not sub_choice.isdigit() or int(sub_choice) not in range(1, len(sub_parts) + 1):
                print("❌ Invalid target area.")
                continue

            sub = sub_parts[int(sub_choice) - 1]

            # SHOW WORKOUT
            show_exercises(body, sub)

        elif option == "2":
            print("\nGoodbye! Keep training 💪")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
