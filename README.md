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
Copy `config/nodes.yaml.dist` to `config/nodes.yaml` and edit.

docker-compose creates the container `configurator` that generates the telegraf.d config files based on `nodes.yaml`.  You can (re)start `configurator` to regenerate the config files.  You need to reload telegraf (`docker-compose exec telegraf kill -SIGHUP 1`) after generating configs.

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
