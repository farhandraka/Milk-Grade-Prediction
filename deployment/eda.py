import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Milks Quality - EDA',
    layout = 'wide')

def run():
    # Membuat tittle
    st.title('Milks Quality Prediction')
    
    # Membuat sub-header
    st.subheader('Exploratory Data Analysis Milks Quality Dataset')
    
    # Menambahkan gambar
    image = Image.open('glassmilk.jpg')
    st.image(image)
    
    # Menambahkan deskripsi
    st.write('# Perkenalan')
    st.write('Nama : Muhammad Farhan Darmawan')
    st.write('Batch : RMT 019')
    st.markdown('---')
    
    '''
    Dataset ini menjelaskan tentang :
    
    | Kolom | Deskripsi |
    | ----- | --------- |
    | pH | Kadar keasaman susu |
    | Temperature | Suhu susu saat sampling |
    | Taste | Rasa susu |
    | Odor | Aroma susu |
    | Fat | Kadar lemak pada susu |
    | Turbidity | Kekeruhan susu |
    | Colour | Warna susu |
    | Grade | Kualitas susu |
    '''
    st.markdown('---')
   
    st.write('# Dataset of Milk')
    # Show dataframe
    data = pd.read_csv('milknew.csv')
    st.dataframe(data)
    st.markdown('---')    
    
    st.write('# Frekuensi Data by Grade')
    # Daftar nama kolom
    cols = ['pH', 'Temprature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Colour', 'Grade']

    # Membuat subplot
    f, axes = plt.subplots(4, 2, figsize=(25, 20), facecolor='white')
    f.suptitle('Frekuensi Data By Grade')

    # Membuat looping
    for i, column in enumerate(cols):
        row = i // 2  # Nomor baris subplot
        col = i % 2   # Nomor kolom subplot
        
        # Menampilkan countplot
        ax = sns.countplot(x=column, hue='Grade', data=data[cols], palette='Blues', ax=axes[row, col])
        ax.set_title(column)
        ax.legend(title='Grade', loc='upper right')

    # Menampilkan plot
    plt.tight_layout()
    plt.show()
    st.pyplot(f)
    st.markdown('---')
    
    st.write('# Histogram Dataset')
    # Membuat subplot dengan ukuran 6 x 4
    fig, axes = plt.subplots(4, 2, figsize=(12, 12))

    # Mendapatkan daftar kolom dalam DataFrame
    columns = data.columns

    # Melakukan looping untuk membuat histogram pada setiap kolom
    for i, ax in enumerate(axes.flatten()):
        if i < len(columns):
            # Membuat histogram
            sns.histplot(data=data, x=columns[i], kde=True, color='steelblue', alpha=0.7, ax=ax)
            ax.set_xlabel(columns[i])
            ax.set_ylabel('frequency')

    # Menyusun tata letak subplot
    plt.tight_layout()

    # Menampilkan plot
    plt.show()
    st.pyplot(fig)
    st.markdown('---')
    
    st.write('# Scatterplot Dataset')
    # Menampilkan scatterplot
    fig = sns.pairplot(data = data, hue = 'Grade', palette='Blues')
    st.pyplot(fig)
    
    st.write(
    '''
    Exploratory Data Analysis :

    - Dari 1059 sample susu diketahui bahwa kebanyakan susu berkualitas rendah dibandingkan dengan kualitas tinggi yang hanya sedikit

    - Susu dengan kualitas medium-bagus memiliki pH 6.5 - 7.0, bertemperature >35 dan <= 50 selain dari itu maka kualitas susu akan rendah, warna susu yaitu berada pada angka 255

    - Susu dengan kualitas bagus memiliki kandungan lemak, bau, rasa, dan turbidity

    - Grafik histogram menunjukan bahwa distribusi yang relatif tidak normal

    - Grafik scatterplot menunjukan bahwa tiap data tidak menunjukan korelasi yang cukup significant
    '''
    )

if __name__ == '__main__':
    run()