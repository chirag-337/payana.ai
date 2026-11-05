from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Payana.ai API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Environment
    ENV: str = "development"
    DEBUG: bool = True
    
    # Supabase / DB Configuration
    SUPABASE_URL: str = "https://your-supabase-project.supabase.co"
    SUPABASE_ANON_KEY: str = "anon-key-placeholder"
    SUPABASE_SERVICE_ROLE_KEY: str = "service-role-key-placeholder"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/payana"
    
    # JWT & Auth
    JWT_SECRET_KEY: str = "payana-jwt-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Digital Twin / Simulation
    TWIN_SERVICE_TOKEN: str = "payana-twin-secret-token"
    
    # City Settings
    DEFAULT_CITY: str = "Bengaluru"
    DEFAULT_LAT: float = 12.9716
    DEFAULT_LNG: float = 77.5946

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

