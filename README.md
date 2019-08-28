# Internet2 Streaming Telemetry Prototype

## Getting Started

### Prerequisites

docker and docker-compose  
See [example router configs](#example-router-configs) below

### Installing

Clone this repo
```
git clone https://github.internet2.edu/internet2/i2-telemetry-prototype.git
```
Create a `.env` file with the following (replace the items in {})
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

Run docker-compose
`docker-compose up -d`

docker-compose creates the container `configurator` to generate the telegraf.d config files based on `nodes.yaml`.  

Edit `nodes.yaml` and add/update Jinja2 templates, then (re)start `configurator` to regenerate the config files.  

Reload telegraf (`docker-compose exec telegraf kill -SIGHUP 1`) after generating configs.

### Using
Chronograf (data exploration) - http://{dockerhost.ip}:8888  
Grafana (visualization) - http://{dockerhost.ip}:3000

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
