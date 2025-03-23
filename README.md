# Satsang Management System

## Overview
The Satsang Management System is a comprehensive web application built using Streamlit for managing and tracking Satsang activities. It provides functionality for data entry, reporting, and administrative settings.

## Features

### 1. Data Entry
- **Main Satsang Details**
  - Date and time selection
  - Duration tracking
  - Language selection (English, Hindi, Punjabi)
  - Preacher details (SK, SR, Cassette)
  - Attendance tracking (Gents, Ladies, Children)
  - Grading system (A to E)
  - Additional details (Pathi Name, Shabad, Bani)

- **Baal Satsang Details**
  - Sunday-specific entries
  - Time and duration tracking
  - Language selection
  - Preacher information
  - Children attendance tracking
  - Grading system

- **Vehicle Details (Common)**
  - Tracks various vehicle types:
    - Two-wheelers (Bicycle, Two-wheeler)
    - Three-wheelers (Rickshaw, Three-wheeler)
    - Four-wheelers (Car, Jeep)
    - Heavy vehicles (Bus, Truck, Tractor-Trolley)
    - Traditional (Bull-Cart)

### 2. Reports

#### A. Average Sangat Report
- **Filters**
  - Year selection (2020-2026)
  - Satsang type (Main/Baal)
  - Language
  - Time slot (Morning/Evening)
  - Geographic filters (Zone, State, Area)
  - Day of week
  - Preacher type

- **Data Display**
  - Zone-wise breakdown
  - Day-wise averages
  - Language-wise distribution
  - Baal Satsang statistics

#### B. Centre Listing Report
- **Geographic Filters**
  - Zone selection
  - State selection
  - Area selection
  - Centre name search

- **Satsang Info Filters**
  - Centre type (C, SC, P)
  - Satsang type
  - Language
  - Day and time slot
  - Preacher details (Type, Gender, Grade)

- **Sangat Count Ranges**
  - Male attendance range
  - Female attendance range
  - Children attendance range

### 3. Settings
- **User Profile Management**
  - Personal information
  - Contact details
  - Role assignment (Organizer, Zonal Staff, Admin)
  - Zone allocation

- **Notification Preferences**
  - Email notifications
  - SMS alerts
  - Report generation notifications

## Technical Details

### Technology Stack
- **Frontend Framework**: Streamlit
- **Data Handling**: Pandas
- **UI Components**: Custom CSS, Streamlit Components

### State Management
- Session state for navigation
- Page routing system
- Filter state management

### Data Export Capabilities
- Excel export
- PDF export

### UI/UX Features
- Responsive design
- Advanced filtering system
- Interactive data tables
- Clean and professional styling

## System Requirements
- Python 3.x
- Required Python packages:
  - streamlit
  - pandas
  - Pillow (PIL)

## Installation and Setup
1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guidelines

### For Users
1. **Data Entry**
   - Select "Data Entry" from navigation
   - Choose between Main or Baal Satsang
   - Fill in required details
   - Add vehicle information
   - Save or cancel the entry

2. **Generating Reports**
   - Navigate to "Reports"
   - Select report type
   - Apply desired filters
   - Use export options as needed

3. **Managing Settings**
   - Update profile information
   - Set notification preferences
   - Save changes

### For Administrators
1. **User Management**
   - Assign roles and permissions
   - Monitor user activities
   - Manage zone allocations

2. **Report Management**
   - Access comprehensive reports
   - Export data for analysis
   - Monitor system usage

## Data Schema

### Satsang Entry
```python
{
    "date": "Date",
    "time": "Time",
    "duration": "Float",
    "language": "String",
    "preacher_type": "String",
    "preacher_name": "String",
    "grading": "String",
    "attendance": {
        "gents": "Integer",
        "ladies": "Integer",
        "children": "Integer"
    },
    "vehicles": {
        "bicycle": "Integer",
        "rickshaw": "Integer",
        # ... other vehicle types
    }
}
```

### Report Structure
```python
{
    "zone": "String",
    "state": "String",
    "area": "String",
    "centre_name": "String",
    "metrics": {
        "attendance": "Integer",
        "frequency": "Integer",
        "average": "Float"
    }
}
```

## Security Considerations
- Role-based access control
- Data validation
- Input sanitization
- Secure export handling

## Future Enhancements
1. Mobile application support
2. Advanced analytics dashboard
3. Real-time reporting
4. Integration with other systems
5. Automated report scheduling

## Support and Contact
For technical support or queries, please contact the system administrator.

## Version History
- Current Version: 1.0
- Last Updated: [Current Date]

---
*This documentation is maintained by the Satsang Management System development team.* 