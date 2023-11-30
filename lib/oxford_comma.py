

def oxford_comma(elements):
    if len(elements) == 0:
        return ""
    elif len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        # Join all elements except the last one with commas
        joined_elements = ", ".join(elements[:-1])
        # Add Oxford comma and the last element
        result = f"{joined_elements}, and {elements[-1]}"
        return result
