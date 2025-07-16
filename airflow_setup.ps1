# Airflow Docker Setup Script for Windows
Write-Host "Setting up Airflow with Docker on Windows..." -ForegroundColor Green

# Create necessary directories
Write-Host "Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path ".\dags"
New-Item -ItemType Directory -Force -Path ".\logs"
New-Item -ItemType Directory -Force -Path ".\plugins"
New-Item -ItemType Directory -Force -Path ".\config"

# Create .env file (optional, but good practice)
Write-Host "Creating .env file..." -ForegroundColor Yellow
@"
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
"@ | Out-File -FilePath ".env" -Encoding utf8

Write-Host "Created .env file with default credentials" -ForegroundColor Green

# Initialize Airflow
Write-Host "Initializing Airflow database..." -ForegroundColor Yellow
docker-compose up airflow-init

if ($LASTEXITCODE -eq 0) {
    Write-Host "Starting Airflow services..." -ForegroundColor Yellow
    docker-compose up -d
    
    Write-Host ""
    Write-Host "Airflow is starting up!" -ForegroundColor Green
    Write-Host "Web UI will be available at: http://localhost:8080" -ForegroundColor Cyan
    Write-Host "Default credentials: username=airflow, password=airflow" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Useful commands:" -ForegroundColor Yellow
    Write-Host "  Check status: docker-compose ps" -ForegroundColor White
    Write-Host "  View logs: docker-compose logs -f" -ForegroundColor White
    Write-Host "  Stop services: docker-compose down" -ForegroundColor White
    Write-Host "  Restart services: docker-compose restart" -ForegroundColor White
} else {
    Write-Host "Initialization failed. Check the logs above." -ForegroundColor Red
}