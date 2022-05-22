import pandas as pd
import numpy as np
import os    

def haversine_distance(lat1, lon1, lat2, lon2):
       r = 6371
       phi1 = np.radians(lat1)
       phi2 = np.radians(lat2)
       delta_phi = np.radians(lat2-lat1)
       delta_lambda = np.radians(lon2-lon1)
       a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
       res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)))
       return np.round(res, 2)


def lat_lon_calculator(source_city, src_country, dest_city, dest_country):
    worldcities= pd.read_csv(os.path.join(os.getcwd(),"worldcities.csv"))
    src_city_desc = worldcities[worldcities['city'] == source_city][worldcities[worldcities['city'] == source_city]['country']==src_country]
    start_lat_src= src_city_desc['Latitude'].values[0]
    start_lng_src= src_city_desc['Longitude'].values[0]
    ports_desc= pd.read_csv(os.path.join(os.getcwd(),"ports.csv"))
    source_ports=ports_desc[ports_desc['Country']==src_country]
    source_ports["Direction from source"]=" "
    ar=[]
    for i in range(len(source_ports["Seaport_Code"])):
        x = source_ports.iloc[[i],[5]].values[0][0]
        if x>start_lng_src:
            ar.append('East')
        else:
            ar.append('West')
    source_ports["Direction from source"]=ar
    dest_city_desc = worldcities[worldcities['city'] == dest_city][worldcities[worldcities['city'] == dest_city]['country']==dest_country]
    start_lat_dest= dest_city_desc['Latitude'].values[0]
    start_lng_dest= dest_city_desc['Longitude'].values[0]
    dest_ports=ports_desc[ports_desc['Country']==dest_country]
    

    dest_ports["Direction from dest"]=" "
    ar2=[]
    for i in range(len(dest_ports["Seaport_Code"])):
        x1 = dest_ports.iloc[[i],[5]].values[0][0]
        if x1>start_lng_dest:
            ar2.append('East')
        else:
            ar2.append('West')
    dest_ports["Direction from dest"]=ar2
    if start_lng_src>start_lng_dest:
        source_ports_dir=source_ports[source_ports['Direction from source']=='West']
        dest_ports_dir=dest_ports[dest_ports['Direction from dest']=='East']
    else:
        source_ports_dir=source_ports[source_ports['Direction from source']=='East'] 
        dest_ports_dir=dest_ports[dest_ports['Direction from dest']=='West']
    if len(dest_ports_dir)==0:
        dest_ports_dir=dest_ports
    if len(source_ports_dir)==0:
        source_ports_dir=source_ports
    
    source_ports_dir["Distance from source"]=" "
    lat=np.array(source_ports_dir["Latitude degree.1"])
    lon=np.array(source_ports_dir["Longitude degree"])
    dist=[]
    for i in range(0,len(lat)):
        dist.append(haversine_distance(start_lat_src,start_lng_src,lat[i],lon[i]))
    source_ports_dir["Distance from source"]=dist
    dist
    y=[]
    d=min(dist)
    for i in range(0,len(dist)):
        if dist[i]==d:
            y.append(i)
    p=[]
    for i in y:
        p.append(source_ports_dir.iloc[i,])
    
    dest_ports_dir["Distance from destination"]=" "
    lat_dest=np.array(dest_ports_dir["Latitude degree.1"])
    lon_dest=np.array(dest_ports_dir["Longitude degree"])
    dist_dest=[]
    for i in range(0,len(lat_dest)):
        dist_dest.append(haversine_distance(start_lat_dest,start_lng_dest,lat_dest[i],lon_dest[i]))
    dest_ports_dir["Distance from destination"]=dist_dest
    
    y_dest=[]
    d_dest=min(dist_dest)
    for i in range(0,len(dist_dest)):
        if dist_dest[i]==d_dest:
            y_dest.append(i)
    p_dest=[]
    for i in y_dest:
        p_dest.append(dest_ports_dir.iloc[i,])
    p_dest
    my_dict = {"Src Country":[],"Src City":[],"Src Port":[],"Src Lat":[],"Src Lng":[],"Src Port Lat":[],"Src Port Lng":[],
           "Dest Country":[],"Dest City":[],"Dest Port":[],"Dest Lat":[],"Dest Lng":[],"Dest Port Lat":[],"Dest Port Lng":[]}
    print(src_country)
    for i in p:
        for j in p_dest:
            my_dict["Src Country"].append(src_country)
            my_dict["Src City"].append(source_city)
            my_dict["Src Port"].append(i["Seaport_Name"])
            my_dict["Src Lat"].append(start_lat_src)
            my_dict["Src Lng"].append(start_lng_src)
            my_dict["Src Port Lat"].append(i["Latitude degree.1"])
            my_dict["Src Port Lng"].append(i["Longitude degree"])
            my_dict["Dest Country"].append(j["Country"])
            my_dict["Dest City"].append(dest_city)
            my_dict["Dest Port"].append(j["Seaport_Name"])
            my_dict["Dest Port Lat"].append(j["Latitude degree.1"])
            my_dict["Dest Port Lng"].append(j["Longitude degree"])
            my_dict["Dest Lat"].append(start_lat_dest)
            my_dict["Dest Lng"].append(start_lng_dest)
    return my_dict


result = lat_lon_calculator('Delhi','India','Lusaka','Zambia')
print(result,'\n\n',type(result))

