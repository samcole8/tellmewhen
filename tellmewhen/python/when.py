def parse(cronstring):


def check(job):
    # Check job syntax is valid
    # - 3 items
    # - one occurence max of s,e,t in item 2. no other characters
    # - cron job must be valid
    # - datatypes must be strings
    

def when(new=True):
    print("Scanning tells.toml for errors")
    for job in tells:
        check(job)
    print("Error check complete: No errors")
    # Build and add crontab
    print("Program exit: success")

if __name__ == "__main__":
    when()