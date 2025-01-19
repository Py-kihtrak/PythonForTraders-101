import time

# Smart API Limits
MAX_REQUESTS_PER_SECOND = 3
MAX_REQUESTS_PER_MINUTE = 180
MAX_REQUESTS_PER_HOUR = 5000
responses = []
requests_made = 0
start_time = time.time()

if requests_made % MAX_REQUESTS_PER_SECOND == 0:
        time.sleep(1)  # Pause for 1 second to respect the per-second limit
    
    # Check limits per minute
    if requests_made % MAX_REQUESTS_PER_MINUTE == 0:
        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            time.sleep(60 - elapsed_time)  # Pause to respect the per-minute limit
            start_time = time.time()  # Reset start time for the next minute

    # Check limits per hour
    if requests_made == MAX_REQUESTS_PER_HOUR:
        elapsed_time = time.time() - start_time
        if elapsed_time < 3600:
            time.sleep(3600 - elapsed_time)  # Pause to respect the hourly limit
            start_time = time.time()  # Reset start time for the next hour
