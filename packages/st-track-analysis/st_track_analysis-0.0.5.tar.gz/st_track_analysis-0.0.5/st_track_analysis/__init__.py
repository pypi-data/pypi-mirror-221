import os
import streamlit.components.v1 as components
import pandas as pd
import base64
import io
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO


_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        "st_track_analysis",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_track_analysis", path=build_dir)


def st_track_analysis(
    date, tracks=[], grounds=[], images=[], shapes=[], names=[], key=None
):
    if not (
        len(tracks) == len(grounds)
        and len(tracks) == len(images)
        and len(tracks) == len(shapes)
    ):
        raise ValueError(
            f"""Length of tracks, grounds, images, shapes and names must be equal:
                         Tracks length: {len(tracks)}
                         Grounds length: {len(grounds)}
                         Images length: {len(images)}
                         Shapes length: {len(shapes)}
                         Names length: {len(names)}"""
        )
    ims = []
    for im in images:
        buffer = BytesIO()
        plt.imsave(buffer, im, cmap="gray", format="png")
        base64_string = base64.b64encode(buffer.getvalue()).decode()
        mime_type = "image/png"
        url_string = f"data:{mime_type};base64,{base64_string}"
        ims.append(url_string)
    component_value = _component_func(
        tracks=tracks,
        date=date,
        images=ims,
        grounds=grounds,
        shapes=shapes,
        names=names,
        key=key,
        default=0,
    )
    return component_value


def process_tracks(tracks):
    time_strings = tracks["Time"].dt.strftime("%Y-%m-%dT%H:%M:%S.%f").tolist()
    tracks = list(
        zip(
            tracks["ID"].tolist(),
            tracks["X"].tolist(),
            tracks["Y"].tolist(),
            tracks["Type"].tolist(),
            tracks["Estimated"].tolist(),
            time_strings,
        )
    )
    tracks = sorted(tracks, key=lambda x: x[5])
    return tracks


# Test code
if not _RELEASE:
    import streamlit as st

    st.set_page_config(layout="wide")
    image = plt.imread("./frontend/src/assets/ground.png")
    image2 = plt.imread("./frontend/src/assets/ground2.png")

    if "key" not in st.session_state:
        st.session_state["key"] = "2023-05-04"
    folder_path = "./CSV2"
    folder_path2 = "./CSV"
    csv_files = os.listdir(folder_path)
    csv_files2 = os.listdir(folder_path2)
    keys = list(map(lambda string: string.split("_")[0], csv_files))
    keys2 = list(map(lambda string: string.split("_")[0], csv_files2))

    if "track_data" not in st.session_state:
        track_data = {}

        for file_name in csv_files:
            if file_name.endswith(".csv"):
                date_str = file_name.split("_")[0]
                date_key = pd.to_datetime(date_str).date().isoformat()
                file_path = os.path.join(folder_path, file_name)
                tracks = pd.read_csv(file_path, sep=";", parse_dates=["Time"])
                track_data[date_key] = tracks
        st.session_state["track_data"] = track_data
    _tracks = (
        process_tracks(st.session_state.track_data[st.session_state.key])
        if st.session_state.key in keys
        else []
    )
    if "track_data2" not in st.session_state:
        track_data = {}
        for file_name in csv_files2:
            if file_name.endswith(".csv"):
                date_str = file_name.split("_")[0]
                date_key = pd.to_datetime(date_str).date().isoformat()
                file_path = os.path.join(folder_path2, file_name)
                tracks = pd.read_csv(file_path, sep=";", parse_dates=["Time"])
                track_data[date_key] = tracks
        st.session_state["track_data2"] = track_data
    _tracks2 = (
        process_tracks(st.session_state.track_data2[st.session_state.key])
        if st.session_state.key in keys2
        else []
    )

    tracks = [_tracks, _tracks2]

    ground = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 30.0, 27.0]
    ground2 = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 90.35000000000001, 82.55000000000001]
    grounds = [ground, ground2]
    shapes = [[600, 540], [1807, 1651]]
    images = [image, image2]
    names = ["A", "B"]
    key = st_track_analysis(
        tracks=tracks,
        date=st.session_state.key,
        images=images,
        grounds=grounds,
        shapes=shapes,
        names=names,
    )
    if not st.session_state.key == key and key != 0:
        st.session_state.key = key
        st.experimental_rerun()
    else:
        pass
