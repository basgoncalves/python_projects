import easygui

re_convert_files_that_already_exist = easygui.boolbox(
    msg="Select an option for re_convert_files_that_already_exist",
    title="Boolean Selection",
    choices=["True", "False"],
)

re_convert_files_that_already_exist = bool(re_convert_files_that_already_exist)

print(f"Selected value for re_convert_files_that_already_exist: {re_convert_files_that_already_exist}")
