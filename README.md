# public_transport_route_optimizer

# Public Transport Route Optimizer

A dynamic AI-powered route planner using Dijkstra’s and A* algorithms to find optimal paths in a public transport network.

## Features
- Choose any source and destination from real stop data
- Get two routes: one from Dijkstra and one from A* algorithm
- Estimate travel time and fare
- Interactive map view of both paths
- Dynamic input via CSV — no hardcoded stops

## Tech Stack
- Streamlit
- Python (NetworkX, Pandas)
- Folium for map visualization

## How to Run Locally
1. Clone the repo:
https://github.com/sushant0codes/public_transport_route_optimizer.git


2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py

## Dataset Format
Sample `stops.csv`:
stop_id,name,lat,lon,connections
A,IIT Gate,28.5450,77.1926,"B:10"
B,Hauz Khas,28.5494,77.2001,"A:10,C:12,D:20"
C,AIIMS,28.5672,77.2100,"B:12,D:15"
D,Rajiv Chowk,28.6328,77.2197,"C:15,B:20,E:5"
E,Connaught Place,28.6315,77.2167,"D:5"



