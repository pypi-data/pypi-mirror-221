from enum import Enum


class TriggerType(str, Enum):
    Webhook = "webhook"
    RestAPI = "rest_api"
    Schedule = "cron_job"


class PythonVersion(str, Enum):
    Python37 = "python3.7"
    Python38 = "python3.8"
    Python39 = "python3.9"
    Python310 = "python3.10"


class GpuType(str, Enum):
    NoGPU = ""
    Any = "any"
    T4 = "T4"
    A10G = "A10G"


class VolumeType(str, Enum):
    Persistent = "persistent"
    Shared = "shared"


class AutoscalingType(str, Enum):
    MaxRequestLatency = "max_request_latency"


class BeamSerializeMode:
    Deploy = "deploy"
    Start = "start"
    Run = "run"
    Stop = "stop"
    Serve = "serve"
