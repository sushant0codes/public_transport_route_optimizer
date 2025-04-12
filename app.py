import streamlit as st
from graph_utils import create_graph, dijkstra_path, a_star_path, path_time, estimate_fare
import folium
from streamlit_folium import st_folium

# Map drawing
def plot_path_on_map(path, stops):
    first_stop = stops[path[0]]
    m = folium.Map(location=[first_stop['lat'], first_stop['lon']], zoom_start=13)
    coordinates = [(stops[code]['lat'], stops[code]['lon']) for code in path]
    folium.PolyLine(coordinates, color='blue', weight=5).add_to(m)
    for code in path:
        stop = stops[code]
        folium.Marker([stop['lat'], stop['lon']], tooltip=stop['name']).add_to(m)
    return m

# Main UI
def main():
    G, stops = create_graph()

    st.title("Public Transport Route Optimizer")
    st.markdown("Plan your journey using shortest and fastest public transport paths.")

    stop_names = {v['name']: k for k, v in stops.items()}
    source_name = st.selectbox("Select Source", list(stop_names.keys()))
    target_name = st.selectbox("Select Destination", list(stop_names.keys()))

    source = stop_names[source_name]
    target = stop_names[target_name]

    if source == target:
        st.warning("Source and destination cannot be the same.")
        return

    if st.button("Find Best Routes"):
        try:
            d_path = dijkstra_path(G, source, target)
            a_path = a_star_path(G, source, target, stops)

            st.subheader("Dijkstra's Path")
            st.write(" -> ".join(stops[code]['name'] for code in d_path))
            d_time = path_time(G, d_path)
            st.write(f"Time: {d_time} mins | Fare: ₹{estimate_fare(d_time)}")
            st_folium(plot_path_on_map(d_path, stops), width=700)

            st.subheader("A* Path")
            st.write(" -> ".join(stops[code]['name'] for code in a_path))
            a_time = path_time(G, a_path)
            st.write(f"Time: {a_time} mins | Fare: ₹{estimate_fare(a_time)}")
            st_folium(plot_path_on_map(a_path, stops), width=700)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == '__main__':
    main()
