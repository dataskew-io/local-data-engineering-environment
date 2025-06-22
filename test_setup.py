#!/usr/bin/env python3
"""
Test script to verify the local data engineering environment setup.
Run this script after setup to ensure everything is working correctly.
"""

import sys
import importlib
import os

def test_imports():
    """Test that all required packages can be imported."""
    print("🔍 Testing package imports...")
    
    required_packages = [
        'dlt',
        'duckdb', 
        'pandas',
        'numpy',
        'jupyter',
        'matplotlib',
        'seaborn',
        'dotenv'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"  ✅ {package}")
        except ImportError as e:
            print(f"  ❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_dlt_pipeline():
    """Test dlt pipeline creation."""
    print("\n🔍 Testing dlt pipeline...")
    
    try:
        import dlt
        
        pipeline = dlt.pipeline(
            pipeline_name="test_pipeline",
            destination="duckdb",
            dataset_name="test_data"
        )
        
        print(f"  ✅ Pipeline created: {pipeline.pipeline_name}")
        print(f"  ✅ Destination: {pipeline.destination}")
        print(f"  ✅ Dataset: {pipeline.dataset_name}")
        
        return True
    except Exception as e:
        print(f"  ❌ dlt pipeline test failed: {e}")
        return False

def test_duckdb_connection():
    """Test DuckDB connection and basic operations."""
    print("\n🔍 Testing DuckDB connection...")
    
    try:
        import duckdb
        
        # Create connection
        con = duckdb.connect()
        print("  ✅ DuckDB connection created")
        
        # Test basic query
        result = con.execute("SELECT 1 as test_value").fetchdf()
        if result.iloc[0]['test_value'] == 1:
            print("  ✅ Basic query executed successfully")
        else:
            print("  ❌ Basic query failed")
            return False
        
        # Close connection
        con.close()
        print("  ✅ Connection closed")
        
        return True
    except Exception as e:
        print(f"  ❌ DuckDB test failed: {e}")
        return False

def test_file_structure():
    """Test that required files and directories exist."""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        'requirements.txt',
        'data/sample.csv',
        'notebooks/data_workflow.ipynb'
    ]
    
    required_dirs = [
        'data',
        'notebooks',
        'output'
    ]
    
    all_good = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} (missing)")
            all_good = False
    
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"  ✅ {dir_path}/")
        else:
            print(f"  ❌ {dir_path}/ (missing)")
            all_good = False
    
    return all_good

def test_sample_data():
    """Test that sample data can be loaded."""
    print("\n🔍 Testing sample data...")
    
    try:
        import pandas as pd
        
        # Load sample data
        df = pd.read_csv('data/sample.csv')
        print(f"  ✅ Sample data loaded: {len(df)} records")
        print(f"  ✅ Columns: {list(df.columns)}")
        
        # Basic data validation
        if len(df) > 0 and len(df.columns) >= 6:
            print("  ✅ Data structure looks good")
            return True
        else:
            print("  ❌ Data structure validation failed")
            return False
            
    except Exception as e:
        print(f"  ❌ Sample data test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing Local Data Engineering Environment Setup")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("dlt Pipeline", test_dlt_pipeline),
        ("DuckDB Connection", test_duckdb_connection),
        ("File Structure", test_file_structure),
        ("Sample Data", test_sample_data)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"  ❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your environment is ready to use.")
        print("\nNext steps:")
        print("1. Activate your virtual environment")
        print("2. Start Jupyter: jupyter notebook")
        print("3. Open notebooks/data_workflow.ipynb")
        return 0
    else:
        print(f"\n⚠️ {total - passed} test(s) failed. Please check the setup.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 