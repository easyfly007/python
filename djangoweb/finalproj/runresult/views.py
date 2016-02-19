from django.shortcuts import render
from django.shortcuts import HttpResponse, render_to_response
from runresult.models import Result
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext
from HSPPlot import HSPPlotter
import numpy as np
from report_analyzer import *
from runshell import shellrun

class ComparableResult(object):
	def __init__(self, case, value):
		self.case=case
		self.value=value


# below for show result
def index(request):
	return render_to_response('search_form.html', locals(),
		context_instance=RequestContext(request))


def showresult(request):
	errors=[]

	target_simulator=request.POST['target_simulator']
	golden_simulator=request.POST['golden_simulator']
	if target_simulator == golden_simulator:
		errors.append('target simulator and golden simulaotr should not be same')

	if 'caselist' in request.POST and request.POST['caselist']:
		caselist=request.POST['caselist']
	else:
		print 'please select a case list'
		errors.append('please select a case list')


	if 'rundate' in request.POST and request.POST['rundate']:
		rundate = request.POST['rundate']
		if len(rundate) !=8:
			errors.append('binary date should be yyyymmdd format')
	else:
		errors.append('please enter the binary date')

	if errors:
	 	return render_to_response('search_form.html', locals(), context_instance=RequestContext(request)) 

	title=target_simulator.lower()+'vs'+golden_simulator.lower()
	results=Result.objects.filter(rundate__contains=rundate, comparenote__contains=title, caselist__contains=caselist).order_by('-trandiff')

	data=[]
	for result in results:
		comparable=ComparableResult(result.case, result.trandiff)
		data.append(comparable)
	
	hspPlotter = HSPPlotter()
	#input data must be a list, like [[a, 1.0], [b,9.0], ...]
	pics = hspPlotter.generatePics(data, title)
	print pics
	#pics=[]
	#pics.append('onepiece.jpg')


	return render_to_response('result_form.html', locals(), context_instance=RequestContext(request))



# below for regression run
def runindex(request):
	return render_to_response('run_form.html', locals(),
		context_instance=RequestContext(request))

def runregression(request):
	errors=[]
	golden_simulator = request.POST['golden_simulator']
	target_simulator = request.POST['target_simulator']

	if target_simulator == golden_simulator:
		errors.append('target simulator and golden simulator should be different')
	
	if 'golden_binary_select' in request.POST and request.POST['golden_binary_select']:
		golden_binary_select = request.POST['golden_binary_select']
		if golden_binary_select=='default':
			golden_binary='default'
		else:
			if 'golden_binary_input' in request.POST and request.POST['golden_binary_input']:
				golden_binary=request.POST['golden_binary_input']
			else:
				errors.append('please select or enter the golden binary!')

	if 'target_binary_select' in request.POST and request.POST['target_binary_select']:
		target_binary_select = request.POST['target_binary_select']
		if target_binary_select=='default':
			target_binary='default'
		else:
			if 'target_binary_input' in request.POST and request.POST['target_binary_input']:
				target_binary=request.POST['target_binary_input']
			else:
				errors.append('please select or enter the target binary!')

	if 'caselist' in request.POST and request.POST['caselist']:
		caselist=request.POST['caselist']
	else:
		errors.append('please select the case list')
	
	if 'rundate' in request.POST and request.POST['rundate']:
		rundate = request.POST['rundate']
		if len(rundate) !=8:
			errors.append('binary date should be yyyymmdd 8 digits format')
	else:
		errors.append('please enter the binary date')

	if errors:
	 	return render_to_response('run_form.html', locals(), context_instance=RequestContext(request))  

	#shellrun(target_simulator, target_binary, golden_simulator, golden_binary, caselist, rundate)
	sum_list=shellrun(target_simulator, target_binary, golden_simulator, golden_binary, caselist, rundate)
	#print sum_list[0]
	#print sum_list[1]

	#dump_result_to_DB("demo.acc", "rd", "20150520", "hspvsfsm")
	dump_result_to_DB(sum_list[0], caselist, rundate, target_simulator.lower()+"vs"+golden_simulator.lower())

	return render_to_response('runregression_form.html', locals(), context_instance=RequestContext(request))


def dump_result_to_DB(summary_name, caselist, rundate, comparenote):
	try:
		f = open(summary_name)
	except IOError:
		print "Invalid summary path or name."
		return
	buf = f.read()
	reportresult = get_dc_diff(buf)
	if reportresult is not None:
		for entry in reportresult:
			Result.objects.get_or_create(case = entry[0], caselist = caselist, 
				rundate = rundate, trandiff = entry[2], comparenote = comparenote)
	reportresult = get_ac_diff(buf)
	if reportresult is not None:
		for entry in reportresult:
			Result.objects.get_or_create(case = entry[0], caselist = caselist, 
				rundate = rundate, trandiff = entry[2], comparenote = comparenote)
	return 1

def mew(request):
    response = HttpResponse('''
     wow not found
            ''')
    response.status_code = 404
    return response
