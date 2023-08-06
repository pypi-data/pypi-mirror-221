from enum import Enum


class MessageSeverity(Enum):

    Debug = 100
    Verbose = 200
    Information = 500
    Warning = 700
    Error = 800
    Critical = 600
    Start = 400
    End = 400
    Exception = 900
    Init = 300
