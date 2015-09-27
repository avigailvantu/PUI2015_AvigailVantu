
import json
import sys
import urllib2
import csv

if __name__=='__main__':
    MTA_KEY = sys.argv[1]
    BUS_LINE = sys.argv[2]
    
    #creating a csv
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        
        #requesting bus locations from url
        url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (MTA_KEY, BUS_LINE)
        request = urllib2.urlopen(url)
        response = json.loads(request.read())

        #copy data onto a csv file
        for vehicle in response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
           Lat = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
           Lon = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
           Stopname = vehicle['MonitoredVehicleJourney']['OnwardCalls']['Onwardcall']['0']['extensions']['stopPointName']
           Statusdatastop = vehicle['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
           writer.writerow([Lon,Lat,Stopname,Statusdatastop])
                




