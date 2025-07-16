# ETL-Pipeline-Portfolio (Work In Progress)
# Airflow Docker Environment for SQL Practice

A containerized Apache Airflow environment with PostgreSQL database for practicing SQL queries, data pipeline development, and workflow orchestration.

## Overview

This project provides a ready-to-use Airflow environment running in Docker containers with:
- **Apache Airflow** (Web UI + Scheduler)
- **PostgreSQL Database** (for both Airflow metadata and practice data)
- **Sample DAGs** for data loading and processing

Perfect for learning SQL, building data pipelines, and experimenting with workflow orchestration.

## Prerequisites

- Docker Desktop installed and running
- Git (for cloning the repository)
- At least 4GB RAM allocated to Docker

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/trueblack/ETL-Pipeline-Portfolio.git
   cd your-repo-name
   ```

2. **Run the setup script**:
   ```powershell
   # Windows PowerShell
   .\setup.ps1
   
 

3. **Access the services**:
   - **Airflow Web UI**: http://localhost:8080
   - **PostgreSQL**: localhost:5432

## Default Credentials

| Service | Username | Password |
|---------|----------|----------|
| Airflow | airflow | airflow |
| PostgreSQL | airflow | airflow |

## Services

### Airflow Web UI (Port 8080)
- View and manage DAGs
- Monitor task execution
- Browse logs and task history
- Trigger manual runs

### PostgreSQL Database (Port 5432)
- **Database**: airflow
- **Host**: localhost
- **Port**: 5432
- Connect using any PostgreSQL client

## Sample DAGs

### Data Loading DAG (`data_loading_pipeline`)
- Creates sample tables (users, products)
- Loads sample data from various sources
- Demonstrates basic ETL operations

### Usage Examples
```sql
-- Connect to PostgreSQL and try these queries
SELECT * FROM users;
SELECT * FROM products;
SELECT age, COUNT(*) FROM users GROUP BY age;
```

## Project Structure

```
├── docker-compose.yml      # Docker services configuration
├── setup.ps1              # Windows PowerShell setup script
├── dags/                   # Airflow DAGs directory
│   ├── data_loading_dag.py
│   └── sample_dag.py
├── logs/                   # Airflow logs (auto-created)
├── plugins/                # Airflow plugins (auto-created)
└── config/                 # Airflow config (auto-created)
```

## Common Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View service status
docker-compose ps

# View logs
docker-compose logs -f airflow-webserver

# Restart services
docker-compose restart
```

## Adding Your Own DAGs

1. Create Python files in the `dags/` directory
2. Airflow will automatically detect new DAGs
3. Use the PostgreSQL connection ID: `postgres_default`

## Database Connection Details

When connecting from external tools:
- **Host**: localhost
- **Port**: 5432
- **Database**: airflow
- **Username**: airflow
- **Password**: airflow

## Learning Resources

- **Airflow Documentation**: https://airflow.apache.org/docs/
- **PostgreSQL Tutorial**: https://www.postgresql.org/docs/
- **SQL Practice**: Use the sample data in the `users` and `products` tables

## Troubleshooting

### Services Won't Start
- Ensure Docker Desktop is running
- Check if ports 8080, 5050, 5432 are available
- Increase Docker memory allocation to 4GB+

### Can't Access Web UI
- Wait 2-3 minutes for services to fully start
- Check logs: `docker-compose logs airflow-webserver`
- Try restarting: `docker-compose restart`

### Database Connection Issues
- Verify PostgreSQL is running: `docker-compose ps`
- Check connection details match the defaults above
- Try connecting via pgAdmin first

## Contributing

Feel free to add new DAGs, improve the setup scripts, or enhance the documentation!

## License

This project is open source and available under the MIT License.