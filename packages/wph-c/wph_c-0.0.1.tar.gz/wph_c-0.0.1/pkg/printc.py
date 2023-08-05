import inspect

def pr_c(text, color_num=0):
    default_color = "\033[0m"

    if not isinstance(color_num, int):
        #print("Wanning: pr_c plase input mun: 0-6,default=0")
        color_num = 0

    color_num = max(0, min(6, color_num))
    color = default_color if color_num == 0 else f"\033[{30 + color_num}m"

    # Get the current call stack information
    current_stack = inspect.stack()
    if len(current_stack) >= 2:
        caller_frame = current_stack[1]
        caller_function_name = caller_frame.function
        caller_line_number = caller_frame.lineno

        file_line_info = f"func: {caller_function_name}, line: {caller_line_number}, "
    else:
        file_line_info = ""

    print(color + file_line_info + text + default_color)

