#Create a dictionary containing security incident information
incident = {
    "username": "test123",
    "ip_address": "192.1999,999.000",
    "event_type": "Unauthrorised Access",
    "risk_level": "critical"
}

#Display the username and IP address
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

#Add new field and name it status
incident["status"] = "Under Investigation"

#Update the risk level
incident["risk_level"] = "Medium"

#Remove the event type field
del incident["event_type"]

#Display all remaining keys and values
print("\nSecurity Incident Details:")

for key, value in incident.items():
    print(key, ":", value)

#Display the total number of key value pairs
print("\nTotal number of fields:", len(incident))
