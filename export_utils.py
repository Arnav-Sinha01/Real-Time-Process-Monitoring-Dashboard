# export_utils.py
import csv
import json
import os
from datetime import datetime
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from process_history import get_process_history

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False

def export_process_history(parent):
    """
    Export process history data to CSV format
    
    Args:
        parent: The parent widget (for dialog display)
    """
    process_history = get_process_history()
    
    if not process_history:
        QMessageBox.warning(parent, "Export Error", "No process history data to export.")
        return
        
    # Generate default filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"process_history_{timestamp}.csv"
    
    # Ask user for file location
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getSaveFileName(
        parent, "Export Process History", default_filename, 
        "CSV Files (*.csv)", options=options
    )
    
    if not file_path:
        return  # User canceled
    
    if not file_path.lower().endswith('.csv'):
        file_path += '.csv'
        
    try:
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['Timestamp', 'PID', 'Name', 'CPU %', 'Memory %'])
            
            # Write data
            for snapshot in process_history:
                timestamp = snapshot['timestamp']
                for process in snapshot['processes']:
                    writer.writerow([timestamp] + list(process))
                    
        QMessageBox.information(parent, "Export Successful", 
                               f"Process history exported successfully to {file_path}")
            
    except Exception as e:
        QMessageBox.critical(parent, "Export Error", f"Failed to export data: {str(e)}")

def export_process_data(parent, process_table):
    """
    Export current process data from the table to various file formats
    
    Args:
        parent: The parent widget (for dialog display)
        process_table: The QTableWidget containing process data
    """
    # Get current process data
    rows = process_table.rowCount()
    columns = process_table.columnCount()
    
    if rows == 0:
        QMessageBox.warning(parent, "Export Error", "No process data to export.")
        return
        
    # Create data structure for export
    headers = []
    for col in range(columns):
        headers.append(process_table.horizontalHeaderItem(col).text())
        
    data = []
    for row in range(rows):
        row_data = []
        for col in range(columns):
            item = process_table.item(row, col)
            row_data.append(item.text() if item else "")
        data.append(row_data)
    
    # Generate default filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"process_data_{timestamp}"
    
    # Prepare file filters based on available libraries
    file_filters = "CSV Files (*.csv);;JSON Files (*.json)"
    if PANDAS_AVAILABLE:
        file_filters += ";;Excel Files (*.xlsx)"
    file_filters = "All Files (*.*);;" + file_filters
    
    # Ask user for file type and location
    options = QFileDialog.Options()
    file_path, selected_filter = QFileDialog.getSaveFileName(
        parent, "Export Process Data", default_filename, 
        file_filters, options=options
    )
    
    if not file_path:
        return  # User canceled
    
    # Ensure file has correct extension
    if selected_filter == "CSV Files (*.csv)" and not file_path.lower().endswith('.csv'):
        file_path += '.csv'
    elif selected_filter == "JSON Files (*.json)" and not file_path.lower().endswith('.json'):
        file_path += '.json'
    elif selected_filter == "Excel Files (*.xlsx)" and not file_path.lower().endswith('.xlsx'):
        file_path += '.xlsx'
        
    try:
        if selected_filter == "CSV Files (*.csv)":
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(data)
                
        elif selected_filter == "JSON Files (*.json)":
            json_data = []
            for row in data:
                json_data.append(dict(zip(headers, row)))
            with open(file_path, 'w') as f:
                json.dump(json_data, f, indent=4)
                
        elif selected_filter == "Excel Files (*.xlsx)" and PANDAS_AVAILABLE:
            df = pd.DataFrame(data, columns=headers)
            df.to_excel(file_path, index=False)
        
        elif selected_filter == "Excel Files (*.xlsx)" and not PANDAS_AVAILABLE:
            QMessageBox.warning(parent, "Export Error", 
                               "Excel export requires pandas and openpyxl. Please install them with: pip install pandas openpyxl")
            return
            
        QMessageBox.information(parent, "Export Successful", 
                               f"Process data exported successfully to {file_path}")
            
    except Exception as e:
        QMessageBox.critical(parent, "Export Error", f"Failed to export data: {str(e)}")