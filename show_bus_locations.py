import json
import sys 
import urllib2

if __name__=='__main__':
	MTA_KEY = sys.argv[1]
	BUS_LINE = sys.argv[2]
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(MTA_KEY, BUS_LINE)
  	request = urllib2.urlopen(url)
  	response = request.read()
	MTA = json.loads(response)
	#print MTA
	print "Bus Line:%s" %(sys.argv[2])

	i=0 
	for vehicle in MTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
		lon =  vehicle['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		lan = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		i+=1
		print " Bus %s is at latitude %s and longitude %s" %(i,lan,lon)
	print "Number of Active Buses: %s" %(i)
   	#MTA = json.loads(response)
   	#print bus_line, MTA[1]

   		#MY MTA KEY is: 67c57a29-cf31-40a9-a532-a776e7117dbf


