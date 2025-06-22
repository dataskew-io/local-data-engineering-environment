# Local Data Engineering Environment

A complete local development environment for data processing and analytics using Jupyter notebooks, dlt for data loading and transformation, and DuckDB for embedded analytics.

## 🎯 Project Overview

This project sets up a modern data engineering environment that runs entirely locally using open-source tools. Perfect for experimentation, prototyping, and personal data projects.

### Key Features

- **dlt**: Modern data loading and transformation library with schema management
- **DuckDB**: Embedded analytical database with SQL query capabilities
- **Jupyter**: Interactive development environment
- **Python Virtual Environment**: Isolated dependencies
- **Data Quality Checks**: Built-in validation and monitoring
- **Schema-Aware Analytics**: Proper handling of dlt's schema system

## 🧰 Prerequisites

- Python 3.9 or higher
- Basic knowledge of Python and SQL
- Familiarity with Jupyter Notebooks
- Git (optional but recommended)

## 📂 Project Structure

```
local-data-engineering-environment/
├── notebooks/
│   └── data_workflow.ipynb          # Main workflow notebook
├── data/
│   └── sample.csv                   # Sample dataset
├── env/                             # Virtual environment (created)
├── output/                          # Generated outputs (created)
├── requirements.txt                 # Python dependencies
├── setup.sh                         # Linux/Mac setup script
├── setup.bat                        # Windows setup script
├── test_setup.py                    # Validation script
├── .env                             # Environment variables (optional)
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd local-data-engineering-environment

# Run the automated setup script
./setup.sh  # Linux/Mac
# OR
setup.bat   # Windows
```

### 2. Launch Jupyter

```bash
# Activate virtual environment
source env/bin/activate  # Linux/Mac
# OR
env\Scripts\activate.bat  # Windows

# Start Jupyter notebook
jupyter notebook
```

### 3. Run the Workflow

1. Open `notebooks/data_workflow.ipynb`
2. Run all cells to see the complete data pipeline in action
3. Explore the generated outputs in the `output/` directory

## 📊 What's Included

### Sample Dataset

The project includes a sample sales dataset (`data/sample.csv`) with:

- Date, product, category, quantity, price, and region data
- 10 sample records for demonstration
- Realistic sales data for testing transformations

### Complete Workflow

The `data_workflow.ipynb` notebook demonstrates:

1. **Environment Setup**: Import libraries and configure dlt pipeline
2. **Data Loading**: Load CSV with transformations and quality checks
3. **Schema Management**: Proper handling of dlt's schema system
4. **Analytics**: SQL queries for insights using DuckDB
5. **Data Export**: Save results to CSV files
6. **Quality Monitoring**: Data validation and anomaly detection

### Key Analytics

- Summary statistics with revenue calculations
- Sales by category and region analysis
- Data quality monitoring and validation
- Automated CSV export functionality

## 🔧 Configuration

### Environment Variables

Create a `.env` file (optional) with:

```env
PIPELINE_NAME=local_data
DATASET_NAME=my_data
DATA_DIR=./data
OUTPUT_DIR=./output
JUPYTER_ENABLE_LAB=yes
JUPYTER_TOKEN=your_token_here
```

### Jupyter Features

The setup includes:

- **Jupyter Notebook**: Interactive development environment
- **black**: Code formatting tool (can be used with notebooks)
- **Built-in extensions**: Table of Contents, Code folding, and more

## 📈 Usage Examples

### Basic Data Loading

```python
import dlt

pipeline = dlt.pipeline(
    pipeline_name="local_data",
    destination="duckdb",
    dataset_name="my_data"
)

# Load your data
info = pipeline.run(your_data_generator(), table_name="your_table")
```

### DuckDB Analytics with Schema Handling

```python
import duckdb

# Get database path from pipeline
db_path = pipeline.sql_client().credentials.database
con = duckdb.connect(db_path)

# Find tables in dlt schema
tables = con.execute("""
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_type = 'BASE TABLE' AND table_schema != 'information_schema'
""").fetchdf()

# Query with proper schema
table_name = f"{tables.iloc[0]['table_schema']}.{tables.iloc[0]['table_name']}"
result = con.execute(f"SELECT * FROM {table_name}").fetchdf()
```

## 🛠️ Customization

### Adding Your Own Data

1. Place your CSV files in the `data/` directory
2. Modify the `load_csv_with_transformations()` function in the notebook
3. Update table names and column mappings as needed

### Extending Analytics

- Add new SQL queries to the notebook
- Create additional DuckDB views
- Implement custom data quality checks
- Add visualization with matplotlib/seaborn

### Adding Data Sources

The dlt library supports many data sources:

- APIs (REST, GraphQL)
- Databases (PostgreSQL, MySQL, etc.)
- Cloud storage (S3, GCS, Azure)
- Streaming platforms (Kafka, etc.)

## 🔍 Data Quality Features

The workflow includes built-in data quality checks:

- Null value detection
- Duplicate record identification
- Data type validation
- Business rule validation (positive quantities, prices)
- Date range validation

## 📁 Output Files

After running the workflow, you'll find these files in the `output/` directory:

- `summary_statistics.csv`: Overall dataset metrics
- `sales_by_category.csv`: Category-wise analysis
- `sales_by_region.csv`: Regional performance

## 🚨 Troubleshooting

### Common Issues

**Import Errors**: Make sure your virtual environment is activated and all dependencies are installed:

```bash
pip install -r requirements.txt
```

**No Tables Found**: The notebook now properly handles dlt's schema system. Tables are created in the dataset schema (e.g., `my_data.sample_data`).

**DuckDB Connection Issues**: The database file is created automatically by dlt. The notebook uses the correct database path from the pipeline.

**Jupyter Not Starting**: Ensure you're in the correct directory and the virtual environment is activated.

### Getting Help

- Check the dlt documentation: https://dlthub.com/docs
- DuckDB documentation: https://duckdb.org/docs/
- Jupyter documentation: https://jupyter.org/documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [dlt](https://dlthub.com/) - Modern data loading library
- [DuckDB](https://duckdb.org/) - Embedded analytical database
- [Jupyter](https://jupyter.org/) - Interactive computing platform

---

**Happy Data Engineering! 🚀**
