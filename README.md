# hxnyc

## Overview
hxnyc is a registration system(prototype) built based on Django framework. It showa a journey of using open-source projects to build production ready application :+1: Check the following roadmap for details
![Screen Shot 2021-04-19 at 10 55 16 PM](https://user-images.githubusercontent.com/10833201/115330639-7b27b980-a162-11eb-916b-f00be16415e3.png)

Components:
1. Framework: Django framwork for a web application with build-in administration system; 
1. Hosting: Application is hosted on DigitalOcean droplet: 1 GB Memory / 25 GB Disk / NYC1 - Ubuntu 18.04 (LTS) x64;
1. Other Tech. Stacks: Gunicorn+Nginx+Postgres for gateway+webServer+database;
1. DNS and SSL: Google Domain opensourcechloe.org; SSL with Let's Encrypt;
1. Tracking and metering: OpenTelemetry intergration;
1. Consent Management: Segment opensource library intergration;

**High Level Architecture**

![Screen Shot 2021-04-20 at 10 01 53 PM](https://user-images.githubusercontent.com/10833201/115486406-9c50de80-a224-11eb-9380-d77c334e7303.png)

## Installation

## Usage
Start the appliation and Promethues
```shell
. start-app.sh
```
Note that your terminal shows the debugging outputs. Stop the web application, simply ctl/command+C

Stop the Promethues service and deactivate the virtual env. 
```shell
. stop-app.sh
```
## Support
### Dev. Env.
### Production Env. 
- Alerting system support
- Security support

## Roadmap
- Containerize Django Application
- ReadOnlyAdmin
- Define more metrics for Prometheus
- Email Notification to confirm user's registration
- React Frontend
- Multi-language
- CSV Data Import/Export
- Django admin access control
- Logging and troubleshooting
- Alerting system integration
- Sentry or OpenTelemetry?
- Security enhancement: XSS, CSRF, SQL Injection
- Celery and Redis?

## Authors
Chloe Wang
* [GitHub](https://github.com/synergit/)
* [LinkedIn](https://www.linkedin.com/in/xwang-1a/)
* [Twitter](https://twitter.com/chloe_wang1)

## Contributing
pull requests are welcome. for major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgement
Thanks to [readme](https://www.makeareadme.com/) for this template. 
