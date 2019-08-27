Create a `.env` file with the following
```
INFLUXDB_USERNAME={influx username}
INFLUXDB_PASSWORD={influx password}
INFLUXDB_DATABASE={influx db_name}
INFLUXDB_URL=http://influxdb:8086

GRAFANA_USERNAME={grafana username}
GRAFANA_PASSWORD={grafana password}

GNMI_USERNAME={router username}
GNMI_PASSWORD={router password}
```

Run
`docker-compose up -d`

### Example router configs
#### Junos
```
set system services extension-service request-response grpc clear-text
set system services extension-service request-response grpc skip-authentication
```
#### IOS-XR
```
grpc
 port 32767
 no-tls
 ```
