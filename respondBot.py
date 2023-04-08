import re


def handle_message(message: str) -> str:
    nmsg = message

    if nmsg == '!ping':
        return 'pong'
    if nmsg == 'INVALID':
        return 'Read the thread'
    if nmsg == 'SUCCESS':
        return 'SUCCESS'
    if nmsg[:7] == 'SUCCESS':
        nmsg = re.sub(r"\bSUCCESS\b", "", nmsg)
        return nmsg
    if nmsg == 'INVALIDUSER':
        return 'Only for registered users'
    if nmsg[:6] == 'FAILED':
        nmsg = re.sub(r"\bFAILED\b", "", nmsg)
        return nmsg
