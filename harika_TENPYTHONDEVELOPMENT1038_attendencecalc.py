
def check_attendance(total_classes, attended_classes, target_percentage):

    current_percentage = (attended_classes / total_classes) * 100

    print(f"\nCurrent Attendance: {current_percentage:.2f}%")

    if current_percentage >= target_percentage:
        print("Attendance requirement is met.")
        return

    print("Attendance requirement is not met.")

    extra_classes = 0

    while ((attended_classes + extra_classes) /
           (total_classes + extra_classes)) * 100 < target_percentage:
        extra_classes += 1

    print(f"You need to attend {extra_classes} more classes continuously to reach {target_percentage}% attendance.")

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
target_percentage = float(input("Enter required attendance percentage: "))

check_attendance(total_classes, attended_classes, target_percentage)