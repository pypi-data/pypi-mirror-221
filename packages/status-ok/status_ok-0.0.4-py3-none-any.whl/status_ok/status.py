from status_ok.status_codex import status_codes

def getStatusMsg(status_code):
    if status_code not in status_codes:
        return "Unknown status code"

    return status_codes[status_code]

def getAllStatusCode():
    return status_codes


def is_success(response):
    return 200 <= response.status_code < 300


def is_client_error(response):
    return 400 <= response.status_code < 500


def is_server_error(response):
    return 500 <= response.status_code < 600


def extract_data(response):
    return response.data


def get_header(response, header_name):
    return response.headers.get(header_name)


def setStatusCode(status_code , msg):
    try:
        status_codes[status_code] = msg
        return True
    except Exception as e:
        print(e)
        return False

