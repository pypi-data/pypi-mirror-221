from status_ok.status_codex import status_codes

class HttpStatusError(Exception):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual
        super().__init__(f"Response mismatch. Expected: {expected} {status_codes[expected]}, "
                         f"Actual: {actual} {status_codes[actual]}")


def check_status_code(response , expected_status , expected_content = None):

    if expected_content is not None:
        if response.content != expected_content:
            raise HttpStatusError( expected_content , response.content)

    if response.status_code not in status_codes:
            raise HttpStatusError(expected_status , response.status_code)

    if expected_status != response.status_code:
        raise HttpStatusError( expected_status , response.status_code)




