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
            scraped_data = {
                'prop_id': '',
                'Geographic_ID': '',
                'Type': '',
                'Property_Use': '',
                'Situs_Address': '',
                'Map_ID': '',
                'Zoning': '',
                'Mapsco': '',
                'Legal_Description': '',
                'Abstract_Subdivision': '',
                'Neighborhood': '',
                'owner_ID': '',
                'name': '',
                'Agent': '',
                'Mailing_Address': '',
                'Ownership': '',
                'Improvement_Homesite_Value': '',
                'personal_property_value': '',
                'Improvement_Non_Homesite_Value': '',
                'Land_Homesite_Value': '',
                'Land_Non_Homesite_Value': '',
                'Agricultural_Market_Valuation': '',
                'Market_Value': '',
                'Appraised_Value': '',
                'Assessed_Value': '',
                'Ag_Use_Value': ''
            }

            if 'prop_id' in selected_fields:
                prop_id = re.findall('Property ID:<\/th>\s+<td class="tbltrwidth">[^<>]*', str(soup))
                prop_id = list(set(prop_id))
                prop_id = ' '.join(prop_id)
                prop_id = re.sub('\s+', ' ', prop_id).replace('Property ID:</th> <td class="tbltrwidth">', '').strip()
                scraped_data['prop_id'] = prop_id

            if 'Geographic_ID' in selected_fields:
                Geographic_ID = re.findall(r'Geographic ID: <\/strong>[^<>]*', str(soup))
                Geographic_ID = list(set(Geographic_ID))
                Geographic_ID = ' '.join(Geographic_ID)
                Geographic_ID = re.sub('\s+', ' ', Geographic_ID).replace('Geographic ID: </strong>', '').strip()
                scraped_data['Geographic_ID'] = Geographic_ID

            # Similar processing for other fields...
            if 'Type' in selected_fields:
                Type = re.findall(
                    r'Type:<\/th>\s+<td>[^<>]*', str(soup))
                Type = list(set(Type))
                Type = ' '.join(Type)
                Type = re.sub('\s+', ' ', Type).replace('Type:</th> <td>', '').strip()
                scraped_data['Type'] = Type

            if 'Property_Use' in selected_fields:
                Property_Use = re.findall(r'Property Use:<\/th>\s<td class="wordbreak">[^<>]*', str(soup))
                Property_Use = list(set(Property_Use))
                Property_Use = ' '.join(Property_Use)
                Property_Use = re.sub('\s+', ' ', Property_Use).replace('Property Use:</th> <td class="wordbreak">',
                                                                        '').strip()
                scraped_data['Property_Use'] = Property_Use

            if 'Situs_Address' in selected_fields:
                Situs_Address = re.findall(r'Situs Address:<\/th><td colspan="3">[^<>]*', str(soup))
                Situs_Address = list(set(Situs_Address))
                Situs_Address = ' '.join(Situs_Address)
                Situs_Address = re.sub('\s+', ' ', Situs_Address).replace('Situs Address:</th><td colspan="3">',
                                                                          '').strip()
                scraped_data['Situs_Address'] = Situs_Address


            if 'Map_ID' in selected_fields:
                Map_ID = re.findall(r'Map ID:<\/th>\s+<td>[^<>]*', str(soup))
                Map_ID = list(set(Map_ID))
                Map_ID = ' '.join(Map_ID)
                Map_ID = re.sub('\s+', ' ', Map_ID).replace('Map ID:</th> <td>', '').strip()
                scraped_data['Map_ID'] = Map_ID

            if 'Zoning' in selected_fields:
                Zoning = re.findall(r'Zoning: <\/strong>[^<>]*', str(soup))
                Zoning = list(set(Zoning))
                Zoning = ' '.join(Zoning)
                Zoning = re.sub('\s+', ' ', Zoning).replace('Zoning: </strong>', '').strip()
                scraped_data['Zoning'] = Zoning

            if 'Mapsco' in selected_fields:
                Mapsco = re.findall(r'Mapsco: <\/strong>[^<>]*', str(soup))
                Mapsco = list(set(Mapsco))
                Mapsco = ' '.join(Mapsco)
                Mapsco = re.sub('\s+', ' ', Mapsco).replace('Mapsco: </strong>', '').strip()
                scraped_data['Mapsco'] = Mapsco


            if 'Legal_Description' in selected_fields:
                Legal_Description = re.findall(r'Legal Description:<\/th>\s+<td colspan="3">[^<>]*', str(soup))
                Legal_Description = list(set(Legal_Description))
                Legal_Description = ' '.join(Legal_Description)
                Legal_Description = re.sub('\s+', ' ', Legal_Description).replace(
                    'Legal Description:</th> <td colspan="3">', '').strip()
                scraped_data['Legal_Description'] = Legal_Description


            if 'Abstract_Subdivision' in selected_fields:
                Abstract_Subdivision = re.findall(r'Abstract\/Subdivision:<\/th><td colspan="3">[^<>]*', str(soup))
                Abstract_Subdivision = list(set(Abstract_Subdivision))
                Abstract_Subdivision = ' '.join(Abstract_Subdivision)
                Abstract_Subdivision = re.sub('\s+', ' ', Abstract_Subdivision).replace(
                    'Abstract/Subdivision:</th><td colspan="3">', '').strip()
                scraped_data['Abstract_Subdivision'] = Abstract_Subdivision



            if 'Neighborhood' in selected_fields:
                Neighborhood = re.findall(r'Neighborhood:<\/th><td class="wordbreak" colspan="3">[^<>]*', str(soup))
                Neighborhood = list(set(Neighborhood))
                Neighborhood = ' '.join(Neighborhood)
                Neighborhood = re.sub('\s+', ' ', Neighborhood).replace(
                    'Neighborhood:</th><td class="wordbreak" colspan="3">', '').strip()
                scraped_data['Neighborhood'] = Neighborhood


            if 'owner_ID' in selected_fields:
                owner_ID = re.findall(r'Owner ID:<\/th><td colspan="3">[^<>]*', str(soup))
                owner_ID = list(set(owner_ID))
                owner_ID = ' '.join(owner_ID)
                owner_ID = re.sub('\s+', ' ', owner_ID).replace('Owner ID:</th><td colspan="3">', '').strip()
                scraped_data['owner_ID'] = owner_ID

            if 'name' in selected_fields:
                name = re.findall(r'Name:<\/th><td colspan="3">[^<>]*', str(soup))
                name = list(set(name))
                name = ' '.join(name)
                name = re.sub('\s+', ' ', name).replace('Name:</th><td colspan="3">', '').strip()
                scraped_data['name'] = name


            if 'basement' in selected_fields:
                Agent = re.findall(r'Agent:<\/th><td colspan="3">[^<>]*', str(soup))
                Agent = list(set(Agent))
                Agent = ' '.join(Agent)
                Agent = re.sub('\s+', ' ', Agent).replace('Agent:</th><td colspan="3">', '').strip()
                scraped_data['Agent'] = Agent


            if 'Mailing_Address' in selected_fields:
                Mailing_Address = re.findall(r'Address:\s*(.*?)\s*<\/tr>', str(soup))
                Mailing_Address = list(set(Mailing_Address))
                Mailing_Address = ' '.join(Mailing_Address)
                Mailing_Address = re.sub('\s+', ' ', Mailing_Address).replace('</th><td colspan="3">', '').strip()
                scraped_data['Mailing_Address'] = Mailing_Address


            if 'Ownership' in selected_fields:
                Ownership = re.findall(r'Ownership:<\/th><td colspan="3">[^<>]*', str(soup))
                Ownership = list(set(Ownership))
                Ownership = ' '.join(Ownership)
                Ownership = re.sub('\s+', ' ', Ownership).replace('Ownership:</th><td colspan="3">', '').strip()
                scraped_data['Ownership'] = Ownership

            if 'Improvement_Homesite_Value' in selected_fields:
                Improvement_Homesite_Value = re.findall(
                    r'Improvement Homesite Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Improvement_Homesite_Value = list(set(Improvement_Homesite_Value))
                Improvement_Homesite_Value = ' '.join(Improvement_Homesite_Value)
                Improvement_Homesite_Value = re.sub('\s+', ' ', Improvement_Homesite_Value).replace(
                    'Improvement Homesite Value:</th><td class="table-number">', '').strip()
                scraped_data['Improvement_Homesite_Value'] = Improvement_Homesite_Value


            if 'personal_property_value' in selected_fields:
                personal_property_value = re.findall(r'Personal Property Value:<\/th><td class="table-number">[^<>]*',
                                                     str(soup))
                personal_property_value = list(set(personal_property_value))
                personal_property_value = ' '.join(personal_property_value)
                personal_property_value = re.sub('\s+', ' ', personal_property_value).replace(
                    'Personal Property Value:</th><td class="table-number">', '').strip()
                scraped_data['personal_property_value'] = personal_property_value

            if 'Improvement_Non_Homesite_Value' in selected_fields:
                Improvement_Non_Homesite_Value = re.findall(
                    r'Improvement Non-Homesite Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Improvement_Non_Homesite_Value = list(set(Improvement_Non_Homesite_Value))
                Improvement_Non_Homesite_Value = ' '.join(Improvement_Non_Homesite_Value)
                Improvement_Non_Homesite_Value = re.sub('\s+', ' ', Improvement_Non_Homesite_Value).replace(
                    'Improvement Non-Homesite Value:</th><td class="table-number">', '').strip()
                scraped_data['Improvement_Non_Homesite_Value'] = Improvement_Non_Homesite_Value

            if 'Land_Homesite_Value' in selected_fields:
                Land_Homesite_Value = re.findall(r'Land Homesite Value:<\/th><td class="table-number">[^<>]*',
                                                 str(soup))
                Land_Homesite_Value = list(set(Land_Homesite_Value))
                Land_Homesite_Value = ' '.join(Land_Homesite_Value)
                Land_Homesite_Value = re.sub('\s+', ' ', Land_Homesite_Value).replace(
                    'Land Homesite Value:</th><td class="table-number">', '').strip()
                scraped_data['Land_Homesite_Value'] = Land_Homesite_Value

            if 'Land_Non_Homesite_Value' in selected_fields:
                Land_Non_Homesite_Value = re.findall(r'Land Non-Homesite Value:<\/th><td class="table-number">[^<>]*',
                                                     str(soup))
                Land_Non_Homesite_Value = list(set(Land_Non_Homesite_Value))
                Land_Non_Homesite_Value = ' '.join(Land_Non_Homesite_Value)
                Land_Non_Homesite_Value = re.sub('\s+', ' ', Land_Non_Homesite_Value).replace(
                    'Land Non-Homesite Value:</th><td class="table-number">', '').strip()

                scraped_data['Land_Non_Homesite_Value'] = Land_Non_Homesite_Value


            if 'Agricultural_Market_Valuation' in selected_fields:
                Agricultural_Market_Valuation = re.findall(
                    r'Agricultural Market Valuation:<\/th><td class="table-number">[^<>]*', str(soup))
                Agricultural_Market_Valuation = list(set(Agricultural_Market_Valuation))
                Agricultural_Market_Valuation = ' '.join(Agricultural_Market_Valuation)
                Agricultural_Market_Valuation = re.sub('\s+', ' ', Agricultural_Market_Valuation).replace(
                    'Agricultural Market Valuation:</th><td class="table-number">', '').strip()
                scraped_data['Agricultural_Market_Valuation'] = Agricultural_Market_Valuation

            if 'Market_Value' in selected_fields:
                Market_Value = re.findall(r'Market Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Market_Value = list(set(Market_Value))
                Market_Value = ' '.join(Market_Value)
                Market_Value = re.sub('\s+', ' ', Market_Value).replace('Market Value:</th><td class="table-number">',
                                                                        '').strip()
                scraped_data['Market_Value'] = Market_Value
            #
            if 'Appraised_Value' in selected_fields:
                Appraised_Value = re.findall(r'Appraised Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Appraised_Value = list(set(Appraised_Value))
                Appraised_Value = ' '.join(Appraised_Value)
                Appraised_Value = re.sub('\s+', ' ', Appraised_Value).replace(
                    'Appraised Value:</th><td class="table-number">', '').strip()
                scraped_data['Appraised_Value'] = Appraised_Value

            if 'Assessed_Value' in selected_fields:
                Assessed_Value = re.findall(r'Assessed Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Assessed_Value = list(set(Assessed_Value))
                Assessed_Value = ' '.join(Assessed_Value)
                Assessed_Value = re.sub('\s+', ' ', Assessed_Value).replace(
                    'Assessed Value:</th><td class="table-number">', '').strip()
                scraped_data['Assessed_Value'] = Assessed_Value

            if 'Ag_Use_Value' in selected_fields:
                Ag_Use_Value = re.findall(r'Ag Use Value:<\/th><td class="table-number">[^<>]*', str(soup))
                Ag_Use_Value = list(set(Ag_Use_Value))
                Ag_Use_Value = ' '.join(Ag_Use_Value)
                Ag_Use_Value = re.sub('\s+', ' ', Ag_Use_Value).replace('Ag Use Value:</th><td class="table-number">',
                                                                        '').strip()
                scraped_data['Ag_Use_Value'] = Ag_Use_Value

            # if 'Exemptions' in selected_fields:
            #     Exemptions = re.findall(r'Exemptions:<\/th>\s+<td colspan="3">[^<>]*', str(soup))
            #     Exemptions = list(set(Exemptions))
            #     Exemptions = ' '.join(Exemptions)
            #     Exemptions = re.sub('\s+', ' ', Exemptions).replace('Exemptions:</th> <td colspan="3">', '').strip()
            #     scraped_data['Exemptions'] = Exemptions

            # Create a dictionary to store the scraped data
            row_dict = {'parcel_number': txroll_cadaccountnumber, **scraped_data}
            rows.append(row_dict)

            # Display estimated time remaining
            elapsed_time = time.time() - start_time
            avg_time_per_request = elapsed_time / idx if idx > 0 else 0
            remaining_requests = total_requests - idx
            estimated_time_remaining = avg_time_per_request * remaining_requests

            st.markdown(
                f"<p style='color: green;'>Estimated time remaining: {round(estimated_time_remaining, 2)} seconds  {idx} completed</p>",
                unsafe_allow_html=True)

        except Exception as e:
            st.warning(f"Failed to fetch data for parcel number {txroll_cadaccountnumber}: {str(e)}")
            # Set all selected fields to empty strings
            scraped_data = {field: '' for field in selected_fields}

    result_df = pd.DataFrame(rows)
    return result_df


def main():
    st.title('Bandera Property Scraper')
    st.write("Upload an Excel file containing 'parcel_number' column.")

    uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx', 'xls'])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            min_range = st.number_input('Enter the start index of parcel numbers:', value=0)
            max_range = st.number_input('Enter the end index of parcel numbers:', value=len(df), min_value=min_range,
                                        max_value=len(df))
            parcel_numbers = df['parcel_number'].iloc[min_range:max_range].tolist()

            # Define available fields for selection
            available_fields = ['Select All', 'prop_id', 'Geographic_ID', 'Type', 'Property_Use', 'Situs_Address',
                                'Map_ID', 'Zoning', 'Mapsco', 'Legal_Description', 'Abstract_Subdivision',
                                'Neighborhood', 'owner_ID', 'name', 'Agent', 'Mailing_Address', 'Ownership',
                                'Improvement_Homesite_Value', 'personal_property_value',
                                'Improvement_Non_Homesite_Value', 'Land_Homesite_Value', 'Land_Non_Homesite_Value',
                                'Agricultural_Market_Valuation', 'Market_Value', 'Appraised_Value', 'Assessed_Value',
                                'Ag_Use_Value']  # Add more fields here

            # Checkbox options for selecting fields
            selected_fields = st.multiselect('Select Fields for Output', available_fields)

            # Check if 'Select All' is chosen and update selected_fields accordingly
            if 'Select All' in selected_fields:
                selected_fields = available_fields[1:]  # Exclude the 'Select All' option

            if st.button('Scrape Data'):
                scraped_data = scrape_data(parcel_numbers, selected_fields)
                st.write(scraped_data)

                # Download the output file
                csv = scraped_data.to_csv(index=False)
                st.download_button(label="Download Output", data=csv, file_name='Bandera_scraped_data.csv',
                                   mime='text/csv')

        except Exception as e:
            st.warning(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
