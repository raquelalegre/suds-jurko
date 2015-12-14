import sys, getopt
from suds.client import Client

def getAvailableMethods(client):
    methods = [method for method in client.wsdl.services[0].ports[0].methods]
    return methods

def printAvailableMethods(method_names):
    print "These are all the methods available: "
    for method_name in method_names:
        param_names = getMethodParams(method_name)
        sys.stdout.write(" * " + method_name + ": ")
        for param_name in param_names:
            sys.stdout.write(param_name + " ")
        sys.stdout.write("\n")

def callSampleMethods(method_names):
    print "Calling all methods that don't need any parameters."
    for method_name in method_names:
        if len(getMethodParams(method_name)) == 0:
            print " * " + method_name
            result = getattr(client.service, method_name)()
            print result

def getMethodParams(method_name):
    method = client.wsdl.services[0].ports[0].methods[method_name]
    params = method.binding.input.param_defs(method)
    param_names = []
    for param in params:
        param_names.append(param[0])
    return param_names

if __name__ == "__main__":
    # Read path to WSDL file from input argument
    url = sys.argv[1]
    print "WSDL file is at this URL: " + url

    # Start a client and point to the WSDL URL
    client = Client(url)
    print client

    # Get some info from available funtionality
    availableMethods = getAvailableMethods(client)
    printAvailableMethods(availableMethods)
    callSampleMethods(availableMethods)
