def my_view(request, template_name):
    var = do_something()
    return render_to_response(template_name, {'var': var})


def myview(request, template_name):
	var = do_something()
	return render_to_response(template_name, {'var':var})