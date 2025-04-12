import networkx as nx
import pandas as pd

# Load stops and create graph from CSV
def create_graph(file_path="stops.csv"):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Initialize graph and stops dictionary
    G = nx.Graph()
    stops = {}

    # Process each stop
    for index, row in df.iterrows():
        stop_id = row['stop_id']
        stop_name = row['name']
        lat = row['lat']
        lon = row['lon']
        connections = row['connections'].split(',')
        
        stops[stop_id] = {
            "name": stop_name,
            "lat": lat,
            "lon": lon,
            "connections": []
        }
        
        # Add connections
        for conn in connections:
            target, time = conn.split(':')
            time = int(time)
            stops[stop_id]["connections"].append({"target": target, "time": time})
            G.add_edge(stop_id, target, weight=time)
    
    return G, stops

# Heuristic for A* (Euclidean distance as time proxy)
def heuristic(a, b, stops):
    from math import sqrt
    a_lat, a_lon = stops[a]["lat"], stops[a]["lon"]
    b_lat, b_lon = stops[b]["lat"], stops[b]["lon"]
    return sqrt((a_lat - b_lat)**2 + (a_lon - b_lon)**2) * 100  # rough scale

# Dijkstra's path
def dijkstra_path(G, source, target):
    return nx.dijkstra_path(G, source, target, weight="weight")

# A* path
def a_star_path(G, source, target, stops):
    return nx.astar_path(G, source, target, heuristic=lambda a, b: heuristic(a, b, stops), weight="weight")

# Total time of a path
def path_time(G, path):
    return sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Estimate fare (e.g., ₹10 base + ₹1 per min)
def estimate_fare(time):
    return 10 + time
