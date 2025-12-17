

if __name__ == "__main__":
def hms(hms_str):
    h, m, s = map(int, hms_str.split(":"))
    return h*3600 + m*60 + s

def ms(ms_val):
    return ms_val / 1000

def minsec(m, s):
    return m*60 + s

def hours(h):
    return h*3600

def format_hms(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h} h {m} min {s} s"

def process(intervals, command):
    secs = [i for i in intervals]
    if command == "sum":
        val = sum(secs)
    elif command == "avg":
        val = sum(secs) / len(secs)
    elif command == "max":
        val = max(secs)
    elif command == "min":
        val = min(secs)
    else:
        return "Unknown command"
    return f"{command.title()}: {format_hms(val)} ({val} s)"
intervals = [
    hms("01:30:00"),   
    ms(90000),        
    minsec(3, 45),     
    hours(2.5)]

for cmd in ["sum", "avg", "max", "min"]:
    print(process(intervals, cmd))