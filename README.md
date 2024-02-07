# tellmewhen

![](https://img.shields.io/badge/status-under%20development-orange)

Schedule custom notifications via Telegram, email, or SMS.

## Usage

### Configuration

Below is an example of a *tell* - a notification set for a fixed time, date or interval.

```bike_maintenance = ["Bike service due.", "set", "0 0 1 1,7 *"]```

- `bike_maintenance` is an arbitrary identifier for the tell. You can use anything you want as long as it is **unique**.
- `"Bike service due."` is the body of the message that will be sent - i.e., what you'll see on telegram/email/sms.
- `set` is the call specifier. `s`=sms, `e`=email, and `t`=telegram. You can omit or include any of these to specify which notification service is used. For example, `st` and `e` are both valid call specifiers.
- `"0 0 1 1,7 *"` is the schedule expression. This particular expression will send the notifications at midnight, on the first day of the month, only in January and July (once every six months). tellmewhen piggybacks on Cron and its syntax, so you can use a tool such as Cronhub's [expression generator](https://crontab.cronhub.io/) to make these.

### Building the container

After cloning the repository and adding at least one tell, you can build and deploy the container with the following steps:

1) Navigate to the parent directory of the Dockerfile.
2) Build the image with `docker build -t tellmewhen .`
3) Run the container with `docker run --name tellmewhen -d tellmewhen`

If new tells are added, the container must be rebuilt.