from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo
import socket


class MyListener(object):

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))


"""zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_oscjson._tcp.local.", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()"""




if __name__ == '__main__':
    print "Multicast DNS Service Discovery for Python, version"
    r = Zeroconf()
    print "1. Testing registration of a service..."
    desc = {'version':'0.10','a':'test value', 'b':'another value'}
    info = ServiceInfo("_jsonosc._tcp.local.",
                       "My Service Name._jsonosc._tcp.local.",
                       socket.inet_aton("127.0.0.1"), 1234, 0, 0, desc)
    print "   Registering service..."
    r.registerService(info)
    print "   Registration done."
    print "2. Testing query of service information..."
    print "   Getting ZOE service:",
    print str(r.getServiceInfo("_http._tcp.local.", "ZOE._http._tcp.local."))
    print "   Query done."
    print "3. Testing query of own service..."
    print "   Getting self:",
    print str(r.getServiceInfo("_http._tcp.local.",
                               "My Service Name._http._tcp.local."))
    print "   Query done."
    print "4. Testing unregister of service information..."
    r.unregisterService(info)
    print "   Unregister done."
r.close()