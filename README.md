```mermaid
stateDiagram
    [*] --> Scrape_Hotel_Reviews


    Scrape_Hotel_Reviews --> Data_Cleaning(Date_formats_etc.)
    Data_Cleaning(Date_formats_etc.) --> Split_by_date
    Split_by_date --> Removing_Stopwords
    Removing_Stopwords --> Topic_Modelling
    Topic_Modelling --> Visualization
```