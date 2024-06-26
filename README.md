# tellmewhen

![](https://img.shields.io/badge/status-maintained-green)
[![](https://img.shields.io/badge/release-v1.0.2_"Quetzal"-blue)](https://github.com/samcole8/tellmewhen/releases/tag/v1.0.2)

Schedule custom notifications via Telegram, email, or SMS.

Full documentation is available [here](http://samcole.me/archive/tellmewhen).

## Configuration

### Settings

For any service in use, every option must be set or the program will exit in error. 

For example, the Telegram bot service will require both `chat_id` and `bot_id` to be set in `[settings.tele]`.

### Tells

Below is an example of a *tell* - a notification set for a fixed time, date, and interval.

```bike_maintenance = ["Bike service due.", "set", "0 0 1 1,7 *"]```

- `bike_maintenance` is an arbitrary identifier for the tell. You can use anything you want as long as it's unique.
- `"Bike service due."` is the body of the message that will be sent - i.e., what you'll see on telegram/email/sms.
- `set` is the call specifier. `s`=sms, `e`=email, and `t`=telegram. You can omit or include any of these to specify which notification service is used. For example, `st` and `e` are both valid call specifiers.
- `"0 0 1 1,7 *"` is the schedule expression. This particular expression will send the notifications at midnight, on the first day of the month, only in January and July (once every six months). TMW piggybacks on Cron and its syntax, so you can use a tool such as Cronhub's [expression generator](https://crontab.cronhub.io/) to make these.

## Building the container

After cloning the repository and adding at least one tell, you can build and deploy the container with the following steps:

1) Navigate to the parent directory of the Dockerfile.
2) Build the image with `docker build -t tellmewhen .`
3) Run the container with `docker run --name tellmewhen -d tellmewhen`

If new tells are added, the container must be rebuilt.

## Troubleshooting

If the container isn't pushing notifications, you can perform the following steps to troubleshoot:

1) Check you have tells in the [tells] configuration file.
2) With Python installed on the Docker host, run tell.py to test your [settings] services: `python3 /path/to/tell.py test`.
3) Check your cron expression is correct.

## Planned features

- Optional configuration check, in `when.py`, during the container build. This should prevent syntax errors from causing difficult-to-diagnose problems during production.
- A setup module that provides a CLI for config generation and a way to test and troubleshoot services.
- Notifications when services fail.
- Retry failed notifications in the event of connectivity problems.
