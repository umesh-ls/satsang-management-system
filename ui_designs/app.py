import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import io
import os
from datetime import datetime, date, time
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Satsang Management System",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .reportview-container {
        background: #f0f2f6;
    }
    .info-box {
        background-color: #e1f5fe;
        border-left: 4px solid #03a9f4;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    /* Navigation menu styling */
    .nav-link {
        padding: 0.5rem 1rem;
        background-color: transparent;
        border: none;
        text-align: left;
        color: #333;
        cursor: pointer;
        width: 100%;
        transition: background-color 0.3s;
    }
    .nav-link:hover {
        background-color: #f0f2f6;
        text-decoration: none;
    }
    .nav-link.active {
        background-color: #e6e6e6;
        font-weight: bold;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 10px 20px;
        background-color: #f0f2f6;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e6e6e6;
    }
    /* Header styling */
    .report-header {
        background-color: white;
        padding: 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Advanced Filters Container */
    .advanced-filters {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin: 1rem 0;
        border: none;
    }
    
    /* Filter Toggle Button */
    .filter-toggle {
        background-color: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        border: 1px solid #e9ecef;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        font-size: 14px;
        color: #495057;
        transition: all 0.2s ease;
    }
    
    .filter-toggle:hover {
        background-color: #e9ecef;
        border-color: #dee2e6;
    }
    
    /* Sub-navigation styling */
    .subnav-container {
        padding: 0.5rem 0;
        margin-left: 1rem;
    }
    
    .subnav-item {
        padding: 0.3rem 1rem;
        color: #666;
        font-size: 0.9em;
    }
    
    /* Empty state styling */
    .empty-state {
        text-align: center;
        padding: 2rem;
        background-color: white;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .container-border {
        border: 1px solid #e6e6e6;
        border-radius: 5px;
        padding: 20px;
        margin: 10px 0;
        background-color: white;
    }
    
    .section-header {
        font-size: 1.1em;
        font-weight: 500;
        margin-bottom: 15px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation using clickable buttons
st.sidebar.title("Navigation")

# Initialize session state for navigation if not exists
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Data Entry"
if 'show_filters' not in st.session_state:
    st.session_state.show_filters = False
if 'current_report' not in st.session_state:
    st.session_state.current_report = None

# Navigation items with sub-sections for Reports
nav_items = ["Data Entry", "Reports", "Settings"]

for nav_item in nav_items:
    is_active = st.session_state.current_page == nav_item
    if st.sidebar.button(
        nav_item,
        key=f"nav_{nav_item}",
        help=f"Go to {nav_item}",
        on_click=lambda x=nav_item: setattr(st.session_state, 'current_page', x)
    ):
        st.session_state.current_page = nav_item
        if nav_item != "Reports":
            st.session_state.current_report = None
    
    # Show sub-navigation for Reports
    if nav_item == "Reports" and st.session_state.current_page == "Reports":
        st.sidebar.markdown('<div class="subnav-container">', unsafe_allow_html=True)
        for report_type in ["Average Sangat Report", "Centre Listing Report"]:
            is_active_report = st.session_state.current_report == report_type
            if st.sidebar.button(
                report_type,
                key=f"subnav_{report_type}",
                help=f"View {report_type}",
                on_click=lambda x=report_type: setattr(st.session_state, 'current_report', x)
            ):
                st.session_state.current_report = report_type
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

def create_data_entry():
    st.header("Data Entry")
    
    # Create tabs for Main and Baal Satsang
    tab1, tab2 = st.tabs(["Main Satsang Details", "Baal Satsang Details"])
    
    # Vehicle Details (Common Section)
    def show_vehicle_details():
        st.subheader("Vehicle Details")
        col1, col2 = st.columns(2)
        with col1:
            vehicles = {
                "Bicycle": st.number_input("Bicycle", min_value=0, key="v_bicycle"),
                "Rickshaw": st.number_input("Rickshaw", min_value=0, key="v_rickshaw"),
                "Bull-Cart": st.number_input("Bull-Cart", min_value=0, key="v_bullcart"),
                "Two-wheeler": st.number_input("Two-wheeler", min_value=0, key="v_twowheeler"),
                "Three-wheeler": st.number_input("Three-wheeler", min_value=0, key="v_threewheeler"),
            }
        with col2:
            vehicles.update({
                "Car": st.number_input("Car", min_value=0, key="v_car"),
                "Jeep": st.number_input("Jeep", min_value=0, key="v_jeep"),
                "Bus": st.number_input("Bus", min_value=0, key="v_bus"),
                "Truck": st.number_input("Truck", min_value=0, key="v_truck"),
                "Tractor-Trolley": st.number_input("Tractor-Trolley", min_value=0, key="v_tractor")
            })
        return vehicles
    
    with tab1:
        # Main Satsang Form
        col1, col2 = st.columns(2)
        
        with col1:
            # Date and Day Selection
            satsang_date = st.date_input("Date", max_value=date.today(), key="main_date")
            day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], key="main_day")
            
            # Start Time Selection with Label
            st.markdown("##### Start Time")
            time_col1, time_col2 = st.columns(2)
            with time_col1:
                hour = st.selectbox("Hour", range(24), format_func=lambda x: f"{x:02d}", key="main_hour")
            with time_col2:
                minute = st.selectbox("Minute", [0, 15, 30, 45], format_func=lambda x: f"{x:02d}", key="main_minute")
            
            # Duration Selection with Hours and Minutes
            st.markdown("##### Duration")
            duration_col1, duration_col2 = st.columns(2)
            with duration_col1:
                duration_hours = st.number_input("Hours", min_value=0, max_value=10, value=1, key="main_duration_hours")
            with duration_col2:
                duration_minutes = st.number_input("Minutes", min_value=0, max_value=59, value=30, key="main_duration_minutes")
            
            language = st.selectbox("Language", ["English", "Hindi", "Punjabi"], key="main_lang")
            preacher_type = st.selectbox("Preacher Type", ["Satsang Karta (SK)", "Satsang Reader (SR)", "Cassette"], key="main_preacher_type")
            
            if preacher_type == "Cassette":
                satsang_by = st.selectbox("Satsang By", ["Huzur Maharaj Ji", "Baba Ji"], key="main_satsang_by")
                preacher_name = st.text_input("Preacher Name", disabled=True, key="main_preacher_name")
            else:
                preacher_name = st.text_input("Preacher Name", key="main_preacher_name")
            
            grading = st.selectbox("Grading (Optional)", ["", "A", "B", "C", "D", "E"], key="main_grading")
            pathi_name = st.text_input("Pathi Name", key="main_pathi")
            shabad_taken = st.text_input("Shabad Taken", key="main_shabad")
            bani_by = st.text_input("Bani by", key="main_bani")
        
        with col2:
            st.subheader("Sangat Count")
            gents = st.number_input("Gents", min_value=0, key="main_gents")
            ladies = st.number_input("Ladies", min_value=0, key="main_ladies")
            children = st.number_input("Children", min_value=0, key="main_children")
        
    with tab2:
        # Baal Satsang Form
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("Baal Satsang is fixed for Sundays")
            satsang_date = st.date_input("Date (Sunday)", max_value=date.today(), key="baal_date")
            
            time_col1, time_col2 = st.columns(2)
            with time_col1:
                hour = st.selectbox("Hour", range(24), format_func=lambda x: f"{x:02d}", key="baal_hour")
            with time_col2:
                minute = st.selectbox("Minute", [0, 15, 30, 45], format_func=lambda x: f"{x:02d}", key="baal_minute")
            
            duration = st.number_input("Duration (hours)", min_value=0.5, max_value=4.0, step=0.5, key="baal_duration")
            language = st.selectbox("Language", ["English", "Hindi", "Punjabi"], key="baal_lang")
            preacher_type = st.selectbox("Preacher Type", ["Satsang Karta (SK)", "Satsang Reader (SR)", "Cassette"], key="baal_preacher_type")
            
            if preacher_type == "Cassette":
                satsang_by = st.selectbox("Satsang By", ["Huzur Maharaj Ji", "Baba Ji"], key="baal_satsang_by")
                preacher_name = st.text_input("Preacher Name", disabled=True, key="baal_preacher_name")
            else:
                preacher_name = st.text_input("Preacher Name", key="baal_preacher_name")
            
            grading = st.selectbox("Grading (Optional)", ["", "A", "B", "C", "D", "E"], key="baal_grading")
        
        with col2:
            st.subheader("Sangat Count")
            children = st.number_input("Children Count", min_value=0, key="baal_children")
    
    # Common Vehicle Details Section
    st.markdown("---")
    vehicles = show_vehicle_details()
    
    # Action Buttons
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save Satsang"):
            st.success("Satsang data saved successfully!")
    with col2:
        if st.button("Cancel Satsang"):
            reason = st.text_input("Reason for Cancellation")
            if reason:
                st.warning("Satsang marked as cancelled")

def create_average_sangat_report():
    # Header in a container
    st.markdown('<div class="report-header">', unsafe_allow_html=True)
    st.header("Average Sangat Report")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Advanced Filters Toggle
    if st.button("🔍 Advanced Filters", key="toggle_filters"):
        st.session_state.show_filters = not st.session_state.show_filters
    
    # Advanced Filters Container
    if st.session_state.show_filters:
        with st.container():
            st.markdown('<div class="advanced-filters">', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                year = st.selectbox("Year", range(2020, 2026))
                satsang_type = st.selectbox("Satsang Type", ["Main", "Baal"])
                language = st.selectbox("Language", ["All", "English", "Hindi", "Punjabi"])
                time_slot = st.selectbox("Time Slot", ["All", "Morning", "Evening"])
                zone = st.selectbox("Zone", ["All", "Zone-2", "Zone-3"])
            
            with col2:
                state = st.selectbox("State", ["All", "Punjab", "Haryana"])
                area = st.selectbox("Area", ["All", "Area A", "Area B"])
                day = st.selectbox("Day of Week", ["All", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
                preacher_type = st.selectbox("Preacher Type", ["All", "SK", "SR", "Cassette"])
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate Report Button
    if st.button("Generate Report"):
        data = {
            "Zone": ["Zone-2", "Zone-2", "Zone-3"],
            "State": ["Punjab", "Punjab", "Haryana"],
            "Area": ["Area A", "Area B", "Area C"],
            "Name of Centre": ["Centre X", "Centre Y", "Centre Z"],
            "Sundays": [50, 45, 40],
            "Wednesday": [30, 25, 20],
            "Thursday": [35, 30, 25],
            "Other Weekdays": [20, 15, 10],
            "English": [40, 35, 30],
            "Baal Satsang": [25, 20, 15]
        }
    else:
        # Empty data for initial display
        data = {
            "Zone": [], "State": [], "Area": [], "Name of Centre": [],
            "Sundays": [], "Wednesday": [], "Thursday": [], "Other Weekdays": [],
            "English": [], "Baal Satsang": []
        }
    
    df = pd.DataFrame(data)
    if df.empty:
        st.markdown('<div class="empty-state">', unsafe_allow_html=True)
        st.info("No data available. Use the filters above and click 'Generate Report' to view data.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.dataframe(df)
    
    # Export buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export to Excel"):
            st.success("Report exported to Excel!")
    with col2:
        if st.button("Export to PDF"):
            st.success("Report exported to PDF!")

def create_centre_listing_report():
    # Header in a container
    st.markdown('<div class="report-header">', unsafe_allow_html=True)
    st.header("Centre Listing Report")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sample data for initial display and after generating report
    def get_report_data():
        return {
            "S.No": [1, 2, 3],
            "Zone": ["Zone-2", "Zone-2", "Zone-3"],
            "State": ["Punjab", "Punjab", "Haryana"],
            "Area": ["Area A", "Area B", "Area C"],
            "Name of Centre": ["Centre X", "Centre Y", "Centre Z"]
        }
    
    # Display initial report
    data = get_report_data()
    df = pd.DataFrame(data)
    st.dataframe(df)
    
    # Advanced Filters Toggle
    if st.button("🔍 Advanced Filters", key="toggle_filters_centre"):
        st.session_state.show_filters = not st.session_state.show_filters
    
    # Advanced Filters Container
    if st.session_state.show_filters:
        with st.container():
            st.markdown('<div class="advanced-filters">', unsafe_allow_html=True)
            
            # Geographic Filters Section
            st.subheader("Geographic Filters")
            col1, col2 = st.columns(2)
            with col1:
                zone = st.selectbox("Zone", ["All", "Zone-2", "Zone-3"])
                state = st.selectbox("State", ["All", "Punjab", "Haryana"])
                area = st.selectbox("Area", ["All", "Area A", "Area B"])
            with col2:
                centre_name = st.text_input("Name of Centre", placeholder="Enter centre name...")
            
            # Satsang Info Filters Section
            st.markdown("---")
            st.subheader("Satsang Info Filters")
            col1, col2 = st.columns(2)
            with col1:
                centre_type = st.selectbox("Centre Type", ["All", "C", "SC", "P"])
                satsang_type = st.selectbox("Satsang Type", ["All", "Main", "Baal"])
                language = st.selectbox("Language", ["All", "English", "Hindi", "Punjabi"])
                day = st.selectbox("Day of Week", ["All", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
            with col2:
                time_slot = st.selectbox("Time Slot", ["All", "Morning", "Evening"])
                preacher_type = st.selectbox("Preacher Type", ["All", "SK", "SR", "Cassette", "Baal Satsang Karta"])
                preacher_gender = st.selectbox("Preacher Gender", ["All", "Male", "Female"])
                preacher_grade = st.selectbox("Preacher Grade", ["All", "A", "B", "C", "D", "E"])
            
            preacher_name = st.text_input("Preacher Name")
            
            # Sangat Count Ranges Section
            st.markdown("---")
            st.subheader("Sangat Count Ranges")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("##### Male Count")
                male_min = st.number_input("Minimum Male Count", min_value=0, value=0)
                male_max = st.number_input("Maximum Male Count", min_value=0, value=1000)
            with col2:
                st.markdown("##### Female Count")
                female_min = st.number_input("Minimum Female Count", min_value=0, value=0)
                female_max = st.number_input("Maximum Female Count", min_value=0, value=1000)
            with col3:
                st.markdown("##### Children Count")
                children_min = st.number_input("Minimum Children Count", min_value=0, value=0)
                children_max = st.number_input("Maximum Children Count", min_value=0, value=1000)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Generate Report Button
    if st.button("Generate Report"):
        # Use the same data structure but could be filtered based on selections
        data = get_report_data()
        df = pd.DataFrame(data)
        st.dataframe(df)
    
    # Export buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export to Excel"):
            st.success("Report exported to Excel!")
    with col2:
        if st.button("Export to PDF"):
            st.success("Report exported to PDF!")

def create_settings():
    st.header("Settings")
    
    # User Profile
    st.subheader("User Profile")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Full Name")
        st.text_input("Email")
        st.selectbox("Role", ["Organizer", "Zonal Staff", "Admin"])
    
    with col2:
        st.text_input("Phone Number")
        st.text_input("Location")
        st.selectbox("Zone", ["Zone-2", "Zone-3"])
    
    # Notification Settings
    st.subheader("Notification Settings")
    st.checkbox("Email Notifications")
    st.checkbox("SMS Notifications")
    st.checkbox("Report Generation Alerts")
    
    # Save Button
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# Page routing based on session state
if st.session_state.current_page == "Data Entry":
    create_data_entry()
elif st.session_state.current_page == "Reports":
    if st.session_state.current_report == "Average Sangat Report":
        create_average_sangat_report()
    elif st.session_state.current_report == "Centre Listing Report":
        create_centre_listing_report()
    else:
        st.markdown('<div class="report-header">', unsafe_allow_html=True)
        st.header("Reports")
        st.markdown('</div>', unsafe_allow_html=True)
        st.info("Please select a report type from the sidebar.")
elif st.session_state.current_page == "Settings":
    create_settings() 