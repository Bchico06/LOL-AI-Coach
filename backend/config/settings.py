from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    name: str
    version: str
    debug: bool = False


class CaptureSettings(BaseModel):
    fps: int = Field(default=1, ge=1)
    monitor: int = 1


class VisionSettings(BaseModel):
    endpoint: str
    timeout: int = 30


class TTSSettings(BaseModel):
    enabled: bool = True


class OverlaySettings(BaseModel):
    enabled: bool = True


class CoachSettings(BaseModel):
    repeat_seconds: int = 20


class LoggingSettings(BaseModel):
    level: str = "INFO"
    file: str = "logs/app.log"


class Settings(BaseModel):
    app: AppSettings
    capture: CaptureSettings
    vision: VisionSettings
    tts: TTSSettings
    overlay: OverlaySettings
    coach: CoachSettings
    logging: LoggingSettings