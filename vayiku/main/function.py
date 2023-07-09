def get_error(form):
    message = ""
    for fields in form:
        if fields.errors:
            message+=fields.errors

    for err in form.non_field_errors():
        message+=str(err)
        print(message)

    return message