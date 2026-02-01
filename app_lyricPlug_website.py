# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:02:43 2026

@author: NdlovuSS2
"""

import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="AfriLyrics - African Language Song Lyrics", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Home", "Browse Lyrics", "Language Explorer", "Submit Lyrics", "Contact"],
)

# Sample lyrics data for different African languages
afrikaans_songs = pd.DataFrame({
    "Song Title": ["De La Rey", "Weeskind", "Kaptein", "Afrikaners is Plesierig", "Sarie Marais"],
    "Artist": ["Bok van Blerk", "Laurika Rauch", "Bok van Blerk", "Steve Hofmeyr", "Traditional"],
    "Year": [2006, 1979, 2008, 1995, 1900],
    "Genre": ["Folk", "Pop", "Folk", "Pop", "Traditional"],
})

isizulu_songs = pd.DataFrame({
    "Song Title": ["Gimme Hope Jo'anna", "Nkalakatha", "Jerusalema", "Imali", "Wololo"],
    "Artist": ["Eddie Grant", "Mandoza", "Master KG", "Nasty C", "Babes Wodumo"],
    "Year": [1988, 2000, 2019, 2017, 2016],
    "Genre": ["Reggae", "Kwaito", "Amapiano", "Hip Hop", "Gqom"],
})

sesotho_songs = pd.DataFrame({
    "Song Title": ["Kea Leboga", "Molaleng", "Ke Nako", "Thapelo", "Lesedi"],
    "Artist": ["Rebecca Malope", "Blaq Diamond", "Local Artist", "Gospel Group", "Traditional"],
    "Year": [1995, 2020, 2018, 2015, 1950],
    "Genre": ["Gospel", "Afro Pop", "Traditional", "Gospel", "Traditional"],
})

# Sections based on menu selection
if menu == "Home":
    st.title("LyricPlug")
    st.subheader("Transcribing African Melodies")
    
    # Welcome message
    st.write("""
    Welcome to LyricPlug, your home for song lyrics in African languages!
    
    We celebrate the rich musical heritage of Africa by providing lyrics in:
    - **Afrikaans** - Die taal van ons hart
    - **isiZulu** - uLimi lwasekhaya
    - **Sesotho** - Puo
    - And many more African languages!
    """)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Songs", "1,247")
    with col2:
        st.metric("Languages", "3")
    with col3:
        st.metric("Artists", "456")
    
    # Featured song of the day
    st.subheader("Featured Song of the Day")
    st.write("**Jerusalema** by Master KG ft. Nomcebo Zikode")
    st.write("Language: isiZulu | Genre: Afro-house")
    
    with st.expander("View Lyrics Preview"):
        st.write("""
        *Jerusalema ikhaya lami*
        *Ngilondoloze*
        *Uhambe nami* 
        *Zungangishiyi lana*
        """)

elif menu == "Browse Lyrics":
    st.title("Browse Song Lyrics")
    st.sidebar.header("Search & Filter")
    
    # Language selection
    language_option = st.sidebar.selectbox(
        "Choose a language", 
        ["Afrikaans", "isiZulu", "Sesotho"]
    )

    if language_option == "Afrikaans":
        st.write("### Afrikaans Songs")
        st.dataframe(afrikaans_songs, use_container_width=True)
        
        # Filter by year
        year_filter = st.slider("Filter by Year", 1900, 2024, (1900, 2024))
        filtered_songs = afrikaans_songs[
            afrikaans_songs["Year"].between(year_filter[0], year_filter[1])
        ]
        st.write(f"Filtered Results for Year Range {year_filter}:")
        st.dataframe(filtered_songs, use_container_width=True)
        
        # Sample lyrics display
        selected_song = st.selectbox("Select a song to view lyrics", afrikaans_songs["Song Title"].tolist())
        if selected_song:
            with st.expander(f"View Lyrics for '{selected_song}'"):
                st.write("*Lyrics would be displayed here in Afrikaans*")
                st.write("Click 'Submit Lyrics' to add translations!")

    elif language_option == "isiZulu":
        st.write("### isiZulu Songs")
        st.dataframe(isizulu_songs, use_container_width=True)
        
        # Filter by genre
        genres = isizulu_songs["Genre"].unique().tolist()
        genre_filter = st.multiselect("Filter by Genre", genres, default=genres)
        filtered_songs = isizulu_songs[isizulu_songs["Genre"].isin(genre_filter)]
        st.write(f"Showing {len(filtered_songs)} songs:")
        st.dataframe(filtered_songs, use_container_width=True)
        
        # Sample lyrics display
        selected_song = st.selectbox("Select a song to view lyrics", isizulu_songs["Song Title"].tolist())
        if selected_song:
            with st.expander(f"View Lyrics for '{selected_song}'"):
                st.write("*Lyrics would be displayed here in isiZulu*")
                st.write("English translation available below")

    elif language_option == "Sesotho":
        st.write("### Sesotho Songs")
        st.dataframe(sesotho_songs, use_container_width=True)
        
        # Filter by year
        year_filter = st.slider("Filter by Year", 1950, 2024, (1950, 2024))
        filtered_songs = sesotho_songs[
            sesotho_songs["Year"].between(year_filter[0], year_filter[1])
        ]
        st.write(f"Filtered Results for Year Range {year_filter}:")
        st.dataframe(filtered_songs, use_container_width=True)
        
        # Sample lyrics display
        selected_song = st.selectbox("Select a song to view lyrics", sesotho_songs["Song Title"].tolist())
        if selected_song:
            with st.expander(f"View Lyrics for '{selected_song}'"):
                st.write("*Lyrics would be displayed here in Sesotho*")
                st.write("Phetolelo ea Senyesemane e teng (English translation available)")

elif menu == "Language Explorer":
    st.title("African Language Explorer")
    st.sidebar.header("Learn More")
    
    # Information about African languages
    st.write("""
    Explore the beautiful languages featured on LyricPlug and learn about their rich cultural heritage.
    """)
    
    language_info = st.selectbox(
        "Select a language to learn more",
        ["Afrikaans", "isiZulu", "Sesotho",]
    )
    
    if language_info == "Afrikaans":
        st.subheader("Afrikaans")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Speakers:** ~7-8 million")
            st.write("**Countries:** South Africa, Namibia")
            st.write("**Language Family:** West Germanic")
        with col2:
            st.write("**Common Greeting:** *Hallo, hoe gaan dit?*")
            st.write("**Translation:** Hello, how are you?")
        
        st.write("### Popular Music Genres")
        st.write("- Afrikaans Rock")
        st.write("- Boeremusiek (Traditional)")
        st.write("- Afrikaans Pop")
        
    elif language_info == "isiZulu":
        st.subheader("isiZulu")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Speakers:** ~12 million")
            st.write("**Countries:** South Africa, Zimbabwe, Lesotho")
            st.write("**Language Family:** Bantu (Nguni)")
        with col2:
            st.write("**Common Greeting:** *Sawubona, unjani?*")
            st.write("**Translation:** Hello, how are you?")
        
        st.write("### Popular Music Genres")
        st.write("- Maskandi")
        st.write("- Kwaito")
        st.write("- Gqom")
        st.write("- Amapiano")
        
    elif language_info == "Sesotho":
        st.subheader("Sesotho")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Speakers:** ~5-6 million")
            st.write("**Countries:** South Africa, Lesotho")
            st.write("**Language Family:** Bantu (Sotho-Tswana)")
        with col2:
            st.write("**Common Greeting:** *Dumela, o phela joang?*")
            st.write("**Translation:** Hello, how are you?")
        
        st.write("### Popular Music Genres")
        st.write("- Famo")
        st.write("- Gospel")
        st.write("- Traditional Sesotho music")

elif menu == "Submit Lyrics":
    st.title("Submit Song Lyrics")
    st.write("Help us grow our collection! Submit lyrics or corrections.")
    
    # Submission form
    with st.form("lyrics_submission"):
        col1, col2 = st.columns(2)
        
        with col1:
            song_title = st.text_input("Song Title *")
            artist = st.text_input("Artist Name *")
            language = st.selectbox("Language *", ["Afrikaans", "isiZulu", "Sesotho", "Setswana", "Xitsonga", "IsiXhosa", "Other"])
        
        with col2:
            year = st.number_input("Year Released", min_value=1900, max_value=2024, value=2020)
            genre = st.text_input("Genre")
            album = st.text_input("Album (Optional)")
        
        lyrics = st.text_area("Lyrics (in original language) *", height=200)
        translation = st.text_area("English Translation (Optional)", height=200)
        
        submitter_name = st.text_input("Your Name (Optional)")
        submitter_email = st.text_input("Your Email (for updates)")
        
        submit_button = st.form_submit_button("Submit Lyrics")
        
        if submit_button:
            if song_title and artist and language and lyrics:
                st.success("✅ Thank you for your submission! We'll review it shortly.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

elif menu == "Contact":
    st.title("Contact Us")
    
    st.write("""
    We'd love to hear from you! Whether you have questions, suggestions, or want to contribute,
    feel free to reach out.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Get in Touch")
        st.write("**Email:** info@lyricPlug.co.za")
        st.write("**Social Media:**")
        st.write("- Twitter: @LyricPlug")
        st.write("- Instagram: @LyricPlug")
        st.write("- Facebook: LyricPlug Official")
    
    with col2:
        st.subheader("Quick Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message", height=150)
            send_button = st.form_submit_button("Send Message")
            
            if send_button:
                if name and email and message:
                    st.success("✅ Message sent! We'll get back to you soon.")
                else:
                    st.error("❌ Please fill in all fields")
    
    st.write("---")
    st.write("**Office Location:** Bloemfontein, Free State, South Africa")
    st.write("*Celebrating African Melodies, one lyric at a time*")