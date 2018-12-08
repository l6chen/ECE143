# ECE143
ECE 143 Repository.

# REQUIREMENTS

Install using conda:
- pandas
- geopandas
- matplotlib
- numpy

## Rough outline and placeholder of our plan for the data inspection and visualization project.

## Applications

### Stop frequency by location
**Data**:
- Location ID / Police Beats
- Number of stops per Location

**Visualization**:
- GIS Map. Warmer colors indicating more stops, cooler colors indicating fewer stops.

### Time and frequency of police stops
**Data**:
- Timestamp
    - Time 'buckets' or intervals to be defined
- Number of stops per time interval
- The result of the stops (they were arrested or just verbally warned)

**Visualization**:
- 2D Scatter Plot
    - X Axis: Time intervals
    - Y Axis: The result of thoses stops

### Race and likelihood of arrest correlation:
**Data**:
- Subject Race
- Arrest vs. No Arrest

**Visualization**:
- Bar chart
    - X Axis: Race
    - Y Axis: Likelihood of arrest (# of arrests / # of all stops per race)

### Age and arrest correlation
**Data**:
- Age
    - Age 'buckets' or intervals to be defined
- Gender

**Visualization**:
- 2D Bar Chart
    - X Axis: Age Bucket
    - Y Axis: Gender of stop subject. Within each bar separate the different causes for the stops.
