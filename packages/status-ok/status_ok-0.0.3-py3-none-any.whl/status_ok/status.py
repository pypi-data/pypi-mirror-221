from status_ok.status_codex import status_codes

def getStatusMsg(status_code):
    if status_code not in status_codes:
        return "Unknown status code"

    return status_codes[status_code]


def getAllStatusCode():
    return status_codes


def setStatusCode(status_code , msg):
    try:
        status_codes[status_code] = msg
        return True
    except Exception as e:
        print(e)
        return False

