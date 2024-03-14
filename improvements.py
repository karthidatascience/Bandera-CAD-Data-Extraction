import streamlit as st
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import time

def scrape_data(parcel_numbers, selected_fields):
    rows = []
    total_requests = len(parcel_numbers)
    start_time = time.time()

    for idx, txroll_cadaccountnumber in enumerate(parcel_numbers, start=1):
        url = f'https://esearch.bancad.org/Property/View/{txroll_cadaccountnumber}?year=2023'
        r = requests.get(url)
        try:
            soup = BeautifulSoup(r.content, 'html.parser')

            scraped_data = {field: '' for field in selected_fields}

            for field in selected_fields:
                pattern = re.compile(rf'{field.replace("_", " ")}:<\/th>\s*<td[^>]*>(.*?)<\/td>', re.IGNORECASE | re.DOTALL)
                match = re.search(pattern, str(soup))
                if match:
                    scraped_data[field] = match.group(1).strip()

            # Additional scraping logic from the second code
            s1 = soup.find_all('div', class_='panel panel-primary')[4]
            description = re.findall(r'Description: <\/strong>[^<>]*', str(s1))
            description = ' '.join(description).replace('Description: </strong>', '')

            Type = re.findall(r'Type: <\/strong>[^<>]*', str(s1))
            Type = ' '.join(Type).replace('Type: </strong>', '')

            State_Code = re.findall(r'State Code: <\/strong>[^<>]*', str(s1))
            State_Code = ' '.join(State_Code).replace('State Code: </strong>', '')

            Living_Area = re.findall(r'Living Area: <\/strong>[^<>]*', str(s1))
            Living_Area = ' '.join(Living_Area).replace('Living Area: </strong>', '')

            Value = re.findall(r'Value: <\/strong>[^<>]*', str(s1))
            Value = ' '.join(Value).replace('Value: </strong>', '')

            for row in s1.find_all('tr'):  # Loop through each row
                columns = row.find_all('td')  # Use 'th' for header cells
                row_data = [column.text for column in columns]

                row_dict = {
                    'parcel_number': txroll_cadaccountnumber,
                    'Value': Value,
                    'row_data': row_data,
                    'description': description,
                    'Type': Type,
                    'State_Code': State_Code,
                    'Living_Area': Living_Area,
                }
                rows.append(row_dict)

            # Display estimated time remaining
            elapsed_time = time.time() - start_time
            avg_time_per_request = elapsed_time / idx if idx > 0 else 0
            remaining_requests = total_requests - idx
            estimated_time_remaining = avg_time_per_request * remaining_requests

            st.markdown(f"<p style='color: green;'>Estimated time remaining: {round(estimated_time_remaining, 2)} seconds  {idx} completed</p>",
                        unsafe_allow_html=True)

        except Exception as e:
            st.warning(f"Failed to fetch data for parcel number {txroll_cadaccountnumber}: {str(e)}")

    result_df = pd.DataFrame(rows)
    return result_df

def main():
    st.title('Bandera Improvements Scraper')
    st.write("Upload an Excel file containing 'parcel_number' column.")

    uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx', 'xls'])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            min_range = st.number_input('Enter the start index of parcel numbers:', value=0)
            max_range = st.number_input('Enter the end index of parcel numbers:', value=len(df), min_value=min_range, max_value=len(df))
            parcel_numbers = df['parcel_number'].iloc[min_range:max_range].tolist()

            available_fields = ['Select All', 'txroll_cadaccountnumber','Value','row_data','description','Type','State_Code','Living_Area']

            selected_fields = st.multiselect('Select Fields for Output', available_fields)

            if 'Select All' in selected_fields:
                selected_fields = available_fields[1:]

            if st.button('Scrape Data'):
                scraped_data = scrape_data(parcel_numbers, selected_fields)
                st.write(scraped_data)

                csv = scraped_data.to_csv(index=False)
                st.download_button(label="Download Output", data=csv, file_name='bandera_scraped_data.csv', mime='text/csv')

        except Exception as e:
            st.warning(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
